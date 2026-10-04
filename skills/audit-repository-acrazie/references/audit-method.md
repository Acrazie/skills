# Audit method

## Evidence order

Prefer the strongest available evidence for the claim:

1. actual repository behavior, configuration, dependency graph, and call sites;
2. targeted existing tests or a minimal safe reproduction;
3. installed package metadata and version-specific interfaces;
4. current official documentation, compatibility tables, release notes, and upstream source;
5. upstream issue trackers, maintainer statements, independent benchmarks, and credible field reports;
6. inference, labeled clearly and never presented as verified fact.

Time-sensitive claims require source date and relevant version. Search official sources first. Community evidence is allowed when official material cannot establish real-world behavior, but identify its limitations.

Do not infer support from package presence, popularity, download count, a passing build alone, or an unopened search result.

## Focus and materiality

The user's question owns the audit. Investigate adjacent evidence only when it can:

- change the requested decision;
- invalidate a current assumption or recommendation;
- expose a likely root cause;
- demonstrate meaningful correctness, performance, operational, maintenance, or integration impact;
- reveal that the apparent local choice is owned by another layer.

An improvement being possible is insufficient. Style preferences, fashionable replacements, speculative abstractions, and unrelated cleanup are not findings.

Continue every relevant material branch until it is resolved or reaches a disclosed evidence gap. Do not cap exploration by time, tokens, files, candidates, or finding count. Conversely, do not explore unrelated branches merely because capacity remains.

When a lead is material but belongs to a different objective or subsystem, state the initial evidence and ask before expanding. Otherwise place at most one concise item under `Out of scope`.

## Compare alternatives

Discover broadly enough not to miss credible emerging options, then deeply compare only candidates that remain relevant after basic fit checks. Do not impose a fixed candidate count.

Use dimensions relevant to the user's decision, commonly:

- native framework or language integration;
- compatibility with actual runtime and dependency versions;
- required capability coverage;
- measured performance under representative conditions;
- configuration and operational complexity;
- developer workflow and failure visibility;
- migration cost and reversibility;
- maintenance activity and release discipline;
- API or configuration stability;
- licensing constraints when they affect adoption.

Maturity is a risk input, not a gate. Never equate age or popularity with quality. A young tool may be the best choice when current evidence proves fit and benefit. When benefit is strong but evidence history is limited, recommend a bounded, reversible pilot and state its success and rollback criteria.

Recommend replacement only when net benefit is material for this repository. Include `keep current approach` as a real option.

### Library, framework, and development-tool adoption

Reuse the comparison above; do not run a second interview or a separate generic
ranking workflow. Inspect actual needs, manifests, lockfiles, and existing native
or installed capabilities. Include adding no dependency as a real option.

Separate elimination criteria from preferences. Check required capability coverage,
runtime/framework compatibility, acceptable licensing, and blocking security risks
against the project's established constraints. Use version-specific upstream
metadata, release/support information, and relevant advisories for proportionate
adoption checks; this is not a full security audit. Distinguish confirmed risk from
unknown information. An unknown elimination criterion blocks the choice until
resolved; unknown preferences lower confidence or remain explicit reservations.
Never infer that uncertainty proves a vulnerability or incompatibility.

Evaluate cost in proportion to capabilities actually used, not package size alone.
A larger candidate may replace several dependencies, remove custom code, or reduce
maintenance. Unused feature breadth is not a benefit. Account for transitive
dependencies, integration complexity, API stability, support/release discipline,
and reversibility. Novelty, popularity, age, or commit frequency alone do not prove
quality or abandonment. Evaluate the specific package/component, not a family's
reputation, and discover credible emerging options without assuming they are best.

Distinguish production cost from local/CI cost. For frontend code, inspect the
actually delivered bundle and runtime cost when relevant, including real import
paths and tree-shaking behavior. For backend code, use relevant startup, memory,
throughput, or latency evidence. For development tools, consider installation and
transitive footprint, CI/runtime cost, configuration, capability coverage, and
whether outputs or components enter production. No universal weight threshold;
do not compare published archive size with compressed bundle size or incompatible
benchmark conditions. Dated upstream claims are not observed project measurements.

Present one argued recommendation with credible alternatives, decisive evidence,
trade-offs, and unresolved conditions, rather than an artificial numeric ranking.
If a gate remains unknown, report the choice as blocked, not accepted; a separately
authorized bounded trial may be the recommended next action. Obtain user acceptance
before recording a decision or handing it off. Implementation remains a separate
task, and the Audit Record's write approval remains separate from choice approval.

## Validate proportionally

Use the smallest sufficient proof for each claim, not the smallest overall investigation.

- Run relevant read-only inspection and targeted existing tests.
- Use benchmarks only for performance claims and make conditions reproducible.
- Distinguish observed results from expected behavior documented upstream.
- Do not install dependencies, update lockfiles, reconfigure tools, generate lasting artifacts, or access non-documentation network services without separate permission.
- If a command may mutate caches or generated files materially, disclose that and ask first.
- Record commands, relevant output summaries, versions, and failures.

When a decisive adoption claim cannot be established with read-only evidence,
describe the smallest targeted trial, its success criteria, side effects, and
cleanup/rollback plan, then request separate permission. Permission for that trial
does not authorize integration or migration. Prefer an isolated disposable fixture
when it can answer the question without modifying the repository.

Lack of executable validation lowers confidence; it does not justify inventing certainty.

## Findings

Rank by relevance to the requested decision, then concrete impact, evidence confidence, effort, and reversibility.

- **Décisif:** changes or blocks the requested decision.
- **Matériel:** meaningful improvement or risk directly related to it.
- **À considérer:** credible option whose value depends on a user choice or missing evidence.
- **Hors périmètre:** relevant initial signal requiring a separate audit.

Translate labels to the report language when needed without changing their meaning.

Each finding must contain:

- concise claim;
- priority and confidence;
- exact evidence and affected path or component;
- concrete scenario and impact;
- recommended action, including no change when appropriate;
- expected effort, tradeoffs, and remaining uncertainty.

Include important elements worth preserving so recommendations do not cause needless churn.
