<p align="center">
  <img src="site/public/images/pixel-cloud-hero.webp" alt="Acrazie Skills Pixel Cloud Hero" width="100%" />
</p>

<h1 align="center">
  <img src="site/public/logo.svg" alt="Acrazie Skills logo" width="32" height="32" valign="middle" /> Acrazie Skills
</h1>

<p align="center">
  <a href="https://skills.sh/Acrazie/skills"><img src="https://skills.sh/b/Acrazie/skills" alt="skills.sh" /></a>
  <a href="https://skills.acrazie.dev"><img src="https://img.shields.io/badge/docs-skills.acrazie.dev-black?style=flat" alt="Documentation" /></a>
  <a href="https://github.com/Acrazie/skills/releases"><img src="https://img.shields.io/github/v/release/Acrazie/skills?style=flat&color=black" alt="Release" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-black?style=flat" alt="License" /></a>
</p>

<p align="center">
  <strong>Focused, production-ready skills for AI coding agents.</strong><br />
  Each skill owns one concrete workflow, maintaining its authoritative instructions, UI metadata, and domain references together.
</p>

---

## Install

Browse and select skills interactively:

```bash
npx skills add Acrazie/skills
```

Install a specific skill directly:

```bash
npx skills add Acrazie/skills@<skill-id>
```

#### Examples

```bash
# Architecture & README design
npx skills add Acrazie/skills@repository-readme-architect-acrazie

# Jenkins CI/CD pipeline automation
npx skills add Acrazie/skills@jenkins-devops-acrazie

# Interactive HTML canvas banners
npx skills add Acrazie/skills@canvas-banner-designer-acrazie

# Autonomous git commit & PR shipping
npx skills add Acrazie/skills@git-ship-acrazie
```

The CLI detects your coding agent (Hermes, Codex, Claude Code, Antigravity, Cursor, etc.) and configures the skill automatically.

---

## Skills Catalog

