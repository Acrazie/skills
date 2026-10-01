---
name: product-critic-acrazie
description: >-
  Critique an existing product's features and codebase against real user needs,
  verifiable benefits, simplicity, and total lifecycle cost. Propose what to retain,
  simplify, retire, or replace. Use only when the user explicitly invokes
  product-critic-acrazie; not for focused technical audits, PR review, tooling
  migrations, or implementation.
disable-model-invocation: true
---

# Product Critic / Acrazie

Challenge the fit between an existing product's uses and its implementation, not
its age. Keeping the current solution can be the best outcome. A newer technology
is not evidence of better performance, lower complexity, or greater user value.

## Entry and boundaries

Run only after explicit human invocation. If activated implicitly, ask the user
to invoke `$product-critic-acrazie`; do not investigate or write a report yet.

- Assess one existing product in one repository, including the implementation
  relevant to its features. Start with a panorama, not an exhaustive health audit.
- Focused technical decisions belong to `audit-repository-acrazie`; setup,
  runtime, framework, and tooling migrations belong to `repo-modernizer-acrazie`.
  PR/diff review, dedicated security audits, external-service selection, and
  multi-repository assessments are outside this workflow.
- Do not edit application code, manifests, tests, configuration, or infrastructure.
  Do not install dependencies, commit, push, deploy, or run implementation here.
  Only approved critique reports and the Interview Foundation's approved task
  documents may be written, subject to repository restrictions and worktree rules.
- Persist all reports and task documents in English. Converse in the user's
  language. Keep secrets, personal data, and unnecessary analytics out of records.

## Inspect facts and establish intent

Read repository instructions, Git state, task documents, glossary, prior reports,
and the smallest useful set of routes, call sites, tests, manifests, and operations
documentation. Trace representative user journeys and implementation invariants.
Record the assessed revision and local changes; never overwrite existing work.

Build a compact panorama connecting features, intended users, jobs they perform,
and material implementation costs. Distinguish repository evidence from user
declarations and unknowns. Code shows what exists, not whether people need it.
Analytics may be incomplete; absent events do not establish absent usage.

Reuse settled answers and an explicitly approved, current Task Contract. When
users, jobs, constraints, priorities, or the report destination are unresolved,
use `interview-acrazie`. Supply verified facts, existing answers, the panorama,
remaining user-owned decisions, scope exclusions, English document requirements,
and expected handoff: an approved persisted contract for this critique.
Let the foundation own clarification; do not duplicate its interview here.

Locate and read the installed skill, using the harness's supported invocation or
following its `SKILL.md` if no Skill tool exists. If clarification is needed but
the foundation is unavailable, ask the user to install it and stop that branch:

```bash
npx skills add Acrazie/skills@interview-acrazie
```

Do not silently install or copy it. Resume from existing answers after installation.
A sufficient approved contract permits continuing without a new interview.
Foundation use does not relax the caller's permissions or scope.

Before deep critique, obtain the user's selection of priorities from the panorama
and confirm the scope and decision criteria through that contract. A global scan
is not approval to investigate every subsystem or rewrite the product.

## Critique selected priorities

For each priority, trace the user's job through current behavior to its responsible
code and constraints. Identify whether the actual mismatch is missing value,
unnecessary behavior, implementation cost, performance, or a combination.
Do not confuse a feature's low frequency with low value: accessibility, emergency
workflows, contractual obligations, and data export may matter rarely but critically.

Compare retaining the current approach with fitting alternatives. Consider
simplifying existing behavior before replacement, and native or installed
capabilities before a new dependency. Compare only material options; no candidate
quota, fashionable stack list, or speculative extension points.

Evaluate user benefit, end-to-end performance, maintenance, dependency and
operational burden, migration cost, compatibility, accessibility, security,
data integrity, rollback, and constraints relevant to the selected problem.
Avoid shifting cost elsewhere and calling that lightweight.

Label claims as observed facts, declared usage, or hypotheses, with source and
confidence. A declared need is usable context, not measured adoption. If benefits
or usage cannot be established, propose the smallest discriminating check rather
than inventing certainty. Performance gains require comparable measurements;
without them, state a hypothesis and a verification method, never a promised gain.

Use read-only evidence where possible. Do not execute unfamiliar project scripts,
benchmarks that mutate data, dependency installation, production load tests, or
credentialed external actions under critique authority. Request separate approval
or report a verification gap. Smallest sufficient proof is not missing proof.

Retirement is a recommendation, not deletion permission. Explain affected users,
fallbacks, obligations, data retention/export, compatibility, and transition risks.
If a material usage or trade-off decision remains unresolved, return that branch
to `interview-acrazie` with accumulated context rather than assuming the answer.

## Report and persist

Use [references/critique-report.md](references/critique-report.md). Present the
prioritized verdict, what to keep, comparisons, evidence gaps, and next decisions.
Use bounded, actionable findings, not a finding-count target. Stop when selected
material branches are resolved, explicitly excluded, or blocked by disclosed gaps.

Validate the report with the user. Before writing, confirm its content and exact
destination `docs/critics/<subject>.md`; use another repository convention only
after agreement. Reuse an existing matching report rather than overwriting an
unrelated document or duplicating the same assessment. Respect its status and
approval history. Report acceptance and option acceptance are separate: do not
record a recommendation as an accepted decision without evidence of acceptance.

## Optional implementation handoff

Report approval never authorizes implementation. On an explicit implementation
request, reuse a sufficient approved targeted Task Contract, or ask
`interview-acrazie` to prepare one linked to the accepted report. Preserve settled
decisions; scope concrete outcomes and checks rather than copying the entire critique.

- New application features: hand off to `feature-builder-acrazie` only after the
  human explicitly invokes or authorizes that skill and the targeted contract is
  approved. Respect its entry guard and specialist exclusions; this critique does
  not implement the feature itself.
- Bug fixes, behavior-preserving refactors, retirement, and migrations: disclose
  the Feature Builder mismatch and agree on a suitable workflow with the user.
  Do not disguise these as features or expand another skill's scope.
- Mixed recommendations: separate their ownership and approval boundaries; do not
  send an unbounded modernization program through Feature Builder.

Finish with the approved report path, accepted decisions, checks actually run,
uncertainties, and the next authorized step. Distinguish local evidence from CI,
deployment, and live usage. A proposal is not an implemented or measured result.
