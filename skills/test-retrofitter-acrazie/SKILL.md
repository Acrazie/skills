---
name: test-retrofitter-acrazie
description: >-
  Add and execute risk-selected automated tests for existing untested or
  insufficiently tested code, after an approved interview contract. Distinguish
  characterization from requirement conformance without changing functional
  behavior. Use when the task requires adding tests to existing behavior.
  Not for new features, bug fixes, tooling migrations, or CI pipelines.
---

# Test Retrofitter / Acrazie

Improve evidence for existing behavior, not the behavior itself. Select this skill
when adding tests is requested or belongs to the authorized task. Under published
library defaults no named skill command is required; explicit kits follow the
project loading boundary below. Relevant discovery may start read-only; implementation still
requires the approved contract below. Do not start an unrelated testing campaign.

## Project loading boundary

Published-library defaults remain model-invocable within the requested task. An
explicit project kit or stricter current instruction takes precedence: propose
this skill from available metadata and wait for the user's explicit command before
reading its instructions. Apply the same gate to each dependency, including a
reviewer dispatched to another context. One invocation does not activate the chain.
Use `$skill-name` in Codex or `/skill-name` in Claude Code; do not silently read a
missing or unactivated dependency as a workaround. These gates are not filesystem
access controls and do not prove live host behavior. Global homonyms may remain a
blocker. Loading approval never grants execution, installation, spawning or shipping
permission. Under ordinary library defaults, retain scoped implicit handoffs.

## User decision format

For any user-owned choice, including execution/setup permission, review and model
selection, display only Current state, numbered Options, Recommendation and
Response. Translate labels/content into the user's language; do not add question
IDs, preselect an answer as consent or treat a recommendation as approval. Ask only
unresolved decisions, with their verified context and concrete consequences.

## Discover the testing boundary

Read repository instructions, relevant task documents, requirements, Git state,
and the smallest useful set of source files, tests, manifests, and test commands.
Trace inputs, observable outputs, invariants, error paths, and side effects before
editing. Run a safe scoped baseline where possible; distinguish existing failures
from failures introduced by the new tests. Preserve unrelated work and respect
repository isolation requirements.

Separate two test oracles:
- **Characterization:** evidence of observed current behavior, which may contain
  bugs. Label it as such; passing does not establish business correctness.
- **Conformance:** evidence against explicit requirements approved by the user.
  Do not infer these solely from implementation or bless a contradiction silently.

If evidence is ambiguous, surface the missing decision rather than inventing an
expected value. Existing tests and documentation are evidence, not automatic proof
that a behavior is intended.

## Obtain the approved contract

Reuse an explicitly approved Task Contract if it covers the current test request,
has approval evidence beyond a status label, and no material discovery invalidates
it. Verify it covers the target behavior and scenarios, oracle for each, test types
and rationale, environment, permissible files/setup, and completion criteria.
Reusing a contract does not require Interview to be installed or loaded. If stale
or incomplete, reopen only affected decisions rather than restarting settled ones.

Interview is mandatory only when no applicable approved contract can be reused.
When required, propose `interview-acrazie`, applying the project loading boundary before
reading or invoking it. Supply objective, verified behavior/baseline, exclusions,
oracle conflicts, risks, missing decisions and expected handoff. Let the foundation
own clarification and persistence; do not embed another interview or create a
duplicate contract. After handoff, resume only under applicable execution authority
and the explicit kit's renewed specialist invocation requirement.

Resolve the target behavior and scenarios, oracle for each, test types selected
with reasons, execution environment, permissible files and setup, and observable
completion criteria. Reuse settled answers. Reopen only materially stale choices.
No implementation begins without applicable explicit approval evidence.

When required Interview is unavailable or not activated, block test implementation
only; request the missing activation or separately approved installation. Locate
it through metadata first, then read/invoke only after the applicable loading gate.
In an explicit kit, use Repo Init's approved project update flow and the project's
pinned selection rather than an unpinned overwrite. Outside a managed kit, propose:

