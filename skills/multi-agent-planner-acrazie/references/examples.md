# Conditional worked examples

These illustrate decisions, not observed runtime results or universal verdicts.
Each execution still needs applicable task, model, capability and action approvals.

## Shared testing conventions across repositories

Start with one agent to inspect the authorized boundaries. If repositories have
independent write sets, stable agreed interfaces and verified worker capacity,
fan-out/fan-in may help. Otherwise use a sequential plan; repository count alone
does not justify delegation.

Proposed phases: establish a concise shared testing specification at an approved
path; freeze its revision; assign bounded repository slices in isolated worktrees;
verify each diff and agreed test output; check cross-repository conformance.
No dependency upgrades or CI changes unless the approved task includes them.
Each worker returns revision, changed paths, exact executed checks/results and
unexecuted checks. The integration owner verifies artifacts rather than trusting
summaries. Unknown model choices remain pending, not inherited silently.

## Large codebase debugging

Start sequentially: authorized reconnaissance identifies symptoms and shared
causes. Reproduction execution needs its own applicable permission. Only genuinely
independent leads with non-overlapping writes may justify fan-out afterward.

Worker contracts state the approved lead, allowed paths, input evidence, forbidden
adjacent refactors and expected causal/regression proof. A shared root cause or
write overlap stops the affected slices for repartitioning. Verify each returned
artifact, then check the integrated final snapshot against the reproduction and
required adjacent tests. One bounded retry per slice; no automatic merge or ship.
