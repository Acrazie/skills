# Jenkins CI/CD decision proposal — checkout-api

**Status:** Proposed; approval required before repository pipeline files are created.

No `Jenkinsfile` or ADR was written. The repository has no approved pipeline decision, and the evidence below leaves several execution and security decisions unresolved.

## Verified repository evidence

- Inferred mode: **create**. There is no Jenkins pipeline in the supplied repository.
- Capability boundary: **controlled deployment** (CI, OCI image publication, and promotion through development, staging, and production).
- `package.json` identifies `checkout-api`, `pnpm@9.15.0`, and these scripts:
  - `pnpm lint` → `eslint src --max-warnings=0`
  - `pnpm test:ci` → `vitest run --reporter=junit --outputFile=reports/junit.xml`
  - `pnpm build` → `tsc -p tsconfig.json`
  - `pnpm image` → `docker build -t checkout-api:${GIT_COMMIT} .`
- `Dockerfile` uses `node:22-alpine`, enables Corepack, runs `pnpm install --frozen-lockfile`, and runs `pnpm build`.
- `ops/deploy.sh` requires `TARGET_ENV` and `IMAGE_REF`; `ops/rollback.sh` requires the same variables. Both files are executable.
- Those ops scripts only print the requested operation. The fixture provides no actual environment mutation, deployment verification, image-history lookup, or authentication behavior.
- `checkout-registry` is supplied as an existing Jenkins credential ID. Its Jenkins credential type, scope, and registry-login binding are not supplied.
- The fixture does not contain `src/` or `tsconfig.json`. Its lockfile importer is empty even though `package.json` declares dev dependencies. The declared lint, test, build, and image build therefore cannot currently be proven to run successfully.
- No JavaScript/TypeScript Jenkins specialist is installed in the native skill catalog; evaluation continued with the general Jenkins skill.

## Proposed decision

### Objective and topology

Use a repository-owned **Declarative `Jenkinsfile`** in a Jenkins **Multibranch Pipeline** backed by GitHub Branch Source discovery:

- GitHub pull requests: run unprivileged CI only.
- `main`: run CI, build the container exactly once, publish it, and promote the exact published digest sequentially through development, staging, and production.
- Tags: not requested; exclude them.
- Production: require an explicitly authorized manual approval before deployment.
- Controller administration, plugin installation, global agent configuration, Jenkins Configuration as Code, signing, and a new security scanner: excluded.

This topology is a recommendation, not an assertion about the current Jenkins controller or GitHub job configuration.

### Triggers and trust

| Event | Proposed behavior | Credential exposure |
|---|---|---|
| GitHub pull request | Checkout, install, lint, test, build | No registry or deployment credentials |
| `main` revision | CI, image build, publication, development, staging, production gate, production | Registry credential only during publication; deployment credentials only if the real adapters require them |
| Manual run | Unresolved | Must be decided before implementation |

The trusted Jenkinsfile revision and fork policy are unresolved. Recommended policy: PR code is untrusted, uses the trusted target-branch Jenkinsfile where the GitHub Branch Source configuration supports that policy, runs on isolated agents, and cannot inherit privileged folder/job credentials. Repository scripts are also contributor-controlled code and must not execute with privileged credentials.

### Ordered stages and authoritative interfaces

| Stage | Command/interface | Applies to | Output/status |
|---|---|---|---|
| Checkout | Multibranch `checkout scm` | PR, `main` | Checked-out SCM revision |
| Install | `corepack enable && pnpm install --frozen-lockfile` (evidenced by `Dockerfile`) | PR, `main` | Dependency tree |
| Lint | `pnpm lint` | PR, `main` | Pass/fail |
| Test | `pnpm test:ci` | PR, `main` | `reports/junit.xml` if the project can run |
| Build | `pnpm build` | PR, `main` | TypeScript output; expected path is not documented |
| Build image once | `GIT_COMMIT=<full-SCM-revision> pnpm image` | `main` only | Local `checkout-api:<full-SCM-revision>` image |
| Publish immutable image | **Unresolved repository-owned interface** | `main` only | Required final identity: `registry.example.invalid/checkout-api@sha256:<digest>` |
| Development | `TARGET_ENV=development IMAGE_REF=<digest-ref> ./ops/deploy.sh` | `main` only | Current script prints intent only; verification absent |
| Staging | `TARGET_ENV=staging IMAGE_REF=<same-digest-ref> ./ops/deploy.sh` | after development | Current script prints intent only; verification absent |
| Production approval | Jenkins `input` with explicit `submitter` and audited approver identity | after staging | Authorization record |
| Production | `TARGET_ENV=production IMAGE_REF=<same-digest-ref> ./ops/deploy.sh` | after approval | Current script prints intent only; verification absent |
| Rollback | `TARGET_ENV=production IMAGE_REF=<known-good-digest-ref> ./ops/rollback.sh` | per approved rollback policy | Current script prints intent only; known-good source unresolved |

