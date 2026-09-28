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
The dynamic SVG favicon (`site/public/favicon.svg`) utilizing embedded `@media (prefers-color-scheme)` queries to invert the Brand Mark ink (`#fafafa` in dark mode, `#151515` in light mode) over a transparent background without container chrome.
*Avoid*: Static favicon, themed icon container.

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
