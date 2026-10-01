# Separate reusable task clarification from feature execution

We use an agent-invocable `interview-acrazie` foundation and an explicitly
human-invoked `feature-builder-acrazie` specialist. The foundation owns user
clarification and a persisted approved Task Contract; the specialist owns scoped
implementation and criterion-linked proof. This boundary was approved during the
2026-10-01 ideation session recorded in
[the skill-tree contract](../specs/software-development-skill-tree.md).

Embedding an interview in every specialist would avoid an installation dependency
but duplicate approval semantics and allow them to drift. A single development
orchestrator would instead blur ownership across features, bugs, refactors, and
existing specialist workflows. We accept the explicit foundation dependency and
stop with an installation request when it is absent; future complementary skills
can reuse the same contract without repeating settled questions. General discovery
does not replace a specialist's own design interview or expand its permissions.

Task contracts are systematic; ADRs remain selective records of durable trade-offs.
Using an ADR for every request would conflate desired behavior with architectural
rationale. Invocation metadata is intentionally different for the reusable
foundation and human-controlled executor.
