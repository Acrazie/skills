# Complementary software development skills

> Invocation update (2026-10-06): historical explicit-only requirements below are superseded by [the approved invocation policy contract](skill-invocation-policy.md). Ownership, task contracts, and action approvals remain unchanged.

## Objective

Save project time by preventing untested feature delivery, misinterpretation of
the user's request, and unrequested additions. Keep the workflow lightweight.

This document records the original two-skill delivery. The subsequent approved
[optional independent-review extension](feature-adversarial-review.md) adds a
bounded reviewer handoff without changing the specialists' implementation ownership.

## Scope

- Deliver `interview-acrazie`, a general reusable clarification and documentation
  foundation, and `feature-builder-acrazie`, its first application specialist.
- The foundation owns the decision-tree interview and an approved persisted Task
  Contract. The specialist owns new application behavior and its test evidence.
- Reuse approved contracts; do not repeat interviews or introduce an orchestrator.
- Exclude bug fixes, behavior-preserving refactors, review of other agents, and
  existing specialists' repository, pipeline, documentation, and visual workflows.
- Do not create or modify those other skills as part of this delivery.

## Success criteria and expected evidence

- C1: Both skills are valid, discoverable repository packages with matching names
  and synchronized invocation metadata. Evidence: repository hooks and YAML checks.
- C2: The foundation interviews relevant unresolved branches, separates facts from
  user decisions, waits for approval, persists a short contract, and does not
  implement. Evidence: a bounded ambiguous-request behavioral exercise.
- C3: The builder reuses a current approved contract and delivers only a new feature
  with criterion-linked tests and regression evidence. Evidence: a bounded feature
  exercise using existing test tooling and an approved contract.
- C4: A missing interview dependency stops implementation and produces an explicit
  installation request with the Skills CLI command. Evidence: a missing-dependency
  exercise; no installation or source modification.
- C5: Documentation distinguishes contracts, glossary terms, and ADRs, and records
  future complementary work without implementing it. Evidence: scoped diff review.

## Decisions and context

- `interview-acrazie` can be called by agents and humans. The builder is explicitly
  human-invoked. Other skills may call the foundation for clarification; they do
  not gain new permissions or lose their domain-specific ownership.
- Use existing spec/ticket conventions or `docs/specs/<subject>.md`. A task contract
  is systematic; an ADR requires a meaningful durable architectural trade-off.
- Ask every relevant frontier question with a recommendation. Stop when relevant
  branches are settled and obtain one explicit final contract approval.
- Reuse test tooling; ask before new dependencies. Test criteria, relevant errors
  and edge cases, and affected regressions, not unrelated behavior or a coverage
  percentage. A test passing is not proof that the request was interpreted correctly.
- Missing foundation: stop and ask for installation using
  `npx skills add Acrazie/skills@interview-acrazie`. Do not silently install or
  duplicate the interview. The command requires the skill to be published first.
- Prior art: all local and fetched remote branch skill specifications were inspected
  on 2026-10-01. No equivalent standalone clarification or application-feature
  realization skill was found. Existing specialist interviews remain their own.

## Approval

Status: approved

In this Codex conversation, the user accepted Q22–Q24 (agent-invocable foundation,
general task contracts, and two-skill first delivery), then replied `go` to the
consolidated “Contrat proposé — première livraison” authorizing creation,
documentation, and validation in an isolated worktree. Bug and refactor skills
remain outside that approval. This record is not approval for installation or
production deployment; repository Git permissions apply separately.

## Complementary backlog

- An approved library, framework, and development-tool selection direction owned
  by the existing `audit-repository-acrazie`, not a new skill. See
  [the selection ideation](library-selection-ideation.md) for scope, cost/utility
  criteria, evidence requirements, and approval boundaries. This is a decision
  specialist alongside implementation skills, not an orchestrator. The selection
  reference records the subsequent scoped enrichment and its local validation.
- A dedicated bug-resolution workflow with reproduction, root-cause evidence, and
  regression tests; distinct from adding new behavior.
- A behavior-preserving refactor workflow with invariants and characterization
  tests; distinct from features and toolchain modernization.

These are recorded directions, not created skills or fixed identifiers. They may
reuse `interview-acrazie` if user-owned decisions remain unresolved.

## Delivery evidence

- C1: Repository `validate-skills.sh` and `check-skill-structure.sh` passed. Both
  frontmatters and UI YAML files were parsed with the installed `gray-matter`
  dependency; names, metadata lengths, prompt references, synchronized invocation
  policies, catalog discovery, and installation commands passed assertions.
- C2: A bounded independent interview exercise asked about ambiguous dashboard
  export behavior, recomputed its frontier after simulated user answers, proposed
  the full contract and destination, waited for explicit simulated approval, then
  persisted the contract and stopped. Artifact inspection found no implementation,
  unnecessary glossary, or ADR. Simulated approval applied only to that fixture.
- C3: A bounded independent feature exercise reused an explicitly approved status
  filter contract and the existing standard-library `unittest` setup. Baseline:
  one passing test. New targeted tests before implementation: six tests with nine
  expected missing-argument errors. After implementation: all six tests passed.
  Criteria covered omitted/None status, exact match and order, unknown/empty results,
  and input preservation. The same contract received actual evidence. A separate
  local rerun of all six tests and `py_compile` also passed.
- C4: A missing-dependency exercise stopped with an installation request and the
  prescribed command. Source readback confirmed the fixture was unchanged; no
  installation, network operation, or copied interview occurred.
- C5: Scoped review confirmed specialist exclusions, the shared contract format,
  selective ADR guidance, glossary terms, and the unimplemented complementary
  backlog. Local Markdown links and maintained eval JSON definitions passed checks.
- `check-readme-links.py` passed all 29 existing README links. `bun install
  --frozen-lockfile` and `bun run build` in `site/` passed without lockfile changes:
  63 pages, including both new skill detail pages in all three existing locales.
  Generated detail pages contain the expected installation commands.

Final behavioral exercises ran inside the isolated worktree's ignored temporary
workspace. Eval prompts and expectations are maintained under each skill's
`evals/evals.json`; raw fixture artifacts are not published skill resources. These
are bounded behavioral checks, not a comparative benchmark or exhaustive proof.
This record reports local validation only, not remote CI, installation, merge,
deployment, or live-public availability.
