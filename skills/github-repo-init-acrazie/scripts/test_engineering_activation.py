"""Offline integration tests in temporary Git repositories; no live agent runs."""

import copy
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

SCRIPT = Path(__file__).with_name("engineering_activation.py")
spec = importlib.util.spec_from_file_location("activation", SCRIPT)
activation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(activation)
SKILL = "feature-builder-acrazie"


class ActivationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.project, self.staged = self.root / "project", self.root / "staged"
        self.project.mkdir()
        subprocess.run(["git", "init", "-q", str(self.project)], check=True, capture_output=True)
        self.request = {
            "schema_version": 1, "source_revision": "a" * 40, "installer_version": "1.7.2",
            "hosts": ["codex", "claude-code"], "skills": [SKILL],
            "permissions": {name: {"mode": "confirm"} for name in activation.ACTIONS},
            "policy_sources": {},
        }
        self.stage(SKILL)

    def stage(self, name, revision=None):
        folder = self.staged / ".agents/skills" / name
        (folder / "agents").mkdir(parents=True, exist_ok=True)
        (folder / "SKILL.md").write_text(f"---\nname: {name}\ndescription: >-\n  Test task owner.\n  Not unrelated work.\n---\n\n# Fixture\n")
        (folder / "agents/openai.yaml").write_text('interface:\n  display_name: "Fixture"\npolicy:\n  allow_implicit_invocation: true\n')
        (folder / "asset.bin").write_bytes(b"\x00binary\xff")
        link = self.staged / ".claude/skills" / name
        link.parent.mkdir(parents=True, exist_ok=True)
        if not link.is_symlink():
            link.symlink_to(f"../../.agents/skills/{name}")
        lock_path = self.staged / "skills-lock.json"
        lock = json.loads(lock_path.read_text()) if lock_path.exists() else {"version": 1, "skills": {}}
        raw_files = {p.relative_to(folder).as_posix(): activation.file(p.read_bytes()) for p in folder.rglob("*") if p.is_file()}
        lock["skills"][name] = {"source": "Acrazie/skills", "sourceType": "github", "ref": revision or self.request["source_revision"], "computedHash": activation.folder_hash(raw_files), "skillPath": f"skills/{name}/SKILL.md"}
        lock_path.write_bytes(activation.encode(lock))

    def prepare(self):
        return activation.plan(self.project, self.request, self.staged)

    def install(self):
        activation.apply(self.project, self.prepare())

    def assertBlocked(self, text, function=None):
        with self.assertRaisesRegex(ValueError, text):
            (function or self.prepare)()

    def test_installer_command_is_pinned_selected_and_project_local(self):
        argv = activation.installer_command(self.request)
        self.assertEqual(argv[:5], ["npx", "--yes", "skills@1.7.2", "add", "Acrazie/skills#" + "a" * 40])
        self.assertEqual(argv[5:], ["--skill", SKILL, "--agent", "codex", "--agent", "claude-code", "--yes"])
        self.assertNotIn("--global", argv)
        self.assertNotIn("--all", argv)

    def test_plan_is_read_only(self):
        self.prepare()
        self.assertEqual(sorted(p.name for p in self.project.iterdir()), [".git"])

    def test_install_metadata_links_binary_and_config(self):
        original = (self.staged / ".agents/skills" / SKILL / "SKILL.md").read_bytes()
        self.install()
        folder = self.project / ".agents/skills" / SKILL
        self.assertIn("disable-model-invocation: true", (folder / "SKILL.md").read_text())
        self.assertIn("allow_implicit_invocation: false", (folder / "agents/openai.yaml").read_text())
        self.assertEqual((folder / "asset.bin").read_bytes(), b"\x00binary\xff")
        self.assertEqual((self.staged / ".agents/skills" / SKILL / "SKILL.md").read_bytes(), original)
        self.assertEqual(os.readlink(self.project / ".claude/skills" / SKILL), f"../../.agents/skills/{SKILL}")
        self.assertEqual(os.readlink(self.project / "CLAUDE.md"), "AGENTS.md")
        config = activation.read_json(self.project / activation.CONFIG)
        self.assertEqual(config["source_revision"], "a" * 40)
        self.assertIn(f".agents/skills/{SKILL}/SKILL.md", config["_managed"]["files"])
        raw = {p.relative_to(folder).as_posix(): activation.file(p.read_bytes()) for p in folder.rglob("*") if p.is_file()}
        lock = activation.read_json(self.project / "skills-lock.json")
        self.assertEqual(lock["skills"][SKILL]["computedHash"], activation.folder_hash(raw))
        self.assertNotEqual(lock["skills"][SKILL]["computedHash"], config["_managed"]["source_hashes"][SKILL])
        self.assertFalse((self.project / ".acrazie/activation.lock").exists())

    def test_repeat_is_noop(self):
        self.install()
        self.assertEqual(self.prepare()["operations"], [])
        persisted = activation.read_json(self.project / activation.CONFIG)
        del persisted["_managed"]
        self.assertEqual(activation.plan(self.project, persisted, self.staged)["operations"], [])

    def test_staging_bytes_must_match_lock_hash(self):
        (self.staged / ".agents/skills" / SKILL / "asset.bin").write_bytes(b"unexpected")
        self.assertBlocked("content/hash mismatch")

    def test_partial_failure_does_not_claim_completion_or_rollback(self):
        prepared = self.prepare()
        replace = activation.os.replace
        writes = 0

        def fail_second(*args):
            nonlocal writes
            writes += 1
            if writes == 2:
                raise OSError("simulated write failure")
            return replace(*args)

        with patch.object(activation.os, "replace", fail_second):
            self.assertBlocked("completed paths.*no automatic rollback", lambda: activation.apply(self.project, prepared))
        self.assertFalse((self.project / activation.CONFIG).exists())
        self.assertFalse((self.project / ".acrazie/activation.lock").exists())
        self.assertTrue(any(self.project.glob(".acrazie/*")))

    def test_preserve_independent_instructions_and_personalization(self):
        (self.project / "AGENTS.md").write_text("# Existing\nNever push main.\n")
        (self.project / "CLAUDE.md").write_text("# Claude-specific\nKeep this.\n")
        self.install()
        self.assertTrue((self.project / "CLAUDE.md").is_file())
        self.assertFalse((self.project / "CLAUDE.md").is_symlink())
        self.assertTrue((self.project / "AGENTS.md").read_text().startswith("# Existing\nNever push main.\n"))
        with (self.project / "AGENTS.md").open("a") as output:
            output.write("\nA new personal rule.\n")
        self.assertEqual(self.prepare()["operations"], [])

    def test_external_claude_link_blocked(self):
        external = self.root / "external.md"
        external.write_text("Untouched")
        (self.project / "CLAUDE.md").symlink_to(external)
        self.assertBlocked("External or independent")
        self.assertEqual(external.read_text(), "Untouched")

    def test_managed_skill_customization_blocks_update(self):
        self.install()
        (self.project / ".agents/skills" / SKILL / "SKILL.md").write_text("Custom")
        self.assertBlocked("Customized managed asset")

    def test_new_unowned_file_in_package_blocks(self):
        self.install()
        (self.project / ".agents/skills" / SKILL / "extra.py").write_text("Custom")
        self.assertBlocked("Unowned file inside")

    def test_customized_block_blocks(self):
        self.install()
        path = self.project / "AGENTS.md"
        path.write_text(path.read_text().replace("## Acrazie engineering", "## Changed"))
        self.assertBlocked("Customized managed block")

    def test_unowned_marker_blocks(self):
        (self.project / "AGENTS.md").write_text(activation.START + "\nold\n" + activation.END)
        self.assertBlocked("Unowned managed markers")

    def test_unowned_collision_blocks(self):
        folder = self.project / ".agents/skills" / SKILL
        folder.mkdir(parents=True)
        (folder / "SKILL.md").write_text("Unrelated existing skill")
        self.assertBlocked("Unowned asset collision")

    def test_missing_staging_lock_blocks(self):
        (self.staged / "skills-lock.json").unlink()
        self.assertBlocked("lock selection")

    def test_wrong_revision_blocks(self):
        self.stage(SKILL, "b" * 40)
        self.assertBlocked("Unverified source/ref/hash")

    def test_staging_extra_skill_blocks(self):
        self.stage("interview-acrazie")
        self.assertBlocked("selection differs")

    def test_staging_fallback_copy_blocks(self):
        link = self.staged / ".claude/skills" / SKILL
        link.unlink()
        link.mkdir()
        self.assertBlocked("local link")

    def test_internal_package_symlink_blocks(self):
        (self.staged / ".agents/skills" / SKILL / "leak").symlink_to(self.project)
        self.assertBlocked("Symlink inside")

    def test_symlink_parent_cannot_write_outside(self):
        external = self.root / "outside"
        external.mkdir()
        (self.project / ".agents").symlink_to(external)
        self.assertBlocked("Symlink parent")
        self.assertEqual(list(external.iterdir()), [])

    def test_existing_other_lock_entries_preserved(self):
        lock_path = self.project / "skills-lock.json"
        lock_path.write_bytes(activation.encode({"version": 1, "skills": {"other-skill": {"source": "Elsewhere", "ref": "v1"}}}))
        self.install()
        lock = activation.read_json(lock_path)
        self.assertEqual(lock["skills"]["other-skill"], {"source": "Elsewhere", "ref": "v1"})
        lock["skills"]["third-skill"] = {"source": "Another"}
        lock_path.write_bytes(activation.encode(lock))
        self.assertEqual(self.prepare()["operations"], [])

    def test_unowned_lock_collision_blocks(self):
        (self.project / "skills-lock.json").write_bytes(activation.encode({"version": 1, "skills": {SKILL: {"source": "Elsewhere"}}}))
        self.assertBlocked("Unowned lock collision")

    def test_lock_entry_customization_blocks(self):
        self.install()
        path = self.project / "skills-lock.json"
        lock = activation.read_json(path)
        lock["skills"][SKILL]["ref"] = "b" * 40
        path.write_bytes(activation.encode(lock))
        self.assertBlocked("Customized lock entry")

    def test_stale_plan_blocks_before_writes(self):
        prepared = self.prepare()
        (self.project / "AGENTS.md").write_text("Written concurrently")
        self.assertBlocked("Stale plan", lambda: activation.apply(self.project, prepared))
        self.assertFalse((self.project / ".agents").exists())
        self.assertEqual((self.project / "AGENTS.md").read_text(), "Written concurrently")

    def test_wrong_project_identity_blocks(self):
        prepared = self.prepare()
        prepared["project"] = str(self.root)
        self.assertBlocked("Wrong plan", lambda: activation.apply(self.project, prepared))

    def test_helper_lock_blocks_second_writer(self):
        prepared = self.prepare()
        lock = self.project / ".acrazie/activation.lock"
        lock.parent.mkdir()
        lock.touch()
        with self.assertRaises(FileExistsError):
            activation.apply(self.project, prepared)
        self.assertTrue(lock.exists())

    def test_update_and_deselection_remove_only_owned_assets(self):
        self.stage("interview-acrazie")
        self.request["skills"].append("interview-acrazie")
        self.install()
        self.request["skills"] = ["interview-acrazie"]
        self.request["source_revision"] = "b" * 40
        removed = self.staged / ".agents/skills" / SKILL
        import shutil
        shutil.rmtree(removed)
        (self.staged / ".claude/skills" / SKILL).unlink()
        (self.staged / "skills-lock.json").unlink()
        self.stage("interview-acrazie")
        self.install()
        self.assertFalse((self.project / ".agents/skills" / SKILL / "SKILL.md").exists())
        self.assertFalse((self.project / ".claude/skills" / SKILL).is_symlink())
        self.assertEqual(set(activation.read_json(self.project / "skills-lock.json")["skills"]), {"interview-acrazie"})

    def test_changed_policy_source_blocks(self):
        path = self.project / "git-policy.md"
        path.write_text("Confirm push")
        self.request["policy_sources"] = {"git-policy.md": activation.digest(path.read_bytes())}
        path.write_text("Forbidden push")
        self.assertBlocked("Policy changed")

    def test_instruction_policy_hash_survives_managed_block(self):
        (self.project / "AGENTS.md").write_text("# Existing\nNo push.\n")
        self.request["policy_sources"] = {"AGENTS.md": activation.policy_hash(self.project, "AGENTS.md")}
        self.install()
        self.assertEqual(self.prepare()["operations"], [])

    def test_permission_validation_and_no_automatic_actions(self):
        rule = {"mode": "preauthorized", "repository": "https://github.com/Acrazie/example", "branches": ["codex/example"], "destinations": ["local"], "checks": ["python3 -m unittest"]}
        self.request["permissions"]["commit"] = rule
        self.install()
        history = subprocess.run(["git", "-C", str(self.project), "rev-parse", "--verify", "HEAD"], capture_output=True)
        self.assertNotEqual(history.returncode, 0)
        invalid = copy.deepcopy(self.request)
        invalid["permissions"]["push"] = {"mode": "preauthorized"}
        self.assertBlocked("Incomplete", lambda: activation.validate_request(invalid))
        invalid = copy.deepcopy(self.request)
        invalid["permissions"]["commit"]["branches"] = ["*"]
        self.assertBlocked("exact branches", lambda: activation.validate_request(invalid))
        invalid = copy.deepcopy(self.request)
        invalid["skills"] = ["../escape-acrazie"]
        self.assertBlocked("Invalid", lambda: activation.validate_request(invalid))

    def test_duplicate_json_keys_and_unknown_fields_block(self):
        path = self.root / "bad.json"
        path.write_text('{"permissions":{},"permissions":{}}')
        self.assertBlocked("Duplicate", lambda: activation.read_json(path))
        self.request["automerge"] = True
        self.assertBlocked("Unsupported configuration")

    def test_question_contract_and_scope_are_explicit(self):
        reference = SCRIPT.parents[1] / "references/engineering-activation.md"
        text = reference.read_text()
        template = text.split("```text\n", 1)[1].split("```", 1)[0]
        fields = [line.split(":", 1)[0] for line in template.splitlines() if ":" in line]
        self.assertEqual(fields, ["Current state", "Options", "Recommendation", "Response"])
        self.assertIn("1. …\n2. …", template)
        normalized = " ".join(text.lower().split())
        for term in ("not verified", "implicit-enabled homonym blocks", "do not modify", "not an atomic multi-file transaction", "disable the Skills API", "exact resulting changes"):
            self.assertIn(term.lower(), normalized)

    def test_bounded_yaml_adapter_rejects_duplicate_identity_and_policy(self):
        self.assertBlocked("identity", lambda: activation.explicit_skill(f"---\nname: {SKILL}\nname: other-acrazie\ndescription: Test\n---\n", SKILL))
        self.assertBlocked("Duplicate Codex", lambda: activation.explicit_codex("policy:\npolicy:\n"))
        self.assertBlocked("Unsupported Codex", lambda: activation.explicit_codex("policy: {allow_implicit_invocation: true}\n"))

    def test_cli_approved_hash_and_apply(self):
        request_path, plan_path = self.root / "request.json", self.root / "plan.json"
        request_path.write_bytes(activation.encode(self.request))
        preview = subprocess.run([sys.executable, str(SCRIPT), "plan", "--request", str(request_path), "--project", str(self.project), "--staged", str(self.staged), "--output", str(plan_path)], capture_output=True, text=True)
        self.assertEqual(preview.returncode, 0, preview.stderr)
        sha = json.loads(preview.stdout)["plan_sha256"]
        args = [sys.executable, str(SCRIPT), "apply", "--project", str(self.project), "--plan", str(plan_path), "--approved-sha256"]
        denied = subprocess.run([*args, "0" * 64], capture_output=True, text=True)
        self.assertNotEqual(denied.returncode, 0)
        self.assertFalse((self.project / ".agents").exists())
        accepted = subprocess.run([*args, sha], capture_output=True, text=True)
        self.assertEqual(accepted.returncode, 0, accepted.stderr)
        self.assertEqual(self.prepare()["operations"], [])


if __name__ == "__main__":
    unittest.main()
