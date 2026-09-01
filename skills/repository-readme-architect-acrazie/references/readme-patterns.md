# README architecture and quality patterns

Use these as conditional heuristics after the interview, never as a universal template.

## Reader-flow patterns

### Evaluation-first

Best when prospective users or adopters are primary. Lead with identity, value, a concrete example or visual, key constraints, then quick start and deeper references.

### Task-first

Best for tools, CLIs, and operational projects. Lead with the shortest path to a successful task, then commands, configuration, examples, and troubleshooting.

### Integration-first

Best for libraries, SDKs, and APIs. Lead with compatibility and installation, then a minimal integration, core interfaces, error behavior, and links to detailed API material.

### Contributor-first

Best only when contribution is the main reader outcome. Lead with project context, repository map, verified local development path, tests, and links to existing contribution policy.

### Navigation-first

Best for monorepos or documentation-rich projects. Lead with package or domain map and audience routes, then shared setup and cross-cutting policies.

Offer two or three patterns only when each produces a materially different reader journey. Adapt or combine them after user selection.

## Project-type emphasis

- **Application:** outcome, demo or screenshot when available, supported deployment/use path, configuration, operational limits.
- **Library/SDK:** install, compatibility, minimal import/use example, principal API concepts, versioning and migration links.
- **CLI:** installation, command synopsis, task examples, flags/config precedence, exit behavior when documented.
- **API/service:** purpose, authentication without secrets, minimal request/response, local run path, endpoint-documentation link, operational status only when real.
- **Infrastructure:** scope, prerequisites, plan/apply or deployment flow, state and safety warnings, environment boundaries, rollback links when documented.
- **Monorepo:** package map, audience routes, shared prerequisites, scoped commands, ownership and documentation links.

## Content heuristics

- Make title and first paragraph answer “what is this?” and “why would this reader care?”
- Put the shortest verified success path before exhaustive reference material.
- Prefer copyable examples whose commands exist in repository metadata or tested documentation.
- State important prerequisites and limitations before they cause failure.
- Link authoritative detailed docs instead of duplicating content likely to drift.
- Use tables only for genuinely tabular comparisons or references.
- Add a table of contents only when navigation benefit exceeds clutter.
- Use badges sparingly. Every badge must have a real source, target, and useful claim.
- Use diagrams or screenshots only when available and useful; add descriptive alt text.
- Avoid marketing claims the repository cannot substantiate.
- Avoid empty standard sections added merely because templates contain them.

## Wireframe format

Each architecture proposal should show:

```text
# Project name
  One-line purpose and primary reader promise

## First reader decision or task
  Expected content; representative example/visual type

## Next section
  Why it follows; facts or choices it communicates

...
```

Name the reader-flow pattern, explain its tradeoff briefly, and identify content it deliberately postpones or omits. Wireframes are structural proposals, not full competing drafts.

## Update quality

- Preserve correct, intentional content unless the approved design visibly supersedes it.
- Surface removals, renamed sections, changed commands, altered claims, and changed link destinations.
- Prefer root-cause correction over duplicated warnings or parallel instructions.
- Preserve useful anchors when feasible; call out unavoidable anchor changes.
- Do not overwrite generated output.

## Validation checklist

- Heading hierarchy is valid and scannable.
- Internal anchors and relative paths resolve for the target platform.
- Fenced code blocks specify a language when appropriate and close correctly.
- Commands, package names, filenames, environment-variable names, and compatibility claims match repository evidence.
- Examples contain no secrets or real credentials.
- Images have useful alt text; link labels make sense out of context.
- Platform-specific Markdown is used only on the detected target.
- External links are checked only when network access is available and authorized; otherwise report them as unchecked.
- Final diff changes only the primary README and contains no accidental loss.

## Authoritative references

Consult these only when their detail affects the current task:

- GitHub, “About READMEs”: https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
- GitHub, “Basic writing and formatting syntax”: https://docs.github.com/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
- GitHub Flavored Markdown specification: https://github.github.com/gfm/
- CommonMark specification: https://spec.commonmark.org/
- GitLab Flavored Markdown: https://docs.gitlab.com/user/markdown/
- SPDX License List: https://spdx.org/licenses/
- Choose a License: https://choosealicense.com/

These references inform README wording and links. They do not authorize creating or changing license, contribution, security, or other policy files.
