# Project-local engineering activation

This mode activates an approved, versioned kit for **Codex + Claude Code** without
scaffolding an existing repository. It uses the existing Skills CLI in disposable
staging and a bundled plan/apply helper for preservation and conflict checks.
No dedicated CLI product, global links, remote administration or Git delivery.

## 1. Discover and interview

Inspect the exact project/root/worktree, applicable instructions, available skills,
existing `.acrazie/engineering.json`, `skills-lock.json`, `.agents/skills`,
`.claude/skills`, `AGENTS.md`, `CLAUDE.md`, Git workflow, protections, hooks and
unrelated changes. Do not assume absent evidence is permission. Check Node/npm,
Git and Python availability before proposing execution; do not install runtimes
silently. The helper needs Python >=3.10 and Node for the upstream folder-hash
ordering. Skills CLI 1.7.2 documents Node >=22.20.0.

Use the project's actual facts to prune questions. For each unresolved decision,
display **only** these four fields, in the user's language:

```text
Current state: …
Options:
1. …
2. …
Recommendation: option N — reason.
Response: …
```

Do not add ID/Decision fields or preselect an answer as consent. Recompute the
frontier rather than force a fixed number of rounds. Inspect facts yourself.

Propose Interview + Feature Builder as an adaptable engineering core. Offer Test
Retrofitter, Adversarial Reviewer and Git Ship according to needs, then existing
stack specialists and visual satellites. Resolve exact available names from the
approved source, not an invented fixed inventory. Explain conditional/mandatory
dependencies and unavailable bug-fix/refactor workflows. The user can select a
subset; an absent mandatory dependency blocks its workflow step, not unrelated
tasks. Do not activate another skill during this interview without its explicit
user invocation.

Import existing action rules, including staging, commit, push, PR creation/update,
merge and deployment. Preserve conventions and safeguards. Show conflicting
sources and consequences, then wait for an explicit resolution; do not change
existing policy merely to make it match a proposed JSON file. Unknown/absent
permissions default to a **proposal** of confirmation, never silent approval.

## 2. Prepare the approved request

Read [engineering-configuration.md](engineering-configuration.md) for the exact
schema. Use `.acrazie/engineering.json` as the structured kit/action policy source
and reconcile other Git documents before activation. Policy remains readable
without invoking any skill. Keep the request in a private temporary directory
outside the target until approval; do not put secrets in it or an approval label
that could be mistaken for actual user authorization.

Record the exact 40-character source commit, pinned installer version, selected
skills, both hosts, separate action modes, bounded preauthorization conditions and
hashes of preserved policy sources. The source is `Acrazie/skills`. Verify source
availability and current installer documentation; never silently substitute a
branch, tag, local checkout or installer version when the approved pin fails.

Present a consolidated blueprint: target project, source revision, installer and
runtime requirements, selected skills/dependencies, versions, permissions and
resolved policy conflicts, expected tracked files, local links and preservation
strategy. Disclose external package execution and network/cache effects. Obtain
approval of staging downloads/execution and the intended project changes. If
discovery finds material differences, reopen only those decisions.

## 3. Stage with the existing installer

Create an empty disposable directory **outside** the target project. Obtain argv
without shell interpolation using the helper:

```bash
python3 <this-skill>/scripts/engineering_activation.py installer-command --request <approved-request.json>
```

The JSON array describes a command of this form, executed only after approval,
with the staging directory as CWD:

```bash
npx --yes skills@1.7.2 add 'Acrazie/skills#<approved-full-SHA>' \
  --skill interview-acrazie --skill feature-builder-acrazie \
  --agent codex --agent claude-code --yes
```

Use the request's exact version/selection, not this example blindly. The first
`--yes` belongs to npm, the last to Skills CLI. Neither is an authorization gate;
the CLI can also detect agents and skip prompts automatically. Never use `--all`,
`--global`, or run the installer/update directly in an existing target: upstream
installation removes/recreates canonical directories.

Minimize network side effects with `DISABLE_TELEMETRY=1` or `DO_NOT_TRACK=1` when
executing approved staging. **Disclose that these also disable the Skills API
security audit, not just telemetry.** npm/Git still use the network. Exact package
pinning does not freeze all transitive npm dependencies. No external security
audit is claimed by this workflow; required project security checks still apply.

CLI exit 0 does not prove valid output: lock-writing errors can be ignored. The
helper requires the exact canonical selection, Claude local symlinks, complete
packages and a valid project lock with matching GitHub source/ref and recomputed
folder hashes. Fallback copies are rejected, not silently accepted. A pinning,
layout or metadata mismatch is a blocker.

## 4. Plan the target integration

```bash
python3 <this-skill>/scripts/engineering_activation.py plan \
  --request <approved-request.json> --project <project-root> \
  --staged <staging-directory> --output <private-new-plan.json>
```

Planning is read-only for the target. It creates a private, new plan outside the
project and prints its SHA-256 plus paths/actions. Review the actual contents/diff,
not just this summary. The plan includes binary payloads and preserved instruction
content; keep it private and do not commit or dump it into logs.

