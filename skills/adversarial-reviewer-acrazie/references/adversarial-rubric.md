# Universal Adversarial Review Rubric

This reference defines the 4-pillar audit framework used by `adversarial-reviewer-acrazie`.
It applies across all programming languages, runtimes, and frameworks. Every check represents
a class of defects that compiles or passes initial linters cleanly, looks plausible on inspection,
and can cause production failures, data corruption, or memory leaks. Before the
four pillars, check affected behavior against the authoritative contract: incorrect
outputs, missing required branches, edge cases, and introduced regressions. Require
a concrete failure scenario and a violated invariant for each rejection; syntax
matches are investigation leads, not proof. Separate pre-existing issues and do
not reject contract-valid empty results, test doubles, or authorized operations.

---

## Pillar 1: Resource & Lifecycle Hazards

### 1.1 Asynchronous cleanup & handle retention
- **Vulnerability**: Dropping or releasing a parent resource while an asynchronous operation,
  event loop callback, worker thread, or goroutine still holds raw references to the underlying resource.
- **Cross-Language Manifestations**:
  - *Go*: Spawning a goroutine that reads from a `net.Conn` or `http.Response.Body` after the caller
    has already closed or returned it.
  - *Node.js / TypeScript*: Attaching event listeners or timers that capture large object contexts
    without removing them on teardown, or closing a socket while an async write is queued.
  - *Python*: Creating `asyncio.Task` instances without holding a reference (causing early garbage
    collection during execution) or closing an event loop with pending asynchronous generators.
  - *Rust / C++*: Calling an asynchronous completion API (e.g. `uv_close`, `epoll`, `io_uring`) on a
    buffer that gets dropped at the end of the enclosing scope before the kernel callback runs.
- **Proof Requirement**: Trace resource lifetime across asynchronous ticks or concurrent thread
  boundaries. Demonstrate any scenario where the resource is released before the asynchronous consumer finishes.

### 1.2 Early-return & exception leaks
- **Vulnerability**: Resources acquired early in a function are not released when subsequent operations
  fail or exit early (via exceptions, error returns, panics, or early `return` statements).
- **Cross-Language Manifestations**:
  - *Python*: Opening a database connection or file without a `with` context manager or `try...finally` block,
    where an intermediary exception aborts execution before `.close()`.
  - *Go*: Acquiring a mutex or response body before an error check, or forgetting `defer mu.Unlock()` /
    `defer resp.Body.Close()` prior to early `return nil, err` points.
  - *Java*: Opening a JDBC `ResultSet`, `Statement`, or file stream without `try-with-resources`.
  - *C / C++*: Multiple exit labels (`return -1;`) failing to jump to the cleanup/free sequence.
- **Proof Requirement**: Trace every error propagation path, exception throw, and early return.
  Verify that all resources acquired up to that point are deterministically released.

### 1.3 State mutation & detached buffers under coercion
- **Vulnerability**: Invoking user-defined callbacks, getters, or string conversions that mutate or
  detach underlying data structures mid-operation.
- **Cross-Language Manifestations**:
  - *JavaScript / TypeScript*: User code inside `valueOf()`, `toString()`, or property getters detaching
    an `ArrayBuffer` or mutating an array during argument coercion before transmission.
  - *Python*: Custom `__getitem__` or `__str__` implementations modifying the dictionary or list currently
    being serialized or iterated.
- **Proof Requirement**: Identify any point where user callbacks or implicit type coercions can interleave
  and mutate underlying buffers or collection state.

### 1.4 Reference cycles and uncollected root pinning
- **Vulnerability**: Circular references in reference-counting runtimes or un-evicted entries in global registries.
- **Cross-Language Manifestations**:
  - *Python*: Self-referencing cycles containing custom `__del__` implementations or closures retaining globals.
  - *TypeScript / JavaScript*: Storing objects in global `Map` or `Set` registries instead of `WeakMap` /
    `WeakSet`, permanently pinning memory.
  - *Go*: Registering closures in long-lived event dispatchers that prevent large captured structs from being collected.
