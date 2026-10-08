import { describe, expect, test } from 'bun:test';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('../../', import.meta.url));
const read = (file: string) => readFileSync(`${root}${file}`, 'utf8');
const ids = [
  'diagnostic-queue-runner-acrazie',
  'feature-builder-acrazie',
  'repository-readme-architect-acrazie',
  'mechanical-port-acrazie',
  'multi-agent-planner-acrazie',
];
const section = (id: string) => read(`skills/${id}/SKILL.md`)
  .split('## Subagent model selection\n')[1]?.split('\n## ')[0]?.trim();

// Static instruction-contract checks, not live model-routing evaluations.
describe('portable subagent model selection', () => {
  for (const id of ids) {
    test(`${id} embeds the complete portable selection gate`, () => {
      const policy = section(id);
      expect(policy).toBeDefined();
      for (const rule of [
        'Verify available models',
        'Propose 2–3 verified options',
        'exactly one recommended option',
        'Prefer an economical model when sufficient',
        'never apply a fixed two-tier downgrade',
        'If fewer options are verified, show only those',
        'If no selectable option can be verified, ask',
        'Wait for explicit user validation before spawning',
        'same role, bounded mission/scope, risk level, and selected model',
        'role, mission/scope, risk level, or model changes',
        'unavailable or model selection is unsupported or unverifiable, stop and ask',
        'Never silently inherit, substitute, or claim an override',
        'does not authorize delegation',
        'fresh-context reviewer isolation',
        'actual model if the runtime reports it',
        'If the runtime reports a different model, stop the lot and ask',
      ]) expect(policy).toContain(rule);
      expect(policy).not.toMatch(/gpt-|claude-|gemini-|spawn_agent\(/i);
    });
  }

  test('standalone installations carry the same policy without a shared-file dependency', () => {
    const policies = ids.map(section);
    expect(policies[0]).toBeDefined();
    for (const policy of policies) expect(policy).toEqual(policies[0]);
  });

  test('execution sites link the gate without relaxing ownership', () => {
    expect(read('skills/diagnostic-queue-runner-acrazie/SKILL.md')).toContain('Approve separate worker and reviewer lots');
    const builder = read('skills/feature-builder-acrazie/SKILL.md');
    expect(builder).toContain('Validate the reviewer lot');
    expect(builder).toContain('fresh agent context without inherited conversation');
    expect(read('skills/repository-readme-architect-acrazie/SKILL.md')).toContain('Before optional delegation');
    expect(read('skills/mechanical-port-acrazie/SKILL.md')).toContain('A same-context skill handoff is not a spawn');
  });

  test('planner carries a pending gate into prompts without executing or bypassing it', () => {
    const planner = read('skills/multi-agent-planner-acrazie/SKILL.md');
    expect(planner).toContain('never spawns workers itself');
    expect(planner).toContain('fast path does not waive model validation');
    expect(planner).toContain('Lot identity, model options/recommendation, and validation status');
    const platforms = read('skills/multi-agent-planner-acrazie/references/platforms.md');
    expect(platforms).toContain('revalidate available models and override support');
    expect(platforms).toContain('Do not assume an alias or model identifier transfers');
  });
});
