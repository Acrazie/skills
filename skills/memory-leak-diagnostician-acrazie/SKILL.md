---
name: memory-leak-diagnostician-acrazie
description: >-
  Diagnose, trace, and eliminate JavaScript and runtime memory leaks through differential heap
  snapshot analysis, retainer tree mapping, and surgical un-retention patching. Use when applications,
  services, or test runners suffer from monotonic RSS growth, Out-Of-Memory (OOM) crashes, lingering
  event listeners, captive closure scopes, or runaway object pools. Not for static-only audits or
  general feature refactoring.
---

# Memory Leak Diagnostician / Acrazie

Isolate root-cause retention chains in JavaScript, TypeScript, and native runtimes (Node.js, Bun, browser)
through differential heap analysis, retainer graph traversal, and zero-side-effect un-retention patches.

## Core axioms & diagnostic invariants

1. **Monotonic Growth Axiom (High RSS ≠ Leak)**:
   High memory consumption that plateaus under load is an allocation footprint or engine cache. A true memory
   leak is characterized by **monotonic, unbounded growth** under steady-state or cycling load where garbage
   collection cycles fail to reclaim memory.
2. **Retainer Causality Invariant**:
   Objects do not leak in a vacuum; they remain alive because a GC root (global object, active timer, active
   promise chain, protected DOM/JSC node, or captive lexical scope) retains an unbroken reference path to them.
3. **No Blind Guesses (Evidence-First)**:
   Never speculate on memory leaks without empirical delta evidence. Diagnostic claims require either:
   - Two or more heap snapshots (`.heapsnapshot`) taken before and after load, OR
   - Time-series memory telemetry (`process.memoryUsage()`, `heapStats()`, RSS metrics) under a reproducible script.
4. **Surgical Un-Retention**:
   Fixes must break the retention chain cleanly without mutating domain logic:
   - Prefer explicit lifecycle cleanup (`Symbol.dispose`, `removeListener`, `AbortSignal.any`),
   - Scope unbinding (`null`-out references when work completes),
   - Zero-copy stream representations (`Blob` over eager array buffer clones).

## Diagnostic workflow

Follow [references/memory-anti-patterns.md](./references/memory-anti-patterns.md) for taxonomy and code patterns:

### Phase 1: Ingestion & differential baseline

1. **Gather artifacts**:
   - Pair of V8/JSC heap snapshots: `baseline.heapsnapshot` (after warm-up) and `after-load.heapsnapshot`.
   - OR structured memory profiling logs: JSON/CSV dumps of `heapUsed`, `external`, `extraMemorySize`, `RSS`.
   - OR isolated reproduction script: `repro.js` or `repro.ts` that reproduces memory growth in under 60 seconds.
2. **Calculate deltas**:
   - Compare instance counts and retained byte sizes across snapshots.
   - Flag constructors with anomalous growth deltas (`+N%` retained size: `Closure`, `Array`, `EventEmitter`, `Promise`, `Uint8Array`).

### Phase 2: Retainer tree traversal & classification

Map the path from GC Root to the leaking target. Classify the root cause into one of the 5 canonical anti-patterns:

| Anti-Pattern | Retainer Signature | Typical Culprit |
| :--- | :--- | :--- |
| **Lexical Scope Retention** | `JSLexicalScope` / `(closure)` retains outer scope | Inner callback retains huge unused variable from outer function |
| **Orphan Event Listener** | `_events` array / `addEventListener` without cleanup | Service or component subscribes repeatedly without `removeListener` |
| **Lingering AbortSignal** | `AbortSignal` listener on long-lived controller | Fetch/SSE handlers attached to an application-wide controller |
| **Buffer Duplication** | Eager typed array cloning in stream responses | `new Response(uint8Array)` copying memory instead of `Blob` zero-copy |
| **Zombie Promise Chain** | Unresolved `Promise` holding rejection callbacks | Abandoned network requests or missing error handling paths |

### Phase 3: Surgical un-retention & non-regression proof

1. **Locate code site**:
   Identify the exact file and line number holding the reference anchor.
2. **Produce un-retention patch**:
   Apply the minimal structural fix:
   - Invert registration to one-time listener: `.once()` instead of `.on()`.
   - Bind explicit teardown: `AbortSignal` cleanup via `signal.addEventListener('abort', fn, { once: true })`.
   - Break scope capture: extract sub-function outside enclosing scope or set reference to `null` post-execution.
   - Adopt modern RAII disposal: `using client = acquire()` with `[Symbol.dispose]()`.
3. **Validate non-regression**:
   Re-run the reproduction harness or test suite. Prove that:
   - Retained size returns to baseline post-GC.
   - All existing functional tests continue to pass.

## Deliverable format

Emit a markdown diagnostic artifact `memory-leak-report.md` structured as:

```markdown
# Memory Leak Diagnostic Report

## 1. Executive Summary & Verdict
- **Target Subsystem**: [File / Class / Route]
- **Leak Severity**: [Monotonic growth rate, e.g. +45 MB / 1,000 requests]
- **Root Cause Category**: [Lexical Scope | Orphan Listener | AbortSignal | Buffer Duplication | Zombie Promise]

## 2. Evidence & Differential Deltas
| Constructor / Object Type | Baseline Count | Post-Load Count | Delta Count | Retained Size Delta |
| :--- | :--- | :--- | :--- | :--- |
| `JSLexicalScope` | 120 | 14,320 | +14,200 | +85.4 MB |

## 3. Retainer Path
\`\`\`mermaid
flowchart TD
    Root["GC Root (Global EventEmitter)"] --> Container["ServiceRegistry._subscribers"]
    Container --> Scope["JSLexicalScope (requestHandler)"]
    Scope --> Leaking["largePayload (Uint8Array 50MB)"]
\`\`\`

## 4. Surgical Patch
\`\`\`diff
--- a/src/handler.ts
+++ b/src/handler.ts
...
\`\`\`

## 5. Non-Regression Verification
- **Test Command**: `bun test ./tests/memory.test.ts`
- **Observed RSS Stability**: Constant at 62 MB across 50,000 iterations.
```
