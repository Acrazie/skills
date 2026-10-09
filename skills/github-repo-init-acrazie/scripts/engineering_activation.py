"""Plan/apply approved, project-local engineering activation. No network or Git mutations.

The existing Skills CLI runs separately in disposable staging. This helper checks
its outputs, adapts invocation flags, and protects project-owned content. It is not
an authorization boundary: the invoking skill must obtain real user approval.
"""

import argparse
import base64
import hashlib
import json
import os
import re
import stat
import subprocess
import tempfile
from pathlib import Path

SOURCE = "Acrazie/skills"
CONFIG = ".acrazie/engineering.json"
CATALOG = ".acrazie/engineering-catalog.md"
LOCK = "skills-lock.json"
START = "<!-- acrazie-engineering:start -->"
END = "<!-- acrazie-engineering:end -->"
ACTIONS = {"stage", "commit", "push", "pr_create", "pr_update", "merge", "deploy"}
HOSTS = ["codex", "claude-code"]
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*-acrazie\Z")
# Match Skills CLI's localeCompare path ordering using its native runtime rather
# than approximating JavaScript collation in Python.
HASH_JS = """
const crypto = require('node:crypto');
let input = ''; process.stdin.setEncoding('utf8');
process.stdin.on('data', chunk => input += chunk);
process.stdin.on('end', () => {
  const hash = crypto.createHash('sha256');
  for (const file of JSON.parse(input).sort((a, b) => a.path.localeCompare(b.path))) {
    hash.update(file.path); hash.update(Buffer.from(file.content, 'base64'));
  }
  process.stdout.write(hash.digest('hex'));
});
"""


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def encode(value):
    return (json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n").encode()


def no_duplicates(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path):
    return json.loads(path.read_text(), object_pairs_hook=no_duplicates)


def strings(value):
    return isinstance(value, list) and bool(value) and all(
        isinstance(x, str) and x.strip() and "\n" not in x and "\x00" not in x for x in value
    ) and len(value) == len(set(value))


def validate_request(data):
    fields = {"schema_version", "source_revision", "installer_version", "hosts", "skills", "permissions", "policy_sources"}
    require(isinstance(data, dict) and set(data) == fields, "Unsupported configuration fields")
    require(type(data["schema_version"]) is int and data["schema_version"] == 1, "Unsupported schema version")
    require(isinstance(data["source_revision"], str) and re.fullmatch(r"[0-9a-f]{40}", data["source_revision"]), "Source must be a full lowercase Git SHA")
    require(isinstance(data["installer_version"], str) and re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", data["installer_version"]), "Pin an exact Skills CLI version")
    require(data["hosts"] == HOSTS, "This mode supports Codex + Claude Code only")
    require(strings(data["skills"]) and all(NAME.fullmatch(x) for x in data["skills"]), "Invalid or duplicate skill selection")
    permissions = data["permissions"]
    require(isinstance(permissions, dict) and set(permissions) == ACTIONS, "Specify each action separately")
    for action, rule in permissions.items():
        require(isinstance(rule, dict) and isinstance(rule.get("mode"), str) and rule["mode"] in {"forbidden", "confirm", "preauthorized"}, f"Invalid permission: {action}")
        if rule["mode"] != "preauthorized":
            require(set(rule) == {"mode"}, f"Unexpected permission fields: {action}")
            continue
        require(set(rule) == {"mode", "repository", "branches", "destinations", "checks"}, f"Incomplete preauthorization: {action}")
        require(isinstance(rule["repository"], str) and rule["repository"].strip() and "\n" not in rule["repository"], f"Missing repository identity: {action}")
        for field in ("branches", "destinations", "checks"):
            require(strings(rule[field]), f"Missing preauthorization {field}: {action}")
        require(all(not any(c in x for c in "*?[") for x in rule["branches"] + rule["destinations"]), "Preauthorization uses exact branches/destinations, not wildcards")
    require(isinstance(data["policy_sources"], dict), "Policy sources must be a path/hash map")
    for path, value in data["policy_sources"].items():
        relative(path)
        require(path not in {CONFIG, CATALOG, LOCK} and not path.startswith((".agents/skills/", ".claude/skills/")), "Policy source cannot be an activation output")
        require(isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value), "Invalid policy source hash")
    return data


def relative(name):
    require(isinstance(name, str) and name and "\\" not in name and "\x00" not in name, "Invalid relative path")
    path = Path(name)
    require(not path.is_absolute() and all(x and x not in {".", "..", ".git"} for x in name.split("/")), f"Unsafe path: {name}")
    return path


def target(project, name):
    path = project / relative(name)
    for parent in path.parents:
        if parent == project:
            break
        require(not parent.is_symlink(), f"Symlink parent: {name}")
        require(not parent.exists() or parent.is_dir(), f"Non-directory parent: {name}")
    return path


def state(path):
    if path.is_symlink():
        return {"kind": "symlink", "target": os.readlink(path)}
    if not path.exists():
        return None
    require(path.is_file(), f"Expected regular file: {path.name}")
    return {"kind": "file", "sha256": digest(path.read_bytes()), "mode": stat.S_IMODE(path.stat().st_mode)}


def file(data, mode=0o644):
    return {"kind": "file", "content": base64.b64encode(data).decode(), "mode": mode}


def folder_hash(files):
    values = [{"path": name, "content": value["content"]} for name, value in files.items()]
    result = subprocess.run(["node", "-e", HASH_JS], input=json.dumps(values), capture_output=True, text=True)
    require(result.returncode == 0 and re.fullmatch(r"[0-9a-f]{64}", result.stdout), "Node could not verify the Skills CLI folder hash")
    return result.stdout


def payload_state(payload):
    if payload is None or payload["kind"] == "symlink":
        return payload
    return {"kind": "file", "sha256": digest(base64.b64decode(payload["content"], validate=True)), "mode": payload["mode"]}


def block(text):
    require(text.count(START) == text.count(END) and text.count(START) <= 1, "Malformed managed instruction markers")
    if START not in text:
        return None
    begin, finish = text.index(START), text.index(END) + len(END)
    require(begin < finish and text.index(START) < text.index(END), "Reversed managed instruction markers")
    return text[begin:finish]


def policy_hash(project, name):
    path = target(project, name)
    require(path.is_file() and not path.is_symlink(), f"Policy source must be a regular file: {name}")
    data = path.read_bytes()
    if name in {"AGENTS.md", "CLAUDE.md"}:
        text = data.decode()
        current = block(text)
        data = (text.replace(current, "") if current else text).strip().encode()
    return digest(data)


def explicit_skill(text, name):
    # A bounded adapter for the published Acrazie layout, not an arbitrary YAML parser.
    lines = text.splitlines()
    require(lines and lines[0] == "---" and "---" in lines[1:], f"Unsupported frontmatter: {name}")
    end = lines.index("---", 1)
    header = lines[1:end]
    require([x for x in header if re.match(r"name\s*:", x)] == [f"name: {name}"], f"Skill identity mismatch: {name}")
    flags = [x for x in header if re.match(r"disable-model-invocation\s*:", x)]
    require(len(flags) <= 1 and all(re.fullmatch(r"disable-model-invocation: (true|false)", x) for x in flags), "Unsupported invocation flag layout")
    header = [x for x in header if not x.startswith("disable-model-invocation:")]
    descriptions = [i for i, x in enumerate(header) if re.match(r"description\s*:", x)]
    require(len(descriptions) == 1 and header[descriptions[0]].startswith("description:"), f"Missing/unsupported description: {name}")
    description = descriptions[0]
    value = header[description].split(":", 1)[1].strip()
    if value in {">", ">-", "|", "|-"}:
        chunks = []
        for line in header[description + 1:]:
            if line and not line.startswith(" "):
                break
            chunks.append(line.strip())
        value = " ".join(chunks).strip()
    else:
        require(value and value[0] not in "&*!{[", "Unsupported description scalar")
        value = value.strip("\"'")
    require(value, f"Empty description: {name}")
    header.append("disable-model-invocation: true")
    return "\n".join(["---", *header, *lines[end:]]) + "\n", value


def explicit_codex(text):
    lines = text.splitlines()
    policies = [i for i, x in enumerate(lines) if re.match(r"policy\s*:", x)]
    require(len(policies) <= 1, "Duplicate Codex policy")
    if not policies:
        require(not any("allow_implicit_invocation:" in x for x in lines), "Misplaced Codex invocation flag")
        return text.rstrip() + "\npolicy:\n  allow_implicit_invocation: false\n"
    start = policies[0]
    require(lines[start] == "policy:", "Unsupported Codex policy layout")
    end = next((i for i in range(start + 1, len(lines)) if lines[i] and not lines[i].startswith(" ")), len(lines))
    entries = lines[start + 1:end]
    require(all(not x.strip() or x.lstrip().startswith("#") or re.fullmatch(r"  allow_implicit_invocation: (true|false)", x) for x in entries), "Unsupported Codex policy entries")
    require(sum(x.startswith("  allow_implicit_invocation:") for x in entries) <= 1, "Duplicate Codex invocation flag")
    entries = [x for x in entries if not x.startswith("  allow_implicit_invocation:")]
    return "\n".join([*lines[:start + 1], "  allow_implicit_invocation: false", *entries, *lines[end:]]) + "\n"


def installer_command(request):
    validate_request(request)
    return ["npx", "--yes", f"skills@{request['installer_version']}", "add", f"{SOURCE}#{request['source_revision']}",
            *[part for name in request["skills"] for part in ("--skill", name)],
            "--agent", "codex", "--agent", "claude-code", "--yes"]


def read_lock(path):
    if not path.exists() and not path.is_symlink():
        return {"version": 1, "skills": {}}
    require(not path.is_symlink(), "Lock must not be a symlink")
    data = read_json(path)
    require(isinstance(data, dict) and data.get("version") == 1 and isinstance(data.get("skills"), dict), "Unsupported Skills lock")
    return data


def managed_path(name, skills):
    relative(name)
    return name == CATALOG or any(name.startswith(f".agents/skills/{x}/") or name == f".claude/skills/{x}" for x in skills)


def plan(project, request, staged):
    project, staged = project.resolve(), staged.resolve()
    require(project.is_dir() and staged.is_dir() and project != staged and project not in staged.parents and staged not in project.parents, "Staging must be outside the target project")
    validate_request(request)
    config_path = target(project, CONFIG)
    require(not config_path.is_symlink(), "Configuration must not be a symlink")
    old = read_json(config_path) if config_path.exists() else None
    previous = {"files": {}, "instructions": {}, "lock_entries": {}, "source_hashes": {}}
    old_skills = []
    if old is not None:
        require(isinstance(old, dict) and "_managed" in old, "Existing configuration is not managed; resolve before adoption")
        validate_request({k: v for k, v in old.items() if k != "_managed"})
        previous, old_skills = old["_managed"], old["skills"]
        require(isinstance(previous, dict) and set(previous) == {"files", "instructions", "lock_entries", "source_hashes"} and all(isinstance(v, dict) for v in previous.values()), "Invalid ownership record")
    guards = {CONFIG: state(config_path)}
    for name, expected in previous["files"].items():
        require(managed_path(name, old_skills), "Unsafe ownership record")
        observed = state(target(project, name))
        require(observed == expected, f"Customized managed asset: {name}")
        guards[name] = observed
    for name, expected in previous["instructions"].items():
        require(name in {"AGENTS.md", "CLAUDE.md"}, "Invalid instruction ownership")
        path = target(project, name)
        require(path.is_file() and not path.is_symlink(), f"Changed managed instructions: {name}")
        owned_block = block(path.read_text())
        require(owned_block is not None and digest(owned_block.encode()) == expected, f"Customized managed block: {name}")
    for name, expected in request["policy_sources"].items():
        require(policy_hash(project, name) == expected, f"Policy changed: {name}")
        guards[name] = state(target(project, name))
    canonical = target(staged, ".agents/skills")
    require(canonical.is_dir() and not canonical.is_symlink(), "Missing canonical staging output")
    require({p.name for p in canonical.iterdir()} == set(request["skills"]), "Staging selection differs from approval")
    source_lock = read_lock(target(staged, LOCK))
    require(set(source_lock["skills"]) == set(request["skills"]), "Staging lock selection differs from approval")
    desired, descriptions, source_hashes, installed_entries = {}, {}, {}, {}
    for name in request["skills"]:
        entry = source_lock["skills"][name]
        require(isinstance(entry, dict) and entry.get("source") == SOURCE and entry.get("sourceType") == "github" and entry.get("ref") == request["source_revision"] and isinstance(entry.get("computedHash"), str) and re.fullmatch(r"[0-9a-f]{64}", entry["computedHash"]), f"Unverified source/ref/hash in staging lock: {name}")
        folder = canonical / name
        require(folder.is_dir() and not folder.is_symlink(), "Unsafe canonical skill")
        link = target(staged, f".claude/skills/{name}")
        require(link.is_symlink() and link.resolve() == folder.resolve(), "Claude staging must use a local link, not fallback copies")
        raw_files = {}
        for source in sorted(folder.rglob("*")):
            require(not source.is_symlink(), f"Symlink inside skill package: {name}")
            rel = source.relative_to(folder)
            require(not any(x.startswith(".") or x in {"node_modules", "__pycache__"} for x in rel.parts), "Internal artifact in skill package")
            if source.is_dir():
                continue
            require(source.is_file(), "Non-regular skill asset")
            content = source.read_bytes()
            raw_files[rel.as_posix()] = file(content)
            if rel.as_posix() == "SKILL.md":
                adapted, descriptions[name] = explicit_skill(content.decode(), name)
                content = adapted.encode()
            elif rel.as_posix() == "agents/openai.yaml":
                content = explicit_codex(content.decode()).encode()
            desired[f".agents/skills/{name}/{rel.as_posix()}"] = file(content, 0o755 if source.stat().st_mode & 0o111 else 0o644)
        require(name in descriptions and f".agents/skills/{name}/agents/openai.yaml" in desired, "Incomplete skill package")
        require(folder_hash(raw_files) == entry["computedHash"], f"Staging content/hash mismatch: {name}")
        source_hashes[name] = entry["computedHash"]
        prefix = f".agents/skills/{name}/"
        installed_entries[name] = {**entry, "computedHash": folder_hash({path[len(prefix):]: value for path, value in desired.items() if path.startswith(prefix)})}
        desired[f".claude/skills/{name}"] = {"kind": "symlink", "target": f"../../.agents/skills/{name}"}
    catalog = "# Installed Acrazie engineering skills\n\nMetadata only; do not read skill bodies before explicit activation.\n\n"
    for name in request["skills"]:
        catalog += f"## {name}\n\n{descriptions[name]}\n\nCodex: `${name}`. Claude Code: `/{name}`.\n\n"
    desired[CATALOG] = file(catalog.encode())
    # Newly added local files also make a package customized; do not leave hidden
    # behavior behind while claiming the installed package matches its revision.
    for name in set(old_skills + request["skills"]):
        folder = target(project, f".agents/skills/{name}")
        require(not folder.is_symlink(), f"Canonical skill is a symlink: {name}")
        if folder.exists():
            require(folder.is_dir(), f"Canonical skill is not a directory: {name}")
            for path in folder.rglob("*"):
                rel = path.relative_to(project).as_posix()
                require(not path.is_symlink(), f"Local symlink inside skill: {rel}")
                if not path.is_dir():
                    require(rel in previous["files"] or rel in desired, f"Unowned file inside skill: {rel}")
    instruction = (f"{START}\n## Acrazie engineering\n\n"
                   f"Configuration and action policy: `{CONFIG}`. Metadata catalog: `{CATALOG}`.\n"
                   "Prefer relevant installed Acrazie skills, not unrelated workflows. Propose the named skill using metadata only.\n"
                   "Wait for explicit user invocation: `$skill-name` in Codex or `/skill-name` in Claude Code.\n"
                   "Do not read a skill body, invoke it autonomously, or imitate a disabled workflow to bypass this gate.\n"
                   "Each dependency requires its own explicit activation; stop the dependent step if unavailable.\n"
                   "Loading never grants installation, delegation, implementation or delivery permissions.\n"
                   "Reuse current approved task contracts; unresolved user decisions require Interview activation.\n"
                   "Apply the configured action-specific mode and scope; restrictive current instructions and protections prevail.\n"
                   "A policy file or approval label alone is not evidence of user authorization. Never self-authorize a policy edit.\n"
                   "Resolve governance conflicts before acting; retain existing Git policy and its safeguards.\n"
                   "Updates must use the approved Repo Init staging/plan workflow, not direct installer writes in this project.\n"
                   "These invocation flags are not filesystem access controls. Host behavior has not been live-verified.\n"
                   f"{END}")
    instructions = {}
    for name in ("AGENTS.md", "CLAUDE.md"):
        path = target(project, name)
        guards[name] = state(path)
        if name == "CLAUDE.md" and path.is_symlink():
            require(not Path(os.readlink(path)).is_absolute() and path.resolve() == (project / "AGENTS.md").resolve(), "External or independent CLAUDE symlink; resolve explicitly")
            continue
        if name == "CLAUDE.md" and not path.exists():
            desired[name] = {"kind": "symlink", "target": "AGENTS.md"}
            continue
        require(not path.is_symlink(), f"Instruction symlink: {name}")
        text = path.read_text() if path.exists() else ""
        current = block(text)
        require(current is None or name in previous["instructions"], f"Unowned managed markers: {name}")
        text = text.replace(current, instruction) if current else text + ("\n" if text.endswith("\n") else "\n\n" if text else "") + instruction + "\n"
        desired[name] = file(text.encode(), guards[name]["mode"] if guards[name] else 0o644)
        instructions[name] = digest(instruction.encode())
    # Preserve unrelated lock entries. Ownership is per entry, not the whole lock.
    lock_path = target(project, LOCK)
    guards[LOCK] = state(lock_path)
    lock = read_lock(lock_path)
    for name, expected in previous["lock_entries"].items():
        require(name in old_skills and lock["skills"].get(name) == expected, f"Customized lock entry: {name}")
        if name not in request["skills"]:
            del lock["skills"][name]
    for name, entry in installed_entries.items():
        require(name not in lock["skills"] or name in previous["lock_entries"] or lock["skills"][name] == entry, f"Unowned lock collision: {name}")
        lock["skills"][name] = entry
    desired[LOCK] = file(encode(lock), guards[LOCK]["mode"] if guards[LOCK] else 0o644)
    managed = {name: payload_state(value) for name, value in desired.items() if managed_path(name, request["skills"])}
    config = {**request, "_managed": {"files": managed, "instructions": instructions, "lock_entries": installed_entries, "source_hashes": source_hashes}}
    desired[CONFIG] = file(encode(config), guards[CONFIG]["mode"] if guards[CONFIG] else 0o644)
    operations = []
    for name in sorted(set(desired) | set(previous["files"]), key=lambda x: (x == CONFIG, x)):
        path = target(project, name)
        before, after = state(path), desired.get(name)
        guards[name] = before
        if name not in previous["files"] and name not in {CONFIG, LOCK, "AGENTS.md", "CLAUDE.md"}:
            require(before is None or before == payload_state(after), f"Unowned asset collision: {name}")
        if before != payload_state(after):
            operations.append({"path": name, "before": before, "after": after})
    return {"schema_version": 1, "project": str(project), "skills": sorted(set(old_skills + request["skills"])),
            "guards": guards, "operations": operations}


def apply(project, prepared):
    project = project.resolve()
    require(prepared.get("schema_version") == 1 and prepared.get("project") == str(project), "Wrong plan/project identity")
    require(strings(prepared.get("skills")) and all(NAME.fullmatch(x) for x in prepared["skills"]), "Invalid plan selection")
    paths = [op["path"] for op in prepared["operations"]]
    require(len(paths) == len(set(paths)), "Duplicate plan operations")
    for name in paths:
        require(name in {CONFIG, LOCK, "AGENTS.md", "CLAUDE.md"} or managed_path(name, prepared["skills"]), "Operation outside activation scope")
        require(name in prepared["guards"], "Missing operation guard")
    # A cooperative lock excludes other instances of this helper, not external writers.
    lock_path = target(project, ".acrazie/activation.lock")
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    completed = []
    try:
        for name, expected in prepared["guards"].items():
            require(state(target(project, name)) == expected, f"Stale plan: {name}")
        for operation in prepared["operations"]:
            name, value = operation["path"], operation["after"]
            path = target(project, name)
            require(state(path) == operation["before"] == prepared["guards"][name], f"Changed before write: {name}")
            if value is None:
                path.unlink()
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                if value["kind"] == "symlink":
                    expected_target = "AGENTS.md" if name == "CLAUDE.md" else f"../../.agents/skills/{name.split('/')[-1]}"
                    require(name == "CLAUDE.md" or name.startswith(".claude/skills/"), "Unexpected symlink output")
                    require(value["target"] == expected_target, "Unsafe symlink target")
                    with tempfile.TemporaryDirectory(dir=path.parent) as tmp:
                        pending = Path(tmp) / "link"
                        pending.symlink_to(value["target"])
                        os.replace(pending, path)
                else:
                    require(value["kind"] == "file" and type(value["mode"]) is int and 0 <= value["mode"] <= 0o777, "Invalid file payload")
                    pending_fd, pending_name = tempfile.mkstemp(dir=path.parent)
                    try:
                        with os.fdopen(pending_fd, "wb") as output:
                            output.write(base64.b64decode(value["content"], validate=True))
                            output.flush()
                            os.fsync(output.fileno())
                        os.chmod(pending_name, value["mode"])
                        os.replace(pending_name, path)
                    finally:
                        if os.path.lexists(pending_name):
                            os.unlink(pending_name)
            require(state(path) == payload_state(value), f"Unverified write: {name}")
            completed.append(name)
    except Exception as error:
        raise ValueError(f"Activation stopped; completed paths: {completed}. Preserve plan and inspect partial state; no automatic rollback. {error}") from error
    finally:
        try:
            owned = os.fstat(fd)
            if lock_path.exists() and not lock_path.is_symlink():
                current = lock_path.stat()
                if (owned.st_dev, owned.st_ino) == (current.st_dev, current.st_ino):
                    lock_path.unlink()
        finally:
            os.close(fd)
    return completed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    argv = commands.add_parser("installer-command")
    argv.add_argument("--request", type=Path, required=True)
    preview = commands.add_parser("plan")
    preview.add_argument("--request", type=Path, required=True)
    preview.add_argument("--project", type=Path, required=True)
    preview.add_argument("--staged", type=Path, required=True)
    preview.add_argument("--output", type=Path, required=True)
    execute = commands.add_parser("apply")
    execute.add_argument("--project", type=Path, required=True)
    execute.add_argument("--plan", type=Path, required=True)
    execute.add_argument("--approved-sha256", required=True)
    args = parser.parse_args()
    try:
        if args.command == "installer-command":
            print(json.dumps(installer_command(read_json(args.request))))
        elif args.command == "plan":
            result = plan(args.project, read_json(args.request), args.staged)
            require(not args.output.resolve().is_relative_to(args.project.resolve()), "Plan must stay outside target project")
            content = encode(result)
            with args.output.open("xb") as output:
                os.fchmod(output.fileno(), 0o600)
                output.write(content)
            print(json.dumps({"plan_sha256": digest(content), "operations": [{"path": op["path"], "operation": "delete" if op["after"] is None else "write"} for op in result["operations"]]}))
        else:
            content = args.plan.read_bytes()
            require(digest(content) == args.approved_sha256, "Plan hash differs from approved snapshot")
            print(json.dumps({"completed": apply(args.project, read_json(args.plan))}))
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.exit(1, f"Activation blocked: {error}\n")


if __name__ == "__main__":
    main()
