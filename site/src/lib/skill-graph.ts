import fs from 'node:fs';
import path from 'node:path';
import { getAllSkills, getRepoRoot, type SkillData } from './skills';

export interface GraphEvidence { path: string; quote: string; line: number; endLine: number }
export interface Invocation { source: string; target: string; conditional: boolean; evidence: GraphEvidence[] }
export interface InvocationDeclaration extends Omit<Invocation, 'evidence'> { evidence: { path: string; quote: string }[] }

// Reviewed instructions, not name matching: mentions and installation suggestions are not calls.
const declarations: InvocationDeclaration[] = [
  {
    source: 'feature-builder-acrazie', target: 'interview-acrazie', conditional: true,
    evidence: [{ path: 'skills/feature-builder-acrazie/SKILL.md', quote: 'Otherwise use `$interview-acrazie`.' }],
  },
  {
    source: 'immersive-hero-designer-acrazie', target: 'canvas-banner-designer-acrazie', conditional: true,
    evidence: [{ path: 'skills/immersive-hero-designer-acrazie/SKILL.md', quote: 'For a procedural Canvas scene or pointer-reactive ambient backdrop alone, use `canvas-banner-designer-acrazie` instead; if it is the chosen medium within a complete hero, follow that skill\'s rendering and lifecycle contract rather than inventing a second one.' }],
  },
  ...['js-ts', 'python', 'rust', 'go', 'symfony-php'].map(stack => ({
    source: 'jenkins-devops-acrazie', target: `jenkins-${stack}-acrazie`, conditional: true,
    evidence: [
      { path: 'skills/jenkins-devops-acrazie/SKILL.md', quote: 'When the runtime exposes a native installed-skill catalog and loader, use them to find and load the exact specialist.' },
      { path: 'skills/jenkins-devops-acrazie/references/specialist-contract.md', quote: `- \`jenkins-${stack}-acrazie\`:` },
    ],
  })),
];

export function resolveInvocations(ids: string[], definitions: InvocationDeclaration[], read: (file: string) => string): Invocation[] {
  const known = new Set(ids);
  const pairs = new Set<string>();
  return definitions.map(definition => {
    const key = `${definition.source}:${definition.target}`;
    if (!known.has(definition.source) || !known.has(definition.target)) throw new Error(`Unknown invocation endpoint: ${key}`);
    if (pairs.has(key)) throw new Error(`Duplicate invocation: ${key}`);
    if (!definition.evidence.length) throw new Error(`Missing evidence: ${key}`);
    pairs.add(key);
    const evidence = definition.evidence.map(item => {
      if (!item.path.startsWith(`skills/${definition.source}/`) || item.path.includes('..') || !item.path.endsWith('.md')) throw new Error(`Invalid evidence path: ${item.path}`);
      const content = read(item.path);
      const offset = content.indexOf(item.quote);
      if (!item.quote.trim() || offset < 0) throw new Error(`Stale invocation evidence: ${key} in ${item.path}`);
      const line = content.slice(0, offset).split('\n').length;
      return { ...item, line, endLine: line + item.quote.split('\n').length - 1 };
    });
    return { ...definition, evidence };
  });
}

const familyStyle: Record<string, { color: string; x: number; y: number }> = {
  'CI/CD & DevOps': { color: '#ffa86b', x: -260, y: -10 },
  'Design & Visuals': { color: '#c4a3ff', x: 100, y: -205 },
  'Agent & DX Tools': { color: '#8ad9ce', x: 265, y: 120 },
  'Repository & Governance': { color: '#efb6cb', x: -250, y: 265 },
  'Architecture & Review': { color: '#a7baff', x: 70, y: 330 },
};

export function createGraphNodes(skills: SkillData[]) {
  const families = [...new Set(skills.map(skill => skill.category))];
  return families.flatMap(category => {
    const members = skills.filter(skill => skill.category === category);
    const style = familyStyle[category] ?? { color: '#c7c7c7', x: 0, y: 0 };
    return members.map((skill, index) => {
      const angle = index * Math.PI * 2 / members.length - Math.PI / 2;
      const hub = skill.id === 'jenkins-devops-acrazie';
      const x = style.x + (members.length === 1 || hub ? 0 : Math.cos(angle) * 145);
      const y = style.y + (members.length === 1 || hub ? 0 : Math.sin(angle) * (members.length < 3 ? 55 : 110));
      return { id: skill.id, category, color: style.color, x, y, fx: x, fy: y };
    });
  });
}

export function getSkillGraph() {
  const root = getRepoRoot();
  const skills = getAllSkills();
  const links = resolveInvocations(skills.map(skill => skill.id), declarations, file => fs.readFileSync(path.join(root, file), 'utf8'));
  // Container builds copy sources, not .git, and do not install a Git executable.
  const revision = /^[a-f0-9]{40}$/i.test(process.env.GITHUB_SHA ?? '') ? process.env.GITHUB_SHA! : 'main';
  return { nodes: createGraphNodes(skills), links, revision };
}
