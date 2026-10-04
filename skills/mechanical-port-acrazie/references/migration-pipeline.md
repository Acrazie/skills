# Mechanical Migration Pipeline Reference

This guide provides the authoritative methodology for language-to-language mechanical codeports.
It applies across any language transition (dynamic-to-static, managed-to-systems, or OO-to-functional).

---

## 1. The Test Oracle Invariant

A mechanical port replaces the entire execution engine. The only safety net between working software
and hallucinated code is an automated test suite whose execution is decoupled from the target compiler.

### Oracle Qualification Checklist
- **Black-Box Invariance**: Tests verify behavior through external APIs, CLI commands, HTTP endpoints,
  or standard library I/O interfaces, rather than inspecting internal language-specific symbols.
- **Pre-Flight Pass**: The suite must achieve 100% green status on the source codebase before any target
  file is written.
- **Remediation when absent**: If no test suite exists, stop immediately and direct the user:
  ```bash
  $test-retrofitter-acrazie
  ```
  Establish regression boundaries first; never port unverified behavior.

---

## 2. Phase 1: The Universal Paradigm Matrix (`PARADIGM-MAPPING.md`)

Before generating target code, document how the source language constructs map to the target language
across four foundational pillars. Store this document at the repository root.

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
| Integer status codes | Exception / Algebraic types | Map error codes into rich domain variants; do not carry negative integer magic numbers forward. |
| Panics / Crashes | Error propagation | Reserve `panic` exclusively for unrecoverable programmer invariants, not routine runtime failures. |

### Pillar C: Concurrency & Asynchrony
| Source Paradigm | Target Paradigm | Mapping Strategy & Hazards |
| :--- | :--- | :--- |
| Event Loop / Promises (JS/Python) | Goroutines / Channels (Go) | Map Promise chains to goroutines and select channels; watch for unclosed channel deadlocks. |
| System Threads & Mutexes | Actors / Async-Await | Map thread locks to structured tasks; prevent holding locks across asynchronous `.await` points. |
| Global Interpreter Lock (GIL) | True Multi-Threading | Expose shared mutable state; introduce explicit synchronization or atomics where source assumed GIL safety. |

### Pillar D: Type System & Nullability
| Source Paradigm | Target Paradigm | Mapping Strategy & Hazards |
| :--- | :--- | :--- |
| Duck Typing / Dynamic `Any` | Interfaces / Traits / Generics | Inventory runtime attributes; synthesize minimal interfaces satisfying all actual usage sites. |
| Nullable pointers (`null`/`nil`/`None`) | Algebraic `Option<T>` | Distinguish "absent value" from "default/empty value"; do not blindly unwrap options. |
| Number coercion (float ↔ int) | Strict numeric types | Explicitly document truncation vs floor on negative values; prevent numeric overflow and signedness bugs. |

---

## 3. Phase 2: Ownership and Resource Matrix (`OWNERSHIP-MATRIX.tsv`)

Before transpiling large modules, produce an inventory TSV documenting resource lifetimes.

```tsv
struct_or_type	field_name	resource_kind	allocation_locus	owner_lifetime	cleanup_trigger	concurrency_model
ConnectionPool	active_sockets	TCP Socket	ConnectionPool::open	Owned by Pool	Pool::close()	Mutex protected
SessionContext	buffer_cache	Heap Memory	Session::read_chunk	Owned by Session	Scope exit	Thread-local
EventDispatcher	listener_list	Callback Ref	Dispatcher::on()	Shared WeakRef	Explicit off()	EventLoop thread
```

---

## 4. Phase 3: Canary Trial Run Protocol

1. Select 3 to 5 canary files:
   - **Type Definition Leaf**: Minimal dependencies, pure data models or types.
   - **Core Logic Unit**: Algorithmic processing, math, or state transformation.
   - **Resource / I/O Handler**: Network, filesystem, or async coordination.
2. Port each canary file mechanically, adhering strictly to `PARADIGM-MAPPING.md`.
3. Submit each canary diff to `$adversarial-reviewer-acrazie`.
4. Iterate until all canary files receive an `ACCEPT` verdict.
5. Update `PARADIGM-MAPPING.md` with any discovered edge cases or refined conventions.

---

## 5. Phase 4: Full Mechanical Translation & Queue Handoff

1. Replicate directory hierarchy and file basenames 1:1.
2. For each file, translate faithfully without attempting stylistic refactoring.
3. Every translated unit must pass `adversarial-reviewer-acrazie`.
4. Once all source files have their mirrored target counter-parts in place, compile or run static analysis across the target project.
5. Export the resulting compiler diagnostics and invoke:
   ```bash
   $diagnostic-queue-runner-acrazie
   ```
