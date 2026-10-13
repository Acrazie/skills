# Bounded planning patterns

## Decision signals

| Signal | Planning consequence |
|---|---|
| Small context, dependent files, expensive coordination | Prefer single sequential |
| Independent writes with shared stable interfaces | Consider fan-out/fan-in |
| Ordered work benefiting from context/role isolation | Consider verified pipeline |
| Unclear ownership, unknown capacity or unverifiable output | Resolve or disclose blocker before runnable schedule |

These are arbitration inputs, not automatic verdicts. Compare coordination,
integration and verification cost against the actual benefit. More agents do not
imply lower latency or token cost.

## Single sequential

One bounded agent owns the task, with explicit scope and final checks. The worker
contract still applies. Do not force model-lot selection for a non-spawn path.

## Fan-out/fan-in

1. One designated owner establishes shared interfaces/specification and freezes a
   revision, if needed. No specification writes are authorized merely by planning.
2. Independent workers operate on non-overlapping write sets with accessible inputs
   and appropriate isolated worktrees. Shared generated files and lockfiles have
   one owner or a serialized stage.
3. An integration owner verifies actual slice artifacts and their identity, combines
   them in an agreed order, then checks the final snapshot against shared criteria.

Bound concurrent workers by verified host capacity, approved count and the
agreed resource budget, not a universal five-worker ceiling. More slices may use later bounded waves only within approved scope
and lots; do not evade limits through cascade spawning.

## Verified pipeline

Stage outputs have explicit acceptance criteria and immutable/verifiable handles.
Verify an output before its dependent stage starts. Role isolation may help even
without parallelism, but must justify extra coordination. Do not relabel a
non-parallel host as proven parallel execution.

## Common contract

Goal, included/excluded paths, accessible inputs/spec revision, write ownership,
isolation and integration owner, bounded steps, exact expected checks, return
handles, unexecuted checks, limits and stop conditions. No secrets, cascade,
unrelated edits or implicit publication permission. Minimal context must still
include every invariant needed for correct work; do not force full history or
remove essential context to meet an arbitrary page budget.

Use the approved bounded retry budget per slice. Renaming the worker does not reset that budget.
Unknown retry budgets remain pending. Stop on exhaustion, repeated failure without a new
causal hypothesis, missing authority or unsafe scope expansion; a remaining budget is not permission to repeat blindly.
Unverified results and collisions pause affected work; final integrated tests are
required when the accepted contract calls for them. URLs and summaries alone do
not prove correctness or permission to inspect external artifacts.
