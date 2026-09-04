# Interview Tree

Ask only user-owned decisions that remain unresolved after repository and authorized environment inspection. Work from prerequisites toward dependent branches.

## 1. Intent and capability boundary

Infer the mode:

- no Jenkins pipeline exists and Jenkins CI/CD is requested -> `create`;
- an existing pipeline's structure, capability, or policy must change -> `modernize`;
- a failed pipeline or run needs a causal correction -> `diagnose`.

Then classify the requested boundary: CI-only, publication, continuous delivery, or deployment. Mark later capabilities `not applicable` when explicitly outside scope. Do not ask a CI-only user for environments or rollback.

Ask the user to choose a mode or boundary only when evidence supports materially different interpretations.

## 2. Pipeline inputs and outputs

Resolve applicable decisions:

1. Which branch, tag, change-request, or manual event triggers work?
2. Which authoritative commands build, lint, test, scan, package, and publish?
3. What immutable artifact leaves CI, where is it stored, and how is overwrite prevented?
4. Which environments exist, and how is the same identity promoted?
5. Which authoritative deploy, verification, and rollback interfaces apply?

An interface may live in the application repository, a governed Shared Library, a platform/GitOps repository, or a managed deployment system. Record source, owner, version, inputs, authentication boundary, and rollback semantics. If absent, do not offer a conventional guess.

## 3. Jenkins execution and trust

Resolve before runnable generation:

- actual controller and relevant plugin versions, or an explicit compatibility gap;
- job type, SCM provider, Branch Source integration, indexing, and webhook ownership;
- verified agent OS, labels/capabilities, isolation, executors, tools, and workspace behavior;
- whether change-request contributors/forks and called repository scripts are trusted;
- separate SCM scan, checkout, build, publication, signing, registry, cloud, and deployment credential boundaries;
- credential IDs, Jenkins types, lowest practical folder/item scope, and allowed jobs;
- global/folder, trusted/sandboxed, implicit/explicit Shared Libraries, immutable revision, SCM owner, and override policy;
- retention, timeout, concurrency, retry, notification, and stale-build policies.

Never expose privileged credentials to untrusted code. Never schedule application work on the built-in node. A Linux recommendation is not a verified agent label.

## 4. Deployment safety

When deployment is applicable, resolve:

- authorized production submitter or policy and the required audit identity;
- evidence required before approval and approval timeout;
- stale-build and concurrent-deployment behavior;
- exact artifact identity carried forward;
- environment-level authorization independent of Jenkins approval;
- post-deployment verification, known-good rollback identity, and rollback command.

“Rollback if needed” and an unrestricted `input` step are not sufficient decisions.

## 5. Remote authorization envelope

Before remote access, present:

- exact controller/registry/cloud/cluster/VM target;
- read, lint, trigger, approve, abort, replay, publish, deploy, or verify operations;
- submitted repository data;
- job full name, branch/ref, source revision, parameters, artifact identity, and environment when relevant;
- possible side effects;
- read-back verification sequence;
- expiry of authorization.

One approval covers only this envelope. Scope changes require reapproval.

## 6. Decision gate

Summarize verified facts, recommendations, selected decisions, rejected alternatives, risks, exclusions, and validation limits. The frontier is empty only when every value needed for the approved capability boundary is known or explicitly excluded.
