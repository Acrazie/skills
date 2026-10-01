import { test, expect } from 'bun:test';
import fs from 'node:fs';
import { getAllSkills, getRepoRoot } from '../src/lib/skills';
import { renderMarkdownWithHeadingOffset } from '../src/lib/markdown';
const dist = `${getRepoRoot()}/site/dist`;
const skills = getAllSkills();
for (const [locale, route, label] of [['en', 'graph', 'Skill map'], ['fr', 'fr/graph', 'Carte des skills'], ['zh', 'zh/graph', '技能地图']]) {
  test(`${locale}: localized static page, every skill and full instructions without JS`, () => {
    const html = fs.readFileSync(`${dist}/${route}/index.html`, 'utf8');
    const data = JSON.parse(html.match(/<script\b[^>]*data-graph-data[^>]*>([\s\S]*?)<\/script>/)![1]);
    expect(data.nodes).toHaveLength(skills.length); expect(data.links).toHaveLength(7);
    expect(data.labels.nav).toBe(label);
    const details = html.match(/<details[^>]*data-content="[^"]+"[^>]*>/g)!;
    expect(details).toHaveLength(skills.length); expect(details.every(tag => !/\bhidden\b/.test(tag))).toBe(true);
    expect(html).toContain('class="map-directory" open');
    for (const skill of skills) {
      expect(html).toContain(`id="map-skill-${skill.id}"`);
      const content = renderMarkdownWithHeadingOffset(skill.content, 2, `https://github.com/Acrazie/skills/blob/${data.revision}/skills/${skill.id}/SKILL.md`);
      expect(html).toContain(content.trim());
    }
  });
}
test('graph entry script is not loaded by catalogue or skill detail', () => {
  const graph = fs.readFileSync(`${dist}/graph/index.html`, 'utf8');
  const scripts = [...graph.matchAll(/<script[^>]*src="([^"]+)"/g)].map(match => match[1]);
  const graphScript = scripts.find(url => url.includes('GraphPage'))!;
  expect(graphScript).toBeDefined();
  for (const route of ['index.html', 'fr/index.html', 'skills/interview-acrazie/index.html']) {
    expect(fs.readFileSync(`${dist}/${route}`, 'utf8')).not.toContain(graphScript);
  }
});