- **Proof Requirement**: Demonstrate whether a resource will be permanently retained in memory even after
  its primary functional lifecycle has ended.

---

## Pillar 2: Concurrency, Re-entrancy & State Invalidation

### 2.1 Re-entrant collection mutation
- **Vulnerability**: Mutating collections, maps, or data structures while an outer scope is iterating over them.
- **Cross-Language Manifestations**:
  - *Python*: `RuntimeError: dictionary changed size during iteration` when an event listener modifies the registry.
  - *Java*: `ConcurrentModificationException` during collection traversal.
  - *Go*: Fatal runtime panic: `concurrent map iteration and map write`.
  - *C++ / Rust*: Re-hashing a map inside a callback, invalidating internal pointers or references currently in use.
- **Proof Requirement**: Demonstrate any path where a callback or nested function call executed during
  iteration can insert, delete, or reallocate the collection.

### 2.2 Data races and un-synchronized mutable state
- **Vulnerability**: Reading and writing shared memory across concurrent threads or coroutines without
  synchronization primitives or atomic barriers.
- **Cross-Language Manifestations**:
  - *Go*: Concurrent reads/writes to struct fields across goroutines without `sync.Mutex` or `sync/atomic`.
  - *JavaScript / Node.js*: Async race conditions where shared state is read before an `await` and written after,
    overwriting intermediate mutations from concurrent requests.
  - *Python*: Modifying non-thread-safe caches across native worker threads without threading locks.
- **Proof Requirement**: Construct an interleaved execution trace showing two concurrent contexts corrupting state.

### 2.3 Deadlocks and lock order inversion
- **Vulnerability**: Acquiring multiple locks in inconsistent order or blocking asynchronous event loops on synchronous locks.
- **Cross-Language Manifestations**:
  - *Go*: Sending to an unbuffered channel where no receiver is active, causing permanent goroutine deadlock.
  - *Node.js / Python asyncio*: Invoking synchronous blocking I/O inside an asynchronous worker, starving the loop.
  - *Java / C++*: Thread 1 acquiring A then B while Thread 2 acquires B then A.
- **Proof Requirement**: Identify cyclic lock acquisition patterns or unbuffered channel blockages.

---

## Pillar 3: Semantic Drift & False Equivalences

### 3.1 Production-erased assertions & debug dead code
- **Vulnerability**: Placing critical runtime logic, state mutations, or security checks inside assertion
  constructs that are stripped in production builds.
- **Cross-Language Manifestations**:
  - *Python*: `assert check_permission(user)` where `python -O` strips all `assert` statements unconditionally.
  - *Rust*: `debug_assert!(cache.insert(key))` where release builds erase the entire expression and its side effect.
  - *C / C++*: `#ifdef NDEBUG` removing function calls inside `assert()`.
  - *JavaScript / TypeScript*: Stripping debug logging branches with bundler tree-shaking that contained state updates.
- **Proof Requirement**: Inspect all assertions. Demonstrate whether any expression inside an assertion
  mutates state or provides necessary validation in production environments.

