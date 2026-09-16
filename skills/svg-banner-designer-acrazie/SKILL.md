---
name: svg-banner-designer-acrazie
description: Design custom vector SVG banners, social cards, and header graphics with platform-specific safe zones, typography, and optional PNG exports. Use when creating or updating banners for GitHub READMEs, OpenGraph cards, X/Twitter, LinkedIn, YouTube, or blog headers.
---

# SVG Banner Designer / Acrazie

Design distinctive, clean vector SVG banners and social preview cards tailored to their platform and audience. Deliver clean native vector markup, not raster art, with proper typography, visual hierarchy, and safe zone compliance.

## 1. Intake

Identify core constraints before designing. Ask only unanswered questions that directly shape composition:

- **Target platform & aspect ratio**: GitHub README, Open Graph card, X/Twitter header, LinkedIn banner, YouTube banner, or blog hero. Read [references/presets.md](references/presets.md) for standard dimensions and safe zones.
- **Content**: Project or brand name, tagline, badges/tech stack, call-to-action or URL.
- **Visual tone**: Minimalist modern, cyberpunk/dark tech, editorial/clean corporate, abstract geometric, or generative.
- **Brand palette**: When the user requests the signature Acrazie retro-tech language or orange-to-violet palette, read [references/visual-identity.md](references/visual-identity.md).

Progress swiftly: if constraints are already provided in the prompt, proceed immediately to concepts.

## 2. Concept phase

Unless the user requests immediate production or provides a locked layout, present 2 to 3 distinct visual directions using compact `BannerDraft` notation. Read [references/banner-draft.md](references/banner-draft.md) for draft structure and wireframe rules.

Each direction must include:
- Name and visual metaphor (e.g., Split Terminal, Centered Monolith, Asymmetric Glow)
- ASCII / block wireframe illustrating spatial composition, text placement, focal art, and platform safe zones
- Key layout recipe (grid structure, focal element, background treatment, typography weight)
- Distinguishing strength and potential tradeoff

Ask the user to select, reject, or combine directions. Once a direction is elected, proceed autonomously to full SVG production.

## 3. SVG production

Generate clean, valid SVG markup directly:

- **ViewBox & sizing**: Set `viewBox="0 0 W H"` matching the chosen preset. Ensure responsive scaling via `width="100%"` with appropriate aspect ratio preserving attributes.
- **Safe zones**: Never place essential text, logos, or focal points inside platform-occluded zones (e.g., avatar overlaps on Twitter/LinkedIn, mobile crops on YouTube).
- **Typography**: Use robust SVG `<text>` elements with clean font stacks (`system-ui`, `-apple-system`, `Inter`, `sans-serif`, or `monospace` for tech contexts). Define font sizes, line heights, font weights, and letter spacing explicitly.
- **Visual elements**: Build backgrounds using native SVG `<defs>`: linear/radial gradients, subtle grid `<pattern>`, glow filters, or geometric vector shapes. Avoid embedded external raster bitmaps.
- **Code cleanliness**: Format SVG with clear grouping (`<g id="...">`), semantic classes or inline presentation attributes, and clean coordinate numbers.
- **Theme adaptability**: Default to dark mode or high-contrast themes popular in developer ecosystems, unless brand guidelines specify light backgrounds.

Deliver the SVG file and provide a concise summary of composition and safe zone handling.

## 4. Refinement and export

- **Iteration**: Adjust hierarchy, font size, contrast, or accent motifs based on user feedback.
- **Export**: When PNG or raster assets are requested, read [references/exports.md](references/exports.md) to inspect and invoke local rendering tools (`resvg`, `rsvg-convert`, `sharp`, `inkscape`, or `cairosvg`).
- **Validation**: Verify that the SVG parses as valid XML, has no clipped content outside the `viewBox`, respects safe zones, and that exported PNG dimensions match requested resolutions.
