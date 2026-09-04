# ADR 0001: Modernize the Jenkins delivery pipeline

- Status: Accepted
- Date: 2026-09-04

## Decision

Convert the repository pipeline to Declarative syntax. Run Composer install from the lockfile, the `ci:lint`, `ci:test`, and `ci:build` scripts, then build and push the container once. Identify the image by the Git commit and capture its immutable registry digest. Promote that same digest to staging and production through `ops/deploy.sh`. Require a manual production approval with a timeout. Use Jenkins credential ID `orders-registry` with username/password type. Preserve `ops/rollback.sh` as the rollback mechanism. Publish JUnit results. Do not install plugins; report any required plugin dependency.

The repository owner has approved this decision and its exact local implementation.
