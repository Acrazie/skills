import { expect, test } from 'bun:test';
import fs from 'node:fs';
import { createHash } from 'node:crypto';
import { getRepoRoot } from '../src/lib/skills';

const root = `${getRepoRoot()}/site`;
const globals = fs.readFileSync(`${root}/src/styles/globals.css`, 'utf8');
const tokens = new Map([...globals.matchAll(/(--[\w-]+):\s*([^;]+);/g)].map(match => [match[1], match[2]]));
function resolve(value: string): string {
  for (let i = 0; i < 8; i++) {
    const next = value.replace(/var\((--[\w-]+)(?:,\s*([^()]+))?\)/g, (match, token, fallback) => tokens.get(token) ?? fallback ?? match);
    if (next === value) return value;
    value = next;
  }
  throw new Error('Theme token cycle');
}
function normalize(value: string): string {
  return resolve(value.replace(/:root\s*\{[^}]*\}/g, ''))
    .replace(/\/\*[\s\S]*?\*\//g, '')
    .replace(/(:\s*)white(?=\s*[;}])/g, '$1#fff')
    .replace(/\s+/g, '');
}

// Baselines preserve the authored surfaces; LanguageSwitcher reflects the approved dock-integrated redesign.
// Expansion must preserve authored values, selector order, layout and motion, not merely similar colors.
const baseline = {
  'src/styles/globals.css': 'f38acfc25d9364b46b4ab1c201dcc4e7f6e3005ce526616548399b671991ff38',
  'src/styles/skill-graph.css': 'ce4b5b75f7e0c884364fb5d2cb5a6e29abcb09c85c696d5ff247c9d3885bf5a2',
  'src/components/LanguageSwitcher.astro': 'f101b8f69479dac1de54a0088508f7d088531c53c85ab0229dc4be54d548f548',
  'src/components/Header.astro': '1b343bf391d611aeb54674453f6720079e21c1d8fc93f30f9b597ce769f84215',
};

test('language control integrates with the dock while preserving accessible navigation', () => {
  const source = fs.readFileSync(`${root}/src/components/LanguageSwitcher.astro`, 'utf8');
  const triggerStyle = source.match(/\.lang-switcher__btn\s*\{([^}]+)\}/)![1];
  expect(triggerStyle).toContain('background: transparent');
  expect(triggerStyle).toContain('border: 0');
  expect(triggerStyle).toContain('min-height: 44px');
  expect(triggerStyle).toContain('min-width: 44px');
  expect(source).toContain('background: var(--dock-surface)');
  expect(source).toContain('background: var(--dock-fallback-surface)');
  expect(source).toContain('box-shadow: var(--shadow-dock)');
  for (const prefix of ['', 'fr/', 'zh/']) {
    const html = fs.readFileSync(`${root}/dist/${prefix}index.html`, 'utf8');
    expect(html).toContain('aria-controls="language-options"');
    expect(html).toContain('aria-expanded="false"');
    expect(html).toMatch(/id="language-options"[^>]*hidden/);
    expect(html.match(/<a\b[^>]*class="lang-switcher__option\b/g)).toHaveLength(3);
  }
});
for (const [path, expected] of Object.entries(baseline)) {
  test(`${path}: token expansion preserves the authored surface`, () => {
    const normalized = normalize(fs.readFileSync(`${root}/${path}`, 'utf8'));
    expect(createHash('sha256').update(normalized).digest('hex')).toBe(expected);
    // Family colors are per-node data shared by the DOM and canvas, not global theme constants.
    expect([...normalized.matchAll(/var\((--[\w-]+)\)/g)].map(match => match[1]))
      .toEqual(path === 'src/styles/skill-graph.css' ? ['--family-color'] : []);
  });
}

test('canvas reads the shared theme once, outside rendering callbacks', () => {
  const source = fs.readFileSync(`${root}/src/scripts/skill-graph.ts`, 'utf8');
  const paletteSource = source.slice(source.indexOf('  const styles ='), source.indexOf('  let graph:'));
  let computedReads = 0;
  const requested: string[] = [];
  const palette = new Function('getComputedStyle', 'root', `${paletteSource}; return palette;`)(() => {
    computedReads++;
    return { getPropertyValue: (name: string) => { requested.push(name); return resolve(tokens.get(name)!); } };
  }, {});
  expect(computedReads).toBe(1);
  expect(requested).toHaveLength(6);
  expect(palette).toEqual({ surface: '#101011', link: '#767481', signal: '#e6d6ff', activeInk: '#fff', labelInk: '#e0e0e5', codeFont: '"JetBrains Mono", monospace' });
  expect(source.match(/getComputedStyle\(/g)).toHaveLength(1);
  expect(source.slice(source.indexOf('.onRenderFramePre'))).not.toContain('getPropertyValue');
  expect(source).toContain('context.strokeStyle = node.color');
});

test('copy colors retain Tailwind OKLCH tokens and exact authored alpha', () => {
  const expected = {
    '--copy-border': 'var(--color-zinc-800)', '--copy-surface': 'color-mix(in oklab, var(--color-zinc-900) 80%, transparent)',
    '--copy-hover-surface': 'var(--color-zinc-800)', '--copy-ink': 'var(--color-zinc-300)',
    '--copy-hover-ink': 'var(--color-zinc-100)', '--copy-focus': 'var(--color-zinc-600)', '--copy-success': 'var(--color-emerald-400)',
  };
  for (const [token, value] of Object.entries(expected)) expect(tokens.get(token)).toBe(value);
  const css = fs.readdirSync(`${root}/dist/_astro`).filter(file => file.endsWith('.css')).map(file => fs.readFileSync(`${root}/dist/_astro/${file}`, 'utf8')).join('\n');
  for (const color of ['zinc-100', 'zinc-300', 'zinc-600', 'zinc-800', 'zinc-900', 'emerald-400']) {
    expect(css).toMatch(new RegExp(`--color-${color}:oklch\\(`));
  }
  expect(css).toContain('background-color:var(--copy-surface)');
  expect(css).toContain('color:var(--copy-success)');
});
