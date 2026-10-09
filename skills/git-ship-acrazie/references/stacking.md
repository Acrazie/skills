# Complete Stacked-PR Lifecycle

## Establish dependencies and authority

Prefer independent PRs for independent changes. Similar files/diffs or simultaneous
branches do not prove dependence. Confirm each child's dependency on its parent and
an acyclic topological order; ambiguous relationships require user resolution.

Use the existing task record/recap to capture each node's repository, branch, owned
worktree, local/remote SHA, PR identity/state, old parent SHA (the exact boundary of
inherited commits), intended new base, and child-only commit range. Record descendants
before changing parents; mutable branch names and reflog guesses are not durable
boundaries. If the range contains unexpected merges/foreign commits or cannot be
established, stop and approve a topology-specific plan rather than blindly rebasing.

Inspect parent and descendant local/remote states, protections, shared use and
applicable rules. Never manipulate another session's checkout or unfinished Git
operation. Coordinate shared branches before rewrites; an isolated worktree does
not confer branch ownership. For cross-fork or unsupported PR bases, verify host/CLI
capabilities and seek an approved compatible plan; no new stack tool installation.

## Create and update a stack

Present per-node scope, base/head, dependencies, validation, push/PR actions and
risks for approval. This approves delivery of existing task content, not implementing
new application changes or inventing branches/dependencies. Create approved new
branches/worktrees only with correct starting state and repository isolation rules.

Deliver parents before children. For each child, validate its complete snapshot and
its child-only diff against the selected parent. Push verified content, then create
or reuse the exact PR with explicit head and `--base <parent-branch>`. Verify PR
head/base and diff; keep dependency links in the applicable PR template/body when
that update is authorized. Do not change unrelated PR fields or merge anything.

When a parent changes, freeze affected writers, capture old boundaries and branch
SHAs, and reevaluate the descendants in topological order. Explain changed ranges,
validation and any remote rewrites before approval. Do not restack by habit when
existing history/base already fits; a base-only update may suffice.

## After merge, closure, or replacement

Read the actual parent PR state, merged result, destination and current descendants.
Do not infer merge from a deleted branch. For a normal merge preserving ancestry,
check whether only retargeting the immediate child's PR is needed. For squash or
rebase merges, inherited old parent commits may no longer be ancestors: do not
replay them into the child or rely on automatic patch detection to identify scope.

Given a verified linear child-only range and authorized local rewrite, the native
pattern is:

```bash
git rebase --onto <verified-new-base-SHA> <recorded-old-parent-SHA> <owned-child-branch>
```

Use immutable recorded boundaries. Preserve approved recovery checkpoints before
rewriting. Validate the resulting tree, intended child-only changes, lost/extra
commits and affected checks. Unexpected dropped commits or content changes stop
publication. For deeper descendants, use their recorded old parent boundary and
their parent's newly verified tip; do not substitute a newly moved branch for the
old parent boundary.

Publish each verified node only under applicable authorization, then update the
exact PR's base (e.g. `gh pr edit <PR> --repo <repo> --base <approved-base>`), inspect
its new diff/head/base, and record outcome before the next node. Parent updates
normally retain parent-branch bases; after a parent merges into the destination,
its immediate children target the approved destination, while deeper children still
target their surviving parent. Re-read actual host behavior; never assume automatic
retargeting or history synchronization has already completed safely.

A closed-but-unmerged parent or replacement parent requires a user decision about
retaining its changes, moving dependencies, or retiring the stack. Do not discard
or absorb the parent's work, reopen PRs, or select a replacement silently. Do not
automatically delete merged branches; retain boundaries needed for recovery.

## Published rewrites and concurrency

Remote non-fast-forward changes require separate authorization identifying affected
branches, expected old remote SHAs, replacement snapshots, collaborators and risks.
Obey protections; no plain force-push. With approved exclusive local ownership and
supported Git, use an explicit immutable expected lease:

```bash
git push --force-with-lease=refs/heads/<branch>:<expected-remote-SHA> <remote> <verified-new-SHA>:refs/heads/<branch>
```

A bare lease can be weakened by background fetch. Capture expected remote SHA from
reviewed actual endpoint state before the rewrite; do not refresh the expectation
merely to make a rejected lease pass. If the remote moves, stop, inspect new work,
replan/revalidate and obtain renewed approval. Lease protection guards one ref,
not an entire stack or concurrent PR metadata. Check and verify each node separately.

## Conflicts, interruption, and rollback

Stop on conflict; preserve operation/worktree state and report affected node.
Resolving application conflicts is not blanket delivery authority: obtain an
approved repair scope. Continue or abort only the agent-owned operation under
applicable authorization; do not reset, clean, stash, or abort someone else's work.

Before resuming, reconcile recorded old/new SHAs with actual branches and PRs.
Already verified nodes are not replayed; pending descendants require fresh checks.
An ambiguous result must be inspected before retry. Any rollback of published
history requires separate authorization and current-state protection; no automatic
multi-branch rollback. Report partial stack status, remaining nodes, CI and
mergeability without claiming all-or-nothing success.

## Documentation consulted

- [Git rebase](https://git-scm.com/docs/git-rebase): transplant child-only ranges with --onto.
- [Git push](https://git-scm.com/docs/git-push): explicit expected-value leases and background-fetch hazards.
- [GitHub CLI edit](https://cli.github.com/manual/gh_pr_edit): change an explicit PR base.
