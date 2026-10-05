# Acrazie Skills Context & Domain Glossary

This document defines the ubiquitous language and domain vocabulary across the skills repository.

## Jenkins Family

**Jenkins Parent**:
The `jenkins-devops-acrazie` skill, responsible for approving, orchestrating, and validating pipeline modifications and production deployments across application repositories.

**Symfony Specialist**:
The `jenkins-symfony-php-acrazie` specialist skill, dedicated to interpreting Symfony application architecture, CI requirements, and runtime dependencies for the Jenkins Parent. It provides CI constraints without directly executing deployment stages.
*Avoid*: Generic PHP specialist, Symfony deployer.

**Python Specialist**:
The `jenkins-python-acrazie` specialist skill, dedicated to Python packaging, testing (pytest/tox), and runtime containerization for Jenkins pipelines.

## Skill Lifecycle & Refinement

**Skill Refiner**:
The interactive feedback workflow (`skill-refiner-acrazie`) that observes real skill usage, records append-only journals under `.skill-refiner/`, and updates living Architectural Decision Records (ADRs).
*Avoid*: Skill Improver (deprecated legacy name).

**Audit Record**:
A formal, read-only technical evaluation artifact created under `docs/audits/` via `audit-repository-acrazie`.

## Complementary Development Skills

**Usage-led Product Critique**:
A recommendation-only assessment of an existing product's features and codebase against user needs, verifiable benefits, simplicity, and total cost. It distinguishes reasons to retain, simplify, retire, or replace existing behavior from focused technical audits and tooling migrations.
*Avoid*: Modernization for its own sake, implementation workflow, general code review.

**Interview Foundation**:
The reusable `interview-acrazie` skill that clarifies user-owned decisions and produces an approved Task Contract without executing the task.
*Avoid*: Development orchestrator, feature implementer.

**Feature Builder**:
The explicitly user-invoked `feature-builder-acrazie` skill that realizes new application behavior from an approved Task Contract with criterion-linked evidence.
*Avoid*: Bug fixer, refactorer, agent reviewer.

**Test Retrofitter**:
The explicitly user-invoked `test-retrofitter-acrazie` skill for adding automated evidence to existing untested or insufficiently tested behavior, distinct from implementing or correcting functionality.
*Avoid*: Feature builder, bug fixer, CI migrator.

**Task Contract**:
The shared, approved outcome record used by the Interview Foundation and its callers, defining scope, observable success criteria, decisions, and expected evidence, with actual delivery evidence recorded separately.
*Avoid*: ADR, interview transcript, implementation plan.

## Verification & Migration Discipline

**Adversarial Review**:
A split-context evaluation role where an agent inspects changes under the strict premise that the code is incorrect, seeking memory hazards, concurrency flaws, and semantic drift while explicitly rejecting stub workarounds.
*Avoid*: General code review, PR summarizer, peer review.

**Semantic Drift**:
Subtle runtime divergence between syntactically similar constructs across languages, runtimes, or APIs (e.g. macro erasure in release builds, eager argument evaluation in fallbacks, truncation vs flooring).
*Avoid*: Type error, compile error, syntax mismatch.

**Proof of Flaw**:
A concrete execution scenario, edge-case input, or state trace provided by an Adversarial Reviewer that conclusively demonstrates why a proposed change fails, without prescribing the implementation patch.
*Avoid*: Fix suggestion, code recommendation.

**Mechanical Port**:
A source-to-target language code porting discipline prioritizing 1:1 structural and syntactic mirroring over premature idiomatic refactoring, validated against an existing agnostic test oracle.
*Avoid*: Rewrite from scratch, architectural redesign, incremental hybrid migration.

**Test Oracle Invariant**:
A mandatory pre-condition for mechanical porting requiring a language-independent or black-box test suite to exist and pass against the source implementation before code migration begins, preventing unverified functional drift.
*Avoid*: Synthetic ad-hoc testing, post-hoc test generation.

