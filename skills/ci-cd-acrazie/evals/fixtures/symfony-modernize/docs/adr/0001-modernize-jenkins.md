# ADR 0001: Modernize the Jenkins delivery pipeline

- Status: Accepted
- Date: 2026-09-04

## Decision

Convert the repository pipeline to Declarative syntax. Run Composer install from the lockfile, the `ci:lint`, `ci:test`, and `ci:build` scripts, then build and push the container once. Identify the image by the Git commit and capture its immutable registry digest. Promote that same digest to staging and production through `ops/deploy.sh`. Require production approval from Jenkins group `orders-release-managers`, capture the approver identity, and expire the approval after 30 minutes. Use Jenkins credential ID `orders-registry` with username/password type. Preserve `ops/rollback.sh` as the rollback mechanism. Publish JUnit results. Do not install plugins; report every required Pipeline capability and its providing plugin, including the production input step.

The repository owner has approved this decision and its exact local implementation.
