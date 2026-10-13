# BannerDraft

Use this optional vocabulary when composition comparison helps. Choose readable
prose, a wireframe or an authorized preview for the actual decision; no fixed
question fields or notation is required. Concepts are not execution or export
approval. Reuse an elected direction; changed scope/assets need affected approvals.

Compact notation and block wireframes for exploring banner compositions during the concept phase. Examples are optional spatial sketches, not requested content, exact geometry or evidence of platform safety. Badges, code cards, metrics and extra copy belong only in a brief that requests them; default to the entrypoint's essential branding.

---

## Draft Structure

Present only genuinely distinct directions needed to resolve the brief. Each direction specifies its layout archetype, a spatial block wireframe, visual recipe, strength, and tradeoff:

```text
Option 1 — Split Terminal
- Archetype: Split 55/45 (Left: Title + Tagline + Badges | Right: Vector Code Window)
- Safe zone plan: Margins and occlusion checks derived from the verified target; not yet rendered or validated.
- Recipe:
  * Background: Radial glow (#1e1035 -> #0b0712) + subtle SVG dot grid
  * Left: Project title 56px bold, tagline 24px regular, 3 pill badges (Rust, Tokio, CLI)
  * Right: Stylized dark terminal window with syntax-highlighted commands and window controls
- Benefit: High-context technical appeal, instantly communicates dev tool value.
- Tradeoff: Code card requires high detail; less impactful if viewed at very small preview sizes.
```

---

## Wireframe Conventions

Use structured ASCII / block diagrams to illustrate spatial distribution and safe zones. Standard symbols:

- `[T]` Title / Primary wordmark
- `[s]` Subtitle / Tagline
- `[#]` Badges / Tech pills / Tags
- `[***]` Visual focal point (illustration, mockup, abstract geometry, logo mark)
- `(AVATAR)` Occlusion zone (e.g., Twitter/LinkedIn profile picture collision)
- `......` Background atmosphere / texture / glow

### Example 1: GitHub / OG Social Card (Only When Extra Copy and Cards Are Requested)

```text
+-------------------------------------------------------------+
|  ......                                             ......  |
|                                     +--------------------+  |
|    [T] PROJECT TITLE                | [***]              |  |
|                                     |     Vector Mockup  |  |
|    [s] Modern agentic toolkit       |     or Code Window |  |
|        for high-performance apps    |                    |  |
|                                     +--------------------+  |
|    [# v1.0]  [# Rust]  [# CLI]                              |
|  ......                                             ......  |
+-------------------------------------------------------------+
```

### Example 2: Twitter / X Header with Avatar Occlusion (Badges Only If Requested)

```text
+-------------------------------------------------------------+
|  ............                                   ..........  |
|                                                             |
|                          [T] CREATIVE STUDIO                |
|                          [s] Building the next web          |
|                                                             |
|  (AVATAR OCCLUSION)      [# Design]  [# Motion]  [# Vector] |
|  (verify target bounds)                                     |
+-------------------------------------------------------------+
```

### Example 3: YouTube Channel Banner with Safe Zone

```text
+-------------------------------------------------------------+
|  [Background artwork: approved canvas, verified safe zone] |
|                                                             |
|      +----------------- SAFE ZONE -----------------+        |
|      |    [***] LOGO   [T] CHANNEL TITLE           |        |
|      |                 [s] Weekly Deep Dives       |        |
|      +---------------------------------------------+        |
|                                                             |
|  [Background artwork continues outside to edge]             |
+-------------------------------------------------------------+
```

---

## Common Layout Archetypes

1. **Split Hero (50/50 or 60/40)**:
   - Best for: Developer tools, libraries, SaaS products.
   - Anatomy: Left side has crisp typographic hierarchy; right side has a high-craft visual component (code window, dashboard card, architecture flow, or geometric illustration).

2. **Centered Monolith**:
   - Best for: Design systems, artistic portfolios, creative brands, event announcements.
   - Anatomy: Symmetrical composition, central brand mark, high-impact headline, surrounded by radiating or balanced geometric vector accents.

3. **Asymmetric Flow / Golden Ratio**:
   - Best for: Social headers (Twitter/LinkedIn) where left-hand avatar occlusion requires shifting weight to the center-right.
   - Anatomy: Heavy content anchor at 60% X position, balanced by subtle background elements across the full canvas.

4. **Bento Grid / Feature Cards (Only When Requested)**:
   - Best for: Feature-rich products, platforms, or multi-faceted toolkits.
   - Anatomy: 2 to 3 clean glassmorphism / card blocks highlighting distinct metrics, badges, or capabilities.

---

## Anti-Patterns & Traps to Avoid

1. **Text Overload & Infographic Clutter**:
   - Do not turn a brand banner into an infographic or marketing feature list unless the brief explicitly requests that content.
   - Keep additional copy limited to what the brief requests and verify readability at the target size.
   - For a branding-only brief, favor the wordmark and at most one short phrase; do not add marketing content implicitly.

2. **Cockpit / Telemetry Clutter**:
   - Avoid piling up fake HUD elements: excessive crosshairs (`+`), random coordinates (`LAT/LON`), artificial progress bars, and dense grid overlays.
   - Every background element must serve the visual hierarchy, not clutter it.

3. **Text Enclosed in Fixed `<rect>` Containers**:
   - Do not assume a fixed-width box will fit every font or renderer.
   - Verify actual text bounds, padding and fallback fonts. Resize the container or use open layout when needed; a validated text box is not inherently an anti-pattern.

4. **Lack of Breathing Room**:
   - Check that the central mark and requested message remain legible at actual display sizes and crops. Adjust spacing to the composition rather than enforcing a fixed empty-area percentage.

