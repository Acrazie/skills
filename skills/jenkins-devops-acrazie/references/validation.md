# Validation Reference

Validation evidence has layers. Report which layer was reached and never promote weaker evidence as proof of stronger behavior.

## Layer 1: authoritative evidence

Confirm that every invoked command or interface has a known source, owner, version, input contract, expected output, authentication boundary, and applicability. Check file paths, executable bits, environment names, artifact identity, credential IDs, Pipeline capabilities, and Shared Library revisions.

Completion criterion: every generated stage maps to authoritative behavior; unresolved execution facts block runnable generation rather than becoming guesses.

## Layer 2: local checks

Run safe repository-supported checks: native syntax, formatter, linter, unit tests, manifest validation, Dockerfile/Compose validation, Helm rendering, Kustomize build, or deployment-script tests.

Do not install or migrate project tooling unless approved. Record exact commands, exit status, material output, and skipped checks with blockers.

## Layer 3: structural Pipeline review

Check syntax model, stage flow, agent-step family, quoting, credential scope, untrusted-code boundaries, artifact handoff, approval authorization, post conditions, and plugin/library references.

Generic Groovy parsing cannot prove CPS compatibility, Declarative-model validity, installed steps, or runtime behavior. Label this evidence structural.

## Layer 4: Declarative controller linter

Jenkins documents a controller-backed Declarative linter:

```text
POST $JENKINS_URL/pipeline-model-converter/validate
form field: jenkinsfile=<contents of Jenkinsfile>
curl form: -F "jenkinsfile=<Jenkinsfile"
```

Official reference: https://www.jenkins.io/doc/book/pipeline/development/#linter

The linter validates the Declarative model/syntax. It does not prove agent labels/tools, arbitrary Scripted behavior, credentials, workspace behavior, network access, external services, publication, deployment, rollback, or successful execution.

Prefer the Jenkins SSH CLI linter when the organization's secure CLI access is already established. For HTTP, use TLS and an existing opaque, least-privilege API-token mechanism. API-token authenticated POST requests are exempt from CSRF crumbs; other clients may require crumb and session handling. Never place tokens in URLs, SCM, reports, or shell history.

Sending a Jenkinsfile discloses repository pipeline content. Obtain a remote authorization envelope first. If the runtime cannot inject credentials opaquely, provide a non-secret command template for the user to execute rather than asking for a token.

Completion criterion: record controller identity/version when known and exact linter diagnostics without secrets.

## Layer 5: authorized run

A real run is the only end-to-end proof of agents, tools, credentials, services, artifacts, approvals, deployment, and rollback behavior.

Before triggering, authorize the exact controller URL, job full name, branch/ref, source revision, parameters, expected artifact, environment, possible publication/deployment, verification reads, and expiry. Treat Replay as privileged remote code execution, not validation.

After trigger, approval, abort, publication, or deployment, read back the exact run/artifact/environment state before claiming success. Before retrying an ambiguous non-idempotent request, check whether the first request took effect.

Completion criterion: record run URL/ID, result, artifact identity, reached environment, read-back evidence, and unexercised stages.

## Diagnostic evidence

Preserve the failing stage/command, first causal error, agent/workspace signals, source revision, artifact identity, relevant plugin diagnostics, and sanitized surrounding log lines. Classify deterministic versus transient failure before recommending retry. Never weaken tests, disable verification, or swallow an exit code merely to turn a build green.
