# Git Ship Critique

## Objective
Assess whether git-ship-acrazie safely delivers work in both personal and third-party repositories when local and remote state can change concurrently, including the complete lifecycle of stacked pull requests.

## Scope
- Included: skill instructions, references, invocation metadata, existing evaluation scenarios, and relevant neighboring ownership boundaries.
- Priorities: local/remote freshness and concurrent work; exact approved delivery snapshot; complete stacked-PR management (creation, base updates, and descendant reorganization after merge); repository-adaptive conventions; action-specific authorization; recovery without duplication; verified delivery outcomes.
- Include parent squash/rebase merges, parent updates/closure/replacement, shared descendants, and separately authorized history rewrites with concurrent-update protection.
- Excluded: modifying skills, implementing recommendations, executing delivery or stack operations, committing, pushing, creating or merging PRs, GitHub administration, deployment, and behavioral evaluations that mutate repositories.
- Only the approved contract may be written now. The English report at docs/critics/git-ship-acrazie.md requires separate approval of its content and exact destination before writing.

## Success criteria and expected evidence
- C1: Trace the current delivery journey and invariants against each selected priority, citing the assessed source revision and precise source locations.
- C2: Distinguish observed instruction gaps, declared user needs, and unverified behavioral hypotheses; do not claim that reading instructions proves live execution failures.
- C3: Compare retaining, simplifying, or extending the current workflow; propose bounded recommendations and smallest discriminating validation scenarios.
- C4: Preserve scope-specific approval, other sessions' work, secrets protection, hook enforcement, and explicit authorization for destructive operations in recommendations.
- C5: Present a proposed critique for user validation; do not persist the report or implement recommendations without separate authorization.

## Decisions and context
- The user uses both personal and third-party repositories, sometimes with concurrent branches and changing configurations.
- The user suspects insufficient repeated local/remote verification; this is declared experience, not a reproduced failure.
- The user selected complete stacked-PR management rather than detection and proposal only.
- Initial discovery examined local main at beb56b1985607f951b0279d0ab1eadce30a84fe9. After refreshing origin/main, assessment uses 38472cbc447eaf5a315a639da0b969da0f9c85e2 in isolated worktree .worktrees/codex/git-ship-critique. Invocation wording changed between revisions; refreshed source is authoritative for findings.

## Approval
Status: approved
On 2026-10-09 in this chat, the user selected both repository audiences, described concurrent-state concerns, requested complete stacking management, then accepted the proposed scope extension with "ok" after the assistant explicitly asked "Tu approuves cette extension ?". This approves the preceding critique contract, its extended dimensions, and its proposed contract destination; it does not approve report content, implementation, or shipping.

## Delivery evidence
C1-C3: Read the refreshed skill, its three references, invocation metadata, and three evaluation prompts. Compared relevant ownership and staged-snapshot principles in repo-modernizer-acrazie and github-repo-init-acrazie. Traced preflight, approval, staging, commit, push, and PR reporting; prepared findings and validation proposals for the approved priorities.

C4: Recommendations preserve other sessions' work and require distinct authorization for delivery scope and history rewrites. No live delivery or stacked-PR behavior was tested; findings establish instruction gaps, not reproduced incidents or measured benefits.

C5: Proposed critique presented in chat; report content and persistence remain unapproved. Only this contract was written. Repository status and worktree inventory inspected; origin/main refreshed successfully after a sandbox permission failure and authorized retry. git diff --check passed for tracked changes (the new untracked contract is not covered by that command); contract content was inspected separately. No skill files changed and no delivery operations executed.
