// Static instruction regressions; these do not execute model/harness scenarios.
import { describe, expect, test } from 'bun:test';
import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve(import.meta.dir, '../..');
const names = ['interview-acrazie', 'repo-modernizer-acrazie'];
const read = (name: string, file = 'SKILL.md') => fs.readFileSync(path.join(root, 'skills', name, file), 'utf8');
const normalize = (text: string) => text.replace(/\s+/g, ' ');
const practice = read(names[0], 'references/portable-practice.md');

describe('portable skill pilot (static proof only)', () => {
  test('standalone copies agree and entrypoints require their local rules', () => {
    for (const name of names) {
      expect(read(name, 'references/portable-practice.md')).toEqual(practice);
      const entry = read(name);
      expect(entry).toContain('[references/portable-practice.md](references/portable-practice.md)');
      expect(normalize(entry)).toContain('before starting this workflow');
      expect(entry).toContain('These rules are local to this skill');
      // A copied package must not require a path outside its own directory.
      const directory = path.join(root, 'skills', name);
      for (const file of ['SKILL.md', ...fs.readdirSync(path.join(directory, 'references')).filter(f => f.endsWith('.md')).map(f => `references/${f}`)]) {
        for (const match of read(name, file).matchAll(/\]\(([^)#]+)(?:#[^)]*)?\)/g)) {
          if (match[1].includes('://')) continue;
          const resolved = path.resolve(directory, path.dirname(file), match[1]);
          expect(resolved.startsWith(directory + path.sep)).toBe(true);
          expect(fs.existsSync(resolved)).toBe(true);
        }
      }
    }
  });

  test('version-applicable documentation is required at use, not model memory', () => {
    const text = normalize(practice);
    for (const clause of [
      'At each execution, verify every changing technical fact used to decide or act',
      "project's version or the proposed target version, not automatically the latest version",
      'syntax, APIs, command flags/effects, compatibility, versions, and maintenance status',
      'Do not substitute model memory',
      'documentation is inaccessible or contradictory',
      'suspend only the dependent decision or action',
      'Continue independent work',
    ]) expect(text).toContain(clause);
    for (const label of ['Fact used', 'Source / locator', 'Version and applicability', 'Checked at', 'Status / limits', 'Dependent decision or action']) expect(practice).toContain(label);
  });

  test('choice template has only four fields, numbered options and one recommendation', () => {
    const template = practice.match(/```text\n([\s\S]*?)\n```/)![1];
    expect([...template.matchAll(/^([A-Za-z ]+):/gm)].map(match => match[1])).toEqual(['Current state', 'Options', 'Recommendation', 'Response']);
    expect([...template.matchAll(/^(\d+)\. /gm)].map(match => Number(match[1]))).toEqual([1, 2]);
    expect([...template.matchAll(/^Recommendation:/gm)]).toHaveLength(1);
    expect(template).toContain("Response: <await the user's choice; do not fill it in for them>");
    expect(normalize(practice)).toContain('exactly one recommendation with a short reason');
    expect(practice).toContain('do not prefill consent');
    expect(practice).toContain("Translate labels and content into the user's language");
  });

  test('completion preserves specialist outputs and scope of evidence', () => {
    for (const label of ['**Decisions:**', '**Evidence:**', '**Limits:**']) expect(practice).toContain(label);
    expect(normalize(practice)).toContain('alongside necessary domain-specific sections');
    expect(normalize(practice)).toContain('Expected checks remain pending');
    expect(normalize(practice)).toContain('never claim the latter from the former');
    expect(normalize(practice)).toContain('does not promise identical wording or results');
    expect(normalize(read('interview-acrazie'))).toContain('this skill never implements');
    expect(read('repo-modernizer-acrazie')).toContain('obtain separate explicit confirmation before destructive rollback');
  });

  test('references replace fixed targets and recipes with evidence-driven discovery', () => {
    const references = ['modernization-catalog.md', 'taxonomy-matrix.md', 'inspection-checklist.md', 'execution-protocol.md', 'commit-strategy.md', 'adr-template.md'];
    for (const file of references) {
      const text = read('repo-modernizer-acrazie', `references/${file}`);
      expect(text).toContain('[portable-practice.md](portable-practice.md)');
      expect(text).not.toMatch(/x25|x50|x100|Node < 20|Python < 3\.10|actions\/checkout@v4|uv add \$\(|EOL proche/);
    }
    const catalog = read('repo-modernizer-acrazie', 'references/modernization-catalog.md');
    expect(catalog).toContain('Keeping the incumbent is a valid recommendation');
    expect(catalog).not.toContain('```bash');
    const adr = read('repo-modernizer-acrazie', 'references/adr-template.md');
    expect(adr).toContain('do not prefill green checks');
    expect(read('repo-modernizer-acrazie')).not.toContain('vitesse x25');
  });

  test('representative scenario definitions exist without pretending they ran', () => {
    for (const name of names) {
      const data = JSON.parse(read(name, 'evals/evals.json'));
      const scenarios = data.evals.filter((e: { name: string }) => e.name.startsWith('portable-pilot-'));
      expect(scenarios.map((e: { name: string }) => e.name)).toEqual([
        'portable-pilot-version-applicable-evidence', 'portable-pilot-unavailable-documentation',
        'portable-pilot-contradictory-documentation', 'portable-pilot-localized-choice-and-portability',
      ]);
      for (const scenario of scenarios) {
        expect(scenario.prompt).toContain('Simulation only');
        expect(scenario.expected_output).toContain('not an executed result');
        expect(scenario.expectations.length).toBeGreaterThan(0);
      }
      const ids = data.evals.map((e: { id: number }) => e.id);
      expect(new Set(ids).size).toBe(ids.length);
    }
    expect(fs.readFileSync(path.join(root, 'docs/portable-skill-standard.md'), 'utf8')).toContain('defining or checking a prompt is not');
  });
});
