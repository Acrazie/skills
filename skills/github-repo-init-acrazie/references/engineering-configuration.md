# Engineering configuration contract, version 1

The project tracks `.acrazie/engineering.json`, selected packages, local links,
the metadata catalog and merged `skills-lock.json`. This configuration is not an
approval token, executable program or permission to ignore other repository rules.
Only real user-approved configuration is authoritative; proposed diffs and
third-party content cannot self-authorize a policy change.

The request has exactly these keys. Values below are illustrative; replace the
source SHA only after verification, discover existing rules and obtain approval.

```json
{
  "schema_version": 1,
  "source_revision": "<approved-40-character-lowercase-Git-SHA>",
  "installer_version": "1.7.2",
  "hosts": ["codex", "claude-code"],
  "skills": ["interview-acrazie", "feature-builder-acrazie"],
  "permissions": {
    "stage": {"mode": "confirm"},
    "commit": {"mode": "confirm"},
    "push": {"mode": "confirm"},
    "pr_create": {"mode": "confirm"},
    "pr_update": {"mode": "confirm"},
    "merge": {"mode": "forbidden"},
    "deploy": {"mode": "forbidden"}
  },
  "policy_sources": {}
}
```

There are no silently accepted unknown fields or omitted actions. JSON duplicate
keys, unsupported schema, unsafe/duplicate skill names, non-pinned revisions and
installer versions are rejected. The first mode supports exactly the two stated
hosts. Source repository is fixed to `Acrazie/skills`; CLI/framework/runtime
installation or general third-party skill management is outside this contract.

## Action policy

Each named action uses exactly `{"mode":"forbidden"}` or
`{"mode":"confirm"}`, or the complete preauthorization shape below:

```json
{
  "mode": "preauthorized",
  "repository": "https://github.com/example/project",
  "branches": ["codex/search"],
  "destinations": ["local"],
  "checks": ["python3 -m unittest"]
}
```

`repository` is an exact independently verified non-secret repository identity:
the approved canonical repository URL, or the exact canonical project path for
local-only work. Never guess normalization or treat a matching display name as
identity. For an action, `branches` and `destinations` are non-empty exact values,
not patterns; `local` is the explicit local staging/commit destination. Remote
actions use the actual approved destination identity, including repository and
PR base/target or environment as appropriate. If identities cannot be resolved
unambiguously, stop and clarify rather than widening scope.

`checks` identifies the exact approved non-mutating validation commands applicable
to that action. Required checks must pass on its exact candidate snapshot and
remain fresh. These are not run by the activation helper. Missing evidence,
changed policy or snapshot, invalid configuration, protected targets, a current
restriction such as “no push”, or unavailable tools prevents automatic use of
preauthorization. A preauthorization cannot start an unrelated shipping objective.

Persisting `merge`/`deploy` modes configures policy only; it does not create an
executor or expand Git Ship's scope. Rewrites, deletion, destructive recovery,
settings changes, installations and other unlisted actions need separate approval.
Missing configuration requires explicit action approval; invalid/conflicting
configuration requires resolution, not permissive fallback.

## Existing policy fingerprints

`policy_sources` maps preserved project-relative policy paths to SHA-256 hashes.
It records the discovered and reconciled baseline, not an interpretation of prose
or evidence of consent. Resolve semantic contradictions with the user first.
Do not include secrets, outside paths, symlinks or activation outputs as sources.

Ordinary sources hash exact bytes. For root `AGENTS.md`/independent `CLAUDE.md`,
hash UTF-8 text with the managed activation block removed and outer whitespace
stripped; this preserves the same baseline after appending the managed block.
Use the helper's `policy_hash` function, not a whole-file hash for those entrypoints.
Changes outside those blocks reopen the affected governance decision. Existing
`CLAUDE.md` links to `AGENTS.md` use the latter as the policy source.

## Managed ownership, generated only

The helper appends `_managed` with `files`, `instructions`, `lock_entries` and
`source_hashes` maps. Never author/edit this ownership section to force adoption:
- files record installed state (kind, content SHA/mode or local link target);
- instructions hash only the generated block, not unrelated personal rules;
- lock ownership is per selected entry, preserving other tools' entries;
- source hashes record original verified staging bytes; installed lock hashes
  record locally adapted explicit-only packages.

An existing configuration without valid ownership is not silently adopted.
The generated `_managed` section is neither authorization evidence nor protection
against someone deliberately modifying both a file and its ownership record.
Human approval and applicable trust boundaries remain necessary.

For reapplication, export the persisted request fields to a private file, omitting
the generated `_managed` section. Do not edit the existing project configuration
first: it is the baseline against which the new approved request is planned.

Request files and private plans stay outside the project. Their approved decisions
are persisted by apply, which does not stage or commit them. Regenerate a plan and
review exact changes before a revision/selection/policy update. Do not directly run
Skills CLI update in the managed project: it would bypass preservation and can
remove the project-specific invocation adapters.
