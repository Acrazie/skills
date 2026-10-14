import { test, expect } from 'bun:test';
import fs from 'node:fs';
import { getRepoRoot, getAllSkills, getSkillSourceUrl } from '../src/lib/skills';
import { renderMarkdownWithHeadingOffset } from '../src/lib/markdown';
import { reserveLabel, type LabelBounds } from '../src/lib/graph-labels';

const dist = `${getRepoRoot()}/site/dist`;

test('canonical English articles announce their language in every locale', () => {
  for (const prefix of ['', 'fr/', 'zh/']) {
    for (const route of ['graph/', 'changelog/', ...getAllSkills().map(skill => `skills/${skill.id}/`)]) {
      const html = fs.readFileSync(`${dist}/${prefix}${route}index.html`, 'utf8');
      const articles = html.match(/<article\b[^>]*class="prose-shadcn[^>]*>/g)!;
      expect(articles.length).toBeGreaterThan(0);
      expect(articles.every(tag => tag.includes('lang="en"'))).toBe(true);
    }
  }
});

test('fiches resolve instructions and sibling reference links against their own source file', () => {
  const skill = getAllSkills().find(skill => skill.id === 'github-repo-init-acrazie')!;
  for (const prefix of ['', 'fr/', 'zh/']) {
    const html = fs.readFileSync(`${dist}/${prefix}skills/${skill.id}/index.html`, 'utf8');
    expect(html).toContain(renderMarkdownWithHeadingOffset(skill.content, 2, getSkillSourceUrl(skill.id)).trim());
    for (const ref of skill.references) {
      expect(html).toContain(renderMarkdownWithHeadingOffset(ref.content, 2, getSkillSourceUrl(skill.id, `references/${ref.name}`)).trim());
    }
    expect(html).not.toMatch(/href="references\//);
    expect(html).not.toMatch(/href="github-settings\.md"/);
  }
});

test('labels reserve complete bounds and reject overlap without consuming space', () => {
  const occupied: LabelBounds[] = [];
  expect(reserveLabel({ left: 0, top: 0, right: 100, bottom: 30 }, occupied)).toBe(true);
  expect(reserveLabel({ left: 50, top: 10, right: 150, bottom: 40 }, occupied)).toBe(false);
  expect(occupied).toHaveLength(1);
  expect(reserveLabel({ left: 100, top: 0, right: 200, bottom: 30 }, occupied)).toBe(true);
  expect(reserveLabel({ left: 0, top: 30, right: 100, bottom: 60 }, occupied)).toBe(true);
});

test('catalogue preserves clipped-container focus and avoids global character shortcuts', () => {
  const root = getRepoRoot();
  const styles = fs.readFileSync(`${root}/site/src/styles/globals.css`, 'utf8');
  expect(styles).toContain('.filter-tag:focus-visible { outline-offset: -2px; }');
  const catalogue = fs.readFileSync(`${root}/site/src/views/CataloguePage.astro`, 'utf8');
  expect(catalogue).not.toContain('<kbd>/</kbd>');
  expect(catalogue).not.toContain("document.addEventListener('keydown'");
});

test('auto-hiding header remains keyboard-reachable and reveals on focus', () => {
  const header = fs.readFileSync(`${getRepoRoot()}/site/src/components/Header.astro`, 'utf8');
  expect(header).not.toContain('dock.inert');
  expect(header).toContain("dock.addEventListener('focusin', show)");
});

test('clipboard rejection exposes local feedback and successful retry removes it', async () => {
  const component = fs.readFileSync(`${getRepoRoot()}/site/src/components/CopyButton.astro`, 'utf8');
  const script = component.split('<script>')[1].split('</script>')[0]
    .replace('let errorMessage: HTMLDivElement | undefined;', 'let errorMessage;')
    .replaceAll('(btn as HTMLElement)', 'btn');
  let click: (event: { preventDefault(): void; stopPropagation(): void }) => Promise<void>;
  let rejected = true;
  const messages: { textContent: string; removed?: boolean; className?: string; setAttribute(): void; remove(): void }[] = [];
  const status = { textContent: '' };
  const card = { append: (message: typeof messages[number]) => messages.push(message) };
  const button = {
    dataset: { copyError: 'Could not copy. Select the command manually.', copySuccess: 'Copied!' },
    getAttribute: (name: string) => name === 'data-copy-text' ? 'npx skills add Acrazie/skills' : null,
    setAttribute() {},
    addEventListener: (_event: string, handler: typeof click) => { click = handler; },
    querySelector: (selector: string) => selector === '.copy-status' ? status : null,
    closest: (selector: string) => selector === '.skill-card' ? card : null,
  };
  const document = {
    querySelectorAll: () => [button],
    addEventListener() {},
    createElement: (tag: string) => {
      expect(tag).toBe('div'); // Catalogue paragraphs occupy the description grid row on mobile.
      return { textContent: '', setAttribute() {}, remove() { this.removed = true; }, removed: false };
    },
  };
  new Function('document', 'navigator', 'console', 'setTimeout', script)(document, {
    clipboard: { writeText: async () => { if (rejected) throw new Error('Clipboard denied'); } },
  }, { error() {} }, () => {});
  const event = { preventDefault() {}, stopPropagation() {} };
  await click!(event);
  expect(messages).toHaveLength(1);
  expect(messages[0].className).toBe('copy-error-message');
  expect(messages[0].textContent).toBe(button.dataset.copyError);
  expect(status.textContent).toBe(button.dataset.copyError);
  rejected = false;
  await click!(event);
  expect(messages[0].removed).toBe(true);
  expect(status.textContent).toBe(button.dataset.copySuccess);
});
