# Campaign journal schema

Use one JSON object with an append-only `events` array. During an active campaign, adding an event means appending a new object to the array; do not mutate older event objects.

## Top-level shape

```json
{
  "schema_version": "1.0",
  "campaign_id": "<unique-id>",
  "target_skill": {
    "name": "<skill-name>",
    "directory": "<resolved-path>",
    "skill_md": "<resolved-path>/SKILL.md",
    "sha256": "<64 lowercase hexadecimal characters>"
  },
  "status": "active",
  "events": []
}
```

Allowed terminal statuses are `closed`, `insufficient_data`, and `version_changed`. `paused` is non-terminal.

## Common event fields

Every event contains:

```json
{
  "event_id": "evt-0001",
  "type": "campaign_started",
  "recorded_at": "<ISO-8601 timestamp>",
  "observation_id": null,
  "data": {}
}
```

- Keep `event_id` unique and monotonically increasing.
- Use one stable `observation_id`, such as `obs-0001`, across all events about the same result.
- Keep events in recording order.
- Store summaries, not full prompts or outputs.
- Replace sensitive content with a marker such as `[REDACTED: credential]` and list redaction categories in `data.redactions`.

## Event types

### `campaign_started`

Record the target digest, resolved paths, scale, and artifact destination.

### `result_presented`

```json
{
  "request_summary": "Short description of what the user asked",
  "result_summary": "Short description of the target-guided result",
  "feedback_state": "awaiting",
  "redactions": []
}
```

### `feedback_recorded`

```json
{
  "score": 4,
  "comment_excerpt": "Short, minimally sufficient quotation",
  "comment_summary": "Neutral summary of the feedback",
  "coherent": true,
  "behavior_to_preserve": null,
  "affected_skill_sections": ["Procedure > Step 3"],
  "redactions": []
}
```

For `5/5`, populate `behavior_to_preserve` from the mandatory comment.

### `ideal_behavior_added`

Use for scores below 5 when the desired state needs its own event:

```json
{
  "source_feedback_event_id": "evt-0003",
  "ideal_behavior": "What would make the behavior conform at 5/5",
  "affected_skill_sections": ["Output format"]
}
```

### `feedback_corrected`

```json
{
  "supersedes_event_id": "evt-0003",
  "score": 3,
  "comment_excerpt": "Corrected short quotation",
  "comment_summary": "Corrected neutral summary",
  "reason": "User corrected the prior observation"
}
```

Never remove the superseded event.

### `observation_skipped`

Record why feedback is absent. A skipped observation cannot support an ADR decision.

### `version_changed`

Record both the starting digest and newly observed digest. Stop collecting evidence for this campaign.

### `decisions_approved`

```json
{
  "decision_ids": ["DEC-001"],
  "approval_summary": "User explicitly approved the consolidated table",
  "evidence_observation_ids": ["obs-0001"]
}
```

### `campaign_closed`

Record final status, counts of complete/skipped observations, approved decision IDs, ADR path if written, and whether the artifact was installed in the target or written to a fallback workspace.

## Validity rules

A complete observation has:

1. one `result_presented` event;
2. a current, non-superseded score from 1 through 5;
3. a substantive comment coherent with the score;
4. for scores below 5, an explicit ideal behavior, either in the feedback itself or in `ideal_behavior_added`.

Only complete observations may support candidate or accepted decisions.