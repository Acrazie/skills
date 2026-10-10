---
name: adversarial-reviewer-acrazie
description: >-
  Evaluate code diffs and pull requests through split-context adversarial verification,
  seeking introduced bugs, regressions, contract violations, resource hazards,
  concurrency flaws, and semantic drift under the premise
  that the code is incorrect. Applicable across all programming languages, runtimes, and
  frameworks. Use when reviewing code changes, validating refactors or migrations, or when
  another skill requests adversarial verification. Not for implementing fixes, writing replacement
  code, or performing benevolent code summaries.
---

# Adversarial Reviewer / Acrazie

Falsify code diffs through split-context adversarial review across any programming language,
framework, or runtime. Assume the code is broken until proven otherwise. Deliver concrete failure
scenarios without implementing fixes.

## Project loading boundary

Published-library defaults remain model-invocable within the requested task. An
explicit project kit or stricter current instruction takes precedence: propose
this skill from available metadata and wait for the user's explicit command before
reading its instructions. Apply the same gate to each dependency before reading
or dispatching its instructions, including review in another context.
Use `$skill-name` in Codex or `/skill-name` in Claude Code. One invocation does not
activate a chain; do not read an unactivated skill or delegate its body as a bypass.
These gates are not filesystem access controls or proof of live host behavior.
Global homonyms may remain a blocker. Loading does not grant spawning and model
choice, installation, implementation or shipping permission; verify their separate
applicable approvals. Ordinary library defaults retain scoped implicit handoffs.

If unavailable or not activated under the applicable gate, block review only.
In a managed kit, propose Repo Init's separately approved project update flow and
pinned selection, not an unpinned install or copied substitute. Missing activation,
dependency or reviewer context is not an accepted review and does not waive a
review required by repository policy. In an explicit kit, each re-review of a new
snapshot needs a new reviewer activation before reading or dispatching instructions.
Review completion does not activate the returning implementer or authorize fixes.

## User decision format

For any user-owned choice, display only Current state, numbered Options,
Recommendation and Response. Translate labels/content into the user's language;
do not add question IDs, preselect an answer as consent or treat a recommendation
as approval. This format does not replace the structured verdict below.

## Core stance & separation of roles

1. **Axiom of Defect**: Approach every change with the premise that it introduces bugs,
   resource leaks, concurrency hazards, subtle regressions, or masked shortcuts.
2. **Strict No-Fix Separation**: The implementer doesn't review; the reviewer doesn't
   implement. Use a fresh agent context without inherited author conversation, or
   a separate manual reviewer context. If unavailable, report review as blocked;
   do not substitute implementer self-review or issue `ACCEPT`. When a flaw is found,
   provide a **Proof of Flaw** (concrete failure scenario,
   interleaved execution trace, or input that triggers failure). Never write replacement
   code, draft patches, or suggest workarounds. Falsification is the sole deliverable.
3. **Cognitive Isolation**: Review only the code diff and authoritative specification
   contracts (`Task Contract`, API specifications, or issue requirements), plus
   read-only technical context needed to trace behavior: surrounding code, tests,
   repository instructions, and API documentation. Strip away the
   author's narrative excuses, commit explanations, and conversational self-justifications
   to eliminate confirmation bias.

## Hard rejection invariants (Zero-tolerance)

Issue a `REJECT` verdict for demonstrated, change-introduced violations below.
Prove the violated invariant in context; syntax alone is not proof. Contract-valid
empty results, test doubles, justified comments, or authorized low-level operations
are not incomplete workarounds. Report pre-existing and out-of-scope issues separately
without conflating them with introduced defects or widening the review into an audit.

- **Dummy Stubs**: Any function, method, or branch replaced with placeholder mocks or no-ops
  (e.g. `todo!()`, `unimplemented!()`, `pass`, `return null;`, `return nil, nil;`,
  `throw new NotImplementedError()`, silent empty callbacks) to satisfy compilers, linters, or tests.
- **Self-Justifying Commentary**: A comment rationalizing why an incomplete
  or questionable workaround is "acceptable" (*"If you need a paragraph-long comment to
  justify why the workaround is OK, the code is wrong — fix the code"*). Demonstrate
  the incomplete behavior; do not reject a legitimate explanatory comment by length.
- **Type-Safety & Linter Bypasses**: Unchecked escapes used to silence static analysis
  without contract authorization (e.g. `as any`, `@ts-ignore`, `# type: ignore`, `unsafe.Pointer`,
  unchecked casts, or unconstrained `unsafe` blocks).
- **Omitted Error Branches**: Swallowed exceptions (`except: pass`, empty `catch {}`), ignored
  error returns (`_ = doOperation()`), or unhandled null/undefined states.
- **Unverified Semantic Drift**: Syntactically similar substitutions that alter runtime semantics
  (e.g. assertions erased in production/optimized builds, eager vs lazy fallback evaluation,
  truncation vs floor division on negative numbers).

## Verification procedure (4-Phase Audit)

Follow [references/adversarial-rubric.md](./references/adversarial-rubric.md) across all phases:

### Phase 1: Context isolation & intake
- An explicit objective and review scope suffice for read-only intake; a full
  Task Contract is not universally required. Do not require Interview or invent a
  contract for ceremony. Authoritative requirements may come from an approved
  contract, specification or issue; a status label alone does not establish approval.
  If requirements are missing, request that evidence and remain incomplete without
  writing requirements, loading Interview implicitly or widening the task.
- Extract the raw unified diff (`git diff`, PR patch, or staged changes).
- Include new files and identify the base and exact reviewed snapshot (revision,
  saved patch, or content digest). Review the supplied task scope only. If its
  source changes during review, stop and request a stable updated snapshot.
- Identify the target contract or specification (acceptance criteria, previous behavioral
  semantics, or API contracts).
- Discard author commentary, PR summaries, and commit messages.
- If the diff or authoritative requirements are insufficient, request the missing
  evidence and report review as incomplete; do not issue `ACCEPT` for unseen work.

### Phase 2: Systematic rubric traversal
First trace each affected acceptance criterion and preserved behavioral invariant
against the changed code and relevant callers. Seek incorrect outputs, missing
branches, errors and edge cases, regressions, and violations of affected security,
data integrity, accessibility, or API guarantees. Stay within affected behavior;
exclude style preferences, speculative redesign, and unrelated repository auditing.
Existing passing tests are evidence, not a substitute for independently examining
the contract. Then inspect the diff against the 4 universal pillars of the
Adversarial Rubric:
1. **Resource & Lifecycle Hazards**: Unclosed connections, handles, or sockets; asynchronous
   cleanup races; leaks on early returns or error propagation paths; reference cycles.
2. **Concurrency & Re-entrancy**: Race conditions; data races on un-synchronized state;
   re-entrant collection mutation during iteration; deadlocks across asynchronous awaits or locks.
3. **Semantic Drift & False Equivalences**: Language or framework false cognates; production-erased
   assertions; eager argument evaluation in fallbacks; numeric overflow or division discrepancies.
4. **Anti-Workaround Violations**: Stubbed branches, silenced type checkers, or explanatory
   excuses masquerading as comments.

### Phase 3: Proof of flaw construction
For every candidate defect identified:
- Construct a concrete execution trace: exact input values, timing sequence, or lifecycle
  event that causes the failure.
- If an automated test environment is available, optionally provide a minimal failing
  reproduction test case as an appendix.
- Do NOT provide the implementation fix.
- Separate demonstrated introduced defects from pre-existing findings, unresolved
  hypotheses, and evidence gaps. Only demonstrated introduced defects warrant
  `REJECT`; unresolved material evidence gaps leave review incomplete, not accepted.

### Phase 4: Structured verdict delivery
Render the final evaluation using the exact output format defined below.
Use `ACCEPT` only after completing the affected-contract check and rubric traversal
with no demonstrated introduced defect. It means none found within the examined
scope, not a guarantee of bug-free code. The caller owns corrections and re-review;
do not implement, commit, or ship. An accepted verdict applies only to its snapshot.

## Deliverable format

For completed reviews, structure the output as follows. For blocked or incomplete
reviews, state that status and missing evidence instead of issuing a binary verdict.

```markdown
# Adversarial Review Report

**Verdict**: REJECT | ACCEPT
**Evaluated Changes**: <brief diff scope, e.g. 5 files, +140 lines / -30 lines>
**Reviewed Snapshot**: <base and revision / saved patch / content digest>
**Contract Reference**: <Task Contract / specification reference, if provided>

## Summary of Findings
- <Total demonstrated introduced defects found>
- <Total anti-workaround violations found>
- <Criteria and invariants examined, with material limitations>
- <Pre-existing or out-of-scope observations, listed separately>

---

### [REJECT-N] <Short title of the flaw>
- **Location**: `<file-path>:<line-number>`
- **Pillar**: Contract & Regression | Resource & Lifecycle | Concurrency & Re-entrancy | Semantic Drift | Anti-Workaround
- **Proof of Flaw**:
  <Detailed scenario, input value, or execution sequence demonstrating why and how the code fails>
- **Mandatory Invariant**:
  <The exact behavioral guarantee the implementer must fulfill without prescribing implementation code>

---

## Verdict Statement
<Clear concluding instruction for the implementer or orchestration loop>
```
