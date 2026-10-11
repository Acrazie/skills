# Modernization Paths and Evidence

Read [portable-practice.md](portable-practice.md) before using this catalogue.
This is a discovery procedure, not a list of permanent winners, supported versions,
installation recipes or guaranteed performance improvements.

## Build a project-specific candidate set

1. Identify the actual runtime, frameworks, package manager and tool versions from
   manifests, lockfiles, configuration, CI and safe local inspection. Separate
   declared versions from locked and observed versions. Include tools not named here.
2. Establish the problem: documented support/security constraint, reproducible
   failure, missing required capability, or measured maintenance/performance cost.
   A familiar tool, an old version number or multiple tools is not itself a defect.
3. Consult the incumbent's official release/support documentation and migration
   guides for the observed version. Compare keeping it, a maintenance update,
   a major update and replacement only where each is viable.
4. For any candidate, verify source/target support, plugins, APIs, configuration,
   deployment environment, licensing constraints and migration coverage. Record
   sources, applicable versions, actual checked date and unresolved facts.
5. Derive exact commands from repository configuration and applicable documentation.
   Verify installation and mutation effects before requesting the relevant permissions.
   Prefer an official applicable migration tool, but do not assume a codemod exists,
   is official, or handles every case. Plan bounded manual work when necessary.
6. Approve scope and checks before execution. Remove old packages/configuration
   only after proving required capabilities are preserved. Do not parse dependency
   files as shell arguments or run bulk removals from a generic recipe.

## Discovery cues, not recommendations

The following names and file families are non-authoritative examples to help locate
project evidence. Their existence here asserts no current support, superiority,
compatibility or migration command. Verify every changing claim when used.

| Area | Illustrative discovery cues | Evidence needed for a decision |
| :--- | :--- | :--- |
| Runtime / language | Node.js, Python, Go, Rust, PHP; runtime declarations and CI images | Official lifecycle, required features and deployed runtime compatibility |
| Quality | ESLint, Prettier, Biome, Ruff, static analyzers | Rule/plugin parity, formatter effects, supported configuration and measured cost |
| Build | Webpack, Vite, Rspack, Rollup | Framework/plugins, output contracts, environment variables, assets and measured build behavior |
| Tests | Jest, Vitest, Cypress, Playwright, pytest, PHPUnit | Mock/timer semantics, isolation, environments, coverage and unchanged test oracle |
| Dependencies | npm, pnpm, Bun, pip, Poetry, uv, Composer | Lockfile/install semantics, workspace resolution, packaging and deployment behavior |
| CI/CD / governance | Workflow definitions, hooks, release metadata | Actual provider support, permissions, policy and operational needs |

Keeping the incumbent is a valid recommendation. Do not promise numerical speedups
without representative project measurements. Do not infer abandonment merely from
a quiet release history or a version being behind the latest.

## Record one coherent migration path

For a viable candidate, record current/target versions, documented path, commands
and their verified effects, retained capabilities, approved scope, required checks,
checkpoint evidence and residual risks in the existing plan. Inaccessible or
contradictory documentation blocks only the dependent path; retain independently
verified findings. Substantial CI/CD realization belongs to `ci-cd-acrazie` under
its loading/authorization boundary, not to a competing recipe in this catalogue.
