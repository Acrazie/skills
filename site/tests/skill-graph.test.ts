import { describe, test, expect } from 'bun:test';
import fs from 'node:fs';
import { createGraphNodes, getSkillGraph, resolveInvocations, type InvocationDeclaration } from '../src/lib/skill-graph';
import { getAllSkills, getRepoRoot } from '../src/lib/skills';

const declaration: InvocationDeclaration = { source: 'a', target: 'b', conditional: true, evidence: [{ path: 'skills/a/SKILL.md', quote: 'Use `$b`.' }] };
const read = () => 'Heading\n\nUse `$b`.\n';
describe('documented invocations', () => {
  test('records direction and exact source line', () => {
    const [link] = resolveInvocations(['a', 'b'], [declaration], read);
    expect(link.source).toBe('a'); expect(link.target).toBe('b');
    expect(link.evidence[0].line).toBe(3); expect(link.conditional).toBe(true);
  });
  test('mere mentions never create edges', () => {
    expect(resolveInvocations(['a', 'b'], [], () => 'Mention `$b`.')).toEqual([]);
  });
  test('rejects absent endpoints, duplicate edges and absent evidence', () => {
    expect(() => resolveInvocations(['a'], [declaration], read)).toThrow('Unknown');
    expect(() => resolveInvocations(['a', 'b'], [declaration, declaration], read)).toThrow('Duplicate');
    expect(() => resolveInvocations(['a', 'b'], [{ ...declaration, evidence: [] }], read)).toThrow('Missing');
  });
  test('rejects changed sources and source traversal', () => {
    expect(() => resolveInvocations(['a', 'b'], [declaration], () => 'Old mention')).toThrow('Stale');
    expect(() => resolveInvocations(['a', 'b'], [{ ...declaration, evidence: [{ path: 'skills/a/../b/SKILL.md', quote: 'Use `$b`.' }] }], read)).toThrow('Invalid');
  });
  test('allows cycles and self-invocations without imposing a tree', () => {
    const reverse = { ...declaration, source: 'b', target: 'a', evidence: [{ path: 'skills/b/SKILL.md', quote: 'Use `$b`.' }] };
    expect(resolveInvocations(['a', 'b'], [declaration, reverse], read)).toHaveLength(2);
    expect(resolveInvocations(['a'], [{ ...declaration, target: 'a' }], read)).toHaveLength(1);
  });
  test('catalogue includes isolated skills and stable, finite positions', () => {
    const skills = getAllSkills(); const graph = getSkillGraph();
    expect(graph.nodes.map(n => n.id).sort()).toEqual(skills.map(s => s.id).sort());
    expect(new Set(graph.nodes.map(n => n.id)).size).toBe(skills.length);
    expect(createGraphNodes(skills)).toEqual(graph.nodes);
    expect(graph.nodes.every(n => Number.isFinite(n.x) && Number.isFinite(n.y))).toBe(true);
    expect(graph.nodes.some(n => !graph.links.some(l => l.source === n.id || l.target === n.id))).toBe(true);
  });
  test('builder Interview edge records the reusable-contract and loading gates', () => {
    const link = getSkillGraph().links.find(link =>
      link.source === 'feature-builder-acrazie' && link.target === 'interview-acrazie');
    expect(link).toBeDefined();
    expect(link!.conditional).toBe(true);
    expect(link!.evidence).toHaveLength(1);
    const evidence = link!.evidence[0];
    expect(evidence.path).toBe('skills/feature-builder-acrazie/SKILL.md');
    expect(evidence.quote).toContain('no applicable approved contract can be reused');
    expect(evidence.quote).toContain('propose `interview-acrazie`');
    expect(evidence.quote).toContain('project loading boundary before\nreading or invoking it');
    const lines = fs.readFileSync(`${getRepoRoot()}/${evidence.path}`, 'utf8').split('\n');
    expect(lines.slice(evidence.line - 1, evidence.endLine).join('\n')).toContain(evidence.quote);
  });
  test('real edges are reviewed calls, never recommendation-only git shipping', () => {
    const graph = getSkillGraph();
    expect(graph.links).toHaveLength(7);
    expect(graph.links.some(l => l.source === 'feature-builder-acrazie' && l.target === 'interview-acrazie')).toBe(true);
    expect(graph.links.some(l => l.source === 'git-ship-acrazie')).toBe(false);
    for (const link of graph.links) for (const evidence of link.evidence) {
      const lines = fs.readFileSync(`${getRepoRoot()}/${evidence.path}`, 'utf8').split('\n');
      expect(lines.slice(evidence.line - 1, evidence.endLine).join('\n')).toContain(evidence.quote);
    }
  });
});

