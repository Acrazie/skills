# Adversarial Review Rubric

This reference defines the 4-pillar audit framework used by `adversarial-reviewer-acrazie`.
Every check represents a class of defects that compiles cleanly, passes naive tests, and causes
severe production failures or memory corruption.

---

## Pillar 1: Resource & Lifetime Hazards

### 1.1 Asynchronous cleanup & handle retention
- **Vulnerability**: Freeing a wrapper object or smart pointer while an asynchronous operating
  system handle or event loop callback holds the underlying raw pointer.
- **Classic Failure**: In libuv / epoll abstractions, calling an async close routine (e.g. `uv_close`)
  on a heap-allocated pipe that drops at the end of the enclosing block. When the event loop fires
  the close callback on the next tick, it accesses freed memory and double-frees the handle.
- **Proof Requirement**: Trace handle lifetime across event loop ticks. Demonstrate if any owner
  drops before the asynchronous completion callback runs.

### 1.2 Early-return & exception allocation leaks
- **Vulnerability**: Memory or system handles acquired early in a function are not released when
  subsequent operations fail (error returns, early `?` operator, panics, or C++ exceptions).
- **Classic Failure**: Allocating a cryptographic context or passphrase buffer, failing on a later
  output buffer allocation, and returning without deallocating the protected buffer.
- **Proof Requirement**: Trace every early exit, error propagation (`?`, `if err != null`), and
  exception point. Check that all resources allocated prior to that point are deterministically freed.

### 1.3 Detached buffers during argument coercion
- **Vulnerability**: Native bindings capturing raw pointers to managed buffers (e.g. JavaScript
  `ArrayBuffer` or Python bytearrays) while invoking user-defined coercions (`valueOf`, `toString`)
  prior to transmission.
- **Classic Failure**: User code executes during argument coercion, detaching or resizing the
  underlying buffer. The native routine proceeds using the stale cached pointer and length, causing
  heap out-of-bounds reads or writes.
- **Proof Requirement**: Identify any point where user code or callbacks can interleave between
  payload buffer acquisition and actual consumption.

### 1.4 Reference count underflow and GC root pinning
- **Vulnerability**: Asymmetric increments and decrements in manual reference counting or managed
  runtime roots.
- **Classic Failure**: Decrementing a reference count upon closing a resource without properly
  removing it from a global GC tracing list, permanently pinning leaked instances in memory.
- **Proof Requirement**: Check life cycle symmetry: every increment/pinning operation must have
  an exact, unskippable decrement/unpinning counterpart.

---

## Pillar 2: Concurrency, Re-entrancy & State Invalidation

### 2.1 Re-entrant container mutation
- **Vulnerability**: Invoking external callbacks while iterating over internal associative arrays,
  vectors, or linked lists.
- **Classic Failure**: Inside an HTTP/2 session loop or timeout listener, a user callback triggers
  a new request. The new request inserts into the session's internal hashmap, triggering a table
  rehash that invalidates stream pointers currently being traversed.
- **Proof Requirement**: Verify whether any function call made inside an iteration loop can
  re-enter the parent structure or trigger structural reallocation.

### 2.2 Torn reads across thread boundaries
- **Vulnerability**: Accessing compound structures or tagged unions across threads without memory
  barriers or synchronization primitives.
- **Classic Failure**: A background garbage collector marker thread inspects an event variant while
  a worker thread writes a payload, observing a torn discriminator/data pointer mismatch.
- **Proof Requirement**: Show that non-atomic shared structures are read concurrently without
  mutual exclusion or synchronization guarantees.

---

## Pillar 3: Semantic Drift & False Equivalences

### 3.1 Erased macro assertions vs active function assertions
- **Vulnerability**: Replacing a function call assertion that always evaluates its arguments with
  a macro that expands to a no-op in release builds (e.g. Zig `assert(insert())` vs Rust
  `debug_assert!(insert())`).
- **Classic Failure**: An assertion argument contains a critical side effect (e.g. registering a
  node in a hot-reload dependency graph). In debug builds, the test suite passes; in release builds,
  the expression is erased, breaking state updates.
- **Proof Requirement**: Inspect all assertions. Demonstrate whether any expression inside an
  assertion mutates state or produces side effects required at runtime.

### 3.2 Eager fallback evaluation vs lazy closure execution
- **Vulnerability**: Using eager fallback evaluators (e.g. `unwrap_or(expr)`) instead of lazy
  evaluators (e.g. `unwrap_or_else(|| expr)`).
- **Classic Failure**: When unpacking optional values where the alternative expression computes or
  panics (e.g. `first.unwrap_or(second.unwrap())`), the fallback is evaluated unconditionally,
  panicking even when the primary value is valid.
- **Proof Requirement**: Demonstrate that any expression passed to an eager fallback helper will
  panic, allocate unnecessarily, or throw when evaluated on the happy path.

### 3.3 Rounding and integer conversion on negative numbers
- **Vulnerability**: Inconsistencies between truncation toward zero (`trunc`) and floor division
  toward negative infinity (`floor`).
- **Classic Failure**: Splitting a timestamp in seconds (`f64`) into `{sec, nsec}` for a POSIX
  `timespec`. For timestamps before 1970 (negative `f64`), `trunc` yields a negative nanosecond
  field (e.g. -500,000,000 ns), violating system invariants. `floor` correctly retains nanoseconds
  within `[0, 1e9)`.
- **Proof Requirement**: Test boundary inputs at zero, negative floats, and minimum signed bounds.

### 3.4 Slice reinterpretation and odd-byte bounds
- **Vulnerability**: Differences in slice casting libraries when handling trailing misaligned bytes.
- **Classic Failure**: A source language ignores trailing odd bytes during 16-bit reinterpretation,
  while a target language library (e.g. `bytemuck::cast_slice`) panics on unaligned lengths.
- **Proof Requirement**: Provide an odd-length input buffer and verify whether the routine panics.

### 3.5 Format string marker injection
- **Vulnerability**: Replacing compile-time template expansions with runtime string post-processing.
- **Classic Failure**: A formatter replaces color markers (e.g. `<r>`) with ANSI escapes at runtime
  after user arguments have already been substituted. If a user argument contains special escape
  sequences (such as OSC 8 hyperlinks ending in backslashes), the marker parser misinterprets the
  input, corrupting CLI output.
- **Proof Requirement**: Inject boundary string inputs containing delimiters, backslashes, and ANSI
  escape sequences into format arguments.

---

## Pillar 4: Anti-Workaround & Hygiene Invariants

### 4.1 Mocking and stubbing evasion
- **Vulnerability**: Submitting non-functional placeholder implementations (`todo!()`,
  `unimplemented!()`, dummy return values like `Ok(())` or `0`) to satisfy compiler errors.
- **Proof Requirement**: Any stub that bypasses requested domain logic without explicit contract
  authorization is an immediate, automatic `REJECT`.

### 4.2 Explanatory self-justification
- **Vulnerability**: Authoring extensive comments to explain away architectural shortcomings,
  leaks, or temporary workarounds.
- **Rule**: *"If you need a paragraph-long comment to justify why the workaround is OK, the code is
  wrong — fix the code."*
- **Proof Requirement**: Any paragraph-length comment explaining why a missing invariant or
  non-standard patch is acceptable triggers an automatic `REJECT`.

### 4.3 Unsafe containment audit
- **Vulnerability**: Broad, multi-line `unsafe` blocks that obscure raw pointer dereferences.
- **Standard**: Unsafe blocks must be tightly scoped (preferably single-line conversions from
  FFI or C/C++ boundaries) with clear prerequisite safety invariants documented.
