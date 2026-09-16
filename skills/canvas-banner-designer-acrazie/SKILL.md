---
name: canvas-banner-designer-acrazie
description: Design and implement animated HTML Canvas banners, web heroes, and ambient backgrounds with purposeful mouse interaction. Use when the user wants a living landscape, procedural scene, interactive line field, atmospheric backdrop, or generative header delivered as standalone HTML or a component in an existing web project. Not for Canva documents, static SVG/social cards, whole-site redesigns, or scroll-only animation.
---

# Canvas Banner Designer / Acrazie

Create a distinctive scene that lives behind real content, not a generic particle wallpaper. Deliver working browser code: standalone HTML or an integration in the user's framework. This complements `svg-banner-designer-acrazie`; it does not replace static image exports or promise JavaScript animation on platforms that only accept images.

## 1. Establish the brief

Inspect the target files, existing visual language, framework, dependencies, and reference supplied by the user before editing. Ask only unanswered questions that change the result:

- **Delivery:** standalone HTML, or a component integrated into a named project? For integration, locate the actual route and lifecycle owner rather than assuming React.
- **Scene:** subject, atmosphere, palette, composition, text, and intended audience. Identify where the eye should land and where content needs quiet space.
- **Motion:** ambient behavior, mouse response, intensity, and what remains on touch devices or with reduced motion.
- **Constraints:** container dimensions, supported devices, dependencies, asset rights, and performance targets when specified.

If “canva” could mean Canva rather than HTML Canvas, clarify before implementation. If the destination is GitHub README, Open Graph, or a social banner, explain that it cannot execute this canvas; offer a static SVG/PNG or a separate hosted web experience instead.

Inspect references in a browser when available. Separate observed appearance and behavior from guesses about implementation. A screenshot proves composition, not motion or a rendering engine. If the reference is inaccessible, say so and request a capture only when fidelity depends on it. Use visual principles, not copied branding, text, or unlicensed assets.

## 2. Select a visual direction

Unless the user has locked a direction or asked for immediate production, offer two or three compact `CanvasDraft` concepts and wait for selection. Read [references/canvas-draft.md](references/canvas-draft.md) for the format and visual families.

Distinguish concepts by scene and behavior, not only color. Specify the idle composition, motion rhythm, pointer influence, mobile crop, and static alternative. Make the tradeoff between visual ambition and rendering cost explicit.

Choose the simplest renderer that preserves the approved effect:

- **Canvas 2D:** layered landscapes, illustrated clouds, flow lines, moderate particles, trails, and modest parallax.
- **WebGL:** effects requiring per-pixel shaders, volumetric appearance, or dense fields that cannot reasonably fit Canvas 2D. Prefer a fitting dependency already installed. Explain new dependencies before adding them.
- **HTML/CSS:** keep headings, links, controls, layout, and simple overlays here. If the requested result needs only CSS, say so rather than adding an unnecessary canvas.

Do not silently turn an illustrated landscape into blurred gradients because gradients are easier. Conversely, do not add 3D machinery for a simple 2D drawing. The scene determines the engine.

## 3. Implement the scene and its lifecycle

Read [references/runtime-contract.md](references/runtime-contract.md) before implementation; it owns the lifecycle, accessibility, and verification contract.

Keep three responsibilities clear without building a framework:

1. **Semantic shell:** real DOM content and usable controls above a decorative canvas, plus a static visual fallback.
2. **Scene renderer:** stable seeded geometry, time-based drawing, bounded local pointer influence, and responsive composition.
3. **Lifecycle owner:** initialization, resizing, animation scheduling, motion preferences, visibility, and complete disposal.

Use one animation loop per scene. Input handlers update targets; they do not start independent loops. Pointer movement should reveal depth, displace nearby elements, or affect a scene-specific force—not merely drag the entire banner around. Return smoothly to the ambient state on pointer leave. Never make hover necessary for understanding or operating the page.

For standalone delivery, prefer a self-contained `index.html` with no build step or network dependencies unless approved assets require them. For integration, use the actual framework's mount/unmount conventions, scoped styles, and existing build tooling. Avoid browser globals during server rendering. Deliver a real mounting example and the commands needed to run it; do not substitute an unrelated HTML simulation for the component preview.

Limit configuration to requested or genuine integration needs. Do not ship a scene engine, plugin system, generic shader library, or unrelated page redesign.

## 4. Prove the result

Use the runtime contract's test matrix. Inspect a desktop and narrow/mobile rendering, observe idle animation over time, exercise pointer entry/movement/leave, and verify that the actual title and controls remain readable and usable.

Check reduced motion, pause/resume, hidden/offscreen suspension, resize, and cleanup. For components, include remount and multiple-instance behavior. For WebGL, verify context failure and context loss. Run the project's smallest relevant build/type/test checks.

Fix issues in a bounded pass, then recheck affected behavior. Distinguish measured results from source inspection and untested states. Do not claim smooth 60 FPS, zero leaks, device coverage, or accessibility conformance from screenshots alone.

## 5. Deliver and refine

Provide:

- The runnable HTML or integrated component, with exact file paths and startup/integration instructions.
- A live preview when tools permit; otherwise provide the files and disclose the preview limitation. Screenshots are supporting evidence, not a substitute for reviewing motion.
- A concise description of the scene, renderer, mouse interaction, touch behavior, reduced-motion result, and static fallback.
- Checks actually performed and remaining limitations.

Ask for focused visual feedback: composition, movement pace, pointer feel, and text legibility. Refine the selected direction rather than replacing its identity. Add image/video exports only when requested and supported by available tools; never present a still image as an animated deliverable.
