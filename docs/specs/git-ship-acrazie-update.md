# Git Ship Update

## Objective
Implement the six recommendations in the [validated critique](../critics/git-ship-acrazie.md) for concurrent delivery and the complete stacked-PR lifecycle in personal and third-party repositories.

## Scope
Update git-ship-acrazie instructions, references, invocation metadata as needed, and focused evaluation/test coverage in the existing isolated worktree. Preserve unrelated documents and work. No actual delivery/stack operations, dependencies, commits, pushes, PR creation, merge, or deployment. Preserve hook enforcement, third-party work, and separately authorized remote history rewrites.

## Success criteria and evidence
- C1: Specify repository-adaptive policy and action-specific approval, including commit-only delivery and safe absence/inaccessibility handling; source-contract tests and scenarios.
- C2: Specify fresh local/remote checks at mutation boundaries and exact approved/validated snapshot handling, including hooks and concurrent edits; tests and scenarios.
- C3: Specify complete conditional stack creation, base updates, parent evolution/merge/closure/replacement, shared descendants, conflicts, and restart-safe reorganization; tests and scenarios.
- C4: Specify verified delivery outcomes and state-aware recovery without duplicates; tests and scenarios.
- C5: Specify content-aware secret checks without disclosure or absolute guarantees; tests and scenarios.
- C6: Consolidate authoritative rules, preserve invocation policy, validate structure and links, and distinguish static checks from simulated or live behavior.

## Decisions and approval
Status: approved
On 2026-10-09 the user requested implementation, then replied "ok" to the explicit proposed implementation contract and change to skill-creator ownership. The accepted proposal covered all six recommendations, this exact destination, the existing isolated worktree, bounded checks, no delivery operations, and an independent review offer requiring a later choice. The critique contract remains a separate historical assessment, not implementation authority.

Use native Git and existing GitHub CLI capabilities; no new stack tool dependency. Retain simple delivery as the default; stacks are conditional on actual dependencies. No automatic merge or destructive recovery.

## Delivery evidence
Implementation applied in the approved worktree; no shipping actions executed.

- C1: Repository-adaptive discovery, actual protected/default branch, action-specific authorization and commit-only exit specified; covered by static tests and policy/scope prompts.
- C2: Boundary freshness, exact index/candidate-tree proof, third-party ownership, changed rules and hook-result verification specified; static tests and freshness/snapshot prompts.
- C3: Conditional native stack protocol specifies immutable old parent boundaries, per-node validation, creation/base updates, squash/rebase/normal merge distinctions, closure/replacement, shared history, explicit leases and interruption recovery; static tests and stack prompts.
- C4: Immutable-SHA push, endpoint/PR verification, existing-PR lookup and state-aware partial recovery specified; static tests and recovery prompts.
- C5: Content-aware secret controls, redaction, example assessment and disclosed limits specified; static tests and secret prompt.
- C6: Main workflow delegates detailed rules to four references; invocation remains model-invocable and task-scoped. No new dependencies.

Proof: the 10 static contract tests initially failed for missing behavior (7 assertion failures, 2 missing stacking-reference errors, 1 pass), then passed 10/10 after changes. Existing validate-skills.sh and check-skill-structure.sh passed. git diff --check passed for tracked changes; new task files were checked separately. Static tests also validate local Markdown links, invocation flags, JSON scenario IDs/content and required category coverage. Ten behavioral prompts are recorded; only IDs 4, 6, 7 were simulated against updated and old instructions (six answers total). Updated answers explicitly covered 10/10 selected assertions; baseline answers lacked those specified safeguards. This is illustrative plan coverage, not an incident reproduction or a reliability/performance benchmark. Each variant processed three scenarios in one fresh context, and baseline instructions asked it to acknowledge gaps. Timing/token metrics were unavailable; no estimates were fabricated. Remaining seven scenarios were not behaviorally run.

Ignored simulation artifacts and static viewer: skills/git-ship-acrazie-workspace/iteration-1/review.html. Native Git and GitHub CLI documentation consulted through Context7 for explicit expected-value leases, child-only --onto transplantation and explicit PR destinations/base updates. No live stack, CI, deployment or target-repository safety verification was performed.

Skill source snapshot SHA-256: `11a5591aefdf5018b158c4897d7e7dbdd27ea623c84ae0741b3b35a40e353adc` over the eight sorted relative source paths, each encoded as path, NUL, file bytes, NUL. The implementation contract and prior critique documents are excluded from this source digest.

Independent review choice: accepted on 2026-10-09. The user replied "ok go" to the explicit independent-review offer; a fresh read-only adversarial reviewer is authorized. Review status: ACCEPT on the final skill source snapshot. Recommend an independent adversarial review because published-history rewrites, concurrent state and permissions cross trust boundaries; cost is one additional review pass and possible scoped corrections. A fresh adversarial reviewer examined the frozen complete eight-file source diff against C1-C6 and the four rubric pillars. Verdict: ACCEPT; zero demonstrated introduced defects. Full report: skills/git-ship-acrazie-workspace/review-1/report.md; frozen patch and manifest alongside it. Source digest remained unchanged after review. ACCEPT applies only to that snapshot and does not prove absence of bugs or live safety. Evaluation agents only generated simulations and did not perform the independent review. Human feedback on the simulation viewer is also pending. Implementation criteria and the accepted independent-review gate are satisfied for this instruction update. Human evaluation-viewer feedback remains optional and pending; no live delivery or publication is claimed.
