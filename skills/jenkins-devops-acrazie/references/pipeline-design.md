# Pipeline Design Reference

## Pipeline as code and syntax policy

Keep the `Jenkinsfile` in source control with the application so it shares review history, branch behavior, and ownership with the code it delivers.

Prefer Declarative Pipeline for new work when its constrained structure fits the workflow. Declarative and Scripted use the same Pipeline subsystem and plugin-provided steps: Declarative offers a model that can be validated, while Scripted offers more Groovy flexibility. A `script {}` block embeds Scripted behavior inside Declarative; large blocks are a signal to move logic into an authoritative project interface or a carefully governed Shared Library.

Do not promise Declarative-only behavior, such as its linter or stage restart model, for Scripted pipelines.

## Keep Groovy as glue

Pipeline Groovy executes on the controller even when surrounded by agent-oriented constructs. An individual plugin step's implementation determines where its work occurs; being inside `node` does not move arbitrary Groovy to the agent.

Prefer this boundary:

- project build tool: compile/package;
- project test runner: unit/integration/end-to-end tests;
- authoritative deployment interface: release, verification, rollback;
- Jenkinsfile: triggers, agents, stage ordering, credentials binding, artifact handoff, authorization, and reporting.

Do not move working project logic into Groovy. Avoid controller-side parsing or large in-memory values. When several shell statements form reusable behavior, prefer independently testable version-controlled code.

## Capability applicability and stages

First classify the requested boundary as CI-only, publication, continuous delivery, or deployment. Mark later capabilities `not applicable` when they are outside scope.

A complete delivery pipeline may contain:

1. checkout and metadata;
2. dependency installation or restore;
3. formatting, lint, and static analysis;
4. unit/integration tests with published reports;
5. approved security checks;
6. package/image build exactly once;
7. immutable publication with provenance;
8. non-production promotion and verification;
9. authorized production promotion, verification, and rollback behavior;
10. post-build reporting and cleanup.

Include only evidence-backed work. Stages are a visibility model, not a mandate to create many tiny Pipeline steps.

## Controller, agents, and workspaces

- Never run application builds on the built-in node. Jenkins recommends zero built-in executors; changing controller configuration remains outside this skill.
- Require a verified label or capability before emitting runnable work. If unknown, leave the agent contract unresolved rather than using `agent any` or inventing a label.
- Recommend Linux only as the fallback proposal when no OS evidence exists. Preserve explicit Windows `bat`/PowerShell and macOS requirements.
- Prefer isolated workspaces and ephemeral agents when the platform supports them.
- Do not co-locate credential-bearing trusted jobs with untrusted jobs on a multi-executor agent; sibling processes may observe environments or temporary files.
- Do not share mutable workspaces across concurrent builds. Transfer intentional outputs through an artifact repository or a narrowly scoped same-run mechanism.
- Treat a host Docker socket as host-equivalent privilege. Containers that can control it are not a security isolation boundary.

Agent-to-controller access control is defense in depth, not a substitute for isolating untrusted builds.

## Reliability controls

Treat every control as an explicit decision:

- `timeout`: bound hung work and manual approval; derive values from evidence or an approved policy.
- `buildDiscarder`: protect storage while preserving audit and rollback needs.
- concurrency controls: prevent races against shared environments without serializing independent work unnecessarily.
- milestones or equivalent stale-build controls: prevent an older approved build from deploying after a newer one.
- `retry`: use only for a classified transient operation; never hide deterministic failures.
- cleanup/post actions: publish diagnostics without masking the primary failure.

Do not present arbitrary numeric defaults as best practices.

## Pipeline capabilities and plugins

Pipeline itself is a plugin suite. Declarative syntax, Multibranch, `input`, credentials binding, Docker agents, JUnit, and many familiar steps may come from separate plugins.

For every required capability:

1. map it to Jenkins core or the providing plugin short name;
2. distinguish the baseline Pipeline suite from additional integrations;
3. use the controller's Pipeline Syntax/Snippet Generator and installed-step reference as authoritative when available;
4. otherwise use the official plugin page and mark installation/version unverified;
5. check minimum Jenkins version, dependencies, deprecation/adoption status, and active security warnings when selecting or modernizing a plugin;
6. never install, upgrade, disable, or approve a plugin from this skill.

Do not use the Script Console merely to inventory plugins.

References:

- Pipeline steps: https://www.jenkins.io/doc/pipeline/steps/
- Managing plugins: https://www.jenkins.io/doc/book/managing/plugins/
- Plugin index: https://plugins.jenkins.io/
- Security advisories: https://www.jenkins.io/security/advisories/

## Shared Libraries

Inventory global, folder-scoped, implicit, explicit, and dynamic libraries from authorized controller evidence when they affect the pipeline.

Record:

- configured scope and whether the library is trusted or sandboxed;
- SCM source and who can modify it;
- default and selected revision;
- whether a Jenkinsfile may override that revision;
- whether the selected revision is immutable under repository controls.