Expected project artifacts:
- `.acrazie/engineering.json`: approved choices and managed ownership fingerprints;
- `.acrazie/engineering-catalog.md`: names, scope descriptions and explicit commands,
  so routing can happen without loading skill bodies;
- `.agents/skills/<selected-skill>/`: canonical, tracked packages;
- `.claude/skills/<selected-skill>`: relative links to those canonical packages;
- `skills-lock.json`: selected entries merged without losing unrelated entries;
- a marked block in `AGENTS.md`, and `CLAUDE.md` handling below.

Installed copies receive `disable-model-invocation: true` and
`policy.allow_implicit_invocation: false`. Published source metadata remains
unchanged: this is a scoped project adapter, not a global invocation-policy change.
The adapter supports the published Acrazie frontmatter and flat Codex policy
layout, rejects unsupported/ambiguous layouts, and is not an arbitrary YAML parser.
Source hashes are retained separately; the merged lock hashes the **adapted**
installed content using upstream Node collation so it does not misrepresent bytes.

Preserve instruction text outside the managed block. An independent `CLAUDE.md`
receives its own block; an existing relative link to root `AGENTS.md` stays intact.
When absent, create that relative link. An external/different symlink, malformed
markers, unowned collisions, modified managed blocks/files, unexpected package
files, policy drift or changed lock entries block integration. Do not repair
these by overwriting, backing up and replacing, or adopting them silently.

Show the exact resulting changes and plan SHA. A materially changed blueprint,
unanticipated instruction edit or new permission needs renewed approval. For an
unchanged, fully covered blueprint, record that its approval covers this exact
plan; never treat a hash or generated status label alone as consent.

## 5. Apply, verify, and report

```bash
python3 <this-skill>/scripts/engineering_activation.py apply \
  --project <project-root> --plan <reviewed-plan.json> \
  --approved-sha256 <approved-plan-SHA256>
```

The hash guards the approved snapshot, not the origin of approval. The helper
validates project identity and all prior states, excludes concurrent helper runs
with a cooperative lock, rechecks before each mutation, writes files by atomic
replacement, verifies readback, and writes the configuration last. It performs
no Git operations and executes no configured validation commands.

This is **not an atomic multi-file transaction** and cannot lock external editors.
After interruption, preserve the plan and observed partial state; report completed
paths and obtain a scoped recovery decision. Never blindly replay, force-remove
the lock, or roll back over another writer. A stale lock needs inspection and
specific recovery authorization. Locks are transient, not tracked artifacts.

Updates or changes to the selected kit reuse the same explicit review/plan flow.
Unchanged reapplication is a no-op; only unchanged owned assets/lock entries can
be updated or removed. New local files inside a managed package count as
customization. Personalization outside instruction blocks is preserved. Do not
install missing dependencies or enable new permissions as an update side effect.

Report exact installed revision/selection, files/links, preserved/customized items,
configured action modes, local checks, failures and remaining work. Explain that
natural requests now produce a proposal: users activate `$skill-name` in Codex or
`/skill-name` in Claude, including each dependency. Flags prevent native autonomous
invocation but are not filesystem access controls. Existing global skills and
homonyms may still be discoverable. Inspect applicable host roots/available skill
metadata before activation; an implicit-enabled homonym blocks a strict project
gate until its resolution is separately approved and observed. Do not modify
global installations or claim exclusive routing from an incomplete inventory.
Live host behavior is **not verified** by the offline tests.
Git staging/commit/push/PR, actual merge and deployment remain separate actions.

## Automated validation

```bash
PYTHONDONTWRITEBYTECODE=1 python3 skills/github-repo-init-acrazie/scripts/test_engineering_activation.py
```

Tests use temporary Git repositories, simulated upstream staging and real helper
plan/apply operations. They do not run Codex/Claude, external installer downloads,
remote mutations or delivery operations. Preserve this distinction in reports.

## Sources verified for the first implementation

- [Skills CLI 1.7.2 metadata](https://registry.npmjs.org/skills/1.7.2)
- [Versioned installer](https://github.com/vercel-labs/skills/blob/671e8c320810d36fed80fac5f1a2c1bf7e82d812/src/installer.ts)
- [Versioned add command](https://github.com/vercel-labs/skills/blob/671e8c320810d36fed80fac5f1a2c1bf7e82d812/src/add.ts)
- [Versioned local lock/hash](https://github.com/vercel-labs/skills/blob/671e8c320810d36fed80fac5f1a2c1bf7e82d812/src/local-lock.ts)
- [Telemetry/audit behavior](https://github.com/vercel-labs/skills/blob/671e8c320810d36fed80fac5f1a2c1bf7e82d812/src/telemetry.ts)
- [OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code skill documentation](https://code.claude.com/docs/en/skills)

Refresh current documentation with Context7 when adapting library/CLI syntax or
host setup. A source/reference check is not proof of a live host outcome.