### 3.2 Eager fallback evaluation vs lazy closure execution
- **Vulnerability**: Unconditionally evaluating expensive or fallible fallback expressions in default-value helpers.
- **Cross-Language Manifestations**:
  - *JavaScript / TypeScript*: Function-call arguments such as
    `chooseDefault(value, createNew())` evaluate `createNew()` before the helper runs.
    In contrast, `map.get(key) ?? createNew()` short-circuits: the fallback runs only
    when the lookup returns `null` or `undefined`. `val || fallback()` also short-circuits,
    but falls back for every falsy value, which can violate contracts preserving `0`,
    `false`, or an empty string. See [MDN's operator reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing).
  - *Python*: Mutable default arguments (`def add_item(val, target=[])`) sharing state across all calls, or
    `dict.get(key, expensive_call())` evaluating `expensive_call()` unconditionally.
  - *Java*: `Optional.orElse(computeDefault())` (eager) instead of `Optional.orElseGet(this::computeDefault)` (lazy).
  - *Rust*: `opt.unwrap_or(panic_expr)` panicking inside the argument evaluation even when `opt` is `Some`.
- **Proof Requirement**: Demonstrate that an eager fallback creates unnecessary resource allocations, performance
  cliffs, or crashes on the standard path.

### 3.3 Numeric division, truncation & rounding asymmetries
- **Vulnerability**: Inconsistencies between floor division, truncation toward zero, and signedness conversions.
- **Cross-Language Manifestations**:
  - *Python vs Go/JS/Java*: `-3 // 2` in Python is `-2` (floor toward negative infinity), whereas `Math.trunc(-3 / 2)`
    or `-3 / 2` in Go/Java is `-1` (truncation toward zero). Porting math logic across this boundary silently corrupts
    timestamps, coordinate systems, and paginate offsets.
  - *Floating point precision*: Comparing floats for exact equality (`f == 0.1 + 0.2`).
  - *Integer overflow*: Silent 32-bit or 64-bit integer wrap-around.
- **Proof Requirement**: Provide concrete negative, zero, or boundary inputs demonstrating calculation drift.

### 3.4 Slicing, indexing & boundary mismatches
- **Vulnerability**: Confusions between inclusive vs exclusive end ranges, 0-indexed vs 1-indexed collections,
  and negative index support.
- **Cross-Language Manifestations**:
  - *Python*: `s[-1]` accesses the last element; in Go or C, `s[-1]` panics or reads out-of-bounds memory.
  - *String lengths*: Measuring length in bytes (Go/Rust UTF-8) vs UTF-16 code units (JS/Java `length`) vs Unicode
    code points (Python `len(str)`). None necessarily measures user-perceived grapheme
    clusters: Python `len("e\u0301")` is 2 for one combining-character cluster.
    Slicing at the wrong unit can split a user-perceived character. See
    [Python's text sequence documentation](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str).
- **Proof Requirement**: Provide a multi-byte, empty, or negative boundary input that causes an off-by-one or panic.

---

## Pillar 4: Anti-Workaround & Hygiene Invariants

### 4.1 Mocking, stubbing & escape hatches
- **Vulnerability**: Submitting non-functional placeholder implementations to satisfy compilers, linters, or test suites.
- **Prohibited Patterns**:
  - Empty or dummy return values: `return null`, `return nil, nil`, `return {}`, `return Ok(())`, `return 0`.
  - Stub macros and exceptions: `todo!()`, `unimplemented!()`, `raise NotImplementedError`, `throw new Error("TODO")`.
  - Placeholder comments: `// TODO: implement later`, `# FIXME`.
  - Empty callbacks or swallowed errors: `catch (e) {}`, `except Exception: pass`.
- **Action**: **`REJECT`** only with proof of an introduced, unauthorized incomplete
  implementation; legitimate contract results and test doubles are not violations.

### 4.2 Explanatory self-justification
- **Vulnerability**: Authoring extensive comments explaining why an incomplete workaround or missing requirement
  is "acceptable" or "can be handled later".
- **Rule**: *"If you need a paragraph-long comment to justify why the workaround is OK, the code is wrong — fix the code."*
- **Action**: **`REJECT`** when the comment masks a demonstrated introduced contract
  violation, not merely because it is long or explains a legitimate trade-off.

### 4.3 Static analysis & type safety bypasses
- **Vulnerability**: Silencing static analyzers and type checkers with unchecked escape hatches instead of fixing
  the underlying type invariant.
- **Prohibited Bypasses**:
  - *TypeScript*: `@ts-ignore`, `@ts-nocheck`, `as any`, non-null assertions `!` without prior checks.
  - *Python*: `# type: ignore`, `cast(Any, ...)`.
  - *Go*: `unsafe.Pointer`, swallowing error returns with blank identifiers `_ = fn()`.
  - *Java*: Raw types, `@SuppressWarnings("unchecked")`.
  - *Rust / C++*: Expanding `unsafe` scopes beyond single-line FFI boundaries.
- **Action**: **`REJECT`** with proof of an introduced unauthorized bypass; respect
  explicitly approved boundaries rather than rejecting syntax alone.
