# Product Critic Skill

## Objective

Create an explicitly user-invoked skill that critiques an existing product's features and codebase against real user needs, verifiable benefits, simplicity, and total lifecycle cost. Modernity is not an independent goal; retaining the existing solution is a valid recommendation.

## Scope

- Included: `product-critic-acrazie` instructions, synchronized invocation metadata, an English report format, documented ownership boundaries, repository validation, and behavioral evaluation scenarios.
- Included: a broad initial overview followed by user-selected priorities, recommendations to retain, simplify, retire, or replace, and reuse of `interview-acrazie` for unresolved user-owned decisions.
- Excluded: modifying the assessed application's code, performing migrations, implementing recommendations, installing dependencies, deployment, or expanding other skills' scope.
- Persisted documents and skill instructions are in English. Reports use `docs/critics/<subject>.md` after the user approves the destination.

## Success criteria and expected evidence

- C1: Only explicit human invocation starts this skill; evidence: consistent `disable-model-invocation: true` and `policy.allow_implicit_invocation: false`, plus repository structure checks.
- C2: Usage-first critique is distinct from focused technical audits, tooling modernization, and feature implementation; evidence: scope/exclusions review against existing owners.
- C3: Existing answers and approved contracts are reused. Missing user decisions go to `interview-acrazie`; if needed but unavailable, request installation without duplicating it; evidence: instructions and missing-usage scenario.
- C4: Recommendations separate observed facts, declared usage, and hypotheses. Missing usage data does not prove disuse; unmeasured performance gains are not claimed as facts; evidence: missing-usage, retirement, and unmeasured-gain scenarios.
- C5: Reports compare retaining the existing solution with alternatives, including benefits, costs, risks, and verification methods, without changing application code; evidence: report template and satisfactory-existing-solution and costly-alternative scenarios.
- C6: Report approval is not execution approval. Explicit implementation requests require an approved targeted Task Contract. New features may use `feature-builder-acrazie`; bugs, refactors, retirement, and migrations require a suitable workflow without expanding its scope; evidence: out-of-scope implementation scenario.
- C7: The skill passes repository validation and the six agreed behavioral scenarios are evaluated with actual outcomes and limitations reported separately; evidence: validator outputs and scenario results.

## Decisions and context

- Accepted recommendations: Q1–Q12 in the current design interview, including the Q6 addition requiring `interview-acrazie`, the Q9 correction to English documents and `critics`, and the Q12 separation of implementation ownership.
- Existing owners: `audit-repository-acrazie` handles focused technical questions; `repo-modernizer-acrazie` handles tooling modernization and approved migrations; `feature-builder-acrazie` handles new application behavior, not general refactoring or migration.
- [Usage-led Product Critique](../../CONTEXT.md) is the glossary term. No ADR is needed for these reversible workflow choices.
- Changes must remain in the isolated `codex/product-critique` worktree. Git delivery must follow repository branch and PR rules.

## Approval

Status: approved

On 2026-10-01, the user replied "ok" directly to the complete contract summary asking for approval of the contract and its document destinations. After a separate clarification asking whether creation was also authorized, the user replied "go", explicitly authorizing implementation of this skill.

## Delivery evidence

- C1: `SKILL.md` and `agents/openai.yaml` contain synchronized explicit-invocation flags. Native Ruby/Psych parsed both YAML documents and verified the identifier, invocation flags, and prompt reference.
- C2: Read-only prior-art review covered 104 local and remote-tracking refs after fetching all configured origin branches, 29 unique skill specification versions, and 20 committed skill identifiers. No conflicting product-critique workflow was found. Independent scope review found no actionable ownership or permission issue.
- C3–C6: Six policy-response scenarios were executed once each by separate with-skill and baseline agents. An independent grader assessed 18 expectations per configuration: 18/18 with the skill, 15/18 without. Foundation-unavailability, retaining an adequate solution, incomplete retirement evidence, costly replacement, unmeasured performance claims, and mixed implementation ownership were exercised.
- C7: `scripts/hooks/validate-skills.sh skills/product-critic-acrazie/SKILL.md`, `scripts/hooks/check-skill-structure.sh`, and `git diff --check` passed. Additional checks verified local Markdown links, the six-case evaluation JSON, and all 12 response artifacts.
- The skill, UI metadata, report reference, glossary entry, and reproducible evaluation prompts are in the isolated worktree. Raw responses, grading, comparison data, and the generated review viewer remain in the ignored `skills/product-critic-acrazie-workspace/iteration-1/` directory, not in the published skill.
- Limitations: simulated scenario facts and next-response exercises, not a live application audit or end-to-end implementation handoff. One run per scenario is not statistical evidence of general effectiveness. Final-response grading does not independently prove execution side effects. No token or timing measurements were available or inferred. Human review of the generated outputs is pending; no installation, deployment, or live production verification has been performed.
