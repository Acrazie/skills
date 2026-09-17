import fs from 'node:fs';
import path from 'node:path';
import matter from 'gray-matter';

export interface SkillReference {
  name: string;
  title: string;
  content: string;
}

export interface SkillData {
  id: string;
  name: string;
  description: string;
  category: string;
  icon: string;
  disableModelInvocation: boolean;
  installCommand: string;
  invocationCommand: string;
  content: string;
  references: SkillReference[];
}

// Categorization helper based on skill ID
function determineCategory(id: string): { category: string; icon: string } {
  if (id.startsWith('jenkins-')) {
    return { category: 'CI/CD & DevOps', icon: 'server' };
  }
  if (id.startsWith('svg-') || id.startsWith('canvas-')) {
    return { category: 'Design & Visuals', icon: 'palette' };
  }
  if (id.startsWith('github-repo-init') || id.includes('governance')) {
    return { category: 'Repository & Governance', icon: 'layers' };
  }
  if (id.startsWith('audit-') || id.startsWith('repository-readme-')) {
    return { category: 'Architecture & Review', icon: 'book' };
  }
  return { category: 'Agent & DX Tools', icon: 'tools' };
}

export function getAllSkills(): SkillData[] {
  // Resolve skills folder relative to project
  const skillsDir = path.resolve(process.cwd(), '../skills');
  if (!fs.existsSync(skillsDir)) {
    return [];
  }

  const entries = fs.readdirSync(skillsDir, { withFileTypes: true });
  const skills: SkillData[] = [];

  for (const entry of entries) {
    if (!entry.isDirectory()) continue;
    const skillPath = path.join(skillsDir, entry.name);
    const skillMdPath = path.join(skillPath, 'SKILL.md');

    if (!fs.existsSync(skillMdPath)) continue;

    const rawContent = fs.readFileSync(skillMdPath, 'utf-8');
    const { data: frontmatter, content } = matter(rawContent);

    const id = entry.name;
    const { category, icon } = determineCategory(id);

    // Read references directory if it exists
    const refsDir = path.join(skillPath, 'references');
    const references: SkillReference[] = [];

    if (fs.existsSync(refsDir)) {
      const refFiles = fs.readdirSync(refsDir);
      for (const refFile of refFiles) {
        if (!refFile.endsWith('.md')) continue;
        const refContent = fs.readFileSync(path.join(refsDir, refFile), 'utf-8');
        const title = refFile.replace(/\.md$/, '').replace(/-/g, ' ').toUpperCase();
        references.push({
          name: refFile,
          title,
          content: refContent,
        });
      }
    }

    skills.push({
      id,
      name: frontmatter.name || id,
      description: frontmatter.description || '',
      category,
      icon,
      disableModelInvocation: Boolean(frontmatter['disable-model-invocation']),
      installCommand: `npx skills add Acrazie/skills@${id}`,
      invocationCommand: `$${id}`,
      content,
      references,
    });
  }

  // Sort alphabetically by ID
  return skills.sort((a, b) => a.id.localeCompare(b.id));
}

export function getSkillById(id: string): SkillData | undefined {
  const all = getAllSkills();
  return all.find((s) => s.id === id);
}

export function getChangelog(): string {
  const changelogPath = path.resolve(process.cwd(), '../CHANGELOG.md');
  if (!fs.existsSync(changelogPath)) {
    return '# Changelog\n\nNo changelog found.';
  }
  return fs.readFileSync(changelogPath, 'utf-8');
}
