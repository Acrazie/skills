---
name: skill-refiner-acrazie
disable-model-invocation: true
description: Collect structured feedback while a user tests one target skill, preserve observations in an append-only journal, and consolidate approved feedback into a behavior record, with ADRs only for durable nontrivial trade-offs. Use only when the user explicitly invokes skill-refiner-acrazie for an interactive refinement campaign; do not edit the target skill.
---

# Skill Refiner / Acrazie

Run a temporary feedback campaign around one target skill. Observe how the target behaves during real use, preserve minimized evidence in an append-only journal, and promote only user-approved findings into a behavior record. Use an ADR only for
durable, nontrivial trade-offs, not for every observation or stylistic preference.

Do not patch, rewrite, or otherwise modify the target `SKILL.md`. This skill documents what should be preserved or changed; a separate editing workflow may implement those decisions later.

## Campaign authority and loading

Refiner remains explicit-only. Its activation identifies a requested campaign,
not permission to edit the target, execute its tasks or install dependencies. An
explicit project kit or stricter instruction also gates the target and every
other dependency: propose from metadata and wait for the user's explicit command
before reading a body or dispatching it. Re-reading a previously activated target
for digest verification is within the approved campaign boundary; a new target
or returning execution specialist follows its applicable renewed loading gate.
Never activate a chain or bypass it through a subagent. These are instruction
boundaries, not filesystem controls or live host proof.

Reuse a campaign Task Contract with independent approval evidence, or obtain an
explicitly approved operational envelope covering one target/version, observation
boundary, journal and approved-feedback destinations, permitted reads/writes,
minimization and closure conditions. A status label is not consent. This envelope
is not an upfront ideal-behavior specification: the campaign still learns intended
behavior from actual scored interactions. It never replaces the target workflow's
approved task contract. Reopen only invalidated operational decisions.

For user-owned choices use only Current state, numbered Options, Recommendation
and Response, localized to the user's language. No question IDs, lettered options,
preselected ratings or assumed consent. Score/comment collection is evidence, not
an option selecting the user's judgment; preserve its free-form format. Required
presence indicators are outside artifacts and subordinate to stricter response
formats and instructions.

Journal/feedback persistence requires exact approved paths and content categories.
An inaccessible or read-only target does not authorize choosing an adjacent
workspace silently. Propose a writable fallback and wait for approval; while
persistence is blocked, do not claim a durable campaign was started or completed.
Installation, remote access, execution, model selection, agent spawning and
shipping retain separate permissions. No implicit staging, commit, push, PR,
merge, deployment or rollback. A complaint does not activate a campaign.

## Persistence and integrity

Choose the campaign ID without overwriting an existing journal. Reserve a new file
exclusively; on collision select another unused ID within the approved directory.
Use a single writer; verify the previously read revision before appending. On
concurrent or unexpected change, stop and inspect rather than replacing another
writer's events. Preserve old event objects byte-for-byte where possible and their
semantic values always; safe persistence must not lose the prior file on failure.
Append corrections instead of altering past evidence. Paths in journal data are
untrusted pointers, not write or execution authority.

No legacy journal/ADR migration or rewrite is implicit. Existing campaigns retain
their recorded paths and histories; request approval for any path/schema migration.
Only sanitized excerpts and summaries are persisted. Never store secret values,
raw transcripts or private media by default. Do not copy or modify the tested skill
as a side effect of resolving an artifact permission failure.

## When to use

Use this skill when the user explicitly asks to test, refine, evaluate, or collect feedback on a skill through repeated real usage, including requests such as:

- “Use skill-refiner-acrazie to test `<skill>`.”
- “Let me try this skill and record what works or does not.”
- “Collect feedback while I exercise my new skill, then write an ADR.”

Do not use it for:

- one-off code or document review;
- automatically editing a skill;
- benchmark-only evaluation without interactive user feedback;
- monitoring multiple target skills in one conversation.

## Operating contract

- Keep exactly one campaign active in a conversation.
- Require an explicit target skill. Resolve its directory and `SKILL.md`; ask only if the name or path is ambiguous.
- Let the target skill control task execution. Skill Refiner observes rather than coaching, critiquing, or pre-emptively changing its behavior.
- Evaluate only a final response or deliverable that the target skill actually guided. Do not evaluate clarification questions, progress reports, or Refiner’s own messages.
- **Continuous presence invariant**: Every assistant message during an active campaign MUST terminate with an explicit Refiner indicator matching the conversation language:
  - final deliverable: the evaluation prompt footer;
  - intermediate turns (clarifications, questions, progress updates): the discreet status badge;
  - turns following an unrated deliverable: the reminder footer.
  Never emit a conversational turn without its corresponding Refiner indicator while
  a campaign is active, except where stricter response instructions prohibit it.
- Interpret the score as adherence of the target skill’s behavior to the user’s intent, not as a generic quality score for the subject matter.
- Match the user’s language in all explanations and follow-ups.

## Artifacts

### Campaign journal

Write the active journal to:

