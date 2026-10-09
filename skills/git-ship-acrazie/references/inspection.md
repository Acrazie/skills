# Repository Identity, Policy, and Scope

## Discover before choosing

Read all applicable instructions, AGENTS.md, CONTRIBUTING.md, docs/git-workflow.md
or its equivalent, templates, hooks, CI, release/signing rules and relevant task
proof. A workflow document does not excuse skipping applicable higher-priority
instructions. Recent commits are evidence of convention, not authorization.

Record the repository root, worktree path, current branch or detached HEAD, HEAD
SHA, index/working status, active merge/rebase/cherry-pick, and other worktrees.
Establish task ownership and delivery scope; do not steal a branch checked out by
another session or modify its worktree. A detached HEAD or uncertain ownership
requires an approved branch/isolation plan before delivery.

Inspect effective relevant Git configuration and hooks, not just tracked files:
configuration, hooks, refs, and remote changes can affect multiple worktrees.
Record only non-secret relevant values; redact credentials in URLs/output.

For every relevant rule, identify source and scope. Apply Conventional Commits only
when required or selected; do not impose a branch prefix, Draft state, or merge
method against repository policy. No co-author trailers. Identify the actual default
and protected branches, not only main/master; block unauthorized direct delivery.
Do not change repository or organization settings to bypass protections.

Distinguish absent rules from inaccessible remote rules. With no documented policy,
propose a minimal explicit delivery strategy using verified facts and ask for
approval: no mandatory initialization or new governance file. Repository setup is
optional, separately requested work. On a policy conflict, block the affected action
and request resolution; a user preference cannot override enforced restrictions.

## Resolve destinations and capabilities

Inspect remotes, effective push URLs/refspecs, upstream, fork relationships, remote
branch state and PR identity. Never assume origin, the current tracking branch, or
the CLI-selected repository is the intended destination. Confirm the PR base/head
repository and branch explicitly. Check the installed CLI's supported flags before
using examples; unavailable tools do not authorize installation or fallback mutations.

Refresh only relevant remote refs when authorized. If refresh/read fails, record
unverified state; stale cached refs are not current remote evidence. A commit-only
request in a local-only repository needs no imaginary remote gate. Block a remote
action when its destination or necessary remote safety evidence is unavailable.

Inspect relevant protections/permissions and existing PRs read-only when accessible.
Do not treat missing access as absence of protections. Determine what checks apply
to the chosen action and destination; do not invent broad remote administration.

## Bound action scope

Separate staging, commit, push, PR creation/update, and stack restructuring in the
recap. Explicitly exclude unrequested steps. PR updates include base/body/state
changes; existing PRs are not blanket edit authorization. Merge, branch deletion,
force-push and destructive recovery need their own authorization.

Default to a proposed Draft PR only when repository policy and user intent permit;
ready requests or repository rules take precedence. A Draft PR can still trigger CI
and notifications; it is not a security or deployment barrier.
