# Jenkins CI/CD decision proposal — approval required

**Status:** Proposed; not approved and not implemented  
**Inferred mode:** `create`  
**Application:** `checkout-api`

No `Jenkinsfile` or ADR has been written. The repository has no existing Jenkins pipeline, and the requested workflow introduces durable CI/CD decisions. Per the required approval gate, implementation must wait until the unresolved decisions below are answered and the resulting complete proposal is explicitly approved.

## Verified repository facts

- The copied repository contains `package.json`, `pnpm-lock.yaml`, `Dockerfile`, `ops/deploy.sh`, and `ops/rollback.sh`. It contains no Jenkinsfile, CI configuration, source tree, TypeScript configuration, ESLint configuration, test files, deployment documentation, or ADR convention.
- `package.json` pins `pnpm@9.15.0` and defines:
  - `pnpm lint` → `eslint src --max-warnings=0`
  - `pnpm test:ci` → `vitest run --reporter=junit --outputFile=reports/junit.xml`
  - `pnpm build` → `tsc -p tsconfig.json`
  - `GIT_COMMIT=<sha> pnpm image` → `docker build -t checkout-api:${GIT_COMMIT} .`
- The Dockerfile uses `node:22-alpine`, enables Corepack, runs `pnpm install --frozen-lockfile`, and runs `pnpm build`.
- `ops/deploy.sh` requires `TARGET_ENV` and an immutable `IMAGE_REF`.
- `ops/rollback.sh` requires `TARGET_ENV` and an `IMAGE_REF` identifying a known-good image.
- Both ops scripts are executable and pass `sh -n`; however, their only current effect is to print the requested operation. No actual rollout, health/readiness check, or deployment target is present in this fixture.
- The lockfile's root importer is empty even though `package.json` declares dev dependencies. The normal frozen install therefore cannot yet be assumed to succeed.
- Registry destination is user-selected as `registry.example.invalid/checkout-api`.
- Jenkins credential ID `checkout-registry` is reported to exist; its Jenkins credential type is not known.
- The fixture has no committed history from which branch, Jenkins, agent, deployment, or ADR conventions can be recovered.
- No installed `jenkins-js-ts-acrazie` specialist was found in the available skill catalog or local skill source, so the generic repository-evidence workflow was used. No additional skill was installed.

## Proposed decision

### Triggers and job model

Use a source-controlled Declarative `Jenkinsfile` in a GitHub-backed **Multibranch Pipeline**:

- GitHub pull requests: run checkout, dependency installation, lint, test, and build only. Do not publish or deploy PR code.
- `main`: run the same CI checks, build the container exactly once, publish it, and promote that exact published digest sequentially through development, staging, and production.
- Tags: excluded unless explicitly requested.
- Production: require a Jenkins manual approval after staging evidence and before deployment.

This is a recommendation, not evidence about the existing Jenkins job model or installed plugins.

### Proposed ordered stages

| Scope | Stage | Repository-backed command / mechanism | Output |
|---|---|---|---|
| PR + `main` | Checkout | Jenkins Multibranch SCM checkout | Exact Git commit |
| PR + `main` | Install | `corepack enable && pnpm install --frozen-lockfile` | Dependencies from lockfile |
| PR + `main` | Lint | `pnpm lint` | Pass/fail |
| PR + `main` | Test | `pnpm test:ci` | `reports/junit.xml` |
| PR + `main` | Build | `pnpm build` | Intended `dist/` output; not verifiable from the incomplete fixture |
| `main` only | Build image once | `GIT_COMMIT="$GIT_COMMIT" pnpm image` | Local `checkout-api:<git-sha>` image |
| `main` only | Publish and resolve digest | **Unresolved: no repository-owned command exists** | Required `registry.example.invalid/checkout-api@sha256:<digest>` |
| `main` only | Development | `TARGET_ENV=development IMAGE_REF="$IMAGE_REF" ./ops/deploy.sh` | Development promotion request |
| `main` only | Verify development | **Unresolved: no verification command exists** | Promotion evidence |
| `main` only | Staging | `TARGET_ENV=staging IMAGE_REF="$IMAGE_REF" ./ops/deploy.sh` | Staging promotion request |
| `main` only | Verify staging | **Unresolved: no verification command exists** | Evidence for production approval |
| `main` only | Production approval | Jenkins manual `input` gate | Recorded approval/rejection |
| `main` only | Production | `TARGET_ENV=production IMAGE_REF="$IMAGE_REF" ./ops/deploy.sh` | Production promotion request |
| `main` only | Verify production | **Unresolved: no verification command exists** | Production result |
| Production rollback | Roll back known-good digest | `TARGET_ENV=production IMAGE_REF="$KNOWN_GOOD_IMAGE_REF" ./ops/rollback.sh` | Production rollback request |

The image digest, not a mutable tag, should become the single `IMAGE_REF` carried through all three environments. The pipeline must not rebuild between environments.

### Agent and workspace proposal

Recommend an isolated Linux agent with a fresh workspace and these pre-provisioned capabilities:

- Node.js compatible with the repository's Node 22 Dockerfile signal;
- Corepack and `pnpm@9.15.0`;
- POSIX `sh`;
- Docker CLI plus access to an approved image builder/daemon.

No agent label, agent provisioning model, Docker trust boundary, or workspace policy is present in the repository. Kubernetes agents, privileged Docker-in-Docker, and host Docker-socket mounting are not proposed without an explicit infrastructure decision.

### Artifact and provenance