**Paradigm Mapping**:
A systematic pre-translation matrix documenting the foundational semantic translations between source and target languages across four dimensions: memory/lifecycle, error handling, concurrency, and type systems/nullability.
*Avoid*: Informal migration notes, syntax cheat sheet.

**Diagnostic Work Queue**:
A structured, persisted partition of compiler or linter diagnostic outputs (e.g. JSON/SARIF or POSIX error dumps) grouped by module or crate, dispatched to parallel worker agents without redundant whole-workspace recompilation.
*Avoid*: Interactive compiler debugging, trial-and-error recompilation loop.

**Isolated Worker Guardrails**:
Operational constraints placed on parallel coding sub-agents prohibiting workspace-wide mutations (`git stash`, `git reset`, un-scoped checkouts) and slow root build commands within inner iteration loops.
*Avoid*: Uncoordinated git operations, agent stepping.

## Runtime & Memory Diagnostics

**Memory Leak Diagnostician**:
The specialist skill `memory-leak-diagnostician-acrazie` dedicated to isolating monotonic heap and RSS growth, mapping GC retainer trees, and generating surgical un-retention patches.
*Avoid*: Static linter, feature builder, generic debugger.

**Retainer Tree**:
The directed acyclic graph of strong references extending from a Garbage Collection root (global scope, timer, DOM node, captive lexical scope) to a target live object, preventing its reclamation by the GC.
*Avoid*: Call stack, dependency graph, heap profile.

**Un-Retention Patch**:
A minimal structural code change that severs an anchor reference (e.g. unbinding closures, RAII disposal, once listeners, WeakRef/WeakMap) without altering functional domain logic.
*Avoid*: Functional rewrite, garbage collector tuning, blind cache clearing.

## Documentation & Deployment Platform

**Skills Documentation Site**:
The Astro-powered documentation portal located in `site/` and built with Bun, compiled into a containerized static site served by an unprivileged Nginx process on port 8080 (`skills.acrazie.dev`).

**Site UI Chrome**:
The localized navigational, filtering, search, and layout elements of the Skills Documentation Site presented in the user's selected language.
*Avoid*: Application skin, site chrome.

**Browser Color Scheme**:
The user-agent and operating system display preference (`prefers-color-scheme: light` or `dark`) governing the client chrome (tab strip, window frame), independent of the site's fixed dark visual aesthetic.
*Avoid*: Site theme, site dark mode.

**Brand Mark**:
The four-bar horizontal geometric glyph representing the Acrazie identity, rendered with `fill="currentColor"` in UI components and adaptive contrast in favicons.
*Avoid*: Skills logo, hamburger icon.

**Adaptive Favicon**:
The dual-file SVG favicon strategy (`site/public/favicon.svg` and `site/public/favicon-dark.svg`) synchronized via a client-side `matchMedia` listener, rendering the Brand Mark in `#151515` on light browser chrome and `#fafafa` on dark browser chrome over 100% transparent backgrounds without container chrome or DOM-level `.ico` references.
*Avoid*: Static favicon, themed icon container, internal SVG media queries.

**Skill Catalog Metadata**:
The localized high-level properties of a skill (display title, category, concise summary) used for discovery and browsing on the portal.
*Avoid*: Prompt copy, skill specification.

**Skill Specification**:
The authoritative, untranslated agent instructions and domain references (`SKILL.md`, `references/*.md`) executed by AI coding agents.
*Avoid*: Documentation markdown, website copy.

**Dokploy Application Service**:
The containerized service hosted on the Netcup VPS, connected to Traefik via `dokploy-network` and routed through the Cloudflare Tunnel wildcard.

**Dokploy Deployment Webhook**:
The protected endpoint (`deploy.acrazie.dev`) authenticated via Cloudflare Zero Trust Service Token headers (`CF-Access-Client-Id` and `CF-Access-Client-Secret`), triggered by the GitHub Actions `deploy-production` job only after CI validation succeeds.
*Avoid*: Enabling Auto Deploy in Dokploy UI (which would bypass CI tests).
