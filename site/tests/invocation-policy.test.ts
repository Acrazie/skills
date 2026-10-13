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
    expect(readSkill('interview-acrazie')).toMatch(/this\s+skill never implements/);
    expect(readSkill('audit-repository-acrazie')).toContain('Keep investigation read-only');
    expect(readSkill('test-retrofitter-acrazie')).toContain('No implementation begins without applicable explicit approval evidence');
    expect(readSkill('product-critic-acrazie')).toContain('Report approval never authorizes implementation');
    expect(readSkill('multi-agent-planner-acrazie')).toContain('never spawns workers itself');
    expect(readSkill('mechanical-port-acrazie')).toContain('already exists and passes against the source codebase');
    expect(readSkill('mechanical-port-acrazie')).toContain('Obtain authorization for that prerequisite testing work');
    expect(readSkill('repo-modernizer-acrazie')).toContain('obtain separate explicit confirmation before destructive rollback');
    expect(readSkill('repo-modernizer-acrazie')).not.toContain('Run `git reset --hard HEAD`');
    expect(readSkill('ci-cd-acrazie')).toContain('No implicit');
    expect(readSkill('ci-cd-acrazie')).toContain('Masking is not isolation');
    expect(readSkill('ci-cd-acrazie')).toContain('Never invent build');
  });

  test('localized catalogues show the same single explicit-only exception', () => {
    for (const locale of ['en', 'fr', 'zh'] as const) {
      const localized = getLocalizedSkills(locale);
      expect(localized.filter(skill => skill.disableModelInvocation).map(skill => skill.id)).toEqual(['skill-refiner-acrazie']);
      expect(localized.find(skill => skill.id === 'audit-repository-acrazie')?.description).not.toMatch(/use only when|invocation explicite|仅在显式调用/i);
    }
  });
});


describe('single repository CI/CD owner', () => {
  test('catalogue replaces six packages with one correctly categorized owner', () => {
    expect(skills.filter(skill => skill.id.startsWith('jenkins-'))).toHaveLength(0);
    const owner = skills.find(skill => skill.id === 'ci-cd-acrazie');
    expect(owner).toBeDefined();
    expect(owner!.category).toBe('CI/CD & DevOps');
    expect(owner!.disableModelInvocation).toBe(false);
    expect(owner!.installCommand).toContain('ci-cd-acrazie');
    expect(owner!.references.some(ref => ref.name === 'stack-evidence.md')).toBe(true);
  });
  test('all locales disclose cross-tool ownership and separate operations', () => {
    for (const locale of ['en', 'fr', 'zh'] as const) {
      const local = getLocalizedSkills(locale);
      expect(local.filter(skill => skill.id.startsWith('jenkins-'))).toHaveLength(0);
      const owner = local.find(skill => skill.id === 'ci-cd-acrazie');
      expect(owner).toBeDefined();
      expect(owner!.description.length).toBeGreaterThan(50);
      expect(owner!.description).toMatch(/authorization|autorisations|授权/);
    }
  });
});

// Static catalogue and ownership proof, not runtime portability certification.
describe('generic execution retirement', () => {
  test('all locales omit retired packages and expose assessment, not refactoring', () => {
    for (const locale of ['en', 'fr', 'zh'] as const) {
      const local = getLocalizedSkills(locale);
      for (const id of ['feature-builder-acrazie', 'script-portability-acrazie']) {
        expect(local.some(skill => skill.id === id)).toBe(false);
      }
      const owner = local.find(skill => skill.id === 'audit-repository-acrazie')!;
      expect(owner.description).toMatch(/read-only|lecture seule|只读/);
      expect(owner.description).toMatch(/separately authorized|séparément autorisé|另行授权/);
      expect(owner.references.some(ref => ref.name === 'script-portability.md')).toBe(true);
    }
  });
});
