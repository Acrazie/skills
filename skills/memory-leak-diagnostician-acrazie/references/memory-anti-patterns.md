# Memory Anti-Patterns & Retainer Diagnostic Reference

Comprehensive technical guide to diagnosing, classifying, and resolving JavaScript and runtime memory leaks across V8 (Node.js, Chrome) and JavaScriptCore (Bun, Safari).

---

## 1. Engine Memory Fundamentals

### V8 vs. JavaScriptCore (JSC) Metrics
* **V8 (Node.js)**:
  - `process.memoryUsage()` returns:
    - `rss`: Resident Set Size (total physical memory in RAM occupied by the process).
    - `heapTotal`: V8's allocated heap space.
    - `heapUsed`: Actual memory occupied by live objects, strings, and closures.
    - `external`: Memory bound to C++ objects linked to JS (Buffers, TypedArrays).
    - `arrayBuffers`: Memory allocated for `ArrayBuffer` and `SharedArrayBuffer`.
  - Snapshots generated via `v8.writeHeapSnapshot('dump.heapsnapshot')`.
* **JavaScriptCore (Bun)**:
  - `import { heapStats } from 'bun:jsc'` provides:
    - `heapSize`: Active memory consumed by JavaScript values.
    - `extraMemorySize`: Native off-heap allocations associated with JS objects (buffers, DOM/native structures).
    - `objectTypeCounts`: Instance count for each JSC cell type.
    - `protectedObjectTypeCounts`: Objects protected from garbage collection (e.g. active timers, roots).
  - High virtual memory in Bun/JSC often reflects security "moats" (guard pages), not physical RSS.

### Shallow Size vs. Retained Size
* **Shallow Size**: The memory held by the object itself (primitive fields, immediate pointers). Typically small (32 to 64 bytes for ordinary objects).
* **Retained Size**: The total memory freed if this specific object were deleted and collected by GC. Includes the object's shallow size plus all children reachable *only* through this object.

---

## 2. The 5 Canonical Memory Anti-Patterns

### Anti-Pattern 1: Lexical Scope Retention (`JSLexicalScope`)

**The Mechanism**:  
In JavaScript, an inner closure retains the entire lexical environment of its enclosing function, not just the variables it references. If an inner closure outlives the outer function (e.g. attached to an event, timer, or exported callback), all variables in that outer scope remain pinned in memory.

#### Leaking Example
```typescript
// ❌ ANTI-PATTERN: largeBuffer retained by the timer closure
function processRequest(req: Request) {
  const largeBuffer = new Uint8Array(50 * 1024 * 1024); // 50 MB
  const requestId = req.headers.get("x-request-id");

  // This small closure keeps largeBuffer alive for 1 hour!
  setInterval(() => {
    console.log(`Status for ${requestId}`);
  }, 3600_000);
}
```

#### Surgical Fix
```typescript
// ✅ FIXED: Isolate the retained primitive into its own unencumbered scope
function scheduleLogger(requestId: string | null) {
  setInterval(() => {
    console.log(`Status for ${requestId}`);
  }, 3600_000);
}

function processRequest(req: Request) {
  const largeBuffer = new Uint8Array(50 * 1024 * 1024);
  const requestId = req.headers.get("x-request-id");
  
  scheduleLogger(requestId);
  // largeBuffer is eligible for GC immediately when processRequest finishes
}
```

---

### Anti-Pattern 2: Orphan Event Listeners

**The Mechanism**:  
Registering a listener on a long-lived publisher (`EventEmitter`, WebSocket client, DOM element) pins both the listener function and whatever it captures in its closure. If the subscriber object is destroyed without unregistering, it leaks permanently.

#### Leaking Example
```typescript
// ❌ ANTI-PATTERN: Handler accumulates on global messageBroker
class UserSession {
  private cache = new Map<string, any>();

  constructor(broker: EventEmitter) {
    broker.on("user:logout", (userId) => {
      this.cache.delete(userId); // 'this' is permanently captured!
    });
  }
}
```

