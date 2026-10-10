---
name: script-portability-acrazie
description: >-
  Audit, refactor, and harden cross-platform automation commands and package scripts (package.json,
  shell scripts) across Linux, macOS, and Windows. Eliminate brittle polyfills (rimraf, cross-env,
  shx), remove subprocess spawning overhead, and prevent shell command injection. Use when scripts
  fail on Windows runners, build steps contain OS-specific syntax, or projects seek to slim down
  developer tooling dependencies. Not for whole-toolchain upgrades or Jenkins pipeline authoring.
---

# Script Portability & Shell Hardening / Acrazie

Improve selected scripts across the approved target OS/shell/runner matrix while
preserving required behavior, error propagation and filesystem boundaries. Keeping
an existing compatible helper can be the correct outcome; modernization is not the goal.

## Project loading boundary

Published-library defaults remain model-invocable within the requested task. An
explicit project kit or stricter current instruction takes precedence: propose
this skill from available metadata and wait for the user's explicit command before
reading its instructions. Apply the same gate to each dependency before reading
or dispatching its instructions; one invocation does not activate a chain.
Use `$skill-name` in Codex or `/skill-name` in Claude Code. These gates are not
filesystem access controls or proof of live host behavior. Global homonyms may
remain a blocker. Do not read or delegate an unactivated skill as a bypass.
Loading grants no editing, installation, network, spawning or shipping permission.
Ordinary library defaults retain scoped implicit handoffs; no new mandatory
Interview dependency is introduced. Keep this specialist's bounded clarification.

## User decision format

For any user-owned choice, display only Current state, numbered Options,
Recommendation and Response. Translate labels/content into the user's language;
do not add question IDs, preselect an answer as consent or treat a recommendation
as approval. Ask only unresolved decisions with verified facts, not a fixed survey.
Reports and code diffs retain their own structures.

## Scope and portability invariants

- Inspect selected scripts and only the callers, dependencies and CI needed to
  trace their behavior. Do not turn a single-script request into a whole-repository
  rewrite, runtime migration or Jenkins pipeline task.
- Preserve approved inputs, outputs, side effects, working-directory/environment
  semantics and success/failure exit codes across the targeted environments.
  If preservation cannot be demonstrated, disclose the gap and block the affected
  change rather than inventing equivalence.
- Polyfills such as `rimraf`, `cross-env`, `shx`, `mkdirp` and `which` are
  candidates, not mandatory removals. Native or installed replacements must fit
  supported runtimes and actual semantics before removal is proposed.
- Avoid shell-string concatenation with untrusted data. Use parameterized APIs or
  supported template escaping; escaping shell syntax does not validate executable
  options, paths, permissions or downstream behavior. Preserve those trust boundaries.
- Prefer fitting native or installed capabilities. Avoid unnecessary shell layers,
  but do not equate an in-process shell with no child process for external programs
  or claim universal latency savings without comparable measurements.
- Cleanup is bounded to approved paths and behavior; recursive/force deletion is
  never a universal requirement. Preserve unrelated work and inspect path/symlink
  effects before proposing filesystem mutations.
- Do not commit, push, create PRs, merge or deploy under this workflow.

## Phase 1: Read-only inventory and contract

Start with read-only discovery of repository instructions, Git state, selected
scripts, callers, runtime/package-manager versions, manifests/lockfiles, actual
shells/runners and relevant existing tests. Do not run unfamiliar scripts just to
inspect them. Read [references/portable-scripting-guide.md](references/portable-scripting-guide.md)
for hazard categories; its examples are illustrations, not certification of runtime
recipes. Consult current documentation and test compatibility before applying one.

Reuse an applicable current agreement with approval evidence beyond a status label.
It must cover selected paths, target matrix, preserved behavior, changes allowed,
checks and write scope. Reopen only materially invalidated decisions through this
specialist's clarification; no duplicate Interview or persisted contract for ceremony.
If needed, propose these unresolved decisions and obtain explicit scoped realization
approval before editing. Approval of a strategy alone is not execution permission.

Do not execute destructive tests, access network or synchronize/install dependencies
without their applicable separate approval. Do not assume a dry-run is non-mutating.
An unavailable required dependency blocks its dependent step, not unrelated discovery.
In a managed kit, missing skills use separately approved Repo Init project updates
and pinned selection after its own activation, not copied or unpinned substitutes.

## Phase 2: Choose and approve the strategy

Compare keeping the current script/helper with a native or installed replacement
fitting the supported runtime and target shells. Do not introduce Bun or upgrade
Node merely to remove a helper. Trace environment precedence, quoting, option-like
inputs, wildcard/path handling, symlinks, cleanup idempotency and failure propagation
where relevant. List exact affected scripts, dependency removals, checks and risks.
Obtain approval for the scoped plan and realization if not already independently
covered by a current agreement. New dependencies, runtime changes or new objectives
require separately approved scope; do not silently expand this workflow.

## Phase 3: Implement the approved changes

Use required repository isolation and preserve unrelated work. Update only approved
scripts and necessary manifests/lockfiles. Remove a helper only after its replacement
covers required behavior and compatibility; retaining it is valid when proof is absent.
Lockfile synchronization must use the repository's package manager and a separately
authorized installation/update command. Do not install tools or update unrelated
versions from refactor approval. Do not bypass hooks or policy to finish the task.

## Phase 4: Verify and report

Use the smallest sufficient checks for affected behavior and relevant regressions.
Tests cover approved success/error outcomes and side effects without operating on
real user data; obtain any required permission for temporary destructive fixtures.
Record actual OS, shell, runtime, runner, command, snapshot, exit result and limits.
Syntax inspection or emulation is not native OS execution. Any unexecuted target is
not verified; disclose unavailable checks and do not declare the full matrix passed.
A required missing proof blocks dependent completion, not a reason to weaken criteria.

Record comparable measurements only when actually performed, with baseline and
workload. Otherwise performance/dependency impacts are hypotheses or not measured;
never invent package counts, disk savings, subprocess counts or timings.

Report in chat by default. A file such as `script-portability-report.md` is optional:
show exact content and destination and obtain approval before writing. Never overwrite
an unrelated report. Do not present recommendations as completed refactors.

## Deliverable format

```markdown
# Script Portability & Shell Hardening Report

## Scope and authority
- Selected scripts/manifests, repository snapshot and exclusions:
- Approved target OS/shell/runtime/runner matrix:
- Scope/realization approval evidence and separately permitted actions:

## Hazards and selected strategy
- Observed hazard, source and impact:
- Options compared, including keeping current helpers:
- Approved changes and preserved behavior:

## Changes and dependency decisions
- Actual changed paths/diff, retained or removed helpers and rationale:
- Manifest/lockfile actions actually authorized and performed:

## Validation and limits
- Actual commands, environments, inputs, exit codes and side-effect checks:
- Required checks passed, failed, unavailable or not verified:
- Comparable measured impact, or not measured:
- Remaining risks and next authorized step:
```

Keep this report factual: static instruction tests do not prove runtime portability
or safety, and loading flags do not prove host behavior. No automatic shipping.
