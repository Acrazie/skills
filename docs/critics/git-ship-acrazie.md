# Git Ship Critique

## Scope and status
- Repository: Acrazie Skills.
- Assessed revision: `38472cbc447eaf5a315a639da0b969da0f9c85e2`, refreshed from `origin/main` on 2026-10-09.
- Assessment worktree: `.worktrees/codex/git-ship-critique`; no skill changes. The only local additions are this report and its approved contract.
- Approved Task Contract: [Git Ship Critique](../specs/git-ship-acrazie-critique.md).
- Selected priorities: concurrent local/remote changes, exact delivery snapshots, complete stacked-PR lifecycle, adaptive repository policy, action authorization, partial-failure recovery, and delivery verification.
- Excluded: implementation, actual delivery/stack operations, merges, history rewrites, GitHub administration, deployment, and mutating behavioral evaluations.
- Report status: validated.
- Approval evidence: on 2026-10-09, the user replied "ok" to the proposed critique and the explicit request to save its English report at `docs/critics/git-ship-acrazie.md` in the same isolated worktree. This approves report content and persistence, not implementation or acceptance of every recommended option as an implementation decision.

## Product panorama

The skill prepares a completed task for delivery through governance discovery, preflight checks, a consolidated approval recap, targeted staging, commit, push, and Draft PR creation.

The user declares use in both personal and third-party repositories, sometimes with concurrent branches and changing configurations. They suspect insufficient repeated verification and request assessment of complete stacked-PR management, not detection alone. These are declared needs; no incident was reproduced and no usage analytics were collected.

Observed implementation is an instruction-driven linear workflow, distributed across the main skill and three references. Its approval boundary and hygiene controls have value, but concurrent-state invariants and stack lifecycle behavior are not specified. Existing evaluation prompts cover normal preparation, refusal on main, and missing governance; they do not establish live execution reliability.

## Verdict and elements to retain

Retain the delivery specialist. Extend its safety model around exact approved state and verified outcomes before treating it as suitable for concurrent work. Add a conditional stack path only when real dependencies justify its cost. Do not replace the workflow or introduce a dependency without further evidence.

Retain explicit delivery approval, targeted staging, hook enforcement, branch protection, non-autonomous force-push behavior, and PR-template compliance. Simplify duplicated rules whose divergence increases maintenance cost.

## Priority 1: Approval and validation can become stale
- User job: deliver the approved task while other work continues locally or remotely.
- Evidence: `skills/git-ship-acrazie/SKILL.md`, Step 2 performs checks; Step 3 waits for approval; Step 4 stages and delivers without requiring a renewed state check. Claim: observed instruction gap, high confidence; not a demonstrated execution failure.
- Impact: branch, index, file content, governance, or destination may change after preparation. An earlier successful check does not prove the later action still satisfies its assumptions.
- Options: retaining the linear flow is simpler for stable single-user work but does not address the declared concurrency need. Repeating every check before every command is burdensome and still does not guarantee atomicity. Prefer invariant-specific checks at mutation boundaries.
- Recommendation: bind approval to precise content and destinations; recheck relevant state before mutation, rerun affected validations after changes, and request renewed approval for material scope or risk changes. Preserve unrelated work; no automatic stash/reset to obtain a clean state.
- Verification proposal: change content, branch, configuration, or remote state after approval. Success means the affected action stops or revalidates appropriately rather than using stale evidence. No claim of performance benefit is made.
- Accepted decision: report validated; implementation option pending.

## Priority 2: File selection is not an exact snapshot guarantee
- User job: commit only intended, validated content.
- Evidence: main skill Step 3 uses `git diff HEAD`; `references/pr-delivery.md`, Targeted Staging Protocol, requires only `git diff --cached --stat`. There is no explicit exact-snapshot validation or post-hook content comparison requirement. Claim: observed instruction gap, high confidence.
- Impact: previously staged third-party content, unrelated edits within a targeted file, unstaged dependencies needed by passing tests, or hook modifications can break the connection between approval, tests, and commit.
- Options: path-only staging is cheap but insufficient. Exact index review and validation adds bounded effort where the delivery invariant belongs. `skills/repo-modernizer-acrazie/references/commit-strategy.md` already describes compatible exact-snapshot and third-party-work protections.
- Recommendation: align with that existing model without invoking a modernization workflow. Inspect complete staged content, preserve foreign changes, validate the snapshot actually delivered, and compare the resulting commit with validated content.
- Verification proposal: contaminated index, mixed edits in one file, tests relying on unstaged content, and a content-changing hook. Success means no unapproved or unvalidated content is declared delivered.
- Accepted decision: report validated; implementation option pending.

