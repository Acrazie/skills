---
name: ci-cd-acrazie
description: >-
  Design, modernize, diagnose and validate repository-owned CI/CD pipelines across
  languages and tools, and conduct explicitly authorized pipeline runs, artifact
  publication, promotion, deployment or rollback through established interfaces.
  Use for substantive pipeline creation, changes or failures. Not for platform,
  controller, global runner or cloud administration, infrastructure provisioning,
  application features, Git shipping or unrelated tool upgrades.
license: MIT
---

# Repository CI/CD / Acrazie

Own one repository's CI/CD workflow, not its platform. Tool and stack differences
are internal references, not separately invocable skills or an executable plugin.
A tool not listed here may be supported through verified project evidence and
current documentation; no tool name implies tested runtime compatibility.

## Loading and authorization

Published defaults permit scoped model invocation. An explicit project kit or
stricter instruction overrides them: propose the named skill from metadata and
wait for its explicit user command before reading or dispatching its body. Apply
this gate separately to each dependency and returning specialist after a handoff.
Use `$skill-name` in Codex or `/skill-name` in Claude Code. Never read or delegate
an unactivated skill as a bypass. Internal references belong to the activated
skill; reading them is not approval to execute their recipes. These gates are not
filesystem controls or live-host proof; global homonyms may remain a blocker.

Selection grants no edits, installations, network, spawning or remote operation.
Reuse an applicable current contract with independent approval evidence, not a
status label; reopen only invalidated decisions. Clarify locally instead of adding
mandatory Interview for every pipeline. Obtain scoped realization approval before
editing; preserve existing files and required repository isolation.

Display user-owned choices with only Current state, numbered Options,
Recommendation and Response, localized. No question IDs, assumed consent or fixed
survey. An ADR is needed only for a durable, non-obvious trade-off; a repair does
not require ceremonial documentation. Reports default to chat; approve content
and destination before writing a report or ADR.

Installation/lockfile changes, effectful checks, remote reads, spawning/model
selection and Git actions retain separate applicable permissions. No implicit
staging, commit, push, PR, merge, auto-merge, deployment or rollback from edit approval.
Follow independently evidenced repository preauthorization only for its exact
conditions; proposed policy is not consent. Do not relax hooks or protections.

## Discover and bound

Read instructions and inspect the selected pipeline, scripts, manifests, lockfiles,
runtime declarations, tests, sanitized logs, artifact/deployment interfaces and
relevant decisions read-only. Do not execute unfamiliar scripts for discovery.
Infer create, modernize or diagnose; ask only material unresolved choices.
Classify CI-only, publication, delivery and deployment separately. Non-requested
capabilities are not applicable; CI-only work does not need production decisions.

Trace commands to project scripts, versioned interfaces or current documentation
for the actual tool/version. Record source, owner, revision, inputs, outputs and
authentication boundary. Conventional commands are candidates, not authoritative
facts. Never invent build, test, scan, publication, deployment or rollback commands.
Missing required execution facts block runnable generation for affected stages;
discover safely or present a clearly non-runnable proposal, not guessed defaults.

Read only matching references:
- [Stack evidence](references/stack-evidence.md): select the actual ecosystem.
- [Jenkins](references/jenkins.md): only for Jenkins-specific DSL, capabilities and trust.
- [Decision record](references/pipeline-decision-record.md) and
  [interview](references/interview-tree.md): unresolved scope/decisions.
- [Pipeline design](references/pipeline-design.md): substantive creation/restructuring.
- [Validation](references/validation.md): proof layers and causal diagnosis.
- [Remote operations](references/remote-operations.md): any remote action.

Other CI providers require their current configuration, permission/event semantics,
validation interfaces and documentation, not Jenkins syntax translated by analogy.
No closed provider list, automatic provider migration or new runtime dependency.

## Plan and implement

Present or reuse the approved outcome, exact edit set, checks and allowed effects.
Resolve applicable triggers/trust, authoritative stages, runner capabilities,
artifact identity, environments, credentials (references only), reliability and
validation limits. The [decision record](references/pipeline-decision-record.md)
is a proposal aid, not a mandatory persisted file or approval label.

Keep orchestration thin; reuse established project interfaces. Preserve behavior
in modernization unless approved otherwise. Diagnose the first causal failure;
do not hide deterministic failure with retry, weakened tests or swallowed exits.
Platform/controller/global runner administration, plugin installation and cloud
provisioning remain outside scope. Missing capabilities block dependent execution,
not permission to provision infrastructure. Repo Init owns minimal bootstrap;
Modernizer owns global audit/plan, not competing substantive pipeline implementation.

## Trust and delivery invariants

- Never request, display or persist secret values. Use an existing approved opaque
  credential mechanism or give a non-secret template for the user to operate.
  Masking is not isolation. Called tests/scripts may be attacker-controlled even
  when the pipeline definition is trusted; untrusted code must not receive privileged
  publication, signing, registry, broad SCM, cloud or production credentials.
- Verify runner OS/tools/isolation and capability instead of assuming a label or
  container boundary. A host Docker socket grants host-equivalent access. Separate
  trusted credential-bearing work from untrusted jobs and concurrent workspaces.
- Build once and promote the same immutable artifact identity; record provenance
  and overwrite controls. Do not rebuild per environment or call mutable tags proof.
- Establish environment authorization separately from a pipeline approval prompt.
  Decide production approver identity, timeouts, stale/concurrent deployment behavior,
  verification and known-good rollback when applicable; never silently fill values.
- Read only the matching existing deployment-interface checklist: [VM/SSH](references/deployment-vm-ssh.md),
  [Compose](references/deployment-docker-compose.md), [Kubernetes](references/deployment-kubernetes.md),
  [AWS](references/deployment-aws.md), [Azure](references/deployment-azure.md),
  [GCP](references/deployment-google-cloud.md). These are checklists, not permission
  to provision infrastructure, choose a vendor or run historical examples.

## Verify and report

Run the smallest sufficient approved project checks on the exact candidate snapshot.
Offer independent review when appropriate; if policy/workflow makes it required or
user accepts the gate, require fresh independent evidence on that snapshot. Reviewer
activation, context isolation, spawning and model choice remain separate; absent
required reviewer blocks acceptance, never substitute implementer self-review.

Distinguish structural checks, provider-aware lint, actual CI run, published artifact
and live deployment/rollback proof. A linter cannot establish runtime success.
Use [remote-operation boundaries](references/remote-operations.md) before triggering,
approving, aborting, publishing, deploying or rolling back. Missing required checks
remain blocked, not waived. Read back exact state after mutation and before retrying
ambiguous non-idempotent actions; do not replay blindly.

Report actual edits, snapshot, commands/environment/results, review status when
applicable, artifact/run identities, remote effects and unverified/blocked stages.
No remote run from local validation success, no deployment claim from a green PR.
