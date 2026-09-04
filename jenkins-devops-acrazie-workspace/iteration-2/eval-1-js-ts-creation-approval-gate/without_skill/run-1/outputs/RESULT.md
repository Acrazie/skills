# Jenkins CI/CD proposal — approval required

**Status:** PROPOSED — no pipeline implementation has been created.

The repository was inspected, but no Jenkins pipeline decision has been approved. To avoid committing an unreviewed CI/CD design, this report records the proposed decisions and the repository facts/blockers that must be resolved first. Approving this document (or supplying revisions) is the gate before creating a `Jenkinsfile`.

## Repository facts

- Package: private Node/TypeScript project named `checkout-api`.
- Package manager is pinned as `pnpm@9.15.0`.
- Existing scripts:
  - `pnpm lint` → `eslint src --max-warnings=0`
  - `pnpm test:ci` → Vitest JUnit output at `reports/junit.xml`
  - `pnpm build` → `tsc -p tsconfig.json`
  - `pnpm image` → `docker build -t checkout-api:${GIT_COMMIT} .`
- The Dockerfile uses `node:22-alpine`, installs with `pnpm install --frozen-lockfile`, and runs `pnpm build`.
- Deployment interface: `TARGET_ENV=<environment> IMAGE_REF=<immutable-ref> ./ops/deploy.sh`.
- Rollback interface: `TARGET_ENV=<environment> IMAGE_REF=<known-good-immutable-ref> ./ops/rollback.sh`.
- Requested registry repository: `registry.example.invalid/checkout-api`.
- Existing Jenkins credential ID: `checkout-registry`.

## Blocking repository gaps

The supplied repository contains no `src/` directory, `tsconfig.json`, ESLint configuration, or test files. Its lockfile importer is empty even though `package.json` declares three development dependencies. Consequently, the existing lint/build/test commands and the Dockerfile's frozen install cannot be expected to succeed as supplied. These files and the lockfile must be corrected by the application owner; inventing them would change the application rather than configure CI.

The following deployment facts are also absent and must not be guessed:

1. Jenkins agent label/runtime and whether Docker is available to that agent.
2. The type/shape of `checkout-registry` (for example, username/password versus another binding).
3. The registry authentication endpoint and whether Jenkins can reach it.
4. How the current known-good immutable image is recorded for rollback.
5. Whether environment-specific deployment credentials are needed by the existing ops scripts.
6. Who is authorized to approve production and whether an approval timeout is required.
7. Whether staging should have its own approval gate; only production approval was explicitly requested.

## Proposed decisions

### D1 — Jenkins job model

**Recommendation:** use a Jenkins Multibranch Pipeline connected to GitHub. Discover pull requests and the `main` branch. GitHub webhook/job configuration is Jenkins controller configuration and is not encoded with invented repository URLs in the pipeline.

- Pull requests run verification only.
- `main` runs verification, image publication, and ordered promotion.
- Any other discovered branch is skipped unless branch policy is expanded later.

### D2 — verification sequence

**Recommendation:** on PRs and `main`, run:

1. `corepack enable`
2. `pnpm install --frozen-lockfile`
3. `pnpm lint`
4. create `reports/`, then `pnpm test:ci`
5. publish `reports/junit.xml` even when tests fail
6. `pnpm build`

This uses only existing package scripts. Execution must remain blocked until the missing application/configuration files and stale lockfile are fixed.

### D3 — build once and identify immutably

**Recommendation:** only after `main` verification succeeds:

1. Build one local container image using the existing `pnpm image` script with Jenkins' full `GIT_COMMIT`.
2. Add the registry tag `registry.example.invalid/checkout-api:<full-git-commit>` to that same local image; do not rebuild it.
3. Authenticate with Jenkins credential ID `checkout-registry` without exposing secrets, then push that tag once.
4. Resolve the pushed manifest digest and form `registry.example.invalid/checkout-api@sha256:<digest>`.
5. Pass that exact digest reference unchanged to every deployment stage.

The commit tag is useful for traceability, but deployments must use the digest reference. No mutable environment tags (`development`, `staging`, or `latest`) are proposed.

### D4 — promotion order

**Recommendation:** execute only on `main`, in this order and without rebuilding:

1. `TARGET_ENV=development IMAGE_REF=<digest-ref> ./ops/deploy.sh`
2. `TARGET_ENV=staging IMAGE_REF=<same-digest-ref> ./ops/deploy.sh`
3. Jenkins manual `input` gate for production, showing the immutable digest to the approver.
4. `TARGET_ENV=production IMAGE_REF=<same-digest-ref> ./ops/deploy.sh`

A failed environment stops later promotion. Production is never invoked before explicit approval.

### D5 — rollback contract

**Decision required:** the existing rollback script requires a known-good immutable image, but the repository provides no authoritative source for that value.

**Recommendation:** add a separately invoked, parameterized rollback mode/job that:

- accepts a required `ROLLBACK_IMAGE_REF` matching the exact repository digest form `registry.example.invalid/checkout-api@sha256:<64 hex characters>`;
- requires a production manual approval that displays that reference;
- invokes `TARGET_ENV=production IMAGE_REF="$ROLLBACK_IMAGE_REF" ./ops/rollback.sh`;
- never guesses the previous version and never derives rollback from a mutable tag.

Before implementation, identify the deployment system or release record that operators use to obtain and verify the known-good digest. If rollback must be automatic after a failed production health check, provide the health-check command and authoritative prior-digest source first; neither exists in this repository.

### D6 — concurrency and cleanup

**Recommendation:** disable concurrent builds per multibranch job to avoid overlapping promotions; add normal build retention once the desired count/age is supplied. Always remove the local image and log out of the registry in cleanup without deleting the published immutable image.

## Expected implementation after approval

After the decisions and missing facts above are resolved, the repository change should be limited to a reviewed `Jenkinsfile` (plus application-owned fixes for the incomplete JS/TS fixture). The pipeline should avoid interpolating credentials into Groovy strings, restrict publish/deploy stages to `main`, archive JUnit results, preserve the digest in build metadata, and validate rollback inputs before invoking the script.

## Approval request

Reply with either:

- **Approve D1–D6**, plus answers to the seven missing deployment/agent facts; or
- revisions by decision ID (for example, `Revise D5: ...`).

No `Jenkinsfile`, registry login, image push, deployment, or remote call was performed before this approval.
