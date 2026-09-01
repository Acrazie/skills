# Audit Record lifecycle

An Audit Record preserves what was examined and decided. It is not an ADR: an audit may end without an architectural decision.

## Discover existing records

Before a new audit, inspect `docs/audits/` and any repository-equivalent convention. Read metadata first, then open records related by scope, topics, components, or decision.

Prioritize `pending` records, but use related resolved records as historical context. Never treat an old conclusion as current without checking affected files, manifests, versions, repository changes since its recorded commit, and dated external sources.

If a pending record overlaps the new request, present:

- common scope and unresolved decisions;
- recorded commit and material repository changes;
- evidence that remains valid or needs revalidation;
- recommended treatment.

Then wait for the user to choose:

- resume it when question and repository state remain comparable;
- create a linked audit when objective, stack, or state changed materially;
- resolve or supersede it only after an explicit user decision.

Do not silently merge, close, supersede, or duplicate records. Comparing current state with the recorded commit measures staleness; it is not a diff or PR review.

## Location and filename

Default to:

```text
docs/audits/YYYY-MM-DD-<concise-scope-slug>.md
```

After write approval, create `docs/` and `docs/audits/` when absent. If an equivalent repository convention exists, present it and ask before deviating from `docs/audits/`. Preserve existing naming conventions. Avoid overwriting; add a meaningful discriminator when a filename collides.

Do not write inside generated documentation. Detect generated-file notices or generated directories and stop the write path when ownership is unclear.

## Metadata

Use YAML frontmatter:

```yaml
---
status: pending
date: 2026-09-01
updated: 2026-09-01
commit: "abc1234"
scope:
  - tooling/pre-commit
topics:
  - linting
  - formatting
supersedes: null
related_audits: []
---
```

Use repository-relative scope values. Use the full commit SHA when practical; use `null` outside Git and explain the missing snapshot in the record.

Statuses:

- `pending`: audit complete, but a decision or follow-up remains unresolved;
- `resolved`: user decision recorded, including a deliberate no-change outcome;
- `superseded`: replaced by a newer linked audit.

Create the record as `resolved` when the user has explicitly settled every resulting decision; otherwise use `pending`. A pending record may be updated as its open decision resolves. Once resolved, freeze it except for clearly identified factual corrections. Later changes get a new linked record.

## Required body

```markdown
# Audit — <precise subject>

## Question
## Scope and exclusions
## Repository state
## Evidence and validations
## Findings
## Alternatives considered
## Elements to preserve
## Decisions confirmed
## Out-of-scope leads
## Limitations
## Follow-up
```

Omit empty optional sections rather than inventing content. `Decisions confirmed` contains only choices explicitly accepted by the user; keep unresolved recommendations visibly pending. Cite external sources with access date and relevant version.

## Approval and write boundary

1. Present the completed audit in chat.
2. Let the user correct findings and confirm decisions.
3. Show the exact proposed record or material update.
4. Ask for explicit approval immediately before writing.
5. Write only the approved Audit Record and any missing parent directories.
6. Show the final diff or file content and validation result.

Do not edit source, configuration, other documentation, ADRs, or Git history. Do not commit.
