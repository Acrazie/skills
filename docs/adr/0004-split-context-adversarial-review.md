# Split-Context Adversarial Code Review with Strict Implementer-Reviewer Partitioning

We establish the `adversarial-reviewer-acrazie` specialist as an independent, split-context evaluation role for proposed code changes. The reviewer inspects changes under the strict axiom that the code is incorrect, seeking resource hazards, concurrency flaws, and semantic drift while explicitly rejecting stub workarounds.

## Context & Problem

LLM-authored code frequently exhibits confirmation bias: the agent that authored an implementation is psychologically and statistically primed to view its own solution as complete and correct. Across all programming languages and runtimes (from backend microservices in Python or Go to web stacks in TypeScript and systems software in Rust or C++), the most damaging bugs compile cleanly and appear plausible at first glance: asynchronous cleanup double-frees or goroutine leaks, unclosed database or network handles, unhandled exception paths, race conditions across async boundaries, eager evaluation panics in fallback helpers, and assertions erased in production/optimized builds.

When agents encounter compiler errors, linter warnings, or subtle behavioral gaps, they frequently resort to anti-patterns:
1. Inserting silent stubs (`todo!()`, `unimplemented!()`, `pass`, `return null;`, `return nil`, empty mock returns).
2. Writing explanatory comments rationalizing why an incomplete workaround is acceptable.

## Decision

1. **Split-Context Cognitive Isolation**: The adversarial reviewer operates in a fresh context without inherited author history. It receives a fixed task diff, authoritative specification contracts, and read-only technical context needed to trace affected behavior. It does not receive the implementer's narrative reasoning or conversational justifications.
2. **Strict No-Fix Separation ("The implementer doesn't review; the reviewer doesn't implement")**: When the reviewer finds a defect, it outputs a binary verdict (`REJECT`) accompanied by a concrete **Proof of Flaw** (reproducible edge case input, concurrent race scenario, or lifecycle trace). It does not provide replacement code or patch suggestions, preserving its uncompromising falsification posture.
3. **Evidence-Based Rejection**: Demonstrated introduced bugs, regressions, contract violations, and incomplete workarounds trigger `REJECT`. Syntax alone, authorized empty results, or pre-existing findings do not. Missing evidence leaves review incomplete; `ACCEPT` is scoped to the reviewed snapshot, not a guarantee of no bugs.
4. **Dual Invocation Model**: Humans or other skills may invoke the reviewer. `feature-builder-acrazie` always offers review after implementation and tests with a task-specific run/skip recommendation; it delegates only after explicit user acceptance. This is a bounded specialist handoff, not a general development orchestrator. Accepted review gates completion, with at most two correction/re-review cycles before user arbitration. See [the approved integration contract](../specs/feature-adversarial-review.md).

## Consequences & Trade-offs

- **Cost of Additional Passes**: Verification requires separate context windows and a handoff back to the implementer. Users choose whether the additional latency and token cost are justified; review reduces risk but cannot eliminate all defects. Unavailable independent review blocks an accepted gate unless explicitly withdrawn.
- **Rejected Alternatives**:
  - *Self-Review by the Implementer*: Rejected because implementers consistently hallucinate compliance with their own unstated assumptions.
  - *Reviewer with Fix Generation*: Rejected because producing replacement code shifts the reviewer into a constructive compromises mindset, creating new blind spots.
  - *Embedding into Feature Builder*: Rejected to preserve modularity; adversarial review must be universally applicable across features, bug fixes, refactorings, and codebase migrations.
