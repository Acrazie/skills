# Portable Skill Standard — Pilot

This repository standard applies to the approved pilot only: `interview-acrazie`
and `repo-modernizer-acrazie`. It does not migrate other skills or replace their
specialist responsibilities. The approved scope is recorded in
[the pilot contract](specs/portable-skill-pilot.md).

## Ownership and standalone installation

Keep the essential rules in each skill entrypoint and the full portable practice
in `references/portable-practice.md` inside its own package. Both pilot copies
carry the same content, checked by a regression test. This deliberate duplication
keeps isolated installations usable without a repository `AGENTS.md`, another
skill, an external shared document, or a particular documentation connector.
This repository standard is for maintainers, not a runtime dependency.

## Evidence before dependent decisions and actions

For each execution, inspect local state and verify changing technical claims used
for a decision or action against official documentation matching the project's
version or the proposed target. Do not automatically use latest-version docs.
This includes syntax, APIs, command effects, compatibility, support and maintenance.
Preserve useful language/tool specialization and discovery cues; remove fixed
version targets, timeless tool rankings and unsupported performance claims.
Examples are non-authoritative discovery aids, never execution recipes or consent.

Trace the claim, source locator, version applicability, actual verification date,
status/limits and dependent step in the existing task record. Documentation and
repository evidence have different scopes: a declaration is not proof of support,
and a passing local check is not universal compatibility proof. Inaccessible or
contradictory documentation leaves the claim unverified and suspends only its
dependent decision/action. Continue independent work, without model-memory fallback.
Authorization remains a separate requirement; documentation cannot grant it.

## Stable interaction contract

Every user-owned choice uses only four localized fields: Current state, Options,
Recommendation and Response. Options are consecutively numbered from 1. Exactly
one recommendation names a valid option and gives a context-specific reason.
The response awaits the user; neither recommendations nor templates prefill consent.
Preserve prerequisite ordering, existing approvals and domain-specific interviews.
Use each package's local template; do not introduce a second question schema.

Final reports/handoffs include Decisions, Evidence and Limits, localized for the
user, alongside required specialist sections. Planned evidence stays pending
until executed. Reproducibility concerns required steps, traceable decisions,
observable criteria and stable output structure, not identical wording/results.

## Validation boundary

Run the pilot static regression test and each skill's existing contract checks,
plus repository structure and invocation/graph checks. The scenario prompts live
in each pilot's existing `evals/evals.json`; defining or checking a prompt is not
executing it. Record actual simulations separately with prompt, sources supplied,
output and evaluation. Distinguish static proof, current-harness simulation and
real multi-model/multi-harness trials. None substitutes for the others.

No new ADR is needed for this bounded, reversible pilot. Generalization requires
its own approved scope and evidence, not this pilot's local success alone.