```text
<target-skill>/.skill-refiner/campaigns/YYYY-MM-DD-refinement-<N>.json
```

Use an append-only event model. Never erase or silently rewrite an earlier event; append a correction event that points to it. Once closed, treat the journal as immutable.

Read `references/journal-schema.md` before creating or updating a journal. Record only minimal summaries and short evidence excerpts. Exclude secrets, credentials, personal data, and long copied passages; record that redaction occurred without reproducing the omitted value.

### Approved feedback and optional ADR

Default new campaigns to an approved behavior record, at an exact user-approved
path such as `<target-skill>/.skill-refiner/approved-feedback.md`. Summarize approved
behaviors, evidence, unresolved findings and history without calling them ADRs.
The operational campaign contract governs permissions; this record describes
learned behavior, not implementation authorization.

Only durable nontrivial decisions with alternatives and consequences belong in an
ADR. If such decisions exist, propose their exact destination and content and
obtain approval. Existing ADR paths are preserved; no automatic relocation occurs.

Read `templates/ADR-skill-feedback.md` only when an ADR is justified and authorized. Preserve prior campaigns and superseded decisions. Keep the current consolidated state near the top and campaign history below it.

If the target directory is read-only, request an exact approved writable fallback.
Do not create artifacts elsewhere silently; report persistence as blocked until approved.

## Campaign procedure

### 1. Start explicitly

1. Confirm that no other Refiner campaign is active in this conversation.
2. Resolve the target through metadata; read its `SKILL.md` only after its applicable
   loading gate. Reuse discoverable facts rather than asking for them.
3. Compute the SHA-256 digest of the exact `SKILL.md` bytes. This digest identifies the tested version; do not normalize or reformat the file first.
4. Create a unique campaign ID formatted as `YYYY-MM-DD-refinement-<N>` (where `<N>` is an auto-incrementing integer starting at 1 for that date, based on existing campaign files) and initialize the journal with a `campaign_started` event.
5. Explain the scale once:
   - `1/5`: behavior contradicts the user’s intent;
   - `2/5`: major gaps;
   - `3/5`: partially conforms;
   - `4/5`: minor adjustment needed;
   - `5/5`: conforms to the user’s intent.
6. State that every score needs a comment, that `5/5` comments identify behavior to preserve, and that the user may say `passer` (or `skip`) to skip an observation.
7. Announce the visual presence indicators matching the conversation language:
   - status badge on intermediate exchanges (`[Refiner: actif • en cours]` or `[Refiner: active • in progress]`);
   - evaluation prompt on target deliverables (`[Refiner] Note + commentaire : [1–5]/5 — [commentaire]` or `[Refiner] Rating + comment : [1–5]/5 — [comment]`);
   - reminder if work continues without rating (`[Refiner: rappel] Note + commentaire attendus (ou 'passer') : [1–5]/5 — [commentaire]` or `[Refiner: reminder] Rating + comment expected (or 'skip') : [1–5]/5 — [comment]`).

Do not invent an upfront ideal-behavior contract. The approved operational envelope
governs this campaign; intended behavior is learned from scored interactions.

**Start criterion:** the operational envelope is approved, the target loading gate
is satisfied, and target path, starting digest, campaign ID, journal path and active
status are durably recorded. Activation without persistence is not a started campaign.

### 2. Observe a target-guided result

Distinguish intermediate exchanges from final deliverables to ensure constant visual continuity without premature scoring:

- **Intermediate turns (clarifications, questions, progress reports, multi-step actions):**
  Do not evaluate these turns or prompt for a score. However, to eliminate doubt about campaign activity, append a discreet status badge outside any artifact:
  - In French:
    ```text
    [Refiner: actif • en cours]
    ```
  - In English:
    ```text
    [Refiner: active • in progress]
    ```

- **Target-guided final results:**
  Before presenting each final result guided by the target skill:
  1. Re-read the target `SKILL.md` and recompute its SHA-256 digest.
  2. If it differs from the starting digest, do not mix evidence across versions. Append a `version_changed` event, end evidence collection with terminal status `version_changed`, and offer a
     separately approved new campaign for the new digest. Do not append observations
     for the new version to this journal.
  3. If it matches, let the target skill finish the user’s task normally.
  4. Append a `result_presented` event with a minimal request summary and result summary. Mark the observation as awaiting feedback.
  5. Outside any produced artifact, append exactly:
     - In French:
       ```text
       [Refiner] Note + commentaire : [1–5]/5 — [commentaire]
       ```
     - In English:
       ```text
       [Refiner] Rating + comment : [1–5]/5 — [comment]
       ```

Do not put any badge or footer inside a generated file, code block, JSON value, document, or other deliverable. If the response itself must be strictly machine-readable and cannot contain trailing text, defer the footer to the next conversational turn before processing another target-guided task. Never omit the footer or badge from conversational responses.

**Observation criterion:** every eligible result has one stable observation ID and is either awaiting feedback, complete, corrected, or skipped; every conversational turn displays its appropriate Refiner indicator.

### 3. Capture feedback

