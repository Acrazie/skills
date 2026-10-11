# Retention investigation reference

These are investigation hypotheses, not certified fixes or an exhaustive taxonomy.
Use only sections relevant to observed evidence. This reference supplies no runnable
runtime recipes; consult current documentation for the actual engine and version
before choosing APIs, commands or disposal syntax.

## Measurement boundaries

RSS describes process residency, not just reachable JavaScript objects. Heap
measurements may include garbage not yet collected. External buffers, native
allocations, fragmentation, caches and runtime reservations require separate
interpretation. Virtual address space is not physical RSS. Do not add metric fields
without checking whether their accounting overlaps.

Shallow size describes an object's own represented allocation. Retained size is
an estimate of memory made collectible if that object no longer retains it, based
on the snapshot's graph and dominators. Other retaining paths matter; deleting one
reference does not guarantee immediate collection or release of resident pages.
Snapshots from different engines/formats are not interchangeable, and may omit
native allocations. Snapshot capture can itself perturb the measurements.

Warm up the same workload, complete relevant lifecycles and compare repeated
cycles under matched concurrency, data size and collection conditions. Agree
acceptable trend/tolerance and measurement uncertainty before declaring success.
A stable graph count can support a lifecycle hypothesis but does not certify all
memory paths. Neither a plateau nor non-monotonic samples settle every leak claim.

## Closures and timers

A reachable callback can retain captured values. Do not assume every closure
retains every unused variable in its outer scope: engine optimizations and actual
reference paths matter. Confirm a path from a surviving owner to the unexpected
object before assigning causality.

Identify who owns the timer/callback and when its lifetime ends. Moving a callback
to another function does not clean up an accumulating interval. Check teardown on
success, error and cancellation and whether repeated registration is intended.
Changing lexical structure is a candidate experiment, not proof of collection.

## Listeners and subscriptions

A long-lived publisher may retain listeners and their captured owners. Compare
registrations with removals across completed subscriber lifecycles. Cleanup must
use the intended handler identity and occur at the actual ownership boundary.
Verify that duplicate registrations and repeated delivery remain correct.

Replacing `.on()` with `.once()` changes delivery semantics; it is not a default
leak fix. Anonymous arrows and bound functions can both retain objects. Switching
between them does not by itself remove retention. Verify runtime/transpiler support
and actual lifecycle invocation before proposing disposal syntax.

## Cancellation listeners

A listener on a long-lived signal may survive a completed operation. `{ once: true }`
removes it after the event fires, not when an operation completes without aborting.
Verify cleanup in completion/error paths as well as cancellation, including already
aborted signals and relevant races. Cancellation must reach the underlying operation;
standard `Request` has no `cancel()` method. Do not invent an API from its name.

## Buffers, streams and backpressure

Measure actual allocation, lifetime, concurrency and queue growth. Duplication or
large temporary working sets are not automatically unreachable-memory leaks.
Check buffering, stream consumption/cancellation and backpressure before changing
representations. `Blob` is not a universal zero-copy guarantee; neither a constructor
name nor an illustrative RSS multiplier proves allocation behavior. Confirm actual
engine/version semantics and compare equivalent response behavior and throughput.

## Pending work and caches

An unresolved Promise is not automatically a permanent GC root. Trace reachable
pending operations, callbacks, queues and their owners. `Promise.race` does not
cancel the losing operation or clean its timers, listeners and resources. Timeouts
need defined cancellation/cleanup semantics and must preserve expected outcomes.

For caches, establish intended ownership, eviction, size/lifetime limits and key
retention. WeakRef and FinalizationRegistry have nondeterministic collection timing;
they are not deterministic cleanup or resource-release mechanisms. Weak values do
not bound a strongly held key map. Do not introduce them without an approved
semantic requirement and evidence that they address the actual retaining path.

## Correction checks

Check lifecycle completion, failure, cancellation and repeated use, then repeat
comparable memory measurements. Functional delivery assertions and ownership
counts can provide focused regression evidence alongside runtime measurements.
Forced GC is neither production remediation nor a substitute for correct cleanup;
use it only when authorized and supported, under comparable conditions. No universal
60-second reproduction requirement, 5 MB threshold or 50,000-iteration proof applies.
Never report exact recovery or global leak freedom from one passing sample.
