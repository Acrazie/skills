# Exact Snapshot and Freshness Controls

## Ownership and content

Review status and full staged/unstaged diffs, untracked files, and task-owned paths
or hunks. `git diff --cached` reviews the index; a stat or file list is insufficient.
An existing third-party index blocks a commit that would absorb it. Do not silently
unstage, stash, reset, clean, or commit other sessions' work. Whole-file staging is
unsafe when a file contains unrelated edits. Obtain an approved isolation/scope plan.

Use the required isolated worktree and avoid sharing a checkout/index during
mutation. If another writer cannot be excluded, stop; repeated checks alone cannot
close the check-to-action race. Different worktrees still share relevant refs and
configuration, so inspect those separately.

Inspect exact candidate content for credentials and transient artifacts, using
available repository controls. File-name patterns are signals, not a guarantee of
zero secret leaks. Assess legitimate non-secret example files by content and policy.
Never print secret values; redact findings. A suspected secret blocks delivery of
the affected content. Do not automatically edit .gitignore or untrack files; leaked
credentials may require separate rotation/remediation, beyond this delivery scope.

## Snapshot proof

After authorized targeted staging, inspect the complete index and identify the
candidate tree with `git write-tree`, plus HEAD and intended paths/hunks. An
unmerged index or unresolved Git operation blocks ordinary delivery.

Run required, inspected repository checks on the exact candidate snapshot using an
approved existing isolation method. A test of a working tree containing unstaged
dependencies does not validate a different index. If exact-snapshot proof is not
available, stop and explain; do not substitute a stat or an unrelated green run.
Do not install dependencies or execute unfamiliar/untrusted scripts without the
necessary permission. Use approved repository commands, not guessed package-manager
commands. Record checks, their results and relevant validation configuration.

After every content change, including formatter or hook edits, invalidate affected
proof and rerun affected checks. Keep hooks enabled; never use `--no-verify`, disable
hooks, or waive required red/unavailable checks as an emergency fast-path.

## Before each mutation

Recheck applicable assumptions immediately before staging, committing, pushing,
editing a PR, or restacking:
- repository/worktree identity, branch, HEAD, index and Git-operation state;
- task-owned content and approved candidate tree;
- material instructions, validation configuration, hooks and effective Git policy;
- for remote mutations, destination, observed remote branch SHA, PR head/base/state,
  and relevant stack parent/descendant state.

Refresh the affected evidence rather than rerunning unrelated scans. If HEAD/index
or content differs, inspect and revalidate the new candidate. If configuration
changes, reevaluate rules and affected checks. Changes in intended content, action,
destination, base/dependency, or destructive/shared-branch risk are material and
require renewed approval. Unrelated remote movement does not invalidate a local-only
commit; changes to its actual rules or content do.

After commit, compare the committed tree with the validated candidate and inspect
hook-modified files and remaining status. A mismatch is partial/unverified delivery,
not a green checkpoint. Preserve it for review; do not auto-amend, reset, or push.
Store the verified commit SHA and proof in the existing task record, not a new journal
framework. For push-only/PR-only requests, validate the relevant committed content
and reuse prior evidence only when it still applies to that exact snapshot.
