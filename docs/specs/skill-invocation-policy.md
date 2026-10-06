# Skill invocation policy

## Objective and approved scope

Allow agents to select matching specialists within the current requested task,
without mandatory skill commands, while retaining scope and action approvals.
Keep `skill-refiner-acrazie` explicit-only because its feedback campaign persists
across turns. Apply the decision in an isolated worktree from current `origin/main`.

- Included: invocation metadata for the 15 previously Codex-blocked skills,
  matching descriptions and entry guards, bounded prerequisite handoffs,
  invocation policy, glossary, rationale, historical-document notices, localized
  catalog consistency, and regression validation.
- Included: preserve action gates; remove contradictory unconditional destructive
  recovery instructions in Modernizer so migration approval is not reset/cleanup
  permission. Retain its bounded correction loop and proposed recovery path.
- Excluded: new skills, scope expansion of existing specialists, a central
  orchestrator, dependencies, live refinement campaigns, deployment, changes to
  installed skill links, and behavior changes in unrelated workflows.
- Repository-authorized dedicated-branch Git delivery applies separately. No
  force-push, branch deletion, direct main push, merge, or production action is
  authorized by this contract.

## Accepted decisions and approval

Status: approved on 2026-10-06.

In this Codex conversation, the user accepted Q1–Q3: select skills inside the
existing request, keep permissions separate, and prevent unsolicited intrusive or
costly workflows. The user accepted Q4–Q6: natural-language requests suffice,
Refiner remains explicit-only, and the planner is selected only for requested
agent planning without spawning workers. The user then answered `b` to the final
synthesis and option B, authorizing documentation and application in a dedicated
worktree with consistency checks.

## Success criteria

- C1: All published skills have equivalent frontmatter and Codex invocation
  policies; only Refiner is explicit-only. YAML parsing and catalog assertions
  verify this, including the six previously mismatched pairs.
- C2: The 14 newly model-invocable skills no longer require a named skill command
  or refuse implicit selection. Descriptions and entry guards retain exact task
  boundaries; read-only Jenkins specialists remain parent-owned.
- C3: Skill selection does not authorize new objectives, contract-free edits,
  publication, sensitive/destructive actions, or agent spawning. Existing report,
  asset, implementation, and independent-review gates remain in force.
- C4: Policy, glossary, current instructions, localized summaries, and historical
  invocation decisions have an explicit, coherent revision trail. No historical
  approval or validation result is rewritten as new evidence.
- C5: Maintained regression checks, repository validators, local links, affected
  site build, and graph checks pass or report precise limitations. Static and
  simulated checks are not represented as live host-triggering evidence.

## Delivery evidence

- Base: fetched `origin/main` at `15f2e0f29a8b09bfff0df888e9c4f7e6cead61b2`.
  The refreshed base contains 26 published skills and 15 Codex-blocked skills,
  correcting the preliminary inventory stated during the interview. The approved
  classification is unchanged: all matching specialists except Refiner.
- C1–C2: added `site/tests/invocation-policy.test.ts` before implementation.
  Baseline: four expected policy failures and one passing retained-gates test,
  including the Jenkins metadata mismatch. After application: five tests pass,
  151 assertions. All 26 YAML pairs agree; 14 change Codex policy from `false`
  to `true`, and Refiner gains its missing frontmatter flag. Six mismatches are
  resolved; the resulting catalog has 25 model-invocable skills and one exception.
- C3: static assertions cover retained contract, Git delivery, publication,
  critique, planning-only, test-oracle, Jenkins read-only, and destructive-recovery
  boundaries. Read-only conformance inspection found no remaining active
  command-only guard outside Refiner. Mechanical Port proposes prerequisite
  testing with separate authorization; Modernizer preserves state and requests
  confirmation rather than resetting/cleaning automatically after three failures.
- C4: policy and glossary updated; ADR 0006 revises only the invocation portion
  of ADR 0003. Prior contracts carry revision notices without changing historical
  approvals or proof. Three localized catalogs and all 78 generated skill detail
  pages show Refiner as their sole explicit-only exception.
- C5: `./scripts/hooks/validate-skills.sh skills/*/SKILL.md`,
  `./scripts/hooks/check-skill-structure.sh`, and `git diff --check` pass.
  `python3 scripts/hooks/check-readme-links.py` validates 30 README links;
  a scoped local Markdown check validates 31 links in affected policy/documents.
  `cd site && bun run build` produces 87 pages; `bun run test:graph` passes all
  17 graph/source/output tests. Invocation tests are added to existing site CI
  before its build, with no new dependency.
- Local runtime: Bun 1.3.14. Existing installed dependencies were copied from a
  sibling isolated worktree with a byte-identical `site/bun.lock`; no package
  installation, lockfile change, or installed-skill relinking was performed.
- Limitations: static assertions and source inspection do not establish actual
  Codex/Claude/Hermes implicit triggering or campaign behavior. No live skill
  workflow, paid benchmark, production deployment, or installation refresh was
  run. CI and Git publication are separate from these local validation results.
