# Repo Modernizer commit strategy task contract

Approved on 2026-10-07 through the grill-with-docs interview. This task updates `repo-modernizer-acrazie`, not a target repository's tooling or remote settings.

## Scope and ownership

Extend the brownfield modernizer's existing inspection and execution guides with two distinct responsibilities: discover or formalize the target repository's Git policy, and follow an approved migration commit plan. Reuse the adaptable governance model already owned by `github-repo-init-acrazie` without invoking it or requiring its installation. No new skill or orchestration layer.

## Approved acceptance criteria

1. Discover applicable Git rules with provenance; preserve existing conventions and block unresolved conflicts. Do not impose Conventional Commits universally.
2. When policy is missing, propose `docs/git-workflow.md` and create it only after approval. Keep existing governance consistent without overwriting it. File creation and enforcement tooling are separate decisions.
3. The approved strategy is binding before every commit: verify exact staged scope, coherent boundaries, selected message convention and validation evidence. Non-compliance blocks execution; no silent exception or hook bypass.
4. Coherent, validated, reversible migration units replace a rigid one-commit-per-tool/layer rule. Group inseparable changes in an announced unit; never generate broken intermediate commits merely for granularity.
5. Follow actual repository/user authorization. Without applicable permission, request it. Staging/commit, push and PR remain distinct permissions; strategy approval alone does not grant them.
6. Compliance checks remain mandatory without hooks or CI. Hooks, dependencies, CI and GitHub settings are separately approved options, not implicit installations.
7. Prepare required Tier 2/3 ADRs before validation and include them in the corresponding migration commit.
8. Record validated checkpoint revisions and their proof. Do not equate HEAD with a green checkpoint. After three unsuccessful repairs, preserve work and report a blocker; no automatic destructive rollback. Any destructive recovery requires separate explicit confirmation and preservation of unrelated work.
9. Preserve the skill's current task-scoped invocation policy and the rest of its six-pillar modernization program.

## Deliverables and proof

- Isolated worktree and dedicated branch.
- Updated entry instructions, inspection/execution references and one focused commit-strategy reference.
- Glossary definitions limited to modernization-specific terms, without implementation details.
- Repository structural validators, local-link checks, static contract regression checks and documented compliance scenarios. Static proof is not a live agent evaluation or enforcement guarantee.
- Independent adversarial review in a fresh context, approved by the user. Acceptance applies only to the exact final snapshot.

## Decisions and exclusions

The policy is mandatory but tooling is optional. Conventional Commits remains valid where chosen or required, including this skills repository; it is not imposed on all target repositories. Existing source rules and remote restrictions cannot be weakened by a local plan.

Do not broaden into framework/runtime recommendations, tooling installation, release setup, production changes, or modification of installed skills. This instruction update is not itself a Tier 2/3 target migration. No separate ADR is required for this readily reversible documentation change; the approved trade-offs are recorded here.

## Delivery evidence

To be recorded after validation and independent review. This contract approval authorizes implementation and local validation; publication follows applicable repository/user delivery permissions.
