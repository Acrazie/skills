---
name: jenkins-devops-acrazie
description: Design, modernize, and debug repository-owned Jenkins CI/CD pipelines. Use for substantial Jenkinsfile, Pipeline as Code, Multibranch, build/test/artifact, promotion, deployment, or pipeline-failure work. Do not use for controller administration, plugin installation, global agents, Jenkins Configuration as Code, or trivial Jenkins questions.
license: MIT
---

# Jenkins DevOps / Acrazie

Design, modernize, and repair CI/CD pipelines owned by one application repository. Keep Jenkins as the orchestration layer, ground executable behavior in authoritative evidence, and make durable pipeline decisions explicit before changing files. Use [references/glossary.md](references/glossary.md) when domain terms such as artifact, promotion, rollback, repair, or specialist are ambiguous.

## Scope and invariants

- Work on one application repository per invocation.
- Infer `create`, `modernize`, or `diagnose` from the request and repository state; ask only when the evidence is ambiguous.
- Support CI-only, artifact publication, continuous delivery, or controlled deployment. Mark non-requested capabilities `not applicable` rather than forcing deployment decisions into CI-only work.
- Do not administer the Jenkins controller, install plugins, configure global agents, or author Jenkins Configuration as Code.
- Do not invent build, test, quality, security, publication, deployment, or rollback commands. Ask when authoritative evidence is insufficient.
- Never request, print, persist, or expose secret values. An opaque credential injected by an approved agent/runtime mechanism may be used without revealing its value; otherwise give the user a non-secret command template to run themselves.
- Modify local repository files only after approval of the exact edit set. A repair may skip an ADR, never approval.
- Obtain separate authorization before a remote operation. One approval may cover a clearly bounded sequence with an exact target, submitted data, side effects, verification reads, and expiry; any scope change requires reapproval.
- Reply and write user-facing reports in the user's language. Keep code identifiers and established repository terminology unchanged.

## Inspect before interviewing

Read repository instructions first. Inspect enough evidence to answer factual questions without burdening the user:

- existing `Jenkinsfile` files, pipeline scripts, CI configuration, deployment documentation, and ADRs;
- manifests, lockfiles, runtime declarations, build scripts, test configuration, quality/security tools, artifact metadata, Dockerfiles, Compose files, Kubernetes manifests, Helm charts, Kustomize overlays, infrastructure code, and independently versioned deployment interfaces referenced by the repository;
- branch/release conventions, environment names, rollback procedures, credential ID references, and history relevant to the pipeline;
- Jenkins version, installed-step documentation, agent labels/capabilities, plugins, folder/job permissions, and Shared Libraries only when already provided or retrievable through an approved remote read.

For a Shared Library, distinguish global, folder-scoped, implicit, and dynamic loading; record its trust level, SCM owner, selected revision, and who can modify it. Repository inspection alone cannot prove controller-configured libraries.

Read [references/interview-tree.md](references/interview-tree.md) after inspection. Separate verified facts, recommendations, and unresolved user-owned decisions.

## Use a stack specialist when available

Read [references/specialist-contract.md](references/specialist-contract.md). Detect the primary stack from repository evidence.

- When the runtime exposes a native installed-skill catalog and loader, use them to find and load the exact specialist.
- Otherwise, do not simulate discovery. Continue generically or present a verified manual installation command.
- Before suggesting `npx skills`, verify that `npx`, network access, and the exact published source are available.
- Never fabricate a package, link, install count, or availability claim.
- Explain that installation changes the agent environment and obtain explicit approval before installing.
- If installation is declined, unavailable, unsupported, or not immediately discoverable, continue with this skill. Never block routine Jenkins work on a specialist.

Planned Acrazie specialist identifiers in the contract are detection hints, not evidence that a published skill exists.

## Establish the pipeline decision

Read [references/pipeline-decision-record.md](references/pipeline-decision-record.md). Build a compact decision proposal covering every applicable item:

1. objective, inferred mode, and capability boundary: CI-only, publication, delivery, or deployment;
2. branches, tags, change requests, and manual triggers;
3. ordered stages and the authoritative command or interface for each;
4. verified agent OS, label/capability, isolation, and workspace assumptions;
5. immutable artifact identity, publication location, and provenance;
6. environments and promotion rules, or an explicit `not applicable`;
7. production authorization and rollback, or an explicit `not applicable`;
8. required credential IDs, types, scopes, and trust boundaries, without values;
9. required Pipeline capabilities, providing plugins, and Shared Libraries with evidence;
10. validation plan, known risks, open decisions, and exclusions.

Recommend a Jenkinsfile-backed Multibranch Pipeline when branches or change requests are part of the workflow and the SCM context supports it. Pull/change-request discovery requires the appropriate Branch Source integration. Before proposing untrusted contribution builds, decide which revision is trusted and ensure those builds cannot access publication, signing, registry, cloud, deployment, or broad SCM credentials.

When an applicable command, target, agent capability, credential ID, retention rule, trigger, environment, approver, or rollback mechanism remains unknown, stop and ask. A default OS or current LTS recommendation is not evidence about an actual controller or agent.