Explore all 17 skills below, or browse the interactive documentation portal at [skills.acrazie.dev](https://skills.acrazie.dev) with full references, search, and multi-language support.

| Skill | Category | Invocation | Description |
| :--- | :--- | :--- | :--- |
| [**repository-readme-architect**](skills/repository-readme-architect-acrazie/SKILL.md) | Architecture & Review | `$repository-readme-architect-acrazie` | Design, restructure, or update a repository primary README via decision-tree interviews. |
| [**audit-repository**](skills/audit-repository-acrazie/SKILL.md) | Architecture & Review | `$audit-repository-acrazie` | Audit a precise technical decision, integration, stack choice, or subsystem in an existing repo. |
| [**jenkins-devops**](skills/jenkins-devops-acrazie/SKILL.md) | CI/CD & DevOps | `$jenkins-devops-acrazie` | Design, modernize, and diagnose repository-owned Jenkins CI/CD pipelines as code. |
| [**jenkins-go**](skills/jenkins-go-acrazie/SKILL.md) | CI/CD & DevOps | `$jenkins-go-acrazie` | Specialist: Inspect Go modules, workspaces, `golangci-lint`, and test targets for Jenkins. |
| [**jenkins-js-ts**](skills/jenkins-js-ts-acrazie/SKILL.md) | CI/CD & DevOps | `$jenkins-js-ts-acrazie` | Specialist: Inspect Node.js/Bun runtimes, package managers, and scripts for Jenkins. |
| [**jenkins-python**](skills/jenkins-python-acrazie/SKILL.md) | CI/CD & DevOps | `$jenkins-python-acrazie` | Specialist: Inspect Python packaging (`uv`, `poetry`), Pytest, and linters for Jenkins. |
| [**jenkins-rust**](skills/jenkins-rust-acrazie/SKILL.md) | CI/CD & DevOps | `$jenkins-rust-acrazie` | Specialist: Inspect Cargo workspaces, `--locked` builds, Clippy, and test targets for Jenkins. |
| [**jenkins-symfony-php**](skills/jenkins-symfony-php-acrazie/SKILL.md) | CI/CD & DevOps | `$jenkins-symfony-php-acrazie` | Specialist: Inspect Composer lockfiles, Symfony console tasks, and PHPUnit for Jenkins. |
| [**svg-icon-designer**](skills/svg-icon-designer-acrazie/SKILL.md) | Design & Visuals | `$svg-icon-designer-acrazie` | Design original SVG icons and logos through iterative drafts, ASCII previews, and exports. |
| [**svg-banner-designer**](skills/svg-banner-designer-acrazie/SKILL.md) | Design & Visuals | `$svg-banner-designer-acrazie` | Design custom vector SVG banners, social cards, and platform header graphics. |
| [**canvas-banner-designer**](skills/canvas-banner-designer-acrazie/SKILL.md) | Design & Visuals | `$canvas-banner-designer-acrazie` | Build animated HTML Canvas banners, web heroes, and interactive ambient backdrops. |
| [**immersive-hero-designer**](skills/immersive-hero-designer-acrazie/SKILL.md) | Design & Visuals | `$immersive-hero-designer-acrazie` | Design and build complete immersive web hero sections (video, 3D, Canvas, or CSS). |
| [**github-repo-init**](skills/github-repo-init-acrazie/SKILL.md) | Git & Governance | `$github-repo-init-acrazie` | Scaffold production-ready GitHub repositories with stack setup, CI/CD, and governance files. |
| [**git-ship**](skills/git-ship-acrazie/SKILL.md) | Git & Governance | `$git-ship-acrazie` | Finalize, commit, push, and open Pull Requests strictly adhering to repository Git rules. |
| [**multi-agent-planner**](skills/multi-agent-planner-acrazie/SKILL.md) | Agent & DX Tools | `$multi-agent-planner-acrazie` | Plan single-agent vs multi-agent execution and generate verified copy-paste workflows. |
| [**repo-modernizer**](skills/repo-modernizer-acrazie/SKILL.md) | Agent & DX Tools | `$repo-modernizer-acrazie` | Audit outdated tools/runtimes and guide safe upgrades across 6 thematic pillars. |
| [**skill-refiner**](skills/skill-refiner-acrazie/SKILL.md) | Agent & DX Tools | `$skill-refiner-acrazie` | Collect structured user feedback on a skill and record append-only ADR journals. |

---

## Monorepo Architecture

```text
skills/
├── <skill-name>-acrazie/
│   ├── SKILL.md              # Authoritative instructions and YAML frontmatter
│   ├── agents/
│   │   └── openai.yaml       # Codex UI metadata and invocation policy
│   ├── references/           # Detailed domain guides, schemas, recipes
│   └── assets/               # Visual assets and logos
site/                         # Astro documentation site (skills.acrazie.dev)
docs/                         # Architecture decisions and repository documentation
scripts/                      # Verification hooks and linking utilities
```

### Conventions

- **Author Signature**: Every skill identifier and directory ends with `-acrazie` (canonical namespace: `Acrazie/skills`).
- **Autonomy**: Each skill operates independently, containing all references needed for its workflow.
- **Invocation Control**: Agents may select relevant skills within the requested task; selection never grants action permissions. Only the persistent `skill-refiner-acrazie` campaign requires explicit skill activation. See [the invocation policy](.agents/invocation.md).

---

## Local Development

Symlink all skills locally into your installed agent directories (`~/.hermes/skills/`, `~/.agents/skills/`, `~/.gemini/config/skills/`, etc.):

```bash
./scripts/link-skills.sh
```

Pre-commit validation hooks can be executed directly:

```bash
./scripts/hooks/check-skill-structure.sh
./scripts/hooks/validate-skills.sh skills/<skill-name>-acrazie/SKILL.md
```

---

## License

Distributed under the [MIT License](LICENSE).

---

<sub>*Historical Note: This monorepo supersedes the standalone `Acrazie/readme-architect` and `Acrazie/audit-repo` repositories.*</sub>