```bash
npx skills add Acrazie/skills@interview-acrazie
```

Do not install silently, copy the foundation, or continue if required installation
fails.
Contract approval authorizes scoped realization only when that authorization is
explicitly evidenced and the applicable loading gate is satisfied. Otherwise ask
for scoped execution authorization before editing. It does not authorize shipping
or otherwise restricted actions.

## Select and build the smallest sufficient proof

Select tests by risk and observable boundary, not a mandatory pyramid or catalog.
Unit, integration, contract, E2E, property-based, regression, security, performance,
and accessibility tests are options, not promises to run every category. For
nonfunctional tests, agree the conditions and acceptance thresholds first.

1. Reuse repository runners, fixtures, and conventions. Prefer native or installed
   tools when sufficient. If no adequate runner exists, include minimal setup,
   dependency installation, and allowed files in the approved contract before
   changing them. Do not migrate existing tooling or edit CI workflows implicitly.
2. Map each agreed scenario to an assertion on meaningful observable behavior.
   Include relevant boundaries, errors, authorization, and data integrity risks.
   Avoid assertions that simply copy internal implementation or snapshots without
   a reviewed behavioral purpose. Mock external boundaries, not the behavior under
   test; use real integration components when the agreed risk requires them.
3. Control time, randomness, concurrency, environment, and state where relevant.
   Use synthetic data and isolated disposable resources by default. Bound execution
   and clean up resources, including on failures. Never silently skip an agreed
   integration boundary or replace it with a mock and claim equivalent proof.
4. Keep production source unchanged by default. If testability requires a refactor,
   explain the obstacle and obtain explicit approval for a narrowly scoped,
   behavior-preserving change before touching source. Functional fixes remain out
   of scope even if tests discover a bug.
5. Run new tests and affected existing checks. Where safe and useful, demonstrate
   an assertion can detect a deliberate fault in an isolated disposable copy;
   do not alter the working source or force every characterization test to fail
   first. An import/setup failure is not proof of defect detection.

External services, secrets, costs, load, or destructive actions require distinct
explicit authorization. Local execution alone does not imply safety: inspect
commands, endpoints, fixtures, and cleanup before running. Never target production
by default, copy secrets into artifacts, or weaken security to make tests run.

## Handle failures without falsifying evidence

When code contradicts an approved requirement, retain a test that reproduces the
mismatch and report the diagnostic. Do not fix functionality, weaken assertions,
change requirements, mark the test skipped, or redefine buggy behavior as correct
merely to obtain green. A red suite is a disclosed nonconformance, not a successful
validation. Pause for renewed scope if the requested outcome requires correction.

For infrastructure failures, identify the blocker rather than treating them as
application defects. Attribute baseline failures separately. Do not add retries or
larger timeouts merely to hide flaky behavior; control its cause within scope or
report it. If required execution is unavailable, report tests as unexecuted and do
not silently downgrade acceptance criteria.

## Deliver and stop

Update the same contract with actual evidence: scenario/criterion, oracle, test
files, exact commands, results, and remaining gaps. Report new failures, baseline
failures, skips, blockers, and approved setup or refactors separately. Distinguish
local execution, CI, and live-service verification.

Stop when the agreed scenarios have meaningful deterministic tests and sufficient
execution evidence, with no unrequested changes. Do not chase arbitrary coverage
percentages. If requirements fail or proof is missing, report incomplete validation
rather than claiming all criteria passed. Follow separate user/repository shipping
permissions; do not infer commit, push, PR, or deployment permission from testing.

## Ownership exclusions

New application behavior and its tests belong to `feature-builder-acrazie`.
General runner/tooling migration belongs to `repo-modernizer-acrazie`. Pipeline
changes belong to their CI workflow, including the Jenkins family where applicable;
GitHub Actions creation or migration is outside this skill. Read-only audits belong
to `audit-repository-acrazie`. Do not silently perform another workflow's task.
