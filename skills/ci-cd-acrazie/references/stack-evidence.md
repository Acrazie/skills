# Targeted Stack Evidence

Inspect only the detected ecosystem and relevant callers. These are evidence
checklists, not separately invocable skills or certified command recipes. A file
or tool name below is a discovery hint, not an instruction to install or execute.
Verify actual versions, project scripts and current documentation before generation.
If ecosystem is absent here, derive its evidence from the repository/docs; support
is open but missing proof blocks affected stages. Do not synthesize conventional
commands as authoritative behavior or introduce runtime/tool upgrades to fit examples.

## Go

Inspect go.mod/go.sum, go.work, vendor/modules.txt, project CI/scripts and tool config.
Distinguish module checksums from a full lockfile, workspaces from one module and
vendoring from module download. Establish actual compiler version, CGO/native
compiler/libc needs, selected test packages and race/coverage/report options from
project evidence; do not force race support on every platform. Detect configured
JUnit converters, output binaries and cache inputs (module/workspace/runtime/config).

## JavaScript / TypeScript

Inspect package scripts/workspaces, one established manager/lockfile, runtime engines,
.nvmrc/.node-version/.bun-version where present, native modules and tests. Preserve
manager and runtime; immutable install flags/version must match actual manager docs.
Determine configured lint/test/build/report/output interfaces, environment precedence,
working directories and target shells. Never replace them with npx downloads or
assume Node-only tooling works under Bun. Cache inputs include lock/runtime/config.

## Python

Inspect pyproject.toml, requirements/constraints and uv/Poetry/PDM or other actual
lockfiles, tox/nox/pytest and scripts. Determine packaging versus application/service,
interpreter matrix, virtual environment and system/native dependencies. Establish
configured lint/test/coverage/report/package outputs; do not assume pytest or force
a manager. Separate distributable package publication from service deployment.

## Rust

Inspect Cargo.toml/Cargo.lock, workspace, rust-toolchain files, features, targets,
build.rs/native dependencies and actual scripts. Establish toolchain/host/target,
locked behavior and configured test/clippy/format/report/binary interfaces. Do not
invent cargo subcommands or infer JUnit export from standard test output. Preserve
feature/target selection; caches depend on lockfile/toolchain/build inputs.

## Symfony / PHP

Inspect composer.json/composer.lock, Symfony configuration, phpunit and project
scripts; establish PHP/extensions/runtime, Composer hooks and service prerequisites.
Dev dependencies may be required for tests even if production excludes them.
Cache warmup, schema/migrations, secrets and environment-dependent commands may
connect to services or mutate data; never execute for inspection. Determine database,
Messenger/worker, assets and release interfaces from project evidence. Migration,
health verification and rollback data effects need explicit authorization; never
assume reverting application code reverses a database migration.
