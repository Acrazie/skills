# Skill Selection and Action Authorization

Published-library defaults keep skills model-invocable within the current requested
task. Under those defaults a clear natural-language request is enough; users do not
need to know a skill's name.
Selecting or reading a skill is not approval of its scope or authorization of its
actions. Skill instructions never override applicable user/repository rules,
tool permissions, or approval requirements.

## Explicit project kits and stricter instructions

An explicit project kit or stricter current instruction overrides the permissive
published defaults for that task. Propose names from available metadata; wait for
the user's explicit skill command before reading its body. Apply this gate to each
dependency and to the returning specialist after Interview. Do not use implicit
handoffs, manually read an unactivated skill, or dispatch its instructions to a
subagent as a bypass. Contract/review approval is not a skill command.

Project adapters may set both explicit-only metadata flags on installed copies;
this does not change published-library metadata or global installations. Native
flags and instruction tests are not filesystem controls or live host proof.
Unresolved implicitly invocable global homonyms block a strict gate claim.
Installation, scoped realization, agent spawning/model choice and shipping retain
their separate permissions. An absent dependency blocks only its dependent step;
an applicable approved contract can satisfy Interview's result without loading it.

## Model-invocable specialists

- In `SKILL.md` frontmatter, omit `disable-model-invocation`.
- In `agents/openai.yaml`, set `policy.allow_implicit_invocation: true` or omit it
  (the default is `true`).
- Descriptions must state matching tasks and exclusions, not require a named
  command. Existing owners retain their specialist scope and approval gates.
- Read-only discovery may begin when relevant to the authorized task. Do not
  launch new objectives, unrelated audits, modernization programs, long interviews,
  or costly campaigns merely because a skill is available.
- A scoped inter-skill handoff may select its responsible specialist without a
  named command. It does not expand the authorized objective or bypass the
  recipient's contract, write, installation, or execution gates.
- Restricted actions, shipping, sensitive settings, paid services, destructive
  recovery, production changes, and agent spawning still follow their applicable
  permissions. Do not infer authorization from skill selection or plan approval.

Examples: a requested Jenkins pipeline task may load a read-only stack specialist;
"publish these changes" may select `git-ship-acrazie` for preparation, but its
delivery recap and confirmation remain required. "Implement this feature" does
not request a multi-agent planning interview or authorize spawning agents.

## Explicit-only exception: Skill Refiner

Only `skill-refiner-acrazie` remains explicit-only. It starts a persistent feedback
campaign with an append-only journal and indicators on subsequent messages. A
complaint about another skill is not consent to start that campaign. An agent may
offer refinement, but the user must deliberately activate Refiner.

Synchronize both declarations:

```yaml
# SKILL.md frontmatter
disable-model-invocation: true
```

```yaml
# agents/openai.yaml
policy:
  allow_implicit_invocation: false
```

Do not emulate an implicit Refiner campaign by manually reading its instructions.
Explicit activation still does not grant permission to edit the target skill.

## Consistency and verification

For every published skill, `disable-model-invocation: true` must be equivalent to
`policy.allow_implicit_invocation: false`; missing fields mean model invocation
is allowed. Validate metadata as YAML and keep entry instructions and localized
catalog descriptions consistent. Do not confuse a synchronized flag with proof
that a host actually selects the skill correctly.

`cd site && bun run test:invocation` checks metadata parity, the single exception,
stale command-only entry guards, representative retained approval boundaries, and
localized catalog flags. CI runs this check before building the site. These are
static regression checks, not live cross-harness triggering evaluations.

Approved rationale: [ADR 0006](../docs/adr/0006-separate-skill-selection-from-action-authorization.md).
Task scope and evidence: [invocation policy contract](../docs/specs/skill-invocation-policy.md).
Codex semantics: [official OpenAI documentation](https://learn.chatgpt.com/docs/build-skills).