- Source identity: Jenkins SCM `GIT_COMMIT`.
- Build tag: local `checkout-api:${GIT_COMMIT}`, produced once through the existing `pnpm image` script.
- Publication destination: `registry.example.invalid/checkout-api`.
- Deployment identity: registry digest form `registry.example.invalid/checkout-api@sha256:<digest>` obtained from the successful push.
- Traceability: retain the Git commit, Jenkins build URL/number, pushed tag, and resolved digest in build metadata/log output; pass only the resolved digest to deployment stages.

The repository does not provide the login, tag, push, or digest-resolution command, so the publication boundary is not executable yet.

### Promotion and rollback rules

- Development starts only after successful CI, one image build, successful publication, and digest capture.
- Staging receives the same digest only after development deployment and its required verification pass.
- Production receives the same digest only after staging deployment, its required verification pass, and manual approval.
- A production rollback must pass a separately selected, previously successful production digest to `ops/rollback.sh`; it must never rebuild an old commit.
- Whether rollback is automatic after failed production verification or a separate manual Jenkins action remains unresolved.

### Credentials

| Credential ID | Required type | Purpose | Status |
|---|---|---|---|
| `checkout-registry` | Must be confirmed; likely a registry-compatible username/password credential, but this cannot be assumed | Scoped registry login for push | ID reported to exist; type/scope unverified |
| GitHub SCM credential | Depends on repository visibility and organization policy | PR discovery and checkout | Unknown |
| Deployment credentials | Depends on the real deployment mechanism | Development/staging/production access | No evidence in repository |

No secret value will be stored in the repository or printed. Registry authentication should be scoped only around login/push and cleaned up afterward.

### Jenkins/plugin prerequisites

| Dependency | Why | Availability |
|---|---|---|
| Declarative Pipeline (`pipeline-model-definition`) | Declarative `Jenkinsfile` | Unknown |
| GitHub Branch Source | GitHub PR discovery in a Multibranch Pipeline | Unknown |
| JUnit | Publish `reports/junit.xml` with the `junit` step | Unknown |
| Credentials Binding or an equivalent approved Jenkins credential mechanism | Bind `checkout-registry` without exposing values | Unknown |

Docker Pipeline plugin syntax is not required by this proposal; standard repository commands can run through `sh` once publication commands and the agent's Docker capability are approved. No Shared Library is declared or proposed.

## Decisions required before implementation

Please provide or select all of the following:

1. **Registry publication:** What repository-owned command should log in, tag, push, and resolve the digest? Alternatively, approve adding a versioned repository script for this contract. Confirm the credential type of `checkout-registry` and whether it may push to `registry.example.invalid/checkout-api`.
2. **Fixture completeness:** Supply the missing `src/`, `tsconfig.json`, ESLint/test configuration, and a lockfile synchronized with `package.json`, or confirm that this intentionally incomplete synthetic fixture should receive an unexecutable pipeline proposal only.
3. **Deployment meaning:** Confirm whether the print-only `ops/deploy.sh` and `ops/rollback.sh` are intentional synthetic stand-ins to invoke as-is. If not, provide the real repository-owned deployment commands/configuration and required Jenkins credential IDs/types.
4. **Environment verification:** Provide the authoritative health/readiness command and timeout/failure behavior for development, staging, and production.
5. **Production approval:** Identify the authorized Jenkins user/group, evidence shown at the gate, approval timeout, and behavior on timeout/rejection.
6. **Rollback policy:** Define how the last known-good production digest is recorded/retrieved and whether rollback is automatic after failed verification or manually invoked. Identify who may invoke it.
7. **Jenkins execution context:** Confirm the Linux agent label and approved Docker build mechanism, Jenkins LTS version, and availability/versions of the listed plugins.
8. **GitHub access:** Confirm repository visibility and any SCM credential ID/type required for PR discovery and checkout.
9. **Operational policy:** Decide whether manual non-production pipeline runs are allowed and provide any required build timeout, retention, concurrency, retry, and notification policy. In the absence of approved values, these controls will not be invented.

After these answers, I will return a completed decision record for explicit approval. Only that approval would authorize creation of `docs/adr/0001-jenkins-ci-cd.md` (no existing ADR convention was found) and the exact pipeline/supporting-file edits described by the accepted decision.

## Alternatives considered

- **Build separately per environment:** rejected because it breaks immutable promotion and the explicit build-once requirement.
- **Deploy pull requests:** rejected as an unsafe default not requested by the user.
- **Mutable environment tags as deployment identity:** rejected; a registry digest provides the required exact identity.
- **Inline long publication/deployment logic in Groovy:** rejected; the repository must own executable operational commands.
- **Assume Docker Pipeline or Kubernetes agents:** rejected because plugin and infrastructure availability are unknown.

## Validation performed

- `sh -n ops/deploy.sh && sh -n ops/rollback.sh` — **PASS**.
- Executable-bit check for both scripts — **PASS** (`-rwxr-xr-x`).
- Repository-evidence mapping — **BLOCKED** for an executable pipeline by missing source/configuration, inconsistent lockfile metadata, missing publication command, missing environment verification, and unresolved Jenkins/approval/rollback facts.
- `pnpm install`, lint, tests, build, and image build — **not run**; the fixture lacks required project inputs and no pipeline decision has been approved.
- Jenkins Declarative linter — **not run**; no Jenkinsfile was created and no controller access was provided or authorized.
- Registry push and deployments — **not attempted**; remote actions require separate explicit approval even after local implementation.

## Explicit exclusions

- Jenkins controller administration or Configuration as Code.
- Plugin installation and global agent configuration.
- Secret creation, retrieval, or storage.
- Unapproved remote Jenkins, registry, or deployment actions.
- Invented deployment, verification, publication, notification, or rollback-selection behavior.
