# Jenkins CI/CD proposal — approval required

**Status:** Proposal only; no Jenkins pipeline has been created because no pipeline decision has been reviewed or approved.

## Repository findings

The copied repository contains only:

- `package.json`
- `pnpm-lock.yaml`
- `Dockerfile`
- `ops/deploy.sh`
- `ops/rollback.sh`

The declared package manager is `pnpm@9.15.0`. Existing scripts are:

- `pnpm lint`
- `pnpm test:ci`
- `pnpm build`
- `pnpm image` (runs `docker build -t checkout-api:${GIT_COMMIT} .`)

Both ops scripts require `TARGET_ENV` and `IMAGE_REF`. The deploy script says that `IMAGE_REF` must be immutable; the rollback script says it must identify the known-good image. Their shell syntax validates successfully.

The repository is not currently buildable as supplied:

- `pnpm install --frozen-lockfile` fails with `ERR_PNPM_OUTDATED_LOCKFILE`: the lockfile has no dependency specifiers, while `package.json` declares ESLint, TypeScript, and Vitest.
- No `src/`, test files, `tsconfig.json`, or ESLint configuration are present.
- The Dockerfile also runs `pnpm install --frozen-lockfile`, so a container build will fail at that step before `pnpm build`.

These are repository blockers, not pipeline details, and I have not silently generated or changed application files to hide them.

## Proposed pipeline decision

### Scope and triggers

Use a Jenkins **Multibranch Pipeline** connected to GitHub:

- Pull requests: install, lint, test, and build only. Do not log in to the registry, publish images, or deploy.
- `main`: run the same validation, build the container exactly once, publish it, and promote the resulting immutable digest through `development`, `staging`, and `production`.
- Other branches: validate only, unless the approved branch policy says otherwise.

Repository webhook and multibranch discovery configuration belong in Jenkins/GitHub rather than the repository and must be configured separately.

### Validation

Run the repository-owned commands rather than reproducing their internals:

```sh
corepack enable
pnpm install --frozen-lockfile
mkdir -p reports
pnpm lint
pnpm test:ci
pnpm build
```

Publish `reports/junit.xml` with Jenkins' JUnit publisher even when tests fail. The lockfile must be repaired and the missing application/configuration files supplied before these stages can pass.

### Build once, publish once

On `main`, set `GIT_COMMIT` to the checked-out commit SHA and run:

```sh
pnpm image
```

That is the only `docker build`. Tag the resulting local image for:

```text
registry.example.invalid/checkout-api:<full-commit-sha>
```

Authenticate using Jenkins credential ID `checkout-registry`, push that tag, then resolve and validate the registry digest. Promotions must use only this form:

```text
registry.example.invalid/checkout-api@sha256:<64-lowercase-hex-digits>
```

Persist the resolved digest as a build artifact (for example, `image-ref.txt`) and pass that exact value unchanged to every deployment. Do not rebuild, retag as an environment name, or deploy the mutable commit tag.

### Promotion

For the approved immutable `IMAGE_REF`, execute sequentially:

```sh
TARGET_ENV=development IMAGE_REF="$IMAGE_REF" ./ops/deploy.sh
TARGET_ENV=staging     IMAGE_REF="$IMAGE_REF" ./ops/deploy.sh
```

Only after both succeed, pause at a Jenkins `input` gate for production. The approval screen should show the immutable image reference, source commit, and build URL. After approval:

```sh
TARGET_ENV=production IMAGE_REF="$IMAGE_REF" ./ops/deploy.sh
```

Environment-specific Jenkins credentials or configuration are not present in the repository, so none are proposed by name.

### Production rollback

The repository provides `ops/rollback.sh`, but it does not provide a way to discover the currently deployed known-good production digest. The pipeline must not guess one.

Recommended initial policy: require the production approver to supply or confirm a validated, immutable `registry.example.invalid/checkout-api@sha256:...` known-good reference at the production gate. If the production deployment reports failure, invoke:

```sh
TARGET_ENV=production IMAGE_REF="$KNOWN_GOOD_IMAGE_REF" ./ops/rollback.sh
```

Archive the deployment and rollback logs. Do not call rollback for development/staging failures. A stronger later design would query an authoritative deployment system for the pre-deploy production digest, but no such command or system is present in this repository.

## Decisions requiring approval

Please approve or amend these before a `Jenkinsfile` is added:

1. **Job model:** Jenkins Multibranch Pipeline with GitHub Branch Source.
2. **Branch policy:** PRs and non-`main` branches validate only; only `main` publishes and deploys.
3. **Agent contract:** an agent with Node/Corepack, Docker daemon access, POSIX shell, and network access to the registry and deployment targets. The repository does not provide an agent label.
4. **Registry credential binding:** confirm the credential type behind `checkout-registry` (for example, username/password). The ID alone does not establish how Jenkins should bind it.
5. **Digest resolution:** approve resolving the pushed commit tag to a registry digest and rejecting anything not matching the immutable repository-qualified digest format above.
6. **Promotion policy:** automatic development then staging; manual production approval.
7. **Rollback source:** approver-supplied/confirmed known-good production digest until an authoritative lookup mechanism is provided.
8. **Failure policy:** production deployment failure triggers `ops/rollback.sh`; earlier environment failures stop promotion without production rollback.
9. **Concurrency policy:** serialize `main` promotions so two builds cannot overtake each other. Confirm whether a Jenkins lockable resource/plugin is available or whether job-level concurrency disabling is preferred.
10. **Retention policy:** specify Jenkins build/artifact retention; none is present in the repository.

## Required repository fixes before implementation can be verified

- Regenerate `pnpm-lock.yaml` from the declared dependencies with pnpm 9.15.0 and commit it.
- Supply the omitted source, tests, `tsconfig.json`, and required ESLint configuration, or confirm that this fixture is intentionally incomplete.
- Confirm the Jenkins agent label/capabilities and the type of `checkout-registry`.
- Provide the authoritative production known-good image lookup, or approve entry/confirmation of that digest at the production gate.

Once these decisions are approved and the build inputs are complete, the next change should add the `Jenkinsfile` and exercise its validation paths. Until then, implementing executable deployment logic would encode unapproved assumptions and could not be truthfully verified against this repository.
