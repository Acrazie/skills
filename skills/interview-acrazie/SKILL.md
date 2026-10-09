---
name: interview-acrazie
description: >-
  Clarify a task through a context-aware decision-tree interview and record an
  explicitly approved task contract. Use when a user requests clarification or
  another skill calls interview-acrazie to resolve user-owned decisions before
  execution. Not for implementation, technical audits, or replacing an existing
  specialist's interview.
---

# Interview / Acrazie

Turn an underspecified request into one concise, documented Task Contract that
another workflow can execute without guessing. Stay persistent about relevant
ambiguity, not exhaustive about hypothetical possibilities.

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

## Boundaries and reuse

- Work directly with the user. Do not create an orchestrator or require subagents.
- Clarify and document only. Do not implement, audit, scaffold, choose a
  single-agent/multi-agent architecture, install dependencies, or ship Git changes.
- A caller supplies the objective, scope, relevant context, decisions needed, and
  expected handoff. If these are missing, discover facts and ask about intent.
- Preserve the caller's narrower scope, write restrictions, and approval gates.
  Calling this skill never grants permissions the caller lacks.
- Reuse an existing specialist's settled decisions and interview; do not restart
  it or take ownership of its domain-specific design work.
- Write instructions in English; interview and task documents in the user's
  language unless the repository requires another documentation language.

## Discover facts first

Read repository instructions, relevant specs/tickets, glossary, decision records,
and the smallest useful set of files, tests, or configuration. Distinguish verified
facts from preferences and missing evidence. Do not ask the user for facts you can
inspect safely. If discovery is unavailable, disclose the gap rather than invent
an answer or treat it as a user preference. Never copy credentials into documents.

Check for an existing Task Contract. Reuse it without another interview or approval
when explicit approval is evidenced, it still covers the requested task, and no
material discovery contradicts it. A status label alone is not approval evidence.
If stale or incomplete, reopen only affected branches.

## Interview the decision frontier

Maintain a small decision tree. The frontier contains unresolved decisions whose
prerequisites are settled; ask the whole current frontier in one round.

1. Group related decisions; each displayed question has only the following four
   fields. Translate the four labels and content into the user's language. Keep
   options numbered and give one recommendation with a short context-specific
   reason. Do not add question IDs, titles, decision fields or a fixed questionnaire.
   A recommendation is not a selected answer or approval.

```text
Current state: <verified context and the unresolved decision>
Options:
1. <choice and consequence>
2. <alternative and consequence>
Recommendation: option <N> — <reason>.
Response: <await the user's choice; do not fill it in for them>
```

2. Never ask a dependent question before its unresolved prerequisite is answered.
3. After each response, record accepted decisions and recompute the frontier.
   A batch acceptance settles the recommendations it actually refers to.
4. Keep asking until all relevant branches are resolved, explicitly excluded, or
   blocked by disclosed factual gaps. No arbitrary round limit or speculative
   branches. Never silently select a material user-facing, scope, data, security,
   billing, or hard-to-reverse choice.
5. Leave ordinary internal implementation choices to the executor under repository
   conventions. Do not force a user to design code to clarify desired behavior.

When intent is clear, summarize the objective, included/excluded work, observable
success criteria, accepted decisions, and planned evidence. Ask for one explicit
approval of this complete contract, including its document destination. Prior
answers to individual questions are not approval of the final contract. If factual
gaps prevent executable criteria or safe scope, present a blocked draft and stop.

## Record and hand off

Read [references/task-contract.md](references/task-contract.md) for the shared
contract format and approval/reuse rules.

- Reuse the project's equivalent spec/ticket convention, without overwriting an
  unrelated or generated document. Otherwise use `docs/specs/<subject>.md`.
  If a ticket cannot hold a persisted contract here, link it from that file.
- Record every completed interview's approved contract. Keep it short; add no
  journal, process framework, or duplicate spec. If writing is forbidden, show the
  proposed contract and stop until authorized persistence is available; do not
  claim it is saved or proceed as though the constraint disappeared.
- If a project-specific term is resolved, update the existing glossary (or create
  `CONTEXT.md`) within authorized scope. Keep it a glossary, not an implementation
  plan. Do not add generic programming definitions.
- Create an ADR only for an approved, costly-to-reverse, non-obvious decision with
  real alternatives. Use the repository's convention or `docs/adr/` with the next
  unused number. Never turn every task contract into an ADR.
- Return the same contract path, approval evidence, relevant glossary/ADR links,
  blocked conditions, and the responsible specialist. Separate outcome approval
  from any explicit authorization to resume scoped realization. Stop here; this
  skill never implements or activates its caller. In an explicit project kit,
  request a new explicit invocation of the specialist to resume, even if it was
  active before the interview. Preserve answers and the approved contract rather
  than restarting the interview. Neither handoff nor outcome approval grants
  deployment, installation, spawning or Git shipping permissions.
