---
name: audit-repository-acrazie
description: >-
  Audit a precise technical decision, integration, subsystem, or choice of library,
  framework, or development tool before adoption in one existing repository. Use
  when the task needs a bounded technical assessment before a decision; not for general
  repository audits, diff or PR review, security audits, documentation audits,
  multi-repository analysis, or external-service selection.
---

# Audit Repository / Acrazie

Audit the question the user actually needs answered. Find material adjacent evidence without turning the task into a general repository health check. Evidence and decision usefulness outrank finding count.

## Project loading boundary

Published-library defaults remain model-invocable within the requested task. An
explicit project kit or stricter current instruction takes precedence: propose
this skill from available metadata and wait for the user's explicit command before
reading its instructions. Apply the same gate to each dependency before reading
or dispatching its instructions; one invocation does not activate a chain.
Use `$skill-name` in Codex or `/skill-name` in Claude Code. These gates are not
filesystem access controls or proof of live host behavior. Global homonyms may
remain a blocker. Do not read an unactivated skill or delegate its body as a bypass.
Loading grants no investigation, writing, installation, spawning or shipping
authority beyond the separately approved scope. Ordinary library defaults retain
scoped implicit handoffs; this audit introduces no mandatory skill dependency.

## Entry and authorization

Select this skill when a bounded technical assessment is requested or necessary to answer the current task. Under published defaults no named skill command is required; the project loading boundary governs explicit kits. Inspect relevant facts read-only; do not turn an unrelated task into an audit. Selection does not approve deep investigation, record writes, or implementation; preserve the scope and approval gates below.

## User decision format

For any user-owned choice, display only Current state, numbered Options,
Recommendation and Response. Translate labels/content into the user's language;
do not add question IDs, preselect an answer as consent or treat a recommendation
as approval. This format governs scope, record lifecycle and write choices, not
the report structure. Keep the specialist interview below; do not duplicate it
through another skill.

## Scope and invariants

- Audit one existing repository, or one subsystem inside it, per invocation.
- Require a precise question, decision, integration, tool, stack choice, or subsystem. Never perform a general audit. When the request is vague, inspect enough to offer concrete audit angles, then let the user choose.
- Cover relevant architecture, stack fit, framework or language integration, dependencies, tooling, tests, CI/CD, performance, operations, maintainability, complexity, and unnecessary elements.
- For adoption decisions, compare libraries, frameworks, and development tools against actual project needs, including retaining the current approach or adding no dependency. External-service selection is excluded: an SDK's size does not establish its provider's suitability, pricing, data handling, or availability.
- Do not review a diff or PR, audit security, audit documentation quality, or analyze multiple repositories.
- Documentation may serve as factual evidence. If an obvious committed secret or critical vulnerability appears incidentally, report it briefly and recommend a dedicated security audit; do not expand into one.
- Keep investigation read-only. Do not install, update, reconfigure, fix, commit, or push. The only allowed write path is an approved final Audit Record under `docs/audits/` as described below.
- Never expose secrets. Quote only evidence needed to support a conclusion.

## Inspect before interviewing

Read repository instructions first. Determine facts the environment can answer: repository root, current Git state and commit, target subsystem, manifests and lockfiles, runtime and framework versions, relevant configuration, scripts, tests, CI, call sites, and existing conventions.

Inspect `docs/audits/` and equivalent decision or audit directories before starting new work. Read [references/audit-record.md](references/audit-record.md) for overlap handling and lifecycle rules. Do not ask the user to rediscover repository facts.

## Establish the audit contract

Reuse an explicitly approved audit contract, including an existing task record or
conversation agreement, when it covers the current question, scope, exclusions,
criteria and permitted validations with approval evidence beyond a status label.
Recheck material repository facts and evidence freshness before relying on it.
Do not repeat an applicable approved shared-understanding checkpoint or create a
second contract for ceremony. If new evidence invalidates it, reopen only affected
decisions through this skill's specialist interview. Contract reuse grants neither
record-write permission nor implementation, installation or shipping authority.

Read [references/interview-tree.md](references/interview-tree.md). Ask only unresolved user-owned decisions whose prerequisites are settled. Normally one compact round is enough; ask another only when an answer exposes a material unresolved branch.

When the frontier is empty, summarize the audit question, scope, exclusions, decision criteria, and relevant existing Audit Records. Get explicit confirmation before deep investigation unless applicable independent approval evidence already covers that exact investigation.

## Investigate

Read [references/audit-method.md](references/audit-method.md) and follow its evidence, comparison, materiality, and validation rules.

For dependency or tool selection, apply its adoption criteria and cost/utility rules. Recommend rather than integrate; this workflow grants no installation or implementation authority.

Keep the user's question central. Expand automatically when a discovered signal can change the requested decision, invalidate an assumption, reveal a likely root cause, or show a material impact. Ask before expanding into a different objective or subsystem. Otherwise record one concise out-of-scope lead and offer a separate audit.

Do not impose time, token, file, candidate, or finding budgets. Never abandon a relevant material branch because it is large. Stop when relevant branches are resolved, explicitly excluded, or blocked by disclosed evidence gaps. Use the smallest sufficient proof for each claim.

## Report

Present:

1. audit question and scope;
2. compact verdict;
3. directly relevant findings, ordered as `Décisif`, `Matériel`, then `À considérer`;
4. alternatives compared when relevant;
5. elements worth keeping;
6. concise out-of-scope leads;
7. validations performed, evidence gaps, and residual uncertainty;
8. confirmed decisions and recommended next decision.

Write the report in the user's language and translate these labels when needed. For each finding give priority, confidence, evidence, concrete impact, recommendation, and implementation effort. Never convert a possibility into a finding. Do not recommend churn merely because an alternative is newer or more popular.

## Record the audit

After the user validates the report, offer to create or update one Audit Record. Show the proposed record and ask for explicit approval immediately before writing.

Use `docs/audits/`; create `docs/` and `docs/audits/` after approval when absent. If the repository already has an equivalent convention, present it and ask before using a path other than `docs/audits/`. Follow [references/audit-record.md](references/audit-record.md).

Record recommendations as decisions only after the user accepts them. Never commit the record.

For adoption, identify the accepted option and any unresolved conditions before handoff to an implementation task. Link the approved Audit Record from that task's contract when applicable; do not edit the contract under audit authority. The audit retains its specialist interview, does not automatically invoke another skill, and does not authorize implementation. An ADR is a separate, explicitly approved activity only when a durable architectural trade-off warrants one.
