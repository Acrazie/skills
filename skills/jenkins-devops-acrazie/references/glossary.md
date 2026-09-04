# Jenkins CI/CD Domain Glossary

## Application repository
The single version-controlled product codebase whose delivery process is being created, modernized, or repaired.

## Pipeline
The ordered, observable flow that converts a source revision into verified delivery outcomes.

## Continuous integration
The part of the pipeline that integrates a source change by building it and evaluating agreed quality signals.

## Continuous delivery
The capability to move a verified artifact through environments by controlled, repeatable promotion.

## Continuous deployment
A delivery policy in which an artifact may advance to production without a manual approval step after all required evidence passes.

## Stage
A named responsibility in the pipeline with a visible outcome and failure boundary.

## Artifact
The versioned output produced by the build and eligible for publication or deployment.

## Immutable artifact
An artifact whose identity always denotes the same content.

## Promotion
Advancing an already-built immutable artifact to another environment without rebuilding it.

## Environment
A distinct operational destination with its own access boundary and verification expectations.

## Production approval
The decision gate that authorizes a specific immutable artifact to enter production.

## Rollback
A defined operation that restores a known-good version or state after an unsuccessful promotion.

## Credential reference
A non-secret identifier that tells Jenkins which managed credential to bind for a narrowly scoped operation.

## Plugin dependency
A Jenkins capability outside the assumed baseline that must exist for a pipeline directive or step to work.

## Shared Library
A separately versioned collection of reusable Jenkins Pipeline code shared across repositories.

## Agent
The execution environment that provides a workspace and runs pipeline commands.

## Validation evidence
A recorded result showing what was checked, in which environment, and what remains unproven.

## Durable pipeline decision
A choice about triggers, stage boundaries, artifacts, environments, credentials, approvals, rollback, or execution architecture whose reversal has meaningful cost.

## Pipeline repair
A change that restores previously decided behavior without changing a durable pipeline decision.

## Stack specialist
A complementary skill that interprets one application ecosystem precisely while leaving Jenkins-wide governance and approval to the general skill.
