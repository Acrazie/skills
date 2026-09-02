---
name: skill-refiner-acrazie
description: Collect structured feedback while a user tests one target skill, preserve observations in an append-only journal, and consolidate approved behavioral decisions into a living ADR. Use only when the user explicitly invokes skill-refiner-acrazie for an interactive refinement campaign; do not edit the target skill.
---

# Skill Refiner / Acrazie

Run a temporary feedback campaign around one target skill. Observe how the target behaves during real use, preserve raw evidence in an append-only journal, and promote only user-approved findings into a living ADR.

Do not patch, rewrite, or otherwise modify the target `SKILL.md`. This skill documents what should be preserved or changed; a separate editing workflow may implement those decisions later.

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
- Interpret the score as adherence of the target skill’s behavior to the user’s intent, not as a generic quality score for the subject matter.
- Match the user’s language in all explanations and follow-ups.

## Artifacts

### Campaign journal

Write the active journal to:

```text
<target-skill>/.skill-improver/campaigns/<campaign-id>.json
```

Use an append-only event model. Never erase or silently rewrite an earlier event; append a correction event that points to it. Once closed, treat the journal as immutable.

Read `references/journal-schema.md` before creating or updating a journal. Record only minimal summaries and short evidence excerpts. Exclude secrets, credentials, personal data, and long copied passages; record that redaction occurred without reproducing the omitted value.

### Living ADR

After approval, update:

```text
<target-skill>/docs/decisions/ADR-skill-feedback.md
```

Read `templates/ADR-skill-feedback.md` before drafting or updating the ADR. Preserve prior campaigns and superseded decisions. Keep the current consolidated state near the top and campaign history below it.

If the target directory is read-only, create both artifacts in an adjacent writable workspace. State their exact paths and say plainly that the ADR was not installed into the target skill.

## Campaign procedure

### 1. Start explicitly

1. Confirm that no other Refiner campaign is active in this conversation.
2. Resolve the target skill and read its `SKILL.md` without asking the user for discoverable filesystem facts.
3. Compute the SHA-256 digest of the exact `SKILL.md` bytes. This digest identifies the tested version; do not normalize or reformat the file first.
4. Create a unique campaign ID and initialize the journal with a `campaign_started` event.
5. Explain the scale once:
   - `1/5`: behavior contradicts the user’s intent;
   - `2/5`: major gaps;
   - `3/5`: partially conforms;
   - `4/5`: minor adjustment needed;
   - `5/5`: conforms to the user’s intent.
6. State that every score needs a comment, that `5/5` comments identify behavior to preserve, and that the user may say `passer` to skip an observation.

Do not create an upfront behavioral contract. The campaign learns the user’s intent from successive scored interactions.

**Start criterion:** the target path, starting digest, campaign ID, journal path, and active status are all recorded.

### 2. Observe a target-guided result

Before each target-guided final result:

1. Re-read the target `SKILL.md` and recompute its SHA-256 digest.
2. If it differs from the starting digest, do not mix evidence across versions. Append a `version_changed` event, pause the campaign, and offer to start a new campaign for the new digest.
3. If it matches, let the target skill finish the user’s task normally.
4. Append a `result_presented` event with a minimal request summary and result summary. Mark the observation as awaiting feedback.
5. Outside any produced artifact, append exactly:

```text
[Refiner] Note + commentaire : 4/5 — …
```

Do not put the footer inside a generated file, code block, JSON value, document, or other deliverable. If the response itself must be strictly machine-readable and cannot contain trailing text, defer the footer to the next conversational turn before processing another target-guided task.

**Observation criterion:** every eligible result has one stable observation ID and is either awaiting feedback, complete, corrected, or skipped.

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

If the user ignores a feedback request, continue their work. Remind them once at the next suitable conversational turn and offer `passer`. Never infer satisfaction from silence. If they pass, append `observation_skipped`.

If the user revises a prior score or comment, append `feedback_corrected` with the superseded event ID and keep both versions visible in the journal.

**Feedback criterion:** a complete observation has coherent score/comment evidence and, below 5, an explicit desired behavior.

### 4. Close only on request

Trigger closure when the user explicitly says “termine la campagne” or an unambiguous equivalent.

1. If an observation is still awaiting feedback, ask the user to score it or say `passer`. Do not block closure after that choice.
2. If there are no complete observations, append `campaign_closed` with status `insufficient_data`. Do not create or change ADR decisions.
3. Consolidate complete observations into candidate decisions. Every complete observation may support a candidate; do not impose an automatic minimum count.
4. Separate candidates into:
   - behavior to preserve;
   - behavior to change;
   - unresolved or contradictory evidence.
5. Show one concise decision table containing candidate ID, proposed decision, evidence strength, affected `SKILL.md` sections, alternatives, and consequences.
6. Expose contradictions and ask the user to resolve them. Never select the newest, harshest, or most frequent feedback automatically.
7. Ask for explicit approval of the consolidated table as a whole. Apply requested corrections and present the corrected table again when material meaning changed.
8. Only after approval, update the living ADR and append `decisions_approved` plus `campaign_closed` events.
9. Mark superseded ADR decisions as `superseded` and link each to its replacement. Never delete the old decision or history.

The ADR may identify affected sections and describe the intent of a future change. It must not contain or apply a patch to `SKILL.md`.

**Closure criterion:** the journal has a terminal status; every accepted ADR statement traces to complete observations; no unapproved decision is presented as settled.

## Interruption and continuity

Rely on the active harness conversation for ordinary pause, compaction, or resume behavior. Do not invent cross-conversation or cross-harness migration machinery. When context is compacted, recover campaign state from the recorded journal if the harness still points to the same conversation and target.

## Pitfalls

- **Contaminating the test:** advice from Refiner before the target acts changes the behavior being measured.
- **Scoring every assistant message:** only target-guided final results qualify.
- **Treating silence as approval:** skipped or missing feedback provides no evidence.
- **Over-questioning:** ask one rating/comment prompt, then only the necessary coherence or below-5 follow-up.
- **Mixing versions:** any digest change ends evidence collection for the original campaign.
- **Turning complaints into decisions:** observations become decisions only after closure synthesis and explicit approval.
- **Copying sensitive context:** evidence should be short, minimized, and redacted.
- **Claiming installation on a read-only target:** report the writable fallback path instead.

## Verification

Before reporting a campaign complete, verify:

- the target digest matches the tested version or the campaign ended with `version_changed`;
- every journal event has a unique ID and events remain in chronological order;
- corrections point to existing earlier events;
- every accepted decision cites one or more complete observation IDs;
- positive `5/5` evidence appears among behaviors to preserve when approved;
- unresolved contradictions are absent from settled decisions;
- the ADR keeps superseded decisions and campaign history;
- the target `SKILL.md` has not been modified by Skill Refiner;
- the final response gives exact journal and ADR paths.