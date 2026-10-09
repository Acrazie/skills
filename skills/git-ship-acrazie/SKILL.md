---
name: git-ship-acrazie
description: >-
  Safely commit, publish branches, and create or update pull requests under repository
  rules, including dependent PR stacks and post-merge restacking. Use when the user
  requests shipping, a commit, a push, a PR, or management of an existing stack;
  not merely because implementation is complete. Not for implementing task code,
  repository initialization, automatic merging, or deployment.
---

# Git Ship / Acrazie

Deliver the requested actions, not an automatic commit/push/PR bundle. A
commit-only request ends after a verified commit. A PR-only request does not
implicitly authorize a commit or push. Keep simple delivery as the default;
use stacks only for actual dependencies.

## Boundaries

- Selection permits discovery and preparation. Before delivery mutations, present
  one consolidated recap and obtain explicit approval of its actions, exact scope,
  destinations, and evidence unless a current,
  independently evidenced repository preauthorization covers that exact action
  and its required conditions. Read [repository action policy](references/repository-action-policy.md)
  when `.acrazie/engineering.json` is present. Existing implementation approval is
  not shipping approval; a policy file or proposed policy edit is not proof of
  consent. One approval can cover named steps; it does not cover material changes.
- Require separate authorization for rewriting published history. Never merge,
  enable auto-merge, delete branches, reset, clean, stash, install tools, change
  governance/settings, or deploy under ordinary delivery approval.
- Respect applicable repository rules and technical protections. Never bypass hooks
  with `--no-verify`, disable checks, or relax required validation to force delivery.
- Preserve unrelated and third-party work, including an existing index. Never include `Co-authored-by:`.
- A worktree isolates files and index, not shared Git configuration or remote refs.
  Fresh observations are not locks; do not promise atomic multi-step delivery.

## 1. Discover identity, rules, and requested outcome

Read [inspection](references/inspection.md). Establish the repository/worktree,
branch and HEAD, applicable instructions, remote and push destination, PR repository
and base, required validations, existing PRs, and explicit action scope. Resolve
material ambiguity before mutation; distinguish inaccessible state from absent state.

For dependent PRs or an existing stack, also read [stacking](references/stacking.md).
Detecting possible dependencies permits a proposal, not automatic restacking.

## 2. Prepare and prove the exact snapshot

Read [pre-flight](references/pre-flight.md). Inspect staged, unstaged, and untracked
content; identify task-owned paths or hunks without absorbing other work. Determine
whether isolation/ownership is sufficient. Validate the exact candidate tree, not a
different working tree. Track checks and material configuration against that tree.

If staging is needed to prepare the candidate, establish scoped staging permission
first, explicitly or through a valid independently evidenced staging grant. Do not commit before the delivery recap.
If required proof is unavailable, disclose the gap and block the affected action.

## 3. Present the delivery recap and establish authorization

Include:
- requested actions and excluded actions;
- repository/worktree, branch, HEAD, candidate tree identity and intended diff;
- remote destination, observed remote SHA or confirmed absence, PR repository,
  head/base and existing PR identity, including stack relationships if applicable;
- discovered policy and conforming message, PR title/body/template and requested state;
- validation results, secret-control limits, stale/inaccessible evidence, and risks;
- for a stack, per-branch old/new bases, commit ranges, affected descendants,
  shared-branch coordination, recovery checkpoints and separately authorized rewrites.

Apply the discovered action-specific authorization mode. Ask for approval when
required; stop when forbidden or the policy conflicts. Use preauthorization only
under the verified repository-action-policy conditions. Do not infer approval from
an unrelated "go", past workflow, completed implementation, a configuration label,
or approval of a different snapshot. Restrictive current instructions prevail.

## 4. Execute only approved steps with boundary checks

Follow [delivery and recovery](references/pr-delivery.md) and, when applicable,
[stacking](references/stacking.md). Before each mutation, recheck relevant identity,
content, policy, and remote assumptions. Changed evidence invalidates affected
checks; material scope/destination/risk changes require renewed approval.

Verify outcomes after each step. Stop on unexpected state, conflicts, failed checks,
or ambiguous remote results. Resume from observed state rather than replaying steps.

## 5. Report verified outcomes

Report actual completed actions, validated tree/commit SHA, verified remote SHA,
PR identity/head/base/state and links, and stack status when relevant. Distinguish
pending/failed CI, unknown mergeability, inaccessible evidence, and partial delivery
from success. Do not claim tests, CI, deployment, or live verification not performed.
Attach created or managed PRs through the harness artifact tool when available.

## Instruction validation

Run `python3 skills/git-ship-acrazie/scripts/test_delivery_contract.py` from the
repository root for static contract/link checks, and
`python3 skills/git-ship-acrazie/scripts/test_repository_authorization.py` for
policy eligibility checks on fixture observations. Behavioral prompts are in
`evals/evals.json`; static checks and simulated answers do not prove live delivery.
