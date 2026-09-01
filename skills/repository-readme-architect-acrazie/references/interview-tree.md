# Adaptive README interview tree

Use this map as decision dependencies, not as a fixed questionnaire. Skip decisions already explicit in the request or settled by verified repository evidence. Ask only user-owned decisions; discover facts yourself.

## 1. Establish facts

Before questions, inspect enough of the repository to record:

- repository root and primary README path;
- create versus update state and generated-file markers;
- hosting platform and supported Markdown dialect;
- project shape: application, library, CLI, API, infrastructure, or monorepo;
- manifests, package metadata, entry points, scripts, examples, tests, and release artifacts;
- documented prerequisites, configuration keys from safe committed sources, and runnable commands;
- existing diagrams, screenshots, logos, badges, license, contribution, security, support, and changelog sources.

Facts may remain unknown in an early-stage project. Label them unknown; do not turn them into decisions or invented prose.

## 2. Root decisions

These usually have no unresolved decision prerequisites:

- **Goal:** create, correct, simplify, restructure, reposition, or update for a specific release.
- **Primary audience:** evaluator, end user, integrator, contributor, operator, or internal team.
- **Reader outcome:** what the primary audience must understand or accomplish first.
- **Publication context:** public or internal, and target host when evidence does not settle it.
- **README language:** based on intended audience; bilingual only when its ongoing maintenance cost is justified.
- **Project maturity:** prototype, active production project, stable package, archived project, or another user-defined status when not factual.

## 3. Dependent decisions

Activate only relevant branches after their prerequisites settle.

### Identity and positioning

Prerequisites: goal, audience, reader outcome.

- title and one-line explanation;
- problem, value proposition, differentiators, and expected context;
- status or limitations that materially affect adoption;
- short evaluation path before detailed setup.

### Getting started

Prerequisites: audience, project type, verified installation and execution facts.

- prerequisites worth surfacing;
- installation route and supported alternatives;
- smallest useful quick start;
- expected output or success signal;
- first troubleshooting guidance when evidence supports it.

Never ask the user to recite commands present in manifests or scripts. Ask them to choose among verified routes or resolve product intent.

### Usage and technical depth

Prerequisites: project type, reader outcome, verified interfaces.

- core examples and progression from basic to advanced;
- configuration concepts and safe example values;
- API, CLI, library, deployment, or operational detail appropriate to project type;
- architecture explanation or diagram when it improves a real reader task;
- limitations, compatibility, migration, or performance claims only when verified.

### Repository navigation

Prerequisites: audience and repository structure.

- whether contributors or operators need a repository map;
- links to existing detailed documentation rather than duplicated content;
- monorepo package navigation when applicable.

### Trust, maintenance, and community

Prerequisites: publication context, maturity, and existence of authoritative files or URLs.

- whether to mention existing license, contributing, security, support, roadmap, changelog, or citation resources;
- factual project status and maintenance expectations;
- badges only when their target and displayed claim are real and useful.

This branch controls README content only. Never create or edit the linked ancillary resources. Never choose a license, security policy, or support promise on the user's behalf.

### Presentation and navigation

Prerequisites: proposed content depth, platform, and available assets.

- concise versus reference-heavy reader journey;
- table of contents when length warrants it;
- screenshots, diagrams, demos, or logo only when they clarify or build justified trust;
- placement of badges and calls to action;
- accessibility: descriptive alt text, meaningful link labels, readable heading hierarchy, and non-color-only meaning.

Missing visual assets may be proposed as a separate future task. Do not create them or expand write scope during this workflow.

## 4. Update-specific branch

Compare existing content with verified facts and settled decisions. Decide explicitly:

- valuable content to preserve;
- obsolete or misleading content to remove;
- sections to reorder, merge, or split;
- semantic changes requiring user attention;
- links or commands needing correction;
- whether the desired outcome is an incremental update or approved full restructuring.

If generated-file markers exist, stop the normal edit path. Identify the generator/source and explain that editing it falls outside README-only scope.

## 5. Handling uncertainty

For each unknown, classify it as:

- **decision:** ask at the correct frontier with a recommendation;
- **discoverable fact:** inspect further;
- **unverifiable fact:** disclose it and omit unsupported claims;
- **deferred content:** exclude it, or use an explicit placeholder only if the user approves.

## 6. Shared-understanding checkpoint

The frontier is empty only when every relevant branch is settled, excluded, or blocked by a disclosed factual gap. Summarize:

1. verified repository facts;
2. user decisions;
3. excluded branches and why;
4. unresolved factual gaps and their effect;
5. planned write target and forbidden side effects.

Wait for explicit confirmation before proposing README architectures.
