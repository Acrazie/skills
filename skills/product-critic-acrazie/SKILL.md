---
name: product-critic-acrazie
description: >-
  Critique an existing product's features and codebase against real user needs,
  verifiable benefits, simplicity, and total lifecycle cost. Propose what to retain,
  simplify, retire, or replace. Use when the user requests an assessment of product
  value, usage fit, or unnecessary behavior; not for focused technical audits, PR review, tooling
  migrations, or implementation.
---

# Product Critic / Acrazie

Challenge the fit between an existing product's uses and its implementation, not
its age. Keeping the current solution can be the best outcome. A newer technology
is not evidence of better performance, lower complexity, or greater user value.

## Project loading boundary

Published-library defaults remain model-invocable within the requested task. An
explicit project kit or stricter current instruction takes precedence: propose
this skill from available metadata and wait for the user's explicit command before
reading its instructions. Apply the same gate to each dependency before reading
or dispatching its instructions. One invocation does not activate the chain.
Use `$skill-name` in Codex or `/skill-name` in Claude Code; do not silently read a
missing or unactivated dependency as a workaround. These gates are not filesystem
access controls and do not prove live host behavior. Global homonyms may remain a
blocker. Loading approval never grants execution, installation, spawning or shipping
permission. Under ordinary library defaults, retain scoped implicit handoffs.

## Entry and boundaries

Select this skill for a requested usage-led product assessment. Under published
defaults no named skill command is required; the project loading boundary above
governs explicit kits. Inspect relevant facts read-only, but do not reinterpret an
implementation task as permission to reconsider the product. Scope, deep critique,
report writes, and implementation retain their distinct approval gates below.

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

## User decision format

For any user-owned choice, display only Current state, numbered Options,
Recommendation and Response. Translate labels/content into the user's language;
do not add question IDs, preselect an answer as consent or treat a recommendation
as approval. Ask only unresolved decisions with their verified context. This format
does not replace the report structure or authorize a parallel interview here.

## Inspect facts and establish intent

Read repository instructions, Git state, task documents, glossary, prior reports,
and the smallest useful set of routes, call sites, tests, manifests, and operations
documentation. Trace representative user journeys and implementation invariants.
Record the assessed revision and local changes; never overwrite existing work.

Build a compact panorama connecting features, intended users, jobs they perform,
and material implementation costs. Distinguish repository evidence from user
declarations and unknowns. Code shows what exists, not whether people need it.
Analytics may be incomplete; absent events do not establish absent usage.

Reuse an explicitly approved Task Contract covering the current critique, with
approval evidence beyond a status label and no materially invalidated decisions.
Continue without installing or loading Interview when that contract suffices.
If new facts invalidate it, reopen only affected decisions and preserve settled answers.
Interview is mandatory only when no applicable approved critique contract can be
reused and user-owned decisions remain unresolved, including users, jobs,
constraints, priorities or report destination. Propose `interview-acrazie`, applying
the project loading boundary before reading or invoking it.
Supply verified facts, existing answers, the panorama,
remaining user-owned decisions, scope exclusions, English document requirements,
and expected handoff: an approved persisted contract for this critique.
Let the foundation own clarification; do not duplicate its interview here.

If required Interview is unavailable or not activated under the applicable gate,
block only the dependent step: deep critique or the unresolved implementation
handoff. Request activation or separately approved installation, not a replacement
interview. Do not silently install or copy it. In an explicit kit, use Repo Init's
approved project update flow and the project's pinned selection; do not bypass
managed packages with an unpinned install. Outside a managed kit, propose:

```bash
npx skills add Acrazie/skills@interview-acrazie
```

Locate the dependency from metadata without reading its body when a loading gate
applies. After activation, use the harness's supported invocation or follow its
installed `SKILL.md` if no Skill tool exists. Failed installation leaves the dependent
step blocked. Resume from existing answers after installation and activation.
In an explicit kit, request a new explicit invocation of Product Critic after
Interview persists the contract and stops. Contract approval is not a skill command
and does not activate the returning specialist. Foundation use does not relax
the caller's permissions or scope.

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
`interview-acrazie` to prepare one linked to the accepted report, applying the same
loading and availability gates above. Preserve settled
decisions; scope concrete outcomes and checks rather than copying the entire critique.

- New application features: hand off to `feature-builder-acrazie` only after the
  human authorizes the feature implementation and the targeted contract is
  approved with independent approval evidence. Under ordinary library defaults a
  natural-language request suffices; in an explicit kit request a separate explicit
  activation of Feature Builder before reading or dispatching its instructions.
  If it is unavailable, block this handoff and request the separately approved
  installation flow above. Report, contract and option approvals do not activate
  it or grant execution, spawning or shipping permissions. Respect its specialist
  exclusions; this critique does not implement the feature itself.
- Bug fixes, behavior-preserving refactors, retirement, and migrations: disclose
  the Feature Builder mismatch and agree on a suitable workflow with the user.
  Do not disguise these as features or expand another skill's scope.
- Mixed recommendations: separate their ownership and approval boundaries; do not
  send an unbounded modernization program through Feature Builder.

Finish with the approved report path, accepted decisions, checks actually run,
uncertainties, and the next authorized step. Distinguish local evidence from CI,
deployment, and live usage. A proposal is not an implemented or measured result.
