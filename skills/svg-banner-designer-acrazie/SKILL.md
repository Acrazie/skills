---
name: svg-banner-designer-acrazie
description: Design custom vector SVG banners, social cards, and header graphics with platform-specific safe zones, typography, and optional PNG exports. Use when creating or updating banners for GitHub READMEs, OpenGraph cards, X/Twitter, LinkedIn, YouTube, or blog headers.
---

# SVG Banner Designer / Acrazie

Design distinctive, clean vector SVG banners and social preview cards tailored to their platform and audience. Deliver clean native vector markup, not raster art, with proper typography, visual hierarchy, and safe zone compliance.

## 1. Intake

Identify core constraints before designing. Ask only unanswered questions that directly shape composition:

- **Target platform & aspect ratio**: GitHub README, Open Graph card, X/Twitter header, LinkedIn banner, YouTube banner, or blog hero. Read [references/presets.md](references/presets.md) for standard dimensions and safe zones.
- **Content & Text Minimalism**: Default strictly to essential branding (Brand Name / Wordmark only, or at most a single short micro-tagline). **Do not treat banners as infographics**: avoid multi-line body paragraphs, marketing bullet points, feature lists, or decorative telemetry clutter unless explicitly requested.
- **Visual tone**: Minimalist modern, high-contrast geometric, editorial, or quiet tech. Prioritize breathing room over decorative density.
- **Brand palette**: When the user requests the signature Acrazie retro-tech language or orange-to-violet palette, read [references/visual-identity.md](references/visual-identity.md).

Progress swiftly: if constraints are already provided in the prompt, proceed immediately to concepts.

## 2. Concept phase

Unless the user requests immediate production or provides a locked layout, present 2 to 3 distinct visual directions using compact `BannerDraft` notation. Read [references/banner-draft.md](references/banner-draft.md) for draft structure, wireframe rules, and anti-pattern guidelines.

Each direction must include:
- Name and visual metaphor (e.g., Split Terminal, Centered Monolith, Asymmetric Glow)
- ASCII / block wireframe illustrating spatial composition, text placement, focal art, and platform safe zones
- Key layout recipe (grid structure, focal element, background treatment, typography weight)
- Distinguishing strength and potential tradeoff

Ask the user to select, reject, or combine directions. Once a direction is elected, proceed autonomously to full SVG production.

## 3. SVG production

Generate clean, valid SVG markup directly:

- **ViewBox & sizing**: Set `viewBox="0 0 W H"` matching the chosen preset. Ensure responsive scaling via `width="100%"` with appropriate aspect ratio preserving attributes.
- **Safe zones & framing**: Maintain at least 50–80px of internal padding around the canvas edges. Ensure all strokes, transforms, and rotated elements remain fully visible within bounds. Respect avatar occlusion zones (e.g., bottom-left on Twitter/LinkedIn).
- **Negative space & visual restraint**: Banners must breathe. Aim for at least 50% to 65% uncluttered negative space. Avoid the "cockpit syndrome" (stacking dense grids, excessive telemetry ticks, multiple concentric rings, and busy speed lines simultaneously).
- **Typography & text-box anti-pattern**:
  - Use robust SVG `<text>` elements with clean font stacks (`system-ui`, `-apple-system`, `Inter`, `sans-serif`, or `monospace` for tech contexts).
  - **CRITICAL ANTI-PATTERN**: Never wrap `<text>` inside a fixed-width `<rect>` pill or container. Because font metrics vary across operating systems and browsers, text will inevitably overflow fixed containers. Structure text through font size, weight, tracking, color contrast, and open rule lines rather than enclosed boxes.
- **Visual elements**: Build backgrounds using native SVG `<defs>`: linear/radial gradients, subtle grid `<pattern>`, glow filters, or geometric vector shapes. Avoid embedded external raster bitmaps.
- **Code cleanliness**: Format SVG with clear grouping (`<g id="...">`), semantic classes or inline presentation attributes, and clean coordinate numbers.
- **Theme adaptability**: Default to dark mode or high-contrast themes popular in developer ecosystems, unless brand guidelines specify light backgrounds.

Deliver the SVG file and provide a concise summary of composition and safe zone handling.

## 4. Refinement and export

- **Iteration**: Adjust hierarchy, font size, contrast, or accent motifs based on user feedback.
- **Export**: When PNG or raster assets are requested, read [references/exports.md](references/exports.md) to inspect and invoke local rendering tools (`resvg`, `rsvg-convert`, `sharp`, `inkscape`, or `cairosvg`).
- **Validation**: Verify that the SVG parses as valid XML, has no clipped content outside the `viewBox`, respects safe zones, and that exported PNG dimensions match requested resolutions.
