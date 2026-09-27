# Separation of Frontend Portal to site/ and Migration to Bun

We decided to relocate the Astro frontend documentation portal from `docs/` to `site/` and migrate its package management and build toolchain from `npm` to `bun`. The `docs/` directory is preserved exclusively for project documentation, architecture records (`docs/adr/`), and repository audit reports (`docs/audits/`).

## Status

accepted

## Context

The Astro documentation portal was historically bootstrapped in `docs/` due to its initial deployment on GitHub Pages. Following migration to Dokploy (containerized Nginx), the `docs/` folder suffered from semantic overload: it housed both frontend application code (Astro, TypeScript, Tailwind, assets, lockfiles) and repository governance documentation (`docs/adr/`).

Furthermore, package installation and builds used `npm`. Switching to `bun` accelerates local builds and CI container compilation, while standardizing the project on a modern text-based lockfile (`bun.lock`) natively supported by Dependabot.

## Considered Options

1. **Keep frontend in `docs/` with npm**: Preserves status quo but perpetuates semantic ambiguity between application code and architecture records.
2. **Move frontend to `site/` while keeping npm**: Resolves the folder semantic overload but misses the performance and tooling improvements offered by Bun.
3. **Move frontend to `site/` and migrate to Bun**: Chosen. It cleanly establishes `site/` as the web presentation layer, reserves `docs/` strictly for architectural and audit records (`docs/adr/`, `docs/audits/`), and provides faster build times with `bun`.

## Consequences

- The Astro application now resides entirely in `site/` (`site/package.json`, `site/astro.config.mjs`, `site/src/`, `site/public/`, `site/bun.lock`).
- `docs/` is now reserved solely for repository-level documentation (`docs/adr/`, future `docs/audits/`).
- `Dockerfile` utilizes `oven/bun:1-alpine` for the build stage and serves static output via `nginxinc/nginx-unprivileged:alpine`.
- CI workflow in `.github/workflows/ci.yml` runs `build-site` via `oven-sh/setup-bun@v2`.
- `.github/dependabot.yml` is updated to track `bun` dependencies in `/site`.
