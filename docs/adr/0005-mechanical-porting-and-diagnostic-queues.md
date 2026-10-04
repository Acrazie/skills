# Language-Agnostic Mechanical Porting with Test Oracles and Topological Diagnostic Queues

We establish `mechanical-port-acrazie` and `diagnostic-queue-runner-acrazie` as complementary, language-agnostic capabilities for large-scale codebase rewrites and mass compiler/linter error resolution.

## Context & Problem

Porting complex codebases between languages or across major runtime paradigms (e.g. Python to Go, Java to Rust, JavaScript to strict TypeScript, C++ to Swift) has historically been considered an engineering anti-pattern due to schedule freezes and behavioral divergence. While LLMs enable massive generation throughput, unconstrained agent porting suffers from four critical failure modes:
1. **Premature Idiomatic Divergence**: Attempting to redesign architecture or invent new abstractions mid-flight creates unreviewable diffs and breaks mental models for existing maintainers.
2. **Ungated Functional Drift**: Rewriting without an independent, language-agnostic behavioral test suite guarantees silent regressions and hallucinated semantics.
3. **Compiler Error Paralysis**: Multi-thousand compiler or linter errors overwhelm single agents or cause iterative thrashing where fixing one error introduces three others.
4. **Agent Concurrency Collisions**: Parallel agents running global workspace builds (`cargo check`, `tsc`, `go build`) or shared git operations (`git stash`, `git reset`) step on each other, corrupting working trees and exhausting I/O.

## Decision

1. **Mandatory Test Oracle Invariant**: Mechanical porting requires a pre-existing or retrofitted black-box test suite (via `test-retrofitter-acrazie`) that runs independently of the target compiler. Translating code without an objective oracle is strictly prohibited.
2. **Faithful 1:1 Structural Mirroring**: The initial port must mechanically mirror the source codebase's file hierarchy, module boundaries, and data structures. Architectural simplification and idiomatization are deferred until the ported suite passes 100% of tests.
3. **Universal 4-Phase Porting Gating**:
   - *Phase 1 — Paradigm Mapping (`PARADIGM-MAPPING.md`)*: Exhaustive cross-language translation table covering memory/resource lifecycle, error models, concurrency, and type systems/nullability.
   - *Phase 2 — Ownership & Resource Matrix (`OWNERSHIP-MATRIX.tsv`)*: Pre-translation inventory of resource allocations, ownership semantics, and cleanup triggers.
   - *Phase 3 — Canary Trial Run*: Mechanical translation of 3–5 representative files evaluated by `adversarial-reviewer-acrazie`.
   - *Phase 4 — Transpilation & Queue Handoff*: Full file-by-file translation followed by delegation of diagnostics to `diagnostic-queue-runner-acrazie`.
4. **Decoupled Universal Diagnostic Queue**: `diagnostic-queue-runner-acrazie` operates independently of language choice. It ingests diagnostics via JSON/SARIF or universal POSIX regex, orders work bottom-up through a topological module DAG (cycles resolved first), and enforces strict worker guardrails (no global builds in inner loops, no destructive git commands).
5. **Closed Adversarial Inner Loop**: Every translated file and diagnostic fix must pass `adversarial-reviewer-acrazie` before atomic commit.

## Consequences & Trade-offs

- **Strict Gating Overhead**: Projects without automated test suites cannot proceed with all-at-once mechanical porting until tests are retrofitted. We accept this constraint because unverified mass migration is non-viable.
- **Temporary Non-Idiomatic Idioms**: Ported code initially mirrors source patterns (e.g. manual pointer manipulations or flat loops) rather than idiomatic target paradigms. This trade-off drastically simplifies verification, allowing idiomatic refactoring to occur safely post-port.
- **Broad Ecosystem Reusability**: By decoupling the diagnostic queue crusher from the porting orchestrator, `diagnostic-queue-runner-acrazie` is universally applicable to monorepo type-checking migrations, strict linter rollouts, and compiler edition upgrades.
