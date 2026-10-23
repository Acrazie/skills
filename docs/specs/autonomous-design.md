# Autonomous Design skill contract

## Objective and approval

Create `autonomous-design-acrazie` for autonomous exploration and decision recording
under an initial user mandate, with optional implementation as an appended step.
The user approved this contract and name in the creation chat on 2026-10-23 after
accepting the two modes, priorities, autonomy boundaries and termination rule.
This approves creating and validating the skill, not its installation or Git delivery.

## Accepted behavior

- Both modes share exactly the same exploration and documentation. Mode 2 adds
  implementation and testing; mode 1 never modifies implementation artifacts.
- Topics are unrestricted in kind; a repository is optional. Implementation needs
  an accessible, authorized target.
- Establish objective, mode, priorities, scope and action authority initially.
  Then operate without follow-up questions, documenting blocked branches instead
  of inventing intent, evidence, or permissions.
- User priorities dominate; simplicity, existing-system coherence and reversibility
  are secondary criteria, never substitutes for missing authority.
- Explore only relevant decision frontiers. Stop when every relevant branch is
  resolved, explicitly excluded or blocked; do not pursue universal exhaustiveness.
- Reuse one central record, adding domain glossary terms and durable ADRs lazily.
- Mode 2 stops at tested local changes. No automatic Git shipping or deployment.

## Ownership and prior art

Local and remote-tracking skill versions were inventoried during discovery; the
working branch starts at fetched `origin/main` (`07e8b7e`). Existing scopes include
interactive clarification, technical assessment, specialist execution and shipping;
the new owner is their absent autonomous decision workflow under delegated authority.

`interview-acrazie` explicitly reserves material decisions and final contract
approval for the user. `audit-repository-acrazie` owns read-only technical assessments
of an existing repository and separately approved recording. Extending either to
autonomous arbitrary-topic decisions and implementation would distort its boundaries.
Dev Flow's internal `design-decisions` is restricted to parent INTAKE/SHAPE phases.
The supplied `grill-with-docs` calls `grilling` and `domain-modeling`; its human
interview cannot be reused unchanged. Reuse their decision-frontier and glossary/ADR
concepts, not their human gates or mandatory runtime dependencies.

## Deliverables and evidence

- A self-contained skill, model-invocable Codex metadata and localized catalogue descriptions.
- Behavioral scenarios covering both modes, authority/access blocks, missing
  mandate, existing records, untrusted input and frontier termination.
- Repository frontmatter and structure validation, YAML/JSON parsing, and available
  catalogue/invocation checks.
- Any same-context walkthrough must be labeled as such; static checks do not prove
  autonomous agent behavior. Independent runs are not implied by scenario definitions.

No installation, unrelated catalogue redesign, new agent orchestration framework,
or change to existing specialist protocols is included.

## Validation performed

Repository frontmatter and structure hooks passed. YAML frontmatter and Codex
metadata were parsed using the installed catalogue dependencies; the eight-scenario
JSON was parsed and checked for complete cases and unique IDs. The system creator's
Python quick validator could not run because PyYAML is unavailable; that is not
reported as a passed check.

The existing invocation/portability suite passed 14 tests. The portal built 66
pages including the new skill in all three locales, and the graph suite passed
19 tests after the build. Initial graph-output checks before building failed due
to absent generated pages; rebuilding supplied that required fixture.

Three isolated same-context walkthroughs exercised cases 2, 3 and 5. Mode 1 and
the repository-gated mode 2 preserved source and test bytes. The permitted mode 2
recorded its design before editing, demonstrated two failing assertions before
implementation, then passed seven unittest checks after the change. These are
smoke checks, not independent agent runs, triggering evaluation, or a benchmark
against the original skills. The other five scenarios remain unexecuted.

Temporary fixtures and a generated review viewer are kept only in ignored
`.skill-improver/autonomous-design/`, not included as package output. No installation
of the skill, commit, push, PR creation or deployment has been performed.
