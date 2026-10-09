import { describe, expect, test } from 'bun:test';
import fs from 'node:fs';
import path from 'node:path';
import matter from 'gray-matter';
import { getAllSkills, getLocalizedSkills, getRepoRoot } from '../src/lib/skills';

const skills = getAllSkills();
const readSkill = (id: string) => fs.readFileSync(path.join(getRepoRoot(), 'skills', id, 'SKILL.md'), 'utf8');

describe('skill invocation policy', () => {
  test('all skills synchronize frontmatter and Codex invocation metadata', () => {
    expect(skills.length).toBeGreaterThan(0);
    for (const skill of skills) {
      const frontmatter = matter(readSkill(skill.id)).data;
      const yaml = fs.readFileSync(path.join(getRepoRoot(), 'skills', skill.id, 'agents/openai.yaml'), 'utf8');
      const metadata = matter(`---\n${yaml}\n---\n`).data;
      const disabled = frontmatter['disable-model-invocation'];
      const implicit = metadata.policy?.allow_implicit_invocation;
      expect(disabled === undefined || typeof disabled === 'boolean').toBe(true);
      expect(implicit === undefined || typeof implicit === 'boolean').toBe(true);
      expect({ id: skill.id, disabled: disabled === true }).toEqual({ id: skill.id, disabled: implicit === false });
    }
  });

  test('only the persistent Refiner campaign requires explicit skill invocation', () => {
    expect(skills.filter(skill => skill.disableModelInvocation).map(skill => skill.id)).toEqual(['skill-refiner-acrazie']);
  });

  test('model-invocable skills no longer demand a skill command', () => {
    for (const skill of skills.filter(skill => !skill.disableModelInvocation)) {
      expect(skill.description).not.toMatch(/use only when.*invok|invoke explicitly/i);
      expect(skill.content).not.toMatch(/run only after explicit (human|user) invocation|if activated implicitly|if the harness activates this skill implicitly|run only when the user explicitly invokes/i);
    }
    expect(readSkill('skill-refiner-acrazie')).toContain('disable-model-invocation: true');
  });

  test('selection does not remove action, contract, or ownership gates', () => {
    const gitShip = readSkill('git-ship-acrazie');
    expect(gitShip).toMatch(/Before delivery mutations, present\s+one consolidated recap and obtain explicit approval/);
    expect(gitShip).toContain('Do not commit before the delivery recap.');
    expect(gitShip).toContain('Execute only approved steps with boundary checks');
    expect(readSkill('github-repo-init-acrazie')).toContain('blueprint approval alone is not publication approval');
    expect(readSkill('feature-builder-acrazie')).toContain('Approval of the feature contract allows scoped implementation');
    expect(readSkill('test-retrofitter-acrazie')).toContain('No implementation begins without applicable explicit approval evidence');
    expect(readSkill('product-critic-acrazie')).toContain('Report approval never authorizes implementation');
    expect(readSkill('multi-agent-planner-acrazie')).toContain('never spawns workers itself');
    expect(readSkill('mechanical-port-acrazie')).toContain('already exists and passes against the source codebase');
    expect(readSkill('mechanical-port-acrazie')).toContain('Obtain authorization for that prerequisite testing work');
    expect(readSkill('repo-modernizer-acrazie')).toContain('obtain separate explicit confirmation before destructive rollback');
    expect(readSkill('repo-modernizer-acrazie')).not.toContain('Run `git reset --hard HEAD`');
    for (const stack of ['go', 'js-ts', 'python', 'rust']) {
      expect(readSkill(`jenkins-${stack}-acrazie`)).toContain('Work strictly in read-only analysis mode');
    }
  });

  test('localized catalogues show the same single explicit-only exception', () => {
    for (const locale of ['en', 'fr', 'zh'] as const) {
      const localized = getLocalizedSkills(locale);
      expect(localized.filter(skill => skill.disableModelInvocation).map(skill => skill.id)).toEqual(['skill-refiner-acrazie']);
      expect(localized.find(skill => skill.id === 'audit-repository-acrazie')?.description).not.toMatch(/use only when|invocation explicite|仅在显式调用/i);
    }
  });
});
