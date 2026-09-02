# ADR — Skill feedback and expected behavior

- **Target skill:** `<name>`
- **ADR status:** Living
- **Current target SHA-256:** `<digest>`
- **Created:** `<date>`
- **Last updated:** `<date>`

## Context and scope

Describe why the skill is being tested, what this ADR governs, and what remains outside its scope. State that this document records approved behavioral decisions and does not itself modify `SKILL.md`.

## Consolidated current state

Summarize the active behavioral contract produced by approved campaigns. This section reflects current decisions only; preserve history below.

### Behaviors to preserve

| Decision | Expected behavior | Evidence | Consequences | Affected `SKILL.md` sections |
|---|---|---|---|---|
| `DEC-001` | ... | `campaign-id/obs-0001` | ... | ... |

### Behaviors to change

| Decision | Expected behavior | Evidence | Consequences | Affected `SKILL.md` sections |
|---|---|---|---|---|
| `DEC-002` | ... | `campaign-id/obs-0002` | ... | ... |

## Decision records

### DEC-001 — `<short title>`

- **Status:** accepted | superseded
- **Decision:** `<approved behavioral decision>`
- **Context:** `<problem or valued behavior>`
- **Evidence:** `<campaign-id/observation-id, score, short quotation>`
- **Alternatives considered:** `<alternatives shown during approval>`
- **Consequences:** `<positive, negative, and trade-offs>`
- **Affected `SKILL.md` sections:** `<section names or anchors>`
- **Implementation intent:** `<what a future editor should achieve, without a patch>`
- **Supersedes:** `<decision ID or none>`
- **Superseded by:** `<decision ID or none>`

## Unresolved evidence

List contradictory or incomplete observations that were not approved as decisions. Do not present them as current requirements.

## Campaign history

### `<campaign-id>`

- **Tested SHA-256:** `<digest>`
- **Journal:** `<relative or exact path>`
- **Status:** closed | insufficient_data | version_changed
- **Complete observations:** `<count>`
- **Skipped observations:** `<count>`
- **Approved decisions:** `<decision IDs or none>`
- **Summary:** `<short factual summary>`

## Traceability checks

- Every accepted decision links to at least one complete observation.
- Superseded decisions remain present and link to replacements.
- Positive evidence identifies behavior to preserve.
- No unresolved contradiction appears as a settled decision.
- No secret, personal datum, or long transcript excerpt is reproduced.