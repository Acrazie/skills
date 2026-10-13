# ADR 0012: Retire generic feature and script execution packages

## Status

Accepted by the user on 2026-10-13: Q1 option 1, Q2 option 1; subsequent
approval of the Lot 4 migration scope. Implementation remains uncommitted.
Supersedes ADR 0003's separate Feature Builder ownership only; Interview's
preparation boundary and independent review separation remain intact.

## Context

Ordinary feature implementation does not justify another generic execution
package when an approved Interview contract and a capable harness already cover
it. Selected-script portability has concrete assessment guarantees, but does not
need its own audit-plus-implementation orchestrator. Deleting packages without
transferring proof and authorization boundaries would be a regression.

## Decision

Retire `feature-builder-acrazie` and `script-portability-acrazie` without aliases.
Interview remains preparation-only. Its existing Task Contract handoff carries
criterion-linked tests, final-snapshot evidence, review offer/explicit choice and
accepted/policy-required independent-review gates to a capable authorized executor.
No hidden implementation workflow or new harness graph node is introduced.

Audit Repository conditionally owns selected-script portability assessment and
its preservation/matrix/native-proof guarantees. It remains read-only and provides
recommendations and an executor handoff, not refactoring authority. Realization,
installation, destructive fixtures, Git shipping and deployment remain separately
authorized. Keep compatibility helpers where equivalence is unproven; no mandatory
runtime switch, helper purge or universal overhead claim.

## Alternatives and consequences

Keeping both packages preserves familiar commands but duplicates ordinary harness
execution and increases lifecycle cost. Simply deleting them loses safety/evidence
coverage. Moving all execution into Interview or Audit distorts their ownership.
The chosen consolidation transfers acceptance obligations to existing responsible
boundaries while preserving domain-specific specialists.

Current package consumers, tests and defined eval scenarios migrate. Historical
specs, ADRs and changelog evidence are not rewritten. Existing global installations,
links and pinned project kits are not automatically changed; installations on older
revisions may still expose retired names until separately authorized migration.

## Evidence and limits

See [approved scope](../specs/execution-consolidation.md). Instruction regression
checks and portal builds cannot certify cross-harness execution, runtime portability
or native Windows behavior. Local proof, independent review and publication are
separate gates; delivery evidence must report their actual state.
