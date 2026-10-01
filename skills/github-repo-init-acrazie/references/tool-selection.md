# Current package, library and tooling selection

Use this procedure for every unresolved adoption choice: scaffolding/frameworks, package managers, hooks, lint/format, tests/build, CI actions, release and dependency tooling. Candidate lists in other references are examples, not exhaustive catalogs. This remains initialization advice, not an implicit invocation of an audit or modernization skill.

## Discover before recommending

1. Establish actual requirements from the requested stack, runtime, file formats, required rules/plugins, release model, CI/platform constraints and existing manifests/lockfiles/scripts. Preserve explicit choices and working configured tools; discovery does not authorize migration.
2. Check current official documentation, package registry metadata and release/support notes. Search for credible alternatives beyond remembered template names, including ecosystem-native tools, the existing approach and adding nothing. Do not attempt to enumerate every package on a registry; account for the relevant capability space and explain material exclusions.
3. For each serious candidate, record exact package/component, version or supported version range, official source URL, consultation date, required runtime/platform, license, maintenance/support, blocking security concerns and coverage gaps. A suite name such as Oxc is not an installable linter/formatter choice by itself: evaluate Oxlint and Oxfmt separately.
4. Compare capabilities actually needed and total integration/maintenance cost: direct/transitive dependencies, additional runtimes, configuration, editor/CI support, compatibility and migration burden. Package archive size alone does not establish lightness; a larger tool can be better if it replaces several dependencies or custom code.
5. Distinguish development/CI install time, memory and execution cost from production bundle/runtime cost. Mark upstream performance claims as claims with version, hardware, dataset and benchmark limitations; do not call them measured in this repository. Run a representative local trial only if decisive and separately authorized; no exploratory installs or lockfile changes before approval.
6. Present a compact comparison and one contextual recommendation with trade-offs and uncertainties. No fixed candidate count, universal weighting or automatic winner. Record the user's acceptance in the blueprint before installation.

## JS/TS lint and format example

Include Oxlint + Oxfmt, Biome and ESLint + Prettier among candidates, and research other credible options when requirements warrant them. Verify current support for framework syntax, embedded formats, rule/plugin coverage, type-aware linting, config/editor integrations and platform/runtime versions. A hybrid is justified only by a concrete coverage gap, not speculative flexibility. Do not infer one tool's capabilities from its companion or assume that fast linting replaces typechecking.

Examples of authoritative starting points:
- [Oxlint](https://oxc.rs/docs/guide/usage/linter.html), [Oxfmt](https://oxc.rs/docs/guide/usage/formatter.html), [Oxc compatibility](https://oxc.rs/docs/guide/compatibility.html)
- [Biome](https://biomejs.dev/), [ESLint](https://eslint.org/docs/latest/), [Prettier](https://prettier.io/docs/)
- [Ruff](https://docs.astral.sh/ruff/), [golangci-lint](https://golangci-lint.run/), [Clippy](https://doc.rust-lang.org/clippy/)

Re-discover options for other choices too; this list must not become the next closed catalog.

## Missing evidence

When tools, network or sources are unavailable, state which comparisons could not be verified. Do not label remembered defaults current or exhaustive. Unknown compatibility, unacceptable licensing or blocking security uncertainty prevents adoption until resolved; offer to defer the affected tool, obtain authoritative evidence or keep a verified existing approach. Other non-blocking gaps may remain explicit reservations accepted by the user. Never infer abandonment from age/commit frequency alone or claim security solely from an absent advisory.

Templates and commands must match the selected versions. Verify official initialization commands, CLI options and config schemas before generating files. Keep package scripts, hooks, onboarding and CI on the same selected toolchain.
