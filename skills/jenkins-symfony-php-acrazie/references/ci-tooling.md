# Symfony CI tooling — static review

Use for Symfony applications (API, web, workers), not standalone bundle development. Inspect repository text with `read_file` and `search_files`; never execute application code, Composer, PHP, tests, containers, Jenkins jobs, or even CLI discovery/help commands. All command strings below are **proposals for the parent/orchestrator**, not permission to run them. Do not install missing tools or change versions. Documentation selectors such as `current` and example manual versions are references, not upgrade targets.

## Establish an evidence chain

For each proposed check, record: purpose → repository file and line → script/wrapper → executable and working directory → configuration → environment/services → exit policy → output path. Mark unknowns explicitly. Conflicting evidence blocks only recommendations depending on that conflict.

- Read `composer.json`, `composer.lock`, existing Jenkinsfiles/shared-library references, container definitions, PHP configuration, test configuration, Makefiles and wrapper scripts. Trace nested Composer script aliases and Flex `auto-scripts` as text; never evaluate them.
- Preserve the existing entry point: a Composer script, `bin/phpunit`, Symfony PHPUnit Bridge `simple-phpunit`, custom PHAR, or vendor binary are not interchangeable. Resolve `config.vendor-dir`, `config.bin-dir`, declared environment overrides and relative paths; `vendor/bin` is a default, not evidence of the actual executable. A lockfile dependency does not prove installation on an agent.
- Detect PHPStan, Psalm, coding-standard tools and Symfony linters only through package/config/script evidence. Do not fabricate `composer test`, `composer lint`, report flags, console paths, service containers or Jenkins tool names. A Symfony console command boots project code even if named `lint:*`.
- Retain PHP, Composer, Symfony and tool versions declared by the project. Separate constraints, locked package versions, configured agent/container images and actual runtime evidence. A floating image tag or unavailable shared library leaves uncertainty; do not replace it with an invented pinned version.

## Dependencies, environment and trust

- CI checks usually need `require-dev`; a production artifact usually does not. Propose separate dependency workspaces/build stages so a `--no-dev` install cannot silently remove test tools or contaminate later checks. Preserve lockfile installs; never propose `composer update` as an ordinary CI install.
- Identify existing test environment variables, isolated databases, transport configuration and fixtures before recommending integration tests. Do not infer production credentials or services from `.env` defaults. Treat Symfony `APP_ENV`/`APP_DEBUG` separately from Composer's dev-package selection.
- `config.platform` emulates PHP/extensions for dependency resolution; it does not install or prove the real runtime. Conditional proposal: `composer check-platform-reqs --no-dev` against installed production dependencies in a target-equivalent runtime; `--lock` checks lockfile requirements instead. It ignores `config.platform`. CLI PHP evidence alone does not establish FPM/worker configuration parity. Do not bypass mismatches with `--ignore-platform-reqs`.
- Composer plugins and scripts execute code. Read `allow-plugins`, root scripts, installer hooks and Flex behavior before suggesting an install. Require explicit trust for specific plugins; never recommend wildcard trust or exposing secrets to untrusted pull-request code. `--no-scripts` and `--no-plugins` disable different mechanisms and may break required setup: propose them only with the omitted behavior and resulting limitations stated.
- Installation/autoload hooks may bootstrap Symfony. Establish the intended environment and available configuration before a proposed production install; do not assume dev-only bundles remain available after `--no-dev`.

## Cache contract

Derive cache paths from repository configuration and supplied agent evidence: `COMPOSER_CACHE_DIR`, Composer `cache-dir` and subdirectories, `COMPOSER_HOME`, OS/XDG defaults, container mounts and user identity. Do not impose `~/.composer` or cache the entire Composer home (which can contain authentication and global configuration). If resolution is unknown, request evidence rather than run a discovery command.

Distinguish downloaded-package caches, installed dependencies, PHPUnit/static-analysis caches, Symfony environment caches and deployable artifacts. Keep untrusted branch caches isolated from trusted builds. Derive keys from lockfile identity and relevant tool/runtime/OS/configuration inputs; installed dependency caches also require dev/prod separation. Never reuse test/dev Symfony caches as production warmup output. Record invalidation and ownership assumptions; do not claim that a cache guarantees reproducibility.

## Test reports and Jenkins handoff

- Read the selected PHPUnit version's XML configuration and wrapper argument forwarding. Conditional proposal: add `--log-junit <report-file>` only to the evidenced runner when supported; do not invent a report directory as an existing path.
- Coverage is separate from JUnit results. Propose a supported format such as `--coverage-clover <report-file>` only with evidence of compatible coverage configuration and an available driver (PCOV or Xdebug with coverage enabled). Report missing capability; do not install an extension or promise coverage.
- Provide the parent with exact producer paths, workspace-relative consumer globs, expected format and failure behavior. Preserve nonzero test exit status; do not hide failures with `|| true`. Recommend publication after failure without making missing/empty reports silently successful.
- `junit` requires the Jenkins JUnit plugin; `recordCoverage` requires the Coverage plugin with a supported parser in the installed version. HTML publication, static-analysis ingestion and cache steps likewise require their respective installed capabilities. Documentation proves an API exists, not that this controller has it. When plugin evidence is absent, mark publication conditional; artifact retention is not equivalent to parsing results or enforcing a quality gate.
- The parent owns Jenkins orchestration, credentials, agents and delivery. Return a capability/evidence table plus conditional command/report proposals, not a claimed successful CI run.

## Official sources

Consult the matching project/tool version before reusing syntax:

- Composer configuration (platform, directories, plugin trust): https://getcomposer.org/doc/06-config.md
- Composer CLI (install, flags, platform checks): https://getcomposer.org/doc/03-cli.md
- Composer script events and aliases: https://getcomposer.org/doc/articles/scripts.md
- Custom vendor binary paths: https://getcomposer.org/doc/articles/vendor-binaries.md
- Symfony deployment environment and dependency separation: https://symfony.com/doc/current/deployment.html
- PHPUnit runner/report options (11.5 manual is an example, not a required version): https://docs.phpunit.de/en/11.5/textui.html
- PHPUnit coverage prerequisites: https://docs.phpunit.de/en/11.5/code-coverage.html
- Jenkins JUnit step and empty-result behavior: https://www.jenkins.io/doc/pipeline/steps/junit/
- Jenkins Coverage plugin and report parsers: https://www.jenkins.io/doc/pipeline/steps/coverage/
