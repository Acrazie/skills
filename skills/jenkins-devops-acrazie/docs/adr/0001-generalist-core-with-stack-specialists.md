# ADR 0001: Generalist Jenkins core with stack specialists

- Status: Accepted
- Date: 2026-09-04

## Context

A single Jenkins skill could cover pipeline design, Jenkins-specific safety, multiple application stacks, deployment targets, diagnosis, and administration. That breadth would make its always-loaded instructions large and would mix stable Jenkins governance with rapidly varying stack details. A set of stack-only skills without a Jenkins core would instead duplicate approval, artifact promotion, credential, plugin, ADR, and validation rules.

The skills must remain useful across Agent Skills-compatible runtimes including Antigravity, Claude Code, Codex, and Hermes.

## Decision

Create `jenkins-devops-acrazie` as a substantive general skill for one application repository. It owns Jenkins-wide inspection, decision capture, approval, ADR lifecycle, pipeline generation/modernization/diagnosis, immutable promotion, deployment safety, validation, and reporting.

Add stack specialists progressively. The planned family is:

- `jenkins-js-ts-acrazie`;
- `jenkins-python-acrazie`;
- `jenkins-rust-acrazie`;
- `jenkins-go-acrazie`;
- `jenkins-symfony-php-acrazie`.

The core must work without a specialist. It may discover a verified specialist and, after explicit approval, offer a portable `npx skills` installation. It must never fabricate availability or silently install a skill.

Deployment-target guidance remains in the general skill as VM/SSH, Docker/Compose, Kubernetes, AWS, Azure, and Google Cloud adapters. Creating skills for every stack-target combination is rejected.

Controller administration, plugin installation, global agent management, and Jenkins Configuration as Code are excluded from the first scope.

## Alternatives considered

### One monolithic Jenkins skill
Rejected because stack recipes and deployment variants would increase context cost, coupling, and maintenance burden.

### Stack skills without a general core
Rejected because Jenkins-wide safety and delivery invariants would be duplicated and could diverge.

### Pure routing hub
Rejected because missing or unavailable specialists would block common Jenkins work and add an unnecessary indirection layer.

### Skills for every stack and deployment-target pair
Rejected because the combinatorial family would duplicate most content and be difficult to discover and maintain.

## Consequences

- The core remains independently useful and testable.
- Stack-specific precision can evolve without bloating the core.
- A clear specialist contract is required to prevent bypassing approval and safety rules.
- The first release cannot claim specialist availability; those skills must be published and evaluated separately.
- `jenkins-js-ts-acrazie` is the first planned specialist after the core is accepted.
