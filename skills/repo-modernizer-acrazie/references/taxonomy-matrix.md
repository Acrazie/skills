# Thematic Taxonomy and Modernization Tiers

Apply [portable-practice.md](portable-practice.md) before classifying findings.
These six pillars and three tiers classify work; they do not rank languages or
prescribe tools, versions, performance gains or universally safe upgrades.

## Six pillars

| Pillar | Inspect | Establish before recommending change |
| :--- | :--- | :--- |
| 1. Runtime and language | Declared, locked and observed versions; development, CI and deployment | Applicable support lifecycle, required features and compatibility |
| 2. Code quality | Linters, formatters, static analysis, rule/plugin configuration | Documented support, required coverage, conflicts and measured friction |
| 3. Build and packaging | Compilers, bundlers, assets, output contracts | Reproducible build issue, requirements and target/plugin compatibility |
| 4. Tests and QA | Unit, integration and end-to-end suites, environments and coverage | Preserved oracle, mock/isolation semantics and representative timings |
| 5. CI/CD and automation | Pipeline definitions, hooks, release and container metadata | Provider support, permissions, policy and actual delivery needs |
| 6. Package management and dependencies | Manifests, lockfiles, workspaces, dependency graph | Resolution/install semantics, advisories and compatible upgrade paths |

Inspect governance transversely: applicable contribution, security, licensing and
Git policies. Missing a preferred hook manager or release tool is not automatically
a gap. Language/tool filenames in the entrypoint and inspection guide are discovery
examples, not exhaustive inventories or evidence of obsolescence.

Support, deprecation, compatibility and maintenance claims need version-applicable
official sources. Age, a major-version gap, a familiar configuration filename or
absence of recent releases alone does not establish a problem. Measure claimed
performance costs in the repository; do not substitute general benchmark ratios.

## Three ambition tiers

| Tier | Scope | Required assessment |
| :--- | :--- | :--- |
| 1. Conservative | Maintenance updates within the incumbent approach | Verify behavior and compatibility; a patch/minor update is not automatically risk-free |
| 2. Major | A major upgrade of an incumbent tool | Verify breaking changes and migration path; prepare the required ADR before validation/commit |
| 3. Replacement | Replace a tool or approach | Verify capability parity and lifecycle cost; prepare the required ADR before validation/commit |

Choose a tier from the actual problem, required benefits, evidence and migration
cost. Keeping the setup unchanged is valid. Risk and effort depend on the project,
not the tier number or assistance by AI. Do not fabricate candidates to fill every
scorecard cell. An unavailable or contradictory fact remains unverified and blocks
only the decision or action that requires it.
