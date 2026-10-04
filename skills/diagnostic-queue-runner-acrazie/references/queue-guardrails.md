# Diagnostic Queue & Worker Guardrails Reference

This reference provides technical specifications, ingestion command recipes, and concurrency
guardrails for `diagnostic-queue-runner-acrazie`.

---

## 1. Universal Diagnostic Ingestion Recipes

Extract diagnostics into a machine-readable format before dispatching worker tasks.

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

### Universal POSIX Fallback Parser
When JSON is not available, standard compiler output follows the universal line structure:
```regex
^([a-zA-Z0-9_\-\./\\]+):([0-9]+):([0-9]+):\s*(error|warning|fatal error|note):\s*(.+)$
```
- Group 1: File path
- Group 2: Line number
- Group 3: Column number
- Group 4: Diagnostic severity
- Group 5: Detailed diagnostic message and compiler code (e.g. `[E0308]`, `TS2322`)

---

## 2. Topological Dependency Ordering & Cycle Breaking

Handling compiler errors in random order leads to cascade re-evaluations. Always process bottom-up.

### Tier Structure (The Dependency DAG)
1. **Tier 0 — Foundation & Primitives**: Basic data types, serialization helpers, string/buffer utilities,
   low-level constants, system error enums. Zero external project dependencies.
2. **Tier 1 — Domain Models & State**: Entities, data structures, storage interfaces, core protocols.
3. **Tier 2 — Services & Runtime**: Network engines, parsers, business logic, asynchronous task queues.
4. **Tier 3 — Presentation & CLI**: Subcommands, HTTP handlers, user interfaces, top-level integration.

### Cycle Breaking Protocol
If two packages depend on each other (Package A ↔ Package B):
1. **Never attempt to fix type errors across a cycle simultaneously.**
2. Identify the shared interface or type causing the mutual dependency.
3. **Cycle Inversion Strategy**:
   - Extract the shared type definition into a new or existing Tier 0 leaf module.
   - Refactor both Package A and Package B to import the extracted leaf type.
   - Re-export or alias if public API backwards compatibility is required.
4. Only once the cycle is broken should normal diagnostic queue processing resume.

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

### Permitted Operations
- ✅ Targeted file editing (`replace_file_content`, scoped file writes).
- ✅ Explicit file staging (`git add path/to/file.ext`).
- ✅ Scoped single-file syntax check (e.g. `rustc --emit=metadata <file>`, `tsc path/to/file.ts --noEmit`).
- ✅ Targeted atomic commit (`git commit -m "fix(module): message"`).

---

## 4. Closed Adversarial Loop Integration

Every diagnostic resolution must pass through `$adversarial-reviewer-acrazie` before being finalized.

### Common AI "Fix" Anti-Patterns to Intercept
1. **The Stub Escape**: Resolving an un-implemented interface by writing empty function bodies or returning dummy values.
   - *Example*: Returning `Ok(())` or `null` just to make the return type match.
   - *Adversarial Action*: Automatic `REJECT`.
2. **The Excuse Comment**: Documenting why an incomplete fix is acceptable with a lengthy comment.
   - *Adversarial Action*: Automatic `REJECT` (*"Fix the code, do not justify the workaround"*).
3. **The Unsafe Bypass**: Wrapping stubborn type errors in `unsafe`, `as any`, or `@ts-ignore` without contract authorization.
   - *Adversarial Action*: Automatic `REJECT`.
