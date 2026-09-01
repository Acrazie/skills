---
name: repository-readme-architect-acrazie
description: Design, create, restructure, or update the primary README of a software repository through repository inspection, an adaptive decision-tree interview, architecture options, and an approval-gated edit. Use for the repository README, not generic Markdown documentation or ancillary files.
---

# Repository README Architect / Acrazie

Produce a README whose structure follows the actual project, audience, and reader journey. Accuracy and reader usability outrank completeness or decoration.

## Scope and invariants

- Work on only the repository's primary README. Preserve an existing filename and case; for a new file, use `README.md` at the repository root.
- Read related files when they provide facts, but never create or edit `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`, changelogs, source code, configuration, or other ancillary files.
- Treat the repository as the source of truth. Never invent commands, compatibility claims, metrics, badges, support promises, release status, or project capabilities.
- Never expose secrets. Avoid secret-bearing files; use committed examples or schemas to discover variable names, and show only fake values.
- Detect generated-file notices before planning an update. Do not overwrite a generated README or modify its generator under this skill. Identify the responsible source, explain the README-only scope conflict, and stop the edit path.
- Do not commit changes.

## Inspect before interviewing

Use read-only inspection to determine facts the environment can answer: repository root, current README, hosting platform, project type, manifests, scripts, package metadata, code entry points, tests, examples, existing media, license and support files, and generated-file markers. Do not ask the user to rediscover these facts.

Inspect directly by default. For a large repository, delegate bounded read-only discovery only when subagents are available, authorized, and materially useful; never make the workflow depend on delegation. Avoid blocking independent interview branches while discovery runs.

Read [references/interview-tree.md](references/interview-tree.md) before running the interview.

## Interview as a decision tree

1. Separate verified facts from user-owned decisions.
2. Maintain prerequisites between decisions. The current frontier contains every unresolved decision whose prerequisites are settled.
3. In each round, ask the whole frontier, grouped by theme and numbered. Give a recommended answer with a short project-specific reason for every question.
4. Do not ask a dependent question in the same round as its unresolved prerequisite.
5. Recompute the tree after every response. Accept a user's batch approval of recommendations without hiding assumptions.
6. If the user does not know, recommend a choice and let them accept, defer, or explicitly exclude that branch. Never convert uncertainty into a fact.
7. Continue until the frontier is empty; do not impose an arbitrary question limit.

When the frontier becomes empty, present a compact shared-understanding record containing verified facts, decisions, exclusions, and unresolved factual gaps. Ask for explicit confirmation. Do not design or edit before confirmation.

## Propose, draft, and edit

After shared understanding is confirmed:

1. Read [references/readme-patterns.md](references/readme-patterns.md).
2. Offer two or three materially different README architectures. Use Markdown/ASCII wireframes showing hierarchy, reader flow, expected content, and representative block types. Do not create cosmetic variants. Use Mermaid only when a real architecture or process benefits from it.
3. Let the user select one option or combine elements. Consolidate the choice before drafting.
4. Prepare one complete candidate outside the repository. Use no silent placeholders; include placeholders only with explicit approval.
5. Show the candidate and, for an update, a diff plus a summary of removals and semantic changes. Preserve intentional existing content unless the approved design supersedes it visibly.
6. Ask for explicit approval immediately before writing the primary README.
7. Write only the approved README, then show and validate the final diff.

## Validation

Check Markdown structure, heading anchors, relative links, code fences, platform compatibility, and consistency with repository facts. Run only safe, cheap commands needed to verify documented instructions. Do not install dependencies, access the network, or run mutating commands without separate permission. If external-link checking is unavailable, report it rather than claiming success.

Adapt the README language to its intended audience; do not automatically mirror the conversation language. Use CommonMark as the baseline and platform-specific extensions only when the detected host supports them.