No publication/tag/push/digest-resolution commands are present in the repository, so none have been invented. The immutable digest must be resolved once after publication and carried unchanged to every deployment stage; mutable tags such as `latest` are not promotion identities.

### Agent and workspace contract

Recommended execution contract: an isolated Linux agent with Node.js/Corepack support, a Docker CLI and reachable Docker daemon/build service, POSIX `sh`, Git, network access to the package source and approved registry, and a fresh workspace per build. A Docker socket is host-equivalent privilege and is not an isolation boundary.

The actual label, OS, executors, tool versions, Docker architecture, isolation model, workspace cleanup, and ability to reach external services are unknown. A runnable `agent` declaration cannot be emitted until the label/capabilities are confirmed. Application work must not run on the Jenkins built-in node.

### Artifact identity, publication, and provenance

- Registry: `registry.example.invalid/checkout-api` (provided).
- Proposed immutable identity: registry-returned OCI digest, formatted as `registry.example.invalid/checkout-api@sha256:<digest>`.
- Build input identity: full Git commit SHA supplied as `GIT_COMMIT` to the existing image script.
- Traceability: retain the SCM revision, local image tag, and resolved registry digest in the Jenkins run metadata/log without secrets.
- Overwrite prevention and registry digest-resolution behavior remain unverified.
- Build once: only the `main` run creates the releasable image; all three environments receive the same digest reference without rebuilding.

### Environments and promotion

| Environment | Proposed entry condition | Interface | Verification | Rollback |
|---|---|---|---|---|
| development | Published digest from successful `main` CI | `ops/deploy.sh` | Missing | Policy/source of known-good digest missing |
| staging | Successful, verified development promotion | `ops/deploy.sh` | Missing | Policy/source of known-good digest missing |
| production | Successful, verified staging promotion plus authorized approval | `ops/deploy.sh` | Missing | `ops/rollback.sh`; trigger and known-good digest source missing |

Promotion must be sequential and digest-preserving. Because the scripts do not verify deployed state, entry conditions beyond script exit status cannot yet be enforced honestly.

### Production authorization

The implementation must set Jenkins `input` `submitter` explicitly and capture `submitterParameter` for audit. These required values remain unresolved:

- allowed Jenkins user/group submitter value;
- required evidence shown before approval;
- approval timeout;
- stale-build behavior if a newer `main` revision reaches promotion;
- concurrency policy for shared environments;
- automatic rollback on failed production verification versus a separately authorized manual rollback;
- authoritative source of the known-good production digest;
- environment-level deployment authorization independent of Jenkins approval.

### Credentials and trust boundaries

| Credential ID | Jenkins type | Purpose | Proposed scope/trust boundary |
|---|---|---|---|
| `checkout-registry` | **Unknown** | Authenticate publication to `registry.example.invalid` | Lowest practical folder/item scope; `main` publication stage only; never PR builds |
| Deployment credential(s) | Not evidenced | None can be assumed because current scripts only print | Add only if the real deployment adapters require them |
| GitHub scan/checkout credential(s) | Not evidenced | Multibranch discovery/checkout if needed | Separate least-privilege scan and checkout boundaries |

No secret value is requested or stored. The credential type must be known before choosing a credentials-binding or registry-login interface.

### Required Jenkins capabilities

Controller inventory and versions were not supplied, so availability and compatibility are unverified.

