# Stack Specialist Contract

The general skill owns Jenkins-wide decisions, approval, ADR lifecycle, trust boundaries, artifact promotion, credentials, plugin accounting, validation, and reporting. A stack specialist contributes precise repository interpretation without bypassing those controls.

## Planned specialists

These identifiers describe the intended Acrazie family; they are not availability claims:

- `jenkins-js-ts-acrazie`: JavaScript/TypeScript with repository-detected Node.js or Bun runtime and package manager;
- `jenkins-python-acrazie`: the project's existing Python environment/dependency tool, with uv recommended only for new work or an approved migration;
- `jenkins-rust-acrazie`: Cargo formatting, lint, tests, build, packaging, and cache semantics;
- `jenkins-go-acrazie`: modules/workspaces, formatting, analysis, tests, build, and packaging;
- `jenkins-symfony-php-acrazie`: Composer and Symfony conventions detected from the project.

The general skill remains functional when none is available.

## Context given to a specialist

Pass only verified or approved facts and never secret values:

```text
mode and capability boundary
repository signals: manifests, lockfiles, runtime declarations
existing authoritative build/test/package/deploy/rollback interfaces
Jenkins syntax and job model
agent capabilities and trust boundary
artifact identity and destination
quality/security tools
approved exclusions and unresolved questions
```

## Specialist response

Require:

1. stack/runtime/package-manager detection with file evidence;
2. exact authoritative commands and expected outputs;
3. cache paths and invalidation inputs;
4. report and artifact paths;
5. agent tools or container constraints;
6. Jenkins capabilities and providing plugins;
7. local validation commands;
8. uncertainties blocking generation.

The general skill integrates this into the decision proposal. A specialist never writes before the general approval gate.

## Portable discovery and installation

1. If the runtime exposes a native installed-skill catalog and loader, use them.
2. Otherwise skip programmatic discovery; continue generically or present a manual command.
3. Search only through a real catalog or source and inspect the candidate's provenance before recommending it.
4. Verify that `npx`, network access, and the exact package exist before suggesting the portable form:

   ```text
   npx skills add Acrazie/skills@<exact-skill-name>
   ```

5. Explain the environment change and obtain explicit approval before installation.
6. Load immediately only when the runtime supports refresh. Otherwise ask the user to re-invoke or restart the skill-aware session.
7. If discovery or installation fails, continue generically rather than inventing specialist behavior.
