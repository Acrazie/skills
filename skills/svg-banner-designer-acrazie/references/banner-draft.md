# BannerDraft

Compact notation and block wireframes for exploring banner compositions during the concept phase.

---

## Draft Structure

Present 2 to 3 genuinely distinct directions. Each direction specifies its layout archetype, a spatial block wireframe, visual recipe, strength, and tradeoff:

```text
Direction A — Split Terminal
- Archetype: Split 55/45 (Left: Title + Tagline + Badges | Right: Vector Code Window)
- Safe zone compliance: Left margin 80px, right margin 80px, no avatar conflict.
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

### Example 1: GitHub / OG Social Card (Split 55/45)

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

### Example 2: Twitter / X Header with Avatar Occlusion

```text
+-------------------------------------------------------------+
|  ............                                   ..........  |
|                                                             |
|                          [T] CREATIVE STUDIO                |
|                          [s] Building the next web          |
|                                                             |
|  (AVATAR OCCLUSION)      [# Design]  [# Motion]  [# Vector] |
|  ( ~380px wide    )                                         |
+-------------------------------------------------------------+
```

### Example 3: YouTube Channel Banner with Safe Zone

```text
+-------------------------------------------------------------+
|  [Background artwork / ambient vector landscape: 2560x1440] |
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

4. **Bento Grid / Feature Cards**:
   - Best for: Feature-rich products, platforms, or multi-faceted toolkits.
   - Anatomy: 2 to 3 clean glassmorphism / card blocks highlighting distinct metrics, badges, or capabilities.

---

## Anti-Patterns & Traps to Avoid

1. **Text Overload & Infographic Clutter**:
   - Never turn a brand banner into an infographic or marketing feature list.
   - Avoid multiple body copy sentences, paragraphs, or lists of bullet points.
   - Favor pure brand authority: Wordmark + at most one short punchy phrase.

2. **Cockpit / Telemetry Clutter**:
   - Avoid piling up fake HUD elements: excessive crosshairs (`+`), random coordinates (`LAT/LON`), artificial progress bars, and dense grid overlays.
   - Every background element must serve the visual hierarchy, not clutter it.

3. **Text Enclosed in Fixed `<rect>` Containers**:
   - Avoid pill shapes or boxes wrapping text with fixed widths.
   - Cross-platform font metrics vary; text will clip or overflow the container box. Use open text layout with generous whitespace.

4. **Lack of Breathing Room**:
   - Always ensure 50% to 65% active negative space so the central mark commands attention.

