# Multi-Agent Planner harmonization contract

## Approval and boundaries

The user requested the next Planner harmonization and selected option 1 of the
bounded proposal. That approval covers an isolated implementation, coherent
references, static regressions, evaluation scenarios and this specification.
It does not authorize executing the generated workflows or Git publication.

Worktree: `.worktrees/codex/planner-harmonization`, main base
`f781d50c7e0c9ce9e01cdbd87ee7b8b1d5c28d7c`.
Allowed files: the Planner entrypoint, its four existing references, new
`evals/evals.json`, new `scripts/test_planner_contract.py`, and this specification.
Metadata, model-selection gate, other skills, graph, lockfiles and versions remain
unchanged. The separate Memory Leak lot is not folded into this branch.

## Acceptance criteria

1. Preserve planning-only ownership and a justified single-agent default. Do not
   turn task implementation approval into a delegation campaign.
2. Reuse approved task contracts; gate Interview when required without duplicating
   task clarification. Keep localized four-field decisions and explicit-kit gates.
3. Bound concurrent workers by a concrete maximum of five, verified capacity and
   approved lot count; one retry per slice cannot reset through worker renaming.
4. Trace dependencies and write ownership, isolate or serialize shared writes,
   designate integration ownership and verify actual artifacts plus final snapshot.
5. Preserve the existing portable model-selection section verbatim. Carry unknown
   runtime capabilities/model choices as pending gates, never fabricated syntax or
   silent inheritance. A provisional fast path cannot approve restricted choices.
6. Reports default to chat. Plan approval remains distinct from execution,
   delegation, model validation, installation, persistence and shipping.
7. Add static checks and eight evaluation scenarios; record real local results and
   unavailable checks without claiming runtime or model evaluation.

## Exclusions

No worker launch, runtime workflow execution, application implementation, profiler,
independent review, installation, concrete platform command generation, host/model
certification, staging, commit, push, PR, merge or deployment. The references provide
adaptation boundaries, not current host API recipes. No new ADR is needed.

## Evidence

Local validation on 2026-10-11:

- 149 Python tests passed, including 11 new Planner instruction/fixture regressions.
- 8 site model-selection tests passed without dependency installation; the shared
  model-selection section remains identical to the existing specialists.
- Skill validation, structure, 26 README links, all skill frontmatter/Codex metadata
  YAML parsing, local reference links and whitespace checks passed.
- Eight scenario definitions passed structural checks but were not executed against
  a model. No worker was launched and no generated workflow was executed.
- Delivery preparation received separate user approval for targeted staging and
  `bun install --frozen-lockfile` in this worktree. Locked installation succeeded
  without version or lockfile changes.
- 34 site tests passed: invocation 7, model selection 8 and graph 19. Astro built
  72 pages. The first graph run failed because build output did not yet exist;
  building first resolved that prerequisite failure without source changes.
- Container build/smoke checks and live model/host evaluation remain unexecuted;
  remote CI has not yet run for this branch.
- The eight-file allowlist was verified before targeted staging. Metadata,
  versions, lockfiles and the other worktrees remain unchanged. The validated
  candidate is identified in the delivery recap; publication still needs approval.

These are static checks, not live host, scheduling, integration or model proof.
