# Symfony delivery constraints — static review

Review application delivery requirements only; the parent/orchestrator owns the pipeline and deployment. Inspect files, do not execute Composer, console commands, asset builds, database queries, migrations, workers or deployment actions. Every command here is a **conditional proposal, never an action to run in this skill**. Preserve the project's tools, versions, custom paths and release strategy. Standalone bundle development is outside scope. Documentation's `current` selector is not a version recommendation.

## Capture the release contract

Read the application's lockfiles, scripts, kernel/console entry points, environment configuration, Docker/runtime definitions and existing release documentation. For each finding cite file and line, affected API/web/worker process, release-order dependency, missing evidence and owner. Do not invent infrastructure or infer installed tools from customary Symfony layouts. Conflicts block only the dependent recommendation.

Distinguish build-time configuration from runtime configuration, immutable release content from shared mutable data, and PHP CLI from FPM/worker requirements. A production dependency proposal may use `composer install --no-dev --optimize-autoloader` only with a lockfile, compatible tool version, trusted hooks and an established production environment. It is not permission to execute. Do not impose authoritative classmaps or other optimizations absent compatibility evidence; see [CI tooling](ci-tooling.md).

## Doctrine migrations: compatibility before ordering

Apply only when Doctrine Migrations packages, configuration and migration classes are evidenced. Locate configured migration paths/namespaces, connection/entity manager and existing deployment entry point; do not assume a default command or database.

- Read migration SQL/PHP without executing it. Identify destructive changes, renames, new constraints/defaults, data backfills, long locks, database-specific DDL and irreversible operations. Mark dynamic behavior and unknown database state as unverified.
- For overlapping old/new application versions, require backward-compatible schema and data access: expand first, deploy compatible readers/writers, backfill under an explicit plan, then contract only after old web processes and workers are retired. Delayed queued messages may outlive a release; include their payload and handler compatibility.
- A migration's `down()` method does not prove reversibility or data recovery. Never attach automatic migration rollback to failed deployment. Returning to old application code is safe only while the schema/data remain compatible; otherwise require an approved forward-fix or recovery plan with tested backup/restore evidence supplied by the owner.
- Transactions and `all_or_nothing` do not make every database's DDL transactional; implicit commits can leave partial changes. Separate transaction policy from operational recovery, concurrency/locking control and maintenance-window decisions.
- If proposing the evidenced migration entry point, name its target, prerequisite compatibility review, single-run owner, failure stop condition and recovery decision. Even a dry-run/status command may bootstrap the application or connect to a database; do not execute it. Never substitute schema-force-update for reviewed migrations.

## Assets: detect, do not prescribe

| Evidence | Conditional delivery constraint |
| --- | --- |
| `symfony/asset-mapper`, mapping configuration and importmap usage | Consider the existing AssetMapper production compilation path. `php bin/console asset-map:compile` is only an illustrative proposal when that console path/command exists. Record actual configured output; `public/assets` is a documented default, not a guaranteed location. Do not add Node/Encore merely because this is a web application. |
| Encore packages, `webpack.config.js`, package scripts and JS lockfile | Preserve the project's package manager, Node/package versions and existing production-build script. Trace configured output, manifest and entrypoints; `public/build` is only a common location. Package final assets and required manifests, not the entire build workspace. |
| Both, another frontend toolchain, or no assets | Map actual entry points and responsibilities; coexistence is not automatically a conflict. Keep another evidenced toolchain; omit asset work for an asset-free API/worker application. Ask only where ownership or output ambiguity affects the recommendation. |

Do not move compilation to production or install tools there without an existing requirement. Identify build-time dev dependencies before proposing production dependency pruning.

## Environment, cache and artifact boundaries

- Identify `APP_ENV`, `APP_DEBUG`, environment-variable precedence, secret injection and writable-directory ownership from evidence. Do not read or echo secret values merely to validate presence. Production cache preparation requires the intended environment; propose `APP_ENV=prod APP_DEBUG=0 php bin/console cache:clear` only when compatible with the real console path and release strategy. Warmers may execute application code and need services/configuration.
- Separate release-local compiled container/cache from shared application pools. Never propose blanket clearing of shared caches, sessions or queues. Do not package developer/test caches as production cache; prewarmed caches need evidence of runtime paths, environment and secret portability, otherwise warm them in the controlled target context.
- Treat `.env.local.php` generated by environment dumping as potentially secret-bearing. `composer dump-env prod` depends on the project's provided command (commonly Flex); do not assume it exists or prescribe it universally. Preserve harmless tracked `.env` defaults if needed, but exclude private environment overrides and secret-bearing dumps from general artifacts.
- Define an explicit artifact allowlist for required code, locked production dependencies and detected compiled assets. Exclude `.git`, Composer `auth.json`/home, credential files, private decryption keys, private `.env.*` overrides, logs, test/coverage reports, package caches, development dependencies and unnecessary frontend build dependencies. Review generated cache/container files and source maps for disclosure. Public/encrypted secret configuration is not the same as a private decryption key; preserve only what the runtime contract requires.
- Keep uploads, sessions, queues and other mutable/shared data out of immutable release archives. Record exclusions and retention expectations; do not generate, publish or deploy an archive here.

## Messenger: graceful exit is not a restart

Apply only when Messenger transports, consumers or worker supervision are evidenced. Read actual receiver names, retry/failure policies, process-manager configuration and shutdown timeouts. Do not start, stop, drain, retry or purge anything.

A proposed `php bin/console messenger:stop-workers` sets a cache-based stop signal: workers finish their current message and exit. It does **not** restart workers or guarantee that replacement processes use the new release. The process manager (for example an evidenced Supervisor/systemd setup) must restart them with the correct release path and environment. If that contract is unknown, block only the restart recommendation and request its evidence.

Old workers and the signal sender must share the relevant application cache backend and namespace. Multiple hosts need a shared adapter; changing release directories can change the namespace, so inspect stable `cache.prefix_seed` configuration where applicable. A stable namespace alone cannot make separate local filesystem caches shared. Coordinate cache preparation and release activation so the stop flag remains visible and replacements load the intended code; do not paste a universal stop/symlink-switch ordering.

Check graceful termination support and the configured grace period against long-running handlers. OS signals and cache-based stop flags are distinct mechanisms; do not infer PCNTL/signal support or prescribe `SIGKILL`. Preserve the evidenced supervisor/orchestrator strategy and account for retries, duplicate delivery and old queued payloads during rollout.

## Handoff and sources

Return constraints and proposed sequencing with evidence, assumptions, dependent blockers, artifact boundaries and owner-approved verification criteria. Never claim migrations, cache warmup, assets or worker restart succeeded from static inspection.

Official sources consulted; select documentation matching the actual installed versions before proposing syntax:

- Symfony deployment (environment, dependencies, cache, environment dumping): https://symfony.com/doc/current/deployment.html
- Symfony Messenger (restart signaling, shared cache, deployment namespaces and supervision): https://symfony.com/doc/current/messenger.html
- AssetMapper compilation and deployment: https://symfony.com/doc/current/frontend/asset_mapper.html
- Encore deployment and built assets: https://symfony.com/doc/current/frontend/encore/faq.html
- Doctrine migration classes and irreversible migrations (3.9 is a reference manual, not a required version): https://www.doctrine-project.org/projects/doctrine-migrations/en/3.9/reference/migration-classes.html
- Doctrine DDL implicit commits: https://www.doctrine-project.org/projects/doctrine-migrations/en/3.9/explanation/implicit-commits.html
- Composer install flags and platform checks: https://getcomposer.org/doc/03-cli.md
