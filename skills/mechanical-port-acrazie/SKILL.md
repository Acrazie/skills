---
name: mechanical-port-acrazie
description: >-
  Plan, orchestrate, and execute language-to-language mechanical codebase migrations
  through 1:1 structural mirroring, pre-translation paradigm mapping, canary trial runs,
  and mandatory test oracle verification. Use when migrating a repository or major component
  from one programming language to another. Not for internal refactoring within the same language,
  fixing isolated bugs, or rewriting without an automated test suite.
disable-model-invocation: true
---

# Mechanical Port / Acrazie

Orchestrate language-to-language mechanical codebase migrations. Prioritize 1:1 structural
fidelity over premature idiomatic refactoring. Never port without an objective test oracle.

## Core principles & invariants

1. **Test Oracle Invariant (Strict Gating)**:
   A mechanical port is permissible ONLY if an automated, black-box or language-independent
   test suite already exists and passes against the source codebase.
   - If tests are missing, incomplete, or coupled to the source compiler, STOP.
   - Instruct the user to first invoke `$test-retrofitter-acrazie` to establish end-to-end
     black-box verification before attempting code translation.
2. **Faithful 1:1 Mirroring (Anti-Premature Redesign)**:
   Translate the codebase preserving identical directory hierarchies, module boundaries,
   naming patterns, and algorithmic flow. Do NOT attempt architectural overhauls, database
   swaps, or stylistic idiomatization during the port. Make it compile, pass tests, and
   resemble the source first; idiomatize later.
3. **All-At-Once over Hybrid Glue**:
   Avoid creating temporary FFI wrappers or bi-directional runtime bindings that pollute
   the architecture. Execute the translation cleanly across the target boundary.
4. **Adversarial Verification Loop**:
   Every canary file and translated module must be falsified by `adversarial-reviewer-acrazie`
   to ensure zero stubs, zero explanatory excuse comments, and zero unverified semantic drift.

## Universal 4-phase migration workflow

Follow [references/migration-pipeline.md](./references/migration-pipeline.md) across all phases:

### Phase 1: Paradigm mapping (`PARADIGM-MAPPING.md`)
Before writing any target code, produce a formal cross-language translation specification
at the root of the port workspace covering the 4 core paradigm dimensions:
- **Memory & Resource Lifecycle**: Garbage collection, RAII, manual allocation, reference
  counting, file descriptor / socket / connection closing semantics.
- **Error Model**: Exceptions vs return codes vs `(value, err)` tuples vs `Result`/`Option`.
- **Concurrency & Asynchrony**: Event loops, promises, OS threads, coroutines, actors, channels.
- **Type Systems & Nullability**: Dynamic vs static typing, duck typing vs explicit interfaces,
  nullable pointers vs algebraic optionals.

### Phase 2: Ownership and resource matrix (`OWNERSHIP-MATRIX.tsv`)
Perform an inventory across all data structures and boundary interfaces. Map:
- Struct/Class identifier and field names.
- Allocation locus and primary owner.
- Deterministic deallocation / cleanup trigger.
- Concurrency and thread-boundary status.

### Phase 3: Canary trial run (3–5 files)
Select 3–5 representative files of varying complexity (e.g. one primitive type/utility, one
stateful data structure, one async/I/O handler):
1. Translate them following `PARADIGM-MAPPING.md`.
2. Submit the diff to `adversarial-reviewer-acrazie`.
3. If defects or ambiguities emerge, refine `PARADIGM-MAPPING.md` before proceeding.

### Phase 4: Full mechanical translation & diagnostic handoff
1. Translate remaining files mechanically, matching the source topology 1:1.
2. Validate each translated file through `adversarial-reviewer-acrazie`.
3. Once all files are placed, hand off the compilation and static analysis errors to
   `$diagnostic-queue-runner-acrazie` for systematic, topological error crushing.

## Deliverable format

Always deliver a structured migration status report:

```markdown
# Mechanical Port Status Report

**Source Language / Environment**: <e.g. Python 3.12 / Zig 0.13 / Java 17>
**Target Language / Environment**: <e.g. Go 1.22 / Rust 2021 / TypeScript 5.4>
**Test Oracle Status**: VERIFIED (<test suite command and assertion count>)
**Current Phase**: Paradigm Mapping | Ownership Matrix | Canary Trial | Full Translation

## Artifacts Produced
- `PARADIGM-MAPPING.md`: <status / key decisions>
- `OWNERSHIP-MATRIX.tsv`: <status / structs inventoried>
- Canary Files: <list of files translated and reviewed>

## Next Actions
<Specific instruction: proceed to canary, full translation, or handoff to diagnostic-queue-runner>
```