## Priority 3: Complete stacked-PR management is absent
- User job: review and deliver dependent changes separately, then keep descendants correct as parents evolve.
- Evidence: the assessed main skill, three references, and evaluation prompts specify no dependency graph, explicit per-PR bases, parent lifecycle, or descendant reorganization. Claim: observed absence in the assessed scope, high confidence.
- Impact: the current workflow cannot be relied on as a specification for creation, base updates, or reorganization after parent merge.
- Options: independent PRs are preferable for independent changes. A conditional stack workflow fits dependent changes but adds history, coordination, validation, and recovery costs. A new stack tool is not justified by this assessment alone.
- Recommendation: preserve the simple delivery path. For genuine stacks, establish dependencies and per-PR content/base explicitly; cover parent updates, squash/rebase merges, closure or replacement, descendant reorganization, conflicts, shared branches, and interrupted operations. A similar diff does not establish a dependency. No implicit merge or remote history rewrite; require separate rewrite authorization and concurrent-update protection.
- Verification proposal: a dependent stack with a squash-merged parent; an updated or closed parent; shared published descendants; and interruption during reorganization. Success means intended changes are preserved, affected validations are renewed, and no unauthorized rewrite occurs.
- Accepted decision: complete lifecycle is approved assessment scope; implementation design remains pending.

## Priority 4: Remote outcomes and partial recovery are underspecified
- User job: know what was actually delivered and resume without duplicates.
- Evidence: main skill Step 4 ends with a SHA and links. `references/pr-delivery.md`, Remote Push Protocol, addresses network/authentication failure but does not define complete recovery or verification of remote SHA, PR head/base/content/state, CI, or mergeability. Claim: observed instruction gap, high confidence.
- Impact: a successful command or available URL can be mistaken for a verified delivery. Retrying a partial workflow can duplicate work or act on outdated assumptions.
- Options: retaining basic error reporting is inexpensive but leaves the declared need unresolved. Prefer outcome checks and state-aware resumption over unconditional replay.
- Recommendation: observe each step's result before continuing; recognize existing commits, branches, and PRs on resume. Distinguish verified delivery, partial delivery, pending/failed CI, and unknown mergeability. CI success is not required to be immediate, but its actual status must not be invented.
- Verification proposal: commit succeeds/push fails, push succeeds/PR creation fails, an existing PR, and a concurrent remote update. Success means no duplication, no overwrite, and an accurate partial/final report.
- Accepted decision: report validated; implementation option pending.

## Priority 5: Adaptive positioning conflicts with rigid delivery behavior
- User job: request only authorized delivery actions under each repository's conventions.
- Evidence: main skill selection includes commit-only requests, while execution bundles commit/push/PR. Core invariants mandate Conventional Commits and default Draft. Missing governance triggers initialization; `references/inspection.md` additionally provides an emergency fast-path absent from the main workflow. Claim: observed scope mismatch and instruction inconsistency, high confidence.
- Impact: third-party conventions and action-specific requests can conflict with the skill's defaults; duplicate rules make resolution ambiguous.
- Options: a rigid opinionated workflow can fit a uniform private environment but not both declared audiences. Prefer repository-adaptive execution and a minimal approved strategy when documentation is absent, without forcing repository initialization.
- Recommendation: separate authorization for commit, push, and PR; discover authoritative repository policy and resolve conflicts explicitly. Never treat absent documentation, inaccessible remote rules, and absent rules as equivalent. Consolidate duplicated instructions. `github-repo-init-acrazie` remains an optional separately requested setup workflow, not a required detour for every delivery.
- Verification proposal: commit-only request, non-Conventional repository policy, no formal workflow document, and conflicting policies. Success means only authorized actions occur under applicable rules without invented conventions.
- Accepted decision: report validated; implementation option pending.

## Priority 6: Secret protection is overstated
- User job: deliver changes without disclosing credentials.
- Evidence: main skill promises "Zero Secret Leaks"; hygiene instructions focus primarily on file-name patterns. Claim: observed mismatch between assurance and specified checks, high confidence. No leak was observed.
- Impact: name-based heuristics cannot establish absence of secrets in ordinary source files. Blanket exclusions can also block legitimate non-secret examples without assessing content.
- Options: retain filename checks as useful signals, not guarantees; supplement with review of exact delivered content and available repository controls. No new scanner dependency is established as necessary.
- Recommendation: inspect content without exposing sensitive values; report control limits and stop on unresolved sensitive content. Do not promise zero leakage from heuristics alone.
- Verification proposal: synthetic secret in an ordinary source file and a legitimate non-secret example file. Success means sensitive content is blocked without disclosure, and legitimate content is assessed rather than silently assumed safe or forbidden.
- Accepted decision: report validated; implementation option pending.

## Checks performed and evidence gaps

Inspected Git status and worktree inventory, refreshed `origin/main`, and read the refreshed skill, all three references, invocation metadata, three evaluation prompts, and relevant neighboring ownership/snapshot rules. Initial local discovery used `beb56b1`; final findings use refreshed `38472cb`, whose invocation wording differs.

The fetch initially failed under sandbox restrictions; an authorized retry succeeded. No project validation scripts, behavioral evaluations, delivery commands, stack operations, or production checks were run. No remote target repository's protections or live PRs were inspected. Recommendations are source-backed specifications and risk hypotheses, not reproduced failures, measured gains, or guarantees of agent behavior.

## Next decisions and optional handoff

The user validated this report and authorized persistence only. All implementation choices remain proposals. A later explicit implementation request requires an approved targeted contract and a suitable skill-update workflow, not Feature Builder application-feature ownership. Preserve existing work and assess final behavior with bounded scenarios. Do not merge, publish, rewrite history, or deploy under report approval.
