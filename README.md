# Acrazie Skills

[![skills.sh](https://skills.sh/b/Acrazie/skills)](https://skills.sh/Acrazie/skills)

Focused skills for AI coding agents. Each skill owns one concrete workflow and keeps its instructions, UI metadata, and supporting references together.

## Install

Browse and select skills interactively:

```bash
npx skills add Acrazie/skills
```

Install one skill directly:

```bash
npx skills add Acrazie/skills@repository-readme-architect-acrazie
npx skills add Acrazie/skills@audit-repository-acrazie
npx skills add Acrazie/skills@svg-icon-designer-acrazie
```

The CLI detects supported coding agents and lets you choose where to install each skill.

## Skills

### [Repository README Architect / Acrazie](skills/repository-readme-architect-acrazie/SKILL.md)

Design, create, restructure, or update a repository's primary README through repository inspection, an adaptive decision-tree interview, architecture options, and an approval-gated edit.

```text
$repository-readme-architect-acrazie
```

### [Audit Repository / Acrazie](skills/audit-repository-acrazie/SKILL.md)

Audit a precise technical decision, integration, tool, stack choice, or subsystem in one existing repository. This skill requires explicit invocation and does not perform general, security, documentation, diff, PR, or multi-repository audits.

```text
$audit-repository-acrazie
```

### [SVG Icon Designer / Acrazie](skills/svg-icon-designer-acrazie/SKILL.md)

<p align="center">
  <img src="skills/svg-icon-designer-acrazie/assets/svg-icon-designer-logo.svg" alt="SVG-ICON Designer geometric wordmark" width="520" />
</p>

Design original icons through compact iterative concepts, detailed ASCII previews, selected-direction refinement, clean SVG production, and requested PNG or favicon exports.

```text
$svg-icon-designer-acrazie
```

## Naming

Published skill IDs keep the function first for discovery and use `-acrazie` as a consistent author signature. The canonical source is `Acrazie/skills`.

## Repository Structure

```text
skills/
├── repository-readme-architect-acrazie/
├── audit-repository-acrazie/
└── svg-icon-designer-acrazie/
```

Each directory contains its `SKILL.md`, `agents/openai.yaml`, and only the references required by that workflow.

## Migrated Repositories

This monorepo supersedes the standalone `Acrazie/readme-architect` and `Acrazie/audit-repo` repositories.

## License

[MIT](LICENSE)
