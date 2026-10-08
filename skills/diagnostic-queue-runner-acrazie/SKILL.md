---
name: diagnostic-queue-runner-acrazie
description: >-
  Ingest, partition, and systematically resolve mass compiler and linter diagnostic queues
  through bottom-up topological module ordering, isolated worker guardrails, and closed
  adversarial verification. Use when resolving hundreds or thousands of static analysis,
  type-checker, or compiler errors across large refactors, framework migrations, or cross-language ports.
  Not for single-line debugging or running uncoordinated workspace builds.
---

# Diagnostic Queue Runner / Acrazie

Crush massive compiler, type-checker, and linter diagnostic backlogs through structured
batching, topological dependency ordering, and zero-tolerance adversarial verification.

## Subagent model selection

Apply this gate only when the workflow calls for an authorized subagent; loading a
skill in the current context is not a spawn. A planner carries the gate into its
generated workflow without executing it.

1. Verify available models and explicit model-selection support in the current
   runtime/account, using exposed tools/configuration and current official
   documentation when needed. Do not infer availability from a provider's catalog.
2. Propose 2–3 verified options in the user's language, with exactly one recommended option
   justified by the lot's work, complexity, risk, and required capabilities. Compare
   cost, capacity, and latency only where supported by evidence; disclose unknowns.
   Prefer an economical model when sufficient; never apply a fixed two-tier downgrade
   or equate generation, price, and capability. If fewer options are verified, show only those.
   If no selectable option can be verified, ask rather than inventing a recommendation.
3. Wait for explicit user validation before spawning. A homogeneous lot comprises
   agents with the same role, bounded mission/scope, risk level, and selected model.
   State that boundary and the proposed agent count. Validation covers that lot,
   including already-scoped retries, not unrelated later work. Request new validation
   if the role, mission/scope, risk level, or model changes.
4. If the chosen model is unavailable or model selection is unsupported or unverifiable, stop and ask
   whether to use a verified alternative, explicitly accept inheritance, or use a
   permitted non-spawn path. Never silently inherit, substitute, or claim an override.
5. Model validation does not authorize delegation or waive contracts, permissions,
   tests, worker limits, or fresh-context reviewer isolation. Pass only the approved
   model through the runtime's supported mechanism; preserve required context isolation.
   Record the lot, options/recommendation, user choice, and actual model if the runtime reports it
   in the existing task/workflow evidence. If actual model identity is not reported,
   record it as unverified rather than claiming the requested model ran.
   If the runtime reports a different model, stop the lot and ask before further delegation.

## Core principles & worker guardrails

1. **Ingest-Once Partitioning (Anti-Thrashing Invariant)**:
   Extract compiler diagnostics **once** into an isolated backlog (`diagnostics.json` or
   `errors.txt`). Do NOT run slow root builds (`cargo build`, `mvn compile`, `tsc --build`)
   inside the inner loop of worker agents. Recompilation occurs only between major topological tiers.
2. **Strict Worker Isolation Guardrails**:
   Worker agents are strictly forbidden from executing destructive or global Git operations:
   - **Banned Commands**: `git stash`, `git stash pop`, `git reset`, `git checkout .`, `git clean`.
   - All commits must be scoped to specific, verified files or modules.
3. **Bottom-Up Topological Ordering**:
   Resolve errors in dependency order: leaves (primitive types, core utilities, domain models)
   must compile cleanly before attempting downstream consumers (runtimes, HTTP servers, CLI commands).
   Circular dependencies must be decoupled before tackling standard compiler errors.
4. **Adversarial Gate on Every Fix**:
   Every diagnostic resolution must be vetted by `$adversarial-reviewer-acrazie`. Stubs
   (`todo!()`, empty mock returns, swallowed errors) and explanatory excuse comments are
   instantly rejected.

## Execution workflow

Follow [references/queue-guardrails.md](./references/queue-guardrails.md) across all phases:

### Phase 1: Diagnostic ingestion & normalization
Extract and persist diagnostics from the project's build tool:
- **Structured JSON/SARIF**: Run compiler or linter with machine-readable output:
  - TypeScript: `tsc --noEmit`
  - Rust: `cargo check --message-format=json`
  - Python: `pyright --outputjson` or `mypy`
  - Go: `golangci-lint run --out-format json`
  - Linter: `eslint -f json`
- **Universal POSIX Fallback**: Parse standard compiler output matching:
  `^([^:]+):([0-9]+):([0-9]+):\s*(error|warning|info):\s*(.+)$`
- Partition the resulting diagnostic list by target module / package / crate.

### Phase 2: Dependency topology & cycle detection
1. Parse project manifests (`package.json`, `Cargo.toml`, `go.mod`, `pom.xml`, or directory tree).
2. Construct the dependency Directed Acyclic Graph (DAG).
3. If circular dependencies exist between compilation units:
   - Halt normal error fixing.
   - Open a targeted cycle-breaking task (extract shared types to a lower leaf module or invert interfaces).
4. Order compilation units from deepest dependency (leaf) to top-level entry point.

### Phase 3: Batched queue dispatch
Approve separate worker and reviewer lots through the subagent model-selection gate
before dispatch. Group only comparable work within the declared scope and risk;
one worker-model approval never covers the independent reviewer role.

For each compilation unit in topological order:
1. Dispatch errors for that unit to a worker agent.
2. The worker inspects the diagnostic, fixes the root type/interface mismatch, and stages only the touched file.
3. Submit the diff to `$adversarial-reviewer-acrazie`.
4. If approved, commit atomically with Conventional Commits (`fix(<module>): resolve diagnostic <id>`).
5. Once a tier is clear, re-run the targeted module compiler to verify error reduction before moving up the DAG.

## Deliverable format

Deliver a live diagnostic queue burn-down summary:

```markdown
# Diagnostic Queue Burn-Down Report

**Diagnostic Tool**: <e.g. tsc, cargo check, pyright, golangci-lint>
**Total Diagnostics Ingested**: <Initial error count>
**Active Phase**: Ingestion | Cycle Breaking | Topological Tier Processing | Final Verification

## Topological Tier Progress
- [x] Tier 0 (Core Primitives / Types): 0 errors remaining (was 420)
- [ ] Tier 1 (Domain Models & Storage): 45 errors remaining (was 1,200)
- [ ] Tier 2 (Application Runtime & Services): Pending
- [ ] Tier 3 (CLI & Entry Points): Pending

## Guardrail Compliance
- Destructive Git operations: ZERO (clean)
- Stub rejections by Adversarial Reviewer: <count of rejected shortcuts>

## Next Tier Target
<Target module and next error batch to assign>
```
