# Library and development-tool selection: approved ideation

> Invocation update (2026-10-06): historical explicit-only requirements below are superseded by [the approved invocation policy contract](skill-invocation-policy.md). Ownership, task contracts, and action approvals remain unchanged.

## Objective and status

Save project time by avoiding poorly fitted, unnecessarily costly, or inadequately
maintained dependencies. Extend `audit-repository-acrazie` rather than create a
duplicate skill. This document records the approved direction and subsequent
scoped skill enrichment, not approval to install a package in a target project.

## Scope and ownership

- Evaluate libraries, frameworks, and development tools before adoption in one
  existing repository. External services, integration, and dependency migrations
  are outside this initial selection workflow.
- Audit owns evidence gathering, comparison, and recommendations. It retains its
  explicit user-invocation requirement and its own specialist interview.
- `interview-acrazie` remains a reusable clarification foundation, not a replacement
  for the audit interview. `feature-builder-acrazie` owns approved feature execution,
  not every tooling integration. Other implementation work uses its appropriate
  specialist or a separately approved task.
- The skill tree describes responsibilities and complementarities, not an imposed
  chronological pipeline or a central orchestrator. Bug and refactor workflows
  remain separate backlog directions.

## Selection behavior

1. Inspect actual needs, manifests, runtime/framework compatibility, existing
   dependencies, and repository constraints before asking unresolved user decisions.
2. Discover credible candidates and compare relevant ones, including the existing
   approach and no new dependency. Do not impose an arbitrary candidate count.
3. Treat functional fit, compatibility, acceptable licensing, and blocking security
   risks as elimination criteria. Establish project-specific constraints rather
   than invent universal weight or performance thresholds.
4. Evaluate cost in proportion to capabilities actually used. Account for replacing
   several dependencies, reducing custom code and maintenance, transitive costs,
   and integration complexity. A larger package can be the better choice; unused
   feature breadth is not a benefit.
5. Distinguish production costs from local/CI costs. Frontend evidence may include
   delivered bundle size and execution cost; backend evidence may include startup,
   memory, throughput, or latency when relevant. Published package size alone is
   not sufficient. Compare only compatible measurement conditions.
6. Verify maintenance, API stability, licensing, security signals, and relevant
   performance using current official sources and version-specific evidence.
   Novelty, popularity, age, or commit frequency alone do not establish quality or
   abandonment. Security checks remain proportionate adoption checks, not a full
   security audit.
7. Distinguish confirmed risks from unknowns. An unresolved elimination criterion
   blocks the choice; other gaps remain explicit reservations. Do not turn an
   upstream performance claim into an observed project result.
8. Use a separately authorized targeted trial only when decisive compatibility or
   performance uncertainty requires it. No silent installations, lockfile changes,
   lasting artifacts, or integration under the audit's read-only authority.
9. Present one argued recommendation with credible alternatives and trade-offs.
   Obtain user acceptance before recording it as a decision and handing it off.
   Use the audit's approved-record lifecycle; associate the accepted decision with
   the implementation contract when applicable. An ADR is warranted only for a
   meaningful durable trade-off.

## Motivating examples, not preferred dependencies

The user cited TanStack, [Fallow](https://github.com/fallow-rs/fallow), and
[Oxc](https://oxc.rs/) to illustrate useful modern packages and tools. Each concrete
package or component still requires project-specific evaluation.

Official material consulted on 2026-10-01 describes Fallow as a repository-analysis
tool sharing a repository graph across analyses, and Oxc as a collection of
JavaScript tools written in Rust. These examples motivated including development
tools alongside libraries and frameworks. No size, performance, maintenance, or
adoption claim was independently validated for a target project.

## Approval and boundaries

On 2026-10-01, the user accepted Q7–Q13 and Q15–Q16, clarified proportional
cost/utility through Q13, and replied `ok` to the consolidated scope and proposal
to record it in an isolated worktree. Q4 produced no concrete failed-adoption
example; none is inferred here.

Approval covers recording this ideation. Editing skill instructions, installing
dependencies, running candidate trials, or implementing integrations requires a
separate implementation request. No new glossary term or ADR is needed for this
reversible extension direction.

The user subsequently replied `go` to the explicit proposal to implement the
enrichment of `audit-repository-acrazie`. This authorizes the scoped skill change
and its validation, not package adoption in another project or implicit invocation
of this user-invoked audit skill.

## Future implementation proof

Before claiming the workflow is implemented, verify that it:

- can recommend retaining the current approach or adding nothing;
- can prefer a larger candidate when demonstrated utility justifies its cost;
- blocks a choice on an unknown elimination criterion without inventing a risk;
- distinguishes upstream claims from observed, comparable measurements;
- treats production and development costs separately and excludes external services;
- preserves explicit invocation, specialist ownership, and audit write permissions.

## Local delivery evidence

The selection behavior is integrated into the existing audit method and adaptive
interview, with entry-point scope and handoff instructions in `SKILL.md`. No new
skill, orchestrator, production dependency, or forced interview dependency was
added. The previously missing `disable-model-invocation: true` now matches the
existing explicit-invocation guard and `allow_implicit_invocation: false` UI policy.

- Repository skill validation and structure hooks passed; `git diff --check` passed.
- Native Bun YAML parsing confirmed identifier, description length, and invocation
  metadata parity. Eval JSON and local Markdown links were validated.
- Three independent bounded synthetic exercises ran against both the updated skill
  and its pre-change snapshot: native/no-dependency choice, larger development tool
  with better actual utility, and unknown licensing plus incomparable upstream
  performance claims and an excluded hosted service. Both versions satisfied all
  11 expectations. This is a regression sanity check, not proof of comparative
  improvement, actual package performance, live research quality, or exhaustive
  correctness. No candidate trial, installation, or integration ran.
- Raw outputs, manual grading, and the generated review viewer remain ignored under
  `.skill-improver/`; maintained prompts and expectations live in the skill's
  `evals/evals.json`. Timing and token metrics were unavailable and were not invented.

These are local results; CI, publication, installation, deployment, and public
availability require separate evidence. A frontend build was not run for this
instructions-only change.
