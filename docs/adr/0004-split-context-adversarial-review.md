# Split-Context Adversarial Code Review with Strict Implementer-Reviewer Partitioning

We establish the `adversarial-reviewer-acrazie` specialist as an independent, split-context evaluation role for proposed code changes. The reviewer inspects changes under the strict axiom that the code is incorrect, seeking resource hazards, concurrency flaws, and semantic drift while explicitly rejecting stub workarounds.

## Context & Problem

LLM-authored code frequently exhibits confirmation bias: the agent that authored an implementation is psychologically and statistically primed to view its own solution as complete and correct. In complex systems programming and mission-critical codebases (exemplified by the 2026 Bun Zig-to-Rust migration), the most damaging bugs compile cleanly and appear plausible at first glance: asynchronous cleanup double-frees (`uv_close`), incorrect arithmetic rounding on negative inputs (`trunc` vs `floor`), eager evaluation panics in fallback helpers (`unwrap_or`), and release-erased assertions (`debug_assert!`).

When agents encounter compiler errors or subtle behavioral gaps, they frequently resort to anti-patterns:
1. Inserting silent stubs (`todo!()`, `unimplemented!()`, dummy mock returns).
2. Writing explanatory comments rationalizing why an incomplete workaround is acceptable.

## Decision

1. **Split-Context Cognitive Isolation**: The adversarial reviewer operates in an isolated context window. It receives only the code diff and authoritative specification contracts (e.g. `Task Contract`, `PORTING.md`, or type signatures). It is strictly forbidden from receiving the implementer's narrative reasoning, conversational justifications, or internal chain-of-thought.
2. **Strict No-Fix Separation ("The implementer doesn't review; the reviewer doesn't implement")**: When the reviewer finds a defect, it outputs a binary verdict (`REJECT`) accompanied by a concrete **Proof of Flaw** (reproducible edge case input, concurrent race scenario, or lifecycle trace). It does not provide replacement code or patch suggestions, preserving its uncompromising falsification posture.
3. **Zero-Tolerance Anti-Workaround Invariants**: Any detected dummy stub, omitted error handling branch, or paragraph-long comment rationalizing a workaround triggers an immediate, non-negotiable rejection.
4. **Dual Invocation Model**: The skill is invocable directly by human developers (`/adversarial-reviewer`) on any git diff or branch, and programmatically as a sub-agent by orchestrators (`multi-agent-planner-acrazie`, `feature-builder-acrazie`) in closed multi-agent verification loops.

## Consequences & Trade-offs

- **Cost of Additional Passes**: Verification requires separate model context windows and an explicit hand-off back to the implementer or a fixer agent. We accept this latency and token overhead to eliminate silent defects before merge.
- **Rejected Alternatives**:
  - *Self-Review by the Implementer*: Rejected because implementers consistently hallucinate compliance with their own unstated assumptions.
  - *Reviewer with Fix Generation*: Rejected because producing replacement code shifts the reviewer into a constructive compromises mindset, creating new blind spots.
  - *Embedding into Feature Builder*: Rejected to preserve modularity; adversarial review must be universally applicable across features, bug fixes, refactorings, and codebase migrations.
