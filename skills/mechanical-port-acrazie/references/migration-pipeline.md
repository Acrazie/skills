# Mechanical Migration Pipeline Reference

This guide supports the entry skill contract for language-to-language mechanical codeports.
It applies across any language transition (dynamic-to-static, managed-to-systems, or OO-to-functional).

## Contract, loading and evidence

Reuse the current independently approved agreement and reopen only invalidated
choices. Before writes or commands, verify approved paths, artifact destinations,
execution effects and permissions. Preserve existing files; a fixed filename is
not overwrite approval. Follow the entry skill's four-field decision format.

In an explicit project kit, each dependency needs its own explicit user activation
before reading or dispatching its body. Each re-review of a new snapshot requires
new reviewer activation; returning to the implementer requires its activation too.
Loading and model choice do not grant realization, installation, network,
spawning, staging, commit or delivery permissions.

Every review covers the base, exact candidate snapshot and authoritative contract
in a fresh context without inherited author conversation (or separate manual
reviewer context). Require `ACCEPT` covering all affected units; `REJECT`,
`INCOMPLETE` or unavailable review blocks their acceptance. Corrections invalidate
affected proof. Do not replace this with implementer self-review or zero-defect
promises. Final target checks and the unchanged behavioral oracle remain required.

The tables below are investigation prompts, not certified runtime recipes or
universal conversion rules. Preserve observed error codes, resource behavior and
concurrency contracts; confirm language/API semantics with current documentation
and tests before applying a mapping.

---

## 1. The Test Oracle Invariant

A mechanical port replaces the entire execution engine. The only safety net between working software
and hallucinated code is an automated test suite whose execution is decoupled from the target compiler.

### Oracle Qualification Checklist
- **Black-Box Invariance**: Tests verify behavior through external APIs, CLI commands, HTTP endpoints,
  or standard library I/O interfaces, rather than inspecting internal language-specific symbols.
- **Pre-Flight Pass**: The adequate suite must pass on the source snapshot before any target
  code is written. Record command, revision, environment, results and coverage limits.
  Compilation alone is not a behavioral oracle; missing, incomplete or compiler-coupled
  tests block translation.
- **Remediation when absent**: If no test suite exists, stop immediately and direct the user:
  ```bash
  $test-retrofitter-acrazie
  ```
  This proposes a dependency, not permission to load or execute it. Obtain its own
  activation, testing contract and realization approval. Establish regression boundaries
  first; never port unverified behavior.

---

## 2. Phase 1: Traceable Paradigm Mapping

Before generating target code, document how the source language constructs map to the target language
across the four foundational pillars below. Reuse an applicable approved specification or record the evidence in an approved accessible document/contract. `PARADIGM-MAPPING.md` is only an example name; the root is only a proposal. No fixed filename, file format or separate artifact is required, and no new write is authorized by this reference.

### Pillar A: Memory & Resource Lifecycle
| Source Paradigm | Target Paradigm | Mapping Strategy & Hazards |
| :--- | :--- | :--- |
| Garbage Collected (Python/JS/Java) | Manual / RAII / Borrowed (Rust/C++) | Identify owners vs borrowers; map GC references to explicit handles or smart pointers (`Rc`/`Arc`). |
| Manual / `defer` (Zig/C) | RAII / `Drop` (Rust/C++) | Ensure cleanup callbacks don't trigger asynchronous double-frees or drop while event loops hold pointers. |
| Object Finalizers | Explicit context managers / `defer` | Replace nondeterministic GC finalization with deterministic `defer file.Close()` or `try-with-resources`. |

### Pillar B: Error Model
| Source Paradigm | Target Paradigm | Mapping Strategy & Hazards |
| :--- | :--- | :--- |
| Exceptions (Python/Java/Ruby) | Explicit Results (Go/Rust/Zig) | Map every `raise`/`throw` to a typed error enum or `(T, error)` tuple. Never swallow errors. |
| Integer status codes | Exception / Algebraic types | Map internal representations only while preserving externally observable error codes and behavior. |
| Panics / Crashes | Error propagation | Reserve `panic` exclusively for unrecoverable programmer invariants, not routine runtime failures. |