## Approval gate and ADR

Present the complete decision proposal before writing pipeline files.

- For creation, modernization, or diagnosis that changes a durable pipeline decision, wait for explicit approval. Then write an ADR using the repository's existing convention; if none exists, use `docs/adr/NNNN-jenkins-ci-cd.md`.
- Never rewrite a historical ADR to conceal a changed decision. Create a new ADR that identifies the superseded record.
- For a repair that restores already-decided behavior, present the causal diagnosis and exact edit/validation plan, then wait for explicit approval. Do not create a ceremonial ADR.
- One approval authorizes the ADR when applicable and the exact local edits described by the proposal. If evidence requires a material deviation, stop, revise the proposal, and obtain approval again.

## Design rules

Read [references/pipeline-design.md](references/pipeline-design.md) before generating or materially restructuring a pipeline.

- Keep the `Jenkinsfile` in source control and treat it as reviewed application code.
- Prefer Declarative Pipeline for new work when its constrained model fits. Declarative is a project policy here, not a claim that Jenkins considers it universally superior. Preserve Scripted Pipeline unless conversion is approved.
- Keep Groovy thin: orchestrate authoritative, version-controlled, independently reviewable build and deployment interfaces rather than implementing heavy logic on the controller.
- Never run application builds on the built-in node. Require a verified agent capability or label before emitting runnable stages; when none is known, recommend Linux only as a proposal and leave execution unresolved.
- Prefer isolated, ephemeral, reproducible agents when available; do not impose Kubernetes or Docker. A Docker socket grants host-equivalent privilege and is not ordinary isolation.
- Account for every required Pipeline capability and map it to Jenkins core or its providing plugin. Distinguish the baseline Pipeline suite from additional integrations; never install a plugin.
- Reuse an existing Shared Library only after its scope, trust, SCM ownership, and revision policy are understood. A trusted global library grants effectively unrestricted Jenkins access to its maintainers.
- Target current Jenkins LTS as a modernization recommendation. Generate against the actual controller and plugin versions when known; otherwise mark compatibility unverified.
- Detect and reuse project quality/security tools. Recommend missing controls separately rather than silently introducing a vendor.
- Promote one immutable artifact or image digest across environments. Do not rebuild per environment.
- Authorize the production approver explicitly; an `input` step without `submitter` allows any Jenkins user by default. Approval does not replace environment authorization or least-privilege deployment credentials.
- Add timeouts, retention, concurrency, cleanup, retry, and reporting only when values and failure semantics are justified.

## Deployment adapters

Load only the adapter matching the approved target:

- [VM/SSH](references/deployment-vm-ssh.md)
- [Docker/Compose](references/deployment-docker-compose.md)
- [Kubernetes](references/deployment-kubernetes.md)
- [AWS](references/deployment-aws.md)
- [Azure](references/deployment-azure.md)
- [Google Cloud](references/deployment-google-cloud.md)

An adapter is a decision and validation framework, not permission to invent commands. The deployment interface may live in the application repository, an approved Shared Library, a platform/GitOps repository, or a managed deployment system, but its source, owner, version, inputs, authentication boundary, verification, and rollback semantics must be known.

## Implement by mode

### Create

Create the smallest pipeline and supporting repository-owned files that satisfy the approved decision. Do not add unrelated infrastructure or migrate tools without approval.

### Modernize

Preserve observable behavior unless the ADR changes it. Prefer incremental changes and identify old job, plugin, library, or controller behavior that cannot be proven.

### Diagnose

Use the `Jenkinsfile`, repository state, and sanitized logs supplied by the user. Trace the first causal error to a concrete command, agent, credential boundary, plugin step, artifact transition, or deployment assumption. Fix the root cause when verifiable; do not suppress it with retries or broad exception handling.

## Validate

Read [references/validation.md](references/validation.md). Run every safe local check supported by the repository and record the exact command and result.

- Validate modified scripts with their native parser, formatter, linter, or tests.
- Treat brace matching or generic Groovy parsing as structural evidence only, never proof that Jenkins accepts the Pipeline DSL.
- Use the official Declarative linter only with an authorized controller and opaque authentication mechanism. It validates the Declarative model/syntax, not runtime success.
- Account for every approved decision and modified file.
- If validation requires unavailable plugins, credentials, agents, services, or a controller, state exactly what remains unverified and the minimal authorized action needed.
- After every remote trigger, approval, abort, publication, or deployment, read back the exact target state before claiming success. Check state before retrying an ambiguous non-idempotent request.

## Report

Return a concise completion report containing:

1. inferred mode and ADR path, or the approved repair-plan summary/reference;
2. files changed;
3. pipeline stages and applicable promotion path;
4. credential IDs, trust boundaries, Pipeline/plugin capabilities, and Shared Library prerequisites;
5. validations run with pass/fail results;
6. unverified controller-dependent behavior and residual risks;
7. any remote action still awaiting authorization.

Do not claim the pipeline works in Jenkins unless controller-aware validation or an actual authorized run proves the relevant behavior.
