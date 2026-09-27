# Documentation Site Internationalization Architecture

The Acrazie Skills documentation portal (`skills.acrazie.dev`) serves an international community of developers and agent builders. We decided to implement full multi-language support for English (`en`), French (`fr`), and Simplified Chinese (`zh`) using Astro 5 native i18n routing, keeping English as the root default (`/`), localized routes under `/fr/` and `/zh/`, and centralizing UI and skill catalog translations in `docs/src/i18n/` while leaving core `SKILL.md` specifications in canonical English.

## Status

accepted

## Context

The documentation portal was previously partially bilingual (French UI with English skill specifications) without explicit routing or language switching. With developers using agents across French, English, and Chinese ecosystems, the portal needed a clear, scalable localization model without compromising the agent prompt instructions published to `skills.sh`.

## Considered Options

1. **Full translation including `SKILL.md` prompt bodies**: Rejected because AI coding agents execute instructions best in canonical English, maintaining multi-lingual copies of prompts would multiply maintenance cost and risk instruction drift, and `skills.sh` expects single authoritative `SKILL.md` files.
2. **Translation keys inside `skills/<skill>/` frontmatter**: Rejected because it couples website localization concerns to core skill metadata and risks breaking repository validation scripts (`validate-skills.sh`, `check-skill-structure.sh`).
3. **Decoupled presentation dictionaries in `docs/src/i18n/` with Astro native routing**: Chosen because it cleanly isolates the Astro presentation layer from published agent skills, preserves root `/` for English while providing SEO-friendly `/fr/` and `/zh/` prefixes, and allows graceful fallback to English.

## Consequences

- The `docs/` Astro site manages translations in `docs/src/i18n/ui.ts` (Site UI Chrome) and `docs/src/i18n/skills.ts` (Skill Catalog Metadata).
- Root `/` serves English; `/fr/` and `/zh/` serve respective locales with identical page structures (`/fr/skills/[skill]/`, `/zh/skills/[skill]/`).
- A Header language switcher allows switching between `EN`, `FR`, and `ZH` while preserving the active route.
- Core skills in `skills/` remain untranslated and 100% compliant with `skills.sh` and CI validation hooks.