### Pillar C: Concurrency & Asynchrony
| Source Paradigm | Target Paradigm | Mapping Strategy & Hazards |
| :--- | :--- | :--- |
| Event Loop / Promises (JS/Python) | Goroutines / Channels (Go) | Investigate ordering, cancellation and error propagation before choosing concurrency constructs; preserve lifecycle behavior. |
| System Threads & Mutexes | Actors / Async-Await | Map thread locks to structured tasks; prevent holding locks across asynchronous `.await` points. |
| Global Interpreter Lock (GIL) | True Multi-Threading | Expose shared mutable state; introduce explicit synchronization or atomics where source assumed GIL safety. |

### Pillar D: Type System & Nullability
| Source Paradigm | Target Paradigm | Mapping Strategy & Hazards |
| :--- | :--- | :--- |
| Duck Typing / Dynamic `Any` | Interfaces / Traits / Generics | Inventory runtime attributes; synthesize minimal interfaces satisfying all actual usage sites. |
| Nullable pointers (`null`/`nil`/`None`) | Algebraic `Option<T>` | Distinguish "absent value" from "default/empty value"; do not blindly unwrap options. |
| Number coercion (float ↔ int) | Strict numeric types | Explicitly document truncation vs floor on negative values; prevent numeric overflow and signedness bugs. |

---

## 3. Phase 2: Traceable Ownership and Resource Evidence

Reuse or record resource-lifetime evidence for the selected boundary after any required content/write/destination approval. It may share the approved mapping document or contract. `OWNERSHIP-MATRIX.tsv` and the TSV below are examples, not required separate files; preserve all relevant ownership, cleanup, aliasing and concurrency facts regardless of representation.

```tsv
struct_or_type	field_name	resource_kind	allocation_locus	owner_lifetime	cleanup_trigger	concurrency_model
ConnectionPool	active_sockets	TCP Socket	ConnectionPool::open	Owned by Pool	Pool::close()	Mutex protected
SessionContext	buffer_cache	Heap Memory	Session::read_chunk	Owned by Session	Scope exit	Thread-local
EventDispatcher	listener_list	Callback Ref	Dispatcher::on()	Shared WeakRef	Explicit off()	EventLoop thread
```

---

## 4. Phase 3: Canary Trial Run Protocol

1. Select representative canary units according to actual semantic risks and dependencies, not a fixed file count. Explain coverage and remaining gaps before translation. The following categories are prompts to inspect where present, not required project roles:
   - **Type Definition Leaf**: Minimal dependencies, pure data models or types.
   - **Core Logic Unit**: Algorithmic processing, math, or state transformation.
   - **Resource / I/O Handler**: Network, filesystem, or async coordination.
2. Port each canary file mechanically, adhering strictly to the approved traceable mapping.
3. Run authorized checks/oracle and propose review for the exact canary snapshot; activate the reviewer separately in an explicit kit.
4. Require independent `ACCEPT` covering all canary files; corrected snapshots need fresh review and affected validations.
5. Update the approved mapping evidence with any discovered edge cases or refined conventions.

---

## 5. Phase 4: Full Mechanical Translation & Queue Handoff

1. Replicate directory hierarchy and file basenames 1:1.
2. For each file, translate faithfully without attempting stylistic refactoring.
3. Every translated unit must be covered by the independent exact-snapshot review gate.
4. Once all source files have their mirrored target counter-parts in place, compile or run static analysis across the target project.
5. For a mass backlog only, propose Diagnostic Queue Runner and obtain its activation
   and applicable execution/write approvals. Pass snapshot, mapping, scope, tool/configuration,
   diagnostics and allowed actions. A small or empty backlog does not require this dependency:
   ```bash
   $diagnostic-queue-runner-acrazie
   ```

After diagnostic corrections, revalidate affected reviews and run required final
target checks and unchanged oracle. An unavailable mandatory dependency blocks its
dependent step, not unrelated discovery. Report actual passed/failed/blocked/not
executed evidence; fewer diagnostics or a source-only pass is not target equivalence.
Reports stay in chat unless content/destination writing is approved. No automatic
staging, commit, push, PR, merge or deployment.