import { redrawDuration } from '../src/lib/graph-motion';
import { renderMarkdownWithHeadingOffset } from '../src/lib/markdown';
describe('motion budget and reading invariants', () => {
  const state = { visible: true, documentHidden: false, reduced: false, paused: false, hasConnections: true };
  test('signals end after 1800ms; normal redraw is 120ms', () => {
    expect(redrawDuration(true, state)).toBe(1800);
    expect(redrawDuration(false, state)).toBe(120);
  });
  test('reduced motion, manual pause and isolated nodes never run signals', () => {
    for (const field of ['reduced', 'paused'] as const) expect(redrawDuration(true, { ...state, [field]: true })).toBe(120);
    expect(redrawDuration(true, { ...state, hasConnections: false })).toBe(120);
  });
  test('offscreen and background pages have no rendering budget', () => {
    expect(redrawDuration(true, { ...state, visible: false })).toBe(0);
    expect(redrawDuration(true, { ...state, documentHidden: true })).toBe(0);
  });
  test('relative references resolve to source, headings retain existing offset', () => {
    const html = renderMarkdownWithHeadingOffset('# Skill\n\n[Guide](references/guide.md)\n\n[External](https://example.com)', 2, 'https://github.com/Acrazie/skills/blob/revision/skills/a/SKILL.md');
    expect(html).toContain('<h3>Skill</h3>');
    expect(html).toContain('https://github.com/Acrazie/skills/blob/revision/skills/a/references/guide.md');
    expect(html).toContain('href="https://example.com"');
    expect(renderMarkdownWithHeadingOffset('[Guide](references/guide.md)', 2)).toContain('href="references/guide.md"');
  });
});

test('graph data works in Docker-style source trees without Git metadata', () => {
  const root = getRepoRoot();
  const directory = fs.mkdtempSync('/private/tmp/skill-graph-source-');
  fs.symlinkSync(`${root}/skills`, `${directory}/skills`, 'dir');
  const original = process.cwd();
  try {
    process.chdir(directory);
    expect(getSkillGraph().nodes).toHaveLength(getAllSkills().length);
  } finally { process.chdir(original); fs.rmSync(directory, { recursive: true }); }
});

test('synchronous renderer zoom notifications cannot recursively resume the loop', () => {
  const source = fs.readFileSync(`${getRepoRoot()}/site/src/scripts/skill-graph.ts`, 'utf8');
  const js = new Bun.Transpiler({ loader: 'ts' }).transformSync(source);
  const wakeFunction = js.slice(js.indexOf('function wake('), js.indexOf('function select('));
  const exercise = new Function('redrawDuration', `
    let count = 0, stopTimer, resuming = false;
    const setTimeout = () => 1, clearTimeout = () => {};
    const visible = true, document = { hidden: false }, reduced = { matches: false }, manualPause = false;
    const neighbors = new Set(['source', 'target']), root = { dataset: {} }, selected = 'source';
    const linked = () => true, sleep = () => {};
    const graph = {
      linkDirectionalParticles() { return this; },
      resumeAnimation() { if (++count > 2) throw new Error('Recursive resume'); wake(); return this; }
    };
    ${wakeFunction}
    wake(true);
    return count;
  `);
  expect(exercise(redrawDuration)).toBe(1);
});