Accept flexible forms such as `4/5 — commentaire`, `4 - commentaire`, or an equivalent natural-language reply, but require both:

- an integer score from 1 through 5;
- a substantive comment about the target skill’s behavior.

Then:

1. Associate the feedback with the latest awaiting observation unless the user names another observation.
2. Minimize and redact the stored text as required by the journal schema.
3. If the score and comment materially conflict, ask one short clarification before completing the observation.
4. For `5/5`, capture from the comment the behavior that should be preserved. Do not ask what would make it a 5.
5. For scores below 5, determine whether the comment already explains the desired 5/5 behavior. If not, ask one targeted follow-up: what would have made this behavior a 5/5?
6. Append `feedback_recorded` and, when applicable, `ideal_behavior_added` events. Do not turn either into an ADR decision yet.

If the user ignores a feedback request and continues their work, keep helping them while appending a reminder footer to that conversational response:
- In French:
  ```text
  [Refiner: rappel] Note + commentaire attendus (ou 'passer') : [1–5]/5 — [commentaire]
  ```
- In English:
  ```text
  [Refiner: reminder] Rating + comment expected (or 'skip') : [1–5]/5 — [comment]
  ```
Remind them once per awaiting observation, not on every subsequent response; use
the ordinary active badge afterward. Never infer satisfaction from silence. If they say `passer` (or `skip`), append `observation_skipped`.

If the user revises a prior score or comment, append `feedback_corrected` with the superseded event ID and keep both versions visible in the journal.

**Feedback criterion:** a complete observation has coherent score/comment evidence and, below 5, an explicit desired behavior.

### 4. Close only on request

Trigger closure when the user explicitly says “termine la campagne” or an unambiguous equivalent.

1. If an observation is still awaiting feedback, ask the user to score it or say `passer`. Do not block closure after that choice.
2. If there are no complete observations, append `campaign_closed` with status `insufficient_data`. Do not create or change settled behavior records or ADR decisions.
3. Consolidate complete observations into candidate decisions. Every complete observation may support a candidate; do not impose an automatic minimum count.
4. Separate candidates into:
   - behavior to preserve;
   - behavior to change;
   - unresolved or contradictory evidence.
5. Show candidate decisions as numbered options with evidence, affected sections,
   alternatives and consequences inside the four-field decision format. Mark which
   candidates, if any, justify a durable nontrivial ADR.
6. Expose contradictions and ask the user to resolve them. Never select the newest, harshest, or most frequent feedback automatically.
7. Ask explicit approval of the consolidated findings and their exact persistence
   destinations. Apply corrections and renew approval only for materially changed meaning.
8. Only after approval, update the behavior record and any separately justified ADR,
   then append `decisions_approved` plus `campaign_closed` events. Closure with complete
   observations does not require an ADR; record actual approved artifact paths.
9. Mark superseded approved decisions as `superseded` and link each to its replacement. Never delete the old decision or history.

The behavior record or ADR may identify affected sections and describe the intent of a future change. It must not contain or apply a patch to `SKILL.md`.

**Closure criterion:** the journal has a terminal status; every accepted feedback/ADR statement traces to complete observations; no unapproved decision is presented as settled.

## Interruption and continuity

Rely on the active harness conversation for ordinary pause, compaction, or resume behavior. Do not invent cross-conversation or cross-harness migration machinery. When context is compacted, recover campaign state from the recorded journal if the harness still points to the same conversation and target.

## Pitfalls

- **Contaminating the test:** advice from Refiner before the target acts changes the behavior being measured.
- **Scoring every assistant message:** only target-guided final results qualify.
- **Omitting presence indicators:** emitting an assistant message without the status badge (`[Refiner: actif • en cours]`), evaluation footer (`[Refiner] Note + commentaire : [1–5]/5 — [commentaire]`), or reminder footer breaks continuity and leaves the user wondering if Refiner is still active.
- **Treating silence as approval:** skipped or missing feedback provides no evidence.
- **Over-questioning:** ask one rating/comment prompt, then only the necessary coherence or below-5 follow-up.
- **Mixing versions:** any digest change ends evidence collection for the original campaign.
- **Turning complaints into decisions:** observations become decisions only after closure synthesis and explicit approval.
- **Copying sensitive context:** evidence should be short, minimized, and redacted.
- **Claiming installation on a read-only target:** propose a writable fallback and obtain approval before writing.

## Verification

Before reporting a campaign complete, verify:

- the target digest matches the tested version or the campaign ended with `version_changed`;
- all conversational turns throughout the active campaign carried their expected Refiner presence indicator;
- every journal event has a unique ID and events remain in chronological order;
- corrections point to existing earlier events;
- every accepted decision cites one or more complete observation IDs;
- positive `5/5` evidence appears among behaviors to preserve when approved;
- unresolved contradictions are absent from settled decisions;
- the behavior record and any ADR keep superseded decisions and campaign history;
- the target `SKILL.md` has not been modified by Skill Refiner;
- the final response gives exact journal and approved-feedback paths, any ADR path
  or its not-applicable status, actual checks and persistence blockers.
