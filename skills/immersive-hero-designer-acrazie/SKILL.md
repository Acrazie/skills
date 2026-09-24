---
name: immersive-hero-designer-acrazie
description: >-
  Design and build an original, complete immersive web hero using the right medium for the effect: supplied or approved video, image sequence, 3D, Canvas, or CSS. Invoke explicitly to create a cinematic, interactive, or scroll-driven section in an existing site; not for copying a reference, redesigning a whole site, or making a standalone video without a web hero.
disable-model-invocation: true
---

# Immersive Hero Designer / Acrazie

Build a distinctive, working hero that earns attention without sacrificing the message or the rest of the page. Treat references as evidence of visual intent, not as code or assets to copy. The deliverable is the complete section: visual, semantic heading and supporting copy, relevant action, and integration into the user's site.

## Invocation and boundary

Run only when the user explicitly invokes this skill. If activated implicitly, ask for explicit invocation before starting. Work on one hero, not a whole-site redesign. Keep existing navigation, brand, content conventions, and framework unless the user requests a change.

This skill owns medium selection, art direction, media approval, and integration of a complete hero. For a procedural Canvas scene or pointer-reactive ambient backdrop alone, use `canvas-banner-designer-acrazie` instead; if it is the chosen medium within a complete hero, follow that skill's rendering and lifecycle contract rather than inventing a second one. Do not force video when CSS, images, Canvas, or 3D better serve the approved concept.

## 1. Inspect and frame

Read project instructions, the target route/component, styles, dependencies, existing assets, and any user references before proposing implementation. Inspect references in a browser when possible; distinguish observed motion and interactions from guesses based on screenshots or descriptions. Identify the intended audience, exact message and action, focal point, contrast, mobile crop, and constraints. Use factual project copy; ask for missing claims rather than inventing them.

Ask only unresolved choices that materially change the result. If the brief is open, propose two or three short directions differentiated by composition, medium, interaction, mobile treatment, and cost; wait for the user's selection. If direction and assets are already precise, implement directly. Do not silently switch from an approved direction to a cheaper-looking generic gradient or stock hero.

## 2. Select medium and approve assets

Choose the least complex medium that achieves the selected effect:

- **HTML/CSS:** typography, layers, transitions, and simple parallax.
- **Video:** continuous cinematic footage with a deliberate poster and crop; not for frame-accurate scroll scrubbing by default.
- **Image sequence:** discrete or frame-accurate scroll storytelling when loading and memory budgets permit.
- **Canvas/WebGL or 3D:** genuinely interactive or procedural depth. Reuse an installed renderer or the Canvas specialist when appropriate; explain a material new dependency before adding it.

Prefer supplied assets. Before integrating hero media, present a compact approval batch with each file or source, proposed placement, crop/edit, and known usage rights; wait for explicit approval. A changed selection requires another approval. Reading assets to assess them is not approval to publish or integrate them. Do not reuse third-party example code, branding, media, or text without a compatible license and user authorization; an unknown license is not permission.

If supplied assets are insufficient, explain the gap and propose generation of the needed image, sequence, or video only when a suitable tool is actually available. State likely format, purpose, limitations, and any known cost; wait for explicit approval before generating or using the result. Never assume a paid service, promise video generation without tooling, expose credentials, or substitute a still image while claiming to have delivered video. Obtain a separate integration approval for newly generated assets.

## 3. Integrate a usable hero

Use the project's actual framework and build tooling. Keep heading, copy, links, and controls in semantic DOM even when imagery is rendered in video or Canvas. Preserve readable contrast over every frame, keyboard operation, visible focus, and a useful static state if media fails. Maintain meaningful page flow; default to normal scrolling. Use scroll locking or scroll-jacking only when explicitly requested, with a clear way through, touch/keyboard behavior, and a non-locked reduced-motion alternative.

For video, use browser-compatible delivery, a poster, appropriate `preload`, responsive crop, and honest loading/error fallback. Muted inline playback may be attempted where suitable, but autoplay is not guaranteed. Never autoplay audio. Provide accessible pause/play control for nonessential moving media; do not hide essential information inside the video. Avoid downloading full-resolution media unnecessarily on narrow or constrained devices.

For image sequences and 3D, bound decoded memory, requests, pixel density, and work while offscreen. Avoid per-frame layout thrash and multiple uncontrolled animation loops. Make pointer effects optional, not necessary to understand or operate the hero. Respect `prefers-reduced-motion` at load and on change: show a stable, well-composed state with no forced scrub, autoplay, or spatial animation. Clean up observers, listeners, media state, and animation handles on unmount. Prefer a simpler static treatment when motion cannot meet performance and accessibility needs.

## 4. Prove and hand off

Run the smallest relevant project checks. Preview the **integrated** section at desktop and narrow widths; inspect composition and text legibility, keyboard and touch paths, pause and reduced-motion behavior, media failure/fallback, and navigation to the next section. Exercise resize and unmount/remount for scripted effects. Check loading cost and runtime behavior with available tools; do not claim a frame rate, Core Web Vitals score, or device coverage without measurement.

Deliver exact changed paths and how to run or view the result. Summarize chosen medium, approved asset sources, interactions, fallback, tests actually run, and unresolved limitations. Request focused feedback on visual composition, motion pace, crop, and message clarity. Do not present reference screenshots or a static mockup as proof of working interaction.
