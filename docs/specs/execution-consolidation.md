# Lot 4: Execution package consolidation

## Objective and approval

Remove redundant generic execution packages without losing contract, proof,
review or script-preservation guarantees. User accepted Q1 option 1 and Q2 option 1,
then answered `ok` to the complete Lot 4 execution scope on 2026-10-13.
This is approval of local migration and independent review, not shipping.

## Scope

- Dedicated worktree `codex/skills-execution-consolidation`, base
  `9e6a6983dac60ebf904cdbc378e0c3419d57c9f0`.
- Retire Feature Builder and Script Portability packages, with no aliases.
- Transfer feature acceptance obligations through Interview's existing contract
  handoff; Interview remains preparation-only and never dispatches workers.
- Add a conditional selected-script guide under Audit; Audit remains read-only.
- Migrate current consumers, static tests and defined eval scenarios. Preserve
  README regression coverage formerly hosted in Script Portability.
- Update current catalogue/glossary and record ADR 0012. Historical documents,
  prior lots, global installations, project kits and lockfile versions are excluded.
- No dependency installation, commit, push, PR, merge or deployment authorization.

## Success criteria and expected evidence

- C1: Packages disappear from current source/catalogue/graph without fabricated
  harness nodes or stale active handoffs. Evidence: consumer search, graph tests,
  localized catalogue checks and portal build.
- C2: Interview carries approval, criterion-linked final-snapshot proof, explicit
  review choice, fresh independent review and bounded correction/arbitration
  obligations without implementation ownership. Evidence: instruction regressions,
  migrated scenarios and independent review.
- C3: Audit carries selected paths/matrix, behavior/errors/environment/paths and
  injection boundaries, helper retention, native-proof honesty and separate
  realization/destructive/install gates. Evidence: guide regressions and scenarios.
- C4: README test coverage, retained specialist guards and package structure/local
  links remain intact. Evidence: migrated and affected existing suites/hooks.

## Decisions

Ordinary authorized execution belongs to the capable harness, not a generic
implementation skill. A needed domain protocol retains its existing specialist.
No copying of rigid runtime recipes, universal performance claims or blanket purges.

## Delivery evidence

Local checks: 138 Python tests in ten affected suites; 40 Bun tests across
invocation, portable evidence, graph/output and model-selection suites. Portal
build: 66 pages; retired routes absent in EN/FR/ZH. Structure/frontmatter hooks,
README local links and diff whitespace checks pass. Existing frozen Lot 3
node_modules were copied into this worktree; no installation command was run,
manifests/lockfile match that environment unchanged. Changes remain unstaged.
Independent final-snapshot review remains pending; its report and snapshot identity
will be preserved outside the frozen patch under `/tmp/lot4-independent-review.md`. Scenario definitions
are not executed behavioral evals. Portal build is not native Windows or live host
proof. Installation migration and integration/shipping of the separate lots remain
outside this contract.