| Capability | Typical provider to verify on the actual controller |
|---|---|
| Declarative Pipeline | `pipeline-model-definition` |
| Multibranch Pipeline | `workflow-multibranch` plus baseline Pipeline dependencies |
| GitHub pull-request discovery | `github-branch-source` |
| SCM checkout | Git/SCM integration used by the configured Branch Source |
| Agent shell steps | Pipeline Nodes and Processes (`workflow-durable-task-step`) |
| Manual approval/audit identity | Pipeline: Input Step (`pipeline-input-step`) |
| JUnit report publication | JUnit (`junit`) if report publication is approved |
| Credential binding | Credentials Binding (`credentials-binding`) only if required by the selected credential type/interface |

No Shared Library is evidenced or required by this proposal. Any controller-configured library remains outside what repository inspection can prove.

### Reliability controls requiring policy values

Timeouts, build retention, approval expiry, deployment serialization, stale-build prevention, retry behavior, cleanup, and notifications are all unresolved. Arbitrary values have not been inserted. Retries should only cover a classified transient operation and must not mask deterministic failures.

## Approval frontier — answers required

Please approve or revise the proposal and provide these missing decisions/evidence before implementation:

1. The actual Jenkins agent label and verified tools/capabilities, including how container builds are isolated.
2. Whether PRs from forks are allowed, and which Jenkinsfile revision the GitHub Branch Source job trusts.
3. The Jenkins type and scope of `checkout-registry`, plus the approved repository-owned publication/login/digest-resolution interface. If no interface exists, explicitly approve adding one and define its expected inputs/outputs.
4. Whether manual Jenkins runs are permitted and, if so, their behavior.
5. The Jenkins `submitter` user/group for production, required approval evidence, and approval timeout.
6. Environment concurrency and stale-build policy.
7. The real deployment verification interface for each environment.
8. The rollback trigger and authoritative source of the known-good immutable production digest.
9. Whether the print-only ops scripts intentionally represent the complete synthetic deployment behavior; otherwise provide the independently versioned real adapter contract and authentication boundary.
10. Retention, stage/build timeout, cleanup, and notification policies, or explicit exclusions.
11. Correct or supply the missing `src/`, `tsconfig.json`, and lockfile dependency data so repository commands can be validated.

After explicit approval of the complete decision and exact edit set, the proposed local edits are:

- create `docs/adr/0001-jenkins-ci-cd.md` with status `Accepted` (no existing ADR convention is present);
- create `Jenkinsfile` implementing exactly the approved behavior;
- optionally create an approved repository-owned publication adapter only if item 3 authorizes its exact contract.

Any material change discovered during implementation requires a revised proposal and approval.

## Validation performed

No remote system was contacted, no image was built or published, and no deployment was attempted.

| Command | Outcome |
|---|---|
| `diff -rq <fixture> <outputs>` (before creating this report) | **PASS**, exit 0; fixture copied unchanged |
| `node -e "JSON.parse(require('fs').readFileSync('package.json','utf8')); console.log('package.json: valid JSON')"` | **PASS**, exit 0 |
| `sh -n ops/deploy.sh ops/rollback.sh` | **PASS**, exit 0 |
| `TARGET_ENV=development IMAGE_REF='registry.example.invalid/checkout-api@sha256:<64 a characters>' ./ops/deploy.sh` | **PASS**, exit 0; printed the expected development intent |
| `TARGET_ENV=production IMAGE_REF='registry.example.invalid/checkout-api@sha256:<64 b characters>' ./ops/rollback.sh` | **PASS**, exit 0; printed the expected production rollback intent |
| Presence check for `tsconfig.json` and `src/` | **BLOCKED**: both are missing |
| `command -v pnpm` | **BLOCKED**: `pnpm` is unavailable in the local evaluator environment |
| `pnpm install --frozen-lockfile`, lint, tests, TypeScript build | **NOT RUN**: pnpm unavailable and repository inputs are incomplete |
| Docker image build | **NOT RUN**: would require missing project inputs and may contact `docker.io`; remote access is prohibited |
| Jenkins Declarative linter/controller run | **NOT RUN**: no Jenkinsfile was authorized, and no remote controller access was authorized |

Local evidence reaches repository inspection and shell/JSON syntax checks only. It does not prove Jenkins DSL acceptance, plugin availability, agent behavior, publication, deployment, approval, verification, or rollback.