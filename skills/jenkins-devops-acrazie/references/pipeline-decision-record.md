# Pipeline Decision Record

Use this structure for the proposal shown before any local edit. After approval, convert it into the repository's ADR format while preserving the substance.

```markdown
# [NNNN]. Jenkins CI/CD for [application]

- Status: Proposed | Accepted | Superseded
- Date: YYYY-MM-DD
- Supersedes: [ADR path or None]

## Context
- Requested outcome:
- Inferred mode: create | modernize | diagnose
- Capability boundary: CI-only | publication | delivery | deployment
- Repository/environment evidence:
- Constraints:

## Decision
### Triggers and trust
- Branches/tags/change requests/manual:
- Trusted Jenkinsfile revision:
- Untrusted contributor policy:

### Stages and commands
| Stage | Authoritative command/interface | Agent capability | Output |
|---|---|---|---|

### Artifact and provenance
- Immutable identifier and overwrite control:
- Repository/registry:
- Build-to-deploy traceability:

### Environments and promotion
| Environment | Entry condition | Deployment interface | Verification | Rollback |
|---|---|---|---|---|

### Production authorization
- Allowed submitter/policy:
- Audit identity:
- Required evidence and timeout:
- Stale/concurrent build behavior:

### Jenkins capabilities
| Capability | Core/plugin/library | Version/trust evidence | Required action |
|---|---|---|---|

### Credentials
| Credential ID | Jenkins type | Purpose | Scope/trust boundary |
|---|---|---|---|

### Validation
- Local checks:
- Declarative/controller checks:
- Authorized run needed:

## Alternatives considered
- [Alternative]: [reason rejected or deferred]

## Consequences and risks
- Positive:
- Negative:
- Residual risks:

## Explicit exclusions
- [Not-applicable capability]
- Controller administration
- Plugin installation
- Global agent configuration
- Jenkins Configuration as Code
```

## Lifecycle

- Draft in the conversation first. Do not write an unapproved proposal to the repository.
- Every local repository edit requires approval of its exact edit set.
- After approval of a durable decision, write the ADR as `Accepted` and implement exactly it.
- Follow the existing ADR directory, naming, metadata, and numbering. Without one, use the next unused `docs/adr/NNNN-jenkins-ci-cd.md`.
- Supersede historical decisions with a new ADR; do not rewrite history.
- A repair may omit the ADR only when it restores already-decided behavior. It still requires approval of the causal diagnosis, exact edit, and validation plan.
