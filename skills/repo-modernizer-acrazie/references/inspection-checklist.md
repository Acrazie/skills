# Passive Inspection Checklist

Apply [portable-practice.md](portable-practice.md) before discovery. Inspection is
read-only: no installation, file modification or Git mutation. Even an information
command may resolve dependencies, write a cache, access the network or run scripts;
verify its documented effects and applicable permissions before execution.

## 1. Local inventory

Inspect applicable instructions and the smallest useful set of manifests,
lockfiles, runtime declarations, tool configuration, scripts and CI definitions.
Names below are non-authoritative discovery examples, not an exhaustive list or
a prescribed stack. Do not infer the active tool solely from a leftover file.

| Area | Illustrative files | Verify locally |
| :--- | :--- | :--- |
| Dependencies | `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `composer.json`; associated lockfiles | Active manifests, workspace boundaries, declared and locked dependencies |
| Runtime | `.nvmrc`, `.node-version`, `.python-version`, `mise.toml`, `.tool-versions`, container/CI definitions | Declared versus observed runtime and deployment requirements |
| Quality/build/tests | Tool configuration, scripts, test directories | Actual invoked tools, plugins, versions, required checks and their effects |
| CI/CD/hooks | Provider workflows, `lefthook.yml`, `.husky/`, `.pre-commit-config.yaml` | Current behavior, permissions, required checks and release constraints |
| Governance | `AGENTS.md`, `CONTRIBUTING.md`, `docs/git-workflow.md`, `SECURITY.md`, `LICENSE` | Applicable instructions, not presumed consent from file presence |

Report inaccessible areas separately from absent ones. Preserve index, tracked and
untracked work. Inspect root, branch and status using verified read-only means.

## 2. Upstream evidence

For the facts used, consult official documentation matching observed and proposed
versions: lifecycle/support policies, advisories, deprecations, migration guides,
plugin support and command effects. Derive safe inspection commands from those
docs and repository configuration; do not execute a fallback chain of guessed
commands or suppress failure as success. A newer release is a candidate, not an
automatic target; a legacy-looking configuration is a cue, not proof of deprecation.

Record sources, applicable versions, actual check date, limits and dependent steps.
If docs are unavailable or contradictory, suspend the dependent recommendation or
action while continuing independent inventory. Do not use remembered support
cutoffs or fixed action tags as evidence. Registry freshness or lack of releases
alone does not prove abandonment. Measure project-specific performance claims.

## 3. Git policy and governance

Read [commit-strategy.md](commit-strategy.md) before proposing governance changes.
Collect rule sources, scope, verification status, message/signature/release
constraints and distinct delivery permissions. Remote protections may be absent,
inaccessible or unverified; these are different states. History is evidence of
practice, not authorization. Resolve conflicts before the affected action.

Une absence de hook n'implique pas une absence de politique.

Do not install enforcement tools or create governance files during inspection.
Only propose missing assets when justified by repository requirements and user
needs, not to impose a preferred stack. Modernization owns inspection and planning;
substantial CI/CD work is handed off to the CI/CD owner under its loading boundary.