A trusted global library can invoke unrestricted Java, Groovy, Jenkins, and plugin APIs; write access to its SCM is effectively privileged Jenkins access. Folder-scoped libraries are untrusted. Pin production-sensitive use to an approved immutable revision when reproducibility requires it. A branch is not immutable, and a tag is only as immutable as its repository controls.

Do not override built-in Pipeline steps. Keep libraries focused. Shared Library Groovy remains controller-side/CPS-transformed and can still impose controller cost.

Official reference: https://www.jenkins.io/doc/book/pipeline/shared-libraries/

## Credentials and untrusted code

Use the lowest practical credential scope, normally the folder or item rather than controller-global. Report ID, Jenkins type, purpose, permission scope, and which trust boundary may use it.

- Never give trusted publication, signing, registry, cloud, deployment, or broad SCM credentials to pull requests/forks or any build that executes user-controlled code.
- Remember that an attacker can modify called build/test scripts without changing the Jenkinsfile.
- Separate SCM scan credentials from checkout/runtime credentials where supported, with only the provider permissions each operation needs.
- Prefer plugin steps that accept `credentialsId` directly.
- Use `withCredentials` only when a downstream tool needs an environment variable or file; bind for the narrowest possible duration.
- For secret files, bind outside `dir('subdir')` so temporary files do not land under a browsable workspace subtree.
- Avoid Groovy interpolation and command arguments containing secrets; arguments may appear in process listings.
- Disable shell tracing when necessary, but treat masking as accidental-disclosure reduction, never a security boundary.
- Never dump environments or persist credentials in artifacts, reports, URLs, SCM, or shell history.

References:

- https://www.jenkins.io/doc/book/security/credentials/
- https://www.jenkins.io/doc/pipeline/steps/credentials-binding/
- https://www.jenkins.io/doc/book/security/securing-org-folders-and-multibranch-pipelines/

## Artifacts and promotion

Build once. Assign a content digest or a non-reused version whose backing repository prevents overwrite. Publish it, record its source revision, and promote that exact identity.

- A mutable tag such as `latest` is not an immutable identity.
- `stash` transfers data within a Pipeline run; it is not a durable cross-run artifact repository and large stashes may burden the controller without a remote Artifact Manager.
- `archiveArtifacts` is basic build archival, commonly controller-backed, not a replacement for Nexus, Artifactory, an OCI registry, or another durable repository.
- Fingerprinting adds traceability; it does not guarantee immutability, authenticity, integrity, or provenance attestation.
- Verify the deployed digest/version after each promotion.
- Define rollback as redeploying a known-good immutable identity or invoking an authoritative versioned rollback interface.

References:

- https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#stash-stash-some-files-to-be-used-later-in-the-build
- https://www.jenkins.io/doc/book/using/fingerprints/

## SCM, Multibranch, and trust

Multibranch discovers branches containing a Jenkinsfile. Pull/change-request discovery requires the matching Branch Source plugin and configuration; indexing behavior depends on job and trigger configuration.

Before recommending change-request builds, determine:

- whether contributors or forks are untrusted;
- which Jenkinsfile revision is trusted;
- which repository-controlled scripts execute;
- which folder/global credentials child jobs can inherit;
- separate scan, checkout, and runtime credential permissions;
- resource limits for untrusted dynamic builds.

Never bind privileged credentials in untrusted change-request builds. Anyone able to supply an accepted Jenkinsfile can use every credential available to that job arbitrarily.

References:

- https://www.jenkins.io/doc/book/pipeline/multibranch/
- https://www.jenkins.io/doc/book/security/securing-org-folders-and-multibranch-pipelines/

## Production authorization

A Jenkins `input` step is an interaction mechanism, not a complete separation-of-duties policy.

- Set and verify `submitter`; without it, any Jenkins user may approve.
- Capture `submitterParameter` when approver identity must be audited.
- Jenkins administrators may still approve, and users with `Job/Cancel` may abort.
- Put approval before agent allocation where possible.
- Combine timeout with concurrency/stale-build controls.
- Keep deployment credentials least-privileged and environment-authorized; approval alone grants no secure environment boundary.

References:

- https://www.jenkins.io/doc/book/pipeline/syntax/#input
- https://www.jenkins.io/doc/pipeline/steps/pipeline-input-step/

## Primary official references

Accessed 2026-09-04:

- Pipeline: https://www.jenkins.io/doc/book/pipeline/
- Pipeline as Code: https://www.jenkins.io/doc/book/pipeline/pipeline-as-code/
- Pipeline best practices: https://www.jenkins.io/doc/book/pipeline/pipeline-best-practices/
- Pipeline syntax: https://www.jenkins.io/doc/book/pipeline/syntax/
- Jenkinsfile and credentials: https://www.jenkins.io/doc/book/pipeline/jenkinsfile/
