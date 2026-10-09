# Delivery and State-Aware Recovery

## Commit

For approved commit-only delivery, commit only the reviewed and validated index,
using the discovered message/signing convention without co-author trailers. Verify
its tree and SHA against approved proof, report remaining changes, then stop.
Do not infer push or PR permission. Never bypass hooks or rewrite a previous commit
to conceal a failure.

## Push

Immediately before pushing, verify approved immutable commit SHA, destination and
observed remote state. Inspect outgoing commits, not just the latest working diff:
pre-existing branch commits must also belong to the approved delivery scope.
For an ordinary existing branch, require a permitted fast-forward; divergence
requires investigation and a separately approved integration plan, not force-push.

Push the verified immutable SHA to the explicit branch ref rather than a mutable
local branch name. Example after substituting validated identifiers:

```bash
git push <remote> <verified-commit-SHA>:refs/heads/<approved-branch>
```

Verify the actual push endpoint's branch SHA equals the delivered SHA. A confirmed
absent branch can use an explicit empty expected lease to prevent racing branch
creation; an existing branch can use its observed expected SHA as a compare-and-set
check for the approved fast-forward. These guards do not authorize non-fast-forward
rewrites. If supported protection is unavailable or the state moves, stop rather
than silently expanding scope. Upstream configuration changes are optional and
require authorization; do not assume `-u` is always needed.

An unexpected result after push is partial/unverified delivery. Preserve evidence,
inspect the remote, and never overwrite or delete another writer's commits.

## Create or update a PR

Query existing PRs, including closed/merged ones, for the exact head repository,
branch and intended base. A branch name alone is insufficient for fork identity.
Reuse an existing PR only if its identity and intended action match approval. On
multiple matches, a closed/merged PR, changed base, or changed head SHA, stop and
clarify rather than duplicating, reopening, or editing automatically.

Before creation, verify the branch was actually pushed and identify explicit
repository/head/base. Use the applicable template and approved title/body/state.
Example, only for authorized PR creation:

```bash
gh pr create --repo <owner/repository> --head <approved-head> --base <approved-base> --title <title> --body-file <body-file>
```

Add `--draft` only according to approved state/policy. Validate fork head support;
unsupported topology requires an approved alternative, not an implicit fork or push.
`gh pr create --dry-run` may still push: do not use it as a read-only safety check.

For updates, name the exact PR and approved fields. Verify actual PR repository,
head SHA/repository/branch, base, state, Draft status, URL and diff against intended
scope after creation/update. Inspect CI status and mergeability when accessible;
pending, failed, unknown, or inaccessible results must be reported accurately.
Attach created/managed PRs using the harness artifact tool when available.

## Recover without duplicates

Commands are not an atomic transaction. After an interruption or ambiguous network
response, query current state before retrying any mutation:
- Commit failed: inspect HEAD, index, hook edits and operation state; do not assume
  nothing changed. Commit succeeded: verify and reuse its SHA, do not recommit.
- Push failed/ambiguous: inspect the actual remote endpoint. If the intended SHA is
  present, verify and continue only remaining authorized steps. If it moved or is
  inaccessible, stop; do not retry with a broader lease or forced update.
- PR creation failed/ambiguous: query exact existing PR identity before retrying.
  Reuse a verified matching existing PR; no duplicate, implicit reopen, or unapproved edit.
- PR update failed/ambiguous: inspect current fields and perform only unapplied,
  still-authorized changes after rechecking state.
- A stack partly updated: use per-node outcomes/checkpoints and the stack recovery
  protocol; never replay all rewrites or assume all descendants succeeded.

Report completed steps, verified SHAs/PR fields, remaining authorized work, changed
assumptions and unresolved proof. Do not start an unattended monitor or merge when
CI is pending. Rollback, cleanup and additional repairs are separate decisions.

## Documentation consulted

- [Git push](https://git-scm.com/docs/git-push): explicit refspecs and expected leases.
- [GitHub CLI create](https://cli.github.com/manual/gh_pr_create): explicit destinations and dry-run side effects.
- [GitHub CLI edit](https://cli.github.com/manual/gh_pr_edit) and
  [view](https://cli.github.com/manual/gh_pr_view): explicit PR identity and verification.

Consult current docs and installed help before adapting commands; examples do not
supersede repository policy or operation-specific approval.
