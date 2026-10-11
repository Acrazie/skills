# Diagnostic Queue & Worker Guardrails Reference

This reference provides technical specifications, ingestion command recipes, and concurrency
guardrails for `diagnostic-queue-runner-acrazie`.

---

## Contract and permissions

Follow the entry skill's current approved agreement, four-field decision format,
project loading boundary and worker/reviewer model gates. Each dependency and each
new review snapshot needs its own explicit activation in an explicit kit; returning
to the implementer also needs activation. An absent mandatory reviewer blocks
acceptance, not unrelated discovery. Do not copy or silently install substitutes.

Execution and writes require scoped permission: approve backlog/report destinations,
protect existing files and redact sensitive output. Installation, lockfile changes,
network, destructive fixtures and spawning remain separate. Reports default to chat.
No implicit staging, commit, push, PR, merge or deployment.

## 1. Illustrative Diagnostic Ingestion Recipes

Ingest once per approved snapshot/checkpoint, then refresh after affected changes
and between tiers. Record snapshot, environment, installed tool/version, command,
configuration, exit status and raw output. Never dispatch stale diagnostics or treat
failed tools as an empty queue. Commands below are historical illustrations, not
certified CLI recipes. Verify current options and project-supported checks before
use; `npx` may install/download and is not authorized by this table. Preserve both
stdout and stderr and distinguish expected diagnostic exits from tool failures.

### Ecosystem Commands
| Environment | Tool | Recommended Ingestion Command | Output Format |
| :--- | :--- | :--- | :--- |
| **TypeScript / JS** | `tsc` | `npx tsc --noEmit --pretty false > diagnostics.txt` | POSIX text |
| **Rust** | `cargo` | `cargo check --message-format=json > diagnostics.json` | JSON stream |
| **Python** | `pyright` | `npx pyright --outputjson > diagnostics.json` | JSON array |
| **Python** | `mypy` | `mypy . --show-column-numbers --no-error-summary > diagnostics.txt` | POSIX text |
| **Go** | `golangci-lint` | `golangci-lint run --out-format json > diagnostics.json` | JSON object |
| **Go** | `go build` | `go build ./... 2> diagnostics.txt` | POSIX text |
| **C / C++** | `clang` | `cmake --build build 2> diagnostics.txt` | POSIX text |
| **Linter (JS/TS)** | `eslint` | `npx eslint . -f json > diagnostics.json` | JSON array |

### Tool-Specific Text Fallback
When machine-readable output is unavailable, a limited illustrative pattern is:
```regex
^([a-zA-Z0-9_\-\./\\]+):([0-9]+):([0-9]+):\s*(error|warning|fatal error|note):\s*(.+)$
```
- Group 1: File path
- Group 2: Line number
- Group 3: Column number
- Group 4: Diagnostic severity
- Group 5: Detailed diagnostic message and compiler code (e.g. `[E0308]`, `TS2322`)

This pattern is not universal: it misses paths with spaces, drive-letter and other
formats, omitted columns and multiline diagnostics. Preserve raw and unmatched
output, measure parse coverage, adapt to verified tool/version formats, and block
assignments dependent on unrecognized data. Do not silently discard records.

---

## 2. Topological Dependency Ordering & Cycle Breaking

Handling compiler errors in random order leads to cascade re-evaluations. Always process bottom-up.

### Tier Structure (The Dependency DAG)
1. **Tier 0 — Foundation & Primitives**: Basic data types, serialization helpers, string/buffer utilities,
   low-level constants, system error enums. Zero external project dependencies.
2. **Tier 1 — Domain Models & State**: Entities, data structures, storage interfaces, core protocols.
3. **Tier 2 — Services & Runtime**: Network engines, parsers, business logic, asynchronous task queues.
4. **Tier 3 — Presentation & CLI**: Subcommands, HTTP handlers, user interfaces, top-level integration.

### Blocking Cycle Protocol

Trace real imports and build configuration; manifests or directory trees alone
are not a complete graph. Find strongly connected components instead of assuming
the whole graph is a DAG. A legal toolchain cycle is not automatically a defect.
If a cycle prevents safe ordering, block that component and propose a separately
approved cycle-breaking task. Type extraction or interface inversion is not
implicitly authorized, especially under a 1:1 mechanical port. Independent
unaffected components may proceed under existing checks and approval.

---

## 3. Strict Concurrency & Git Guardrails

In parallel agent environments, the most common source of corrupted states is agents using global Git commands.

### Prohibited Operations
- ❌ `git stash` / `git stash pop`: Stashes affect the entire working tree. When Agent A stashes,
  it wipes out uncommitted work being drafted by Agent B.
- ❌ `git reset HEAD --hard`: Destroys all parallel in-flight edits across the entire workspace.
- ❌ `git checkout .`: Reverts all files globally, not just the file assigned to the worker.
- ❌ Running whole-project builds inside the worker loop: In large codebases, running `cargo check`
  or `mvn compile` inside a loop for every single file burns I/O and freezes disk read/writes.

### Scoped Work and Checkpoints

- Edit only assigned paths under approved realization; avoid overlapping writers.
- Run approved scoped checks using project configuration; guessed single-file
  compiler invocations do not prove module correctness.
- Coordinator runs approved tier/checkpoint and final project validations.
- Scoped editing never authorizes `git add` or `git commit`. Separately authorized
  delivery follows repository action policy and exact-snapshot proof.
- Reconcile resolved, remaining, new, blocked and not revalidated diagnostics.
  A count drop with changed rules/configuration is not proof of correction.

---

## 4. Closed Adversarial Loop Integration

Every diagnostic resolution must pass through `$adversarial-reviewer-acrazie` before being finalized.

### Evidence-Based Rejection and Acceptance

Give the activated reviewer base, exact candidate snapshot, authoritative contract,
scoped diff and relevant read-only context in a fresh context without inherited
author conversation, or a separate manual reviewer context. Require `ACCEPT`
covering every fix, including every fix in a coherent batch. `REJECT`, `INCOMPLETE`
or unavailable isolation blocks acceptance. Later corrections invalidate affected
review and require fresh checks/review; implementer self-review is not a substitute.

Reject demonstrated introduced incomplete stubs, swallowed errors and unauthorized
bypasses that violate requirements. Empty results, test doubles, comments and
low-level operations alone are not proof of a defect; review needs a concrete
failure scenario. Review reduces risk, never establishes zero defects.

Before closure, run required final project and behavioral regression checks on the
final snapshot. Parser gaps, stale diagnostics, disabled rules, failed/unavailable
checks or pending review block dependent completion. Report actual counts,
commands, snapshots, verdicts and guardrail evidence, not assumed clean compliance.
