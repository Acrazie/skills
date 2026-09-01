---
name: audit-repository-acrazie
description: Audit a precise technical decision, integration, tool, stack choice, or subsystem in one existing repository. Use only when the user explicitly invokes audit-repository-acrazie; not for general repository audits, diff or PR review, security audits, documentation audits, or multi-repository analysis.
---

# Audit Repository / Acrazie

Audit the question the user actually needs answered. Find material adjacent evidence without turning the task into a general repository health check. Evidence and decision usefulness outrank finding count.

## Invocation guard

Run only after explicit user invocation. If the harness activates this skill implicitly, do not start an audit; ask the user to invoke `$audit-repository-acrazie` (or the platform-equivalent explicit command).

## Scope and invariants

- Audit one existing repository, or one subsystem inside it, per invocation.
- Require a precise question, decision, integration, tool, stack choice, or subsystem. Never perform a general audit. When the request is vague, inspect enough to offer concrete audit angles, then let the user choose.
- Cover relevant architecture, stack fit, framework or language integration, dependencies, tooling, tests, CI/CD, performance, operations, maintainability, complexity, and unnecessary elements.
- Do not review a diff or PR, audit security, audit documentation quality, or analyze multiple repositories.
- Documentation may serve as factual evidence. If an obvious committed secret or critical vulnerability appears incidentally, report it briefly and recommend a dedicated security audit; do not expand into one.
- Keep investigation read-only. Do not install, update, reconfigure, fix, commit, or push. The only allowed write path is an approved final Audit Record under `docs/audits/` as described below.
- Never expose secrets. Quote only evidence needed to support a conclusion.

## Inspect before interviewing

Read repository instructions first. Determine facts the environment can answer: repository root, current Git state and commit, target subsystem, manifests and lockfiles, runtime and framework versions, relevant configuration, scripts, tests, CI, call sites, and existing conventions.

Inspect `docs/audits/` and equivalent decision or audit directories before starting new work. Read [references/audit-record.md](references/audit-record.md) for overlap handling and lifecycle rules. Do not ask the user to rediscover repository facts.

## Establish the audit contract

Read [references/interview-tree.md](references/interview-tree.md). Ask only unresolved user-owned decisions whose prerequisites are settled. Normally one compact round is enough; ask another only when an answer exposes a material unresolved branch.

When the frontier is empty, summarize the audit question, scope, exclusions, decision criteria, and relevant existing Audit Records. Get explicit confirmation before deep investigation.

## Investigate

Read [references/audit-method.md](references/audit-method.md) and follow its evidence, comparison, materiality, and validation rules.

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