#### Surgical Fix
```typescript
// ✅ FIXED: Explicit cleanup or Symbol.dispose (RAII pattern)
class UserSession implements Disposable {
  private cache = new Map<string, any>();
  private readonly handler = (userId: string) => this.cache.delete(userId);

  constructor(private broker: EventEmitter) {
    broker.on("user:logout", this.handler);
  }

  [Symbol.dispose]() {
    this.broker.removeListener("user:logout", this.handler);
    this.cache.clear();
  }
}

// In consumer:
{
  using session = new UserSession(globalBroker);
  // session automatically cleaned up when leaving block scope
}
```

---

### Anti-Pattern 3: Lingering AbortSignal Listeners

**The Mechanism**:  
`AbortSignal` listeners attach to the `AbortController`. If a singleton controller is reused or a signal has a long lifespan, adding `'abort'` listeners on individual transient requests without unregistering causes memory to grow monotonically.

#### Leaking Example
```typescript
// ❌ ANTI-PATTERN: Listener stays attached if signal does not abort
async function fetchWithTimeout(url: string, parentSignal: AbortSignal) {
  const req = new Request(url);
  parentSignal.addEventListener("abort", () => {
    req.cancel();
  });
  return fetch(req);
}
```

#### Surgical Fix
```typescript
// ✅ FIXED: Clean up the listener in finally or use { once: true }
async function fetchWithTimeout(url: string, parentSignal: AbortSignal) {
  const req = new Request(url);
  const abortHandler = () => req.cancel();

  parentSignal.addEventListener("abort", abortHandler, { once: true });
  try {
    return await fetch(req);
  } finally {
    parentSignal.removeListener?.("abort", abortHandler);
  }
}
```

---

### Anti-Pattern 4: Buffer Duplication in Streams

**The Mechanism**:  
Passing raw typed arrays or buffers to constructors like `new Response(uint8Array)` or through unoptimized serialization copies the buffer into internal memory structures. When done frequently under high concurrency, memory usage explodes (e.g. 22x multiplier).

#### Leaking / Wasteful Example
```typescript
// ❌ INEFFICIENT: Uint8Array forces eager internal duplication (~1GB RSS)
export function serveFile(buffer: Uint8Array) {
  return new Response(buffer, {
    headers: { "Content-Type": "application/octet-stream" },
  });
}
```

#### Surgical Fix
```typescript
// ✅ FIXED: Zero-copy Blob representation preserves memory footprint (~60MB RSS)
export function serveFile(buffer: Uint8Array) {
  const blob = new Blob([buffer]);
  return new Response(blob, {
    headers: { "Content-Type": "application/octet-stream" },
  });
}
```

---

### Anti-Pattern 5: Zombie Promises & Function Binds

**The Mechanism**:  
- Creating a `Promise` that never resolves or rejects retains all chained `.then()` callbacks and their associated lexical closures in the microtask / GC root queue indefinitely.
- `Function.prototype.bind()` creates an internal bound function object holding a strong reference to the target function, `this`, and all arguments.

#### Surgical Fix
- Always ensure promises have a bounded timeout race: `Promise.race([work, timeout(30_000)])`.
- Prefer arrow functions or explicit instance methods over dynamic `.bind()`.
- Use `WeakRef` and `FinalizationRegistry` when caching object references that should not prevent GC:
```typescript
const cache = new Map<string, WeakRef<LargeObject>>();
```

---

## 3. Automated Non-Regression Test Harness

To verify that a memory leak fix is robust and persistent, write an automated non-regression test:

```typescript
import { test, expect } from "bun:test";
import { gc } from "bun:jsc";

test("memory-leak non-regression: session cache cleans up after disposal", () => {
  // 1. Warm-up
  for (let i = 0; i < 100; i++) {
    const s = new UserSession();
    s[Symbol.dispose]();
  }
  gc();

  const baselineMemory = process.memoryUsage().heapUsed;

  // 2. High-iteration cycling load
  for (let i = 0; i < 50_000; i++) {
    const s = new UserSession();
    s[Symbol.dispose]();
  }

  // 3. Force garbage collection
  gc();
  const postLoadMemory = process.memoryUsage().heapUsed;

  // 4. Verify no monotonic growth (allow modest buffer variance < 5MB)
  const growthBytes = postLoadMemory - baselineMemory;
  expect(growthBytes).toBeLessThan(5 * 1024 * 1024);
});
```
