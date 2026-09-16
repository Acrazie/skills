# Canvas runtime contract

Apply this to both standalone HTML and framework components. These are behavioral requirements, not a mandatory class hierarchy or code template.

## Rendering and sizing

- Size against the host container, using `ResizeObserver` where available. CSS size and backing-store size are separate: use CSS-pixel drawing coordinates and a capped device pixel ratio (usually at most 2). Reset the transform after a backing-store resize; do not compound scaling.
- Bound geometry count, buffers, drawing resolution, and per-frame work. Cache static layers or reusable sprites when useful. Avoid full-resolution blur and fresh random geometry every frame.
- Advance simulation with elapsed time, not frame count. Clamp large deltas after suspension and reset the timestamp on resume, so a background tab does not cause a jump.
- Preserve a stable seed/layout across frames and ordinary resizes; recompute only what sizing requires. Avoid putting per-frame values into framework reactive state.
- Handle zero-sized containers without division by zero or scheduling useless work. Repaint a paused/static scene on a meaningful resize without resuming its animation.

## One scheduler, explicit eligibility

Treat these as independent conditions:

```text
animate = mounted AND rendererReady AND nonzeroSize
          AND documentVisible AND intersectsViewport
          AND NOT userPaused AND NOT reducedMotion
```

Initialization, resize, visibility, viewport intersection, pause controls, and media-query changes all reconcile the same scheduler. Keep at most one pending `requestAnimationFrame`; cancelling also clears its stored identifier. Returning onscreen must not override a user's pause or reduced-motion preference.

Use `visibilitychange` and `IntersectionObserver` to suspend background work. With no intersection API, degrade to document visibility rather than breaking rendering. A scheduler with no animated state should draw once and stop.

## Pointer behavior

- Derive pointer coordinates relative to the host's current bounding rectangle, not the viewport origin. Clamp input and influence radius. Read layout on input/resize rather than for every particle.
- Use Pointer Events. Passive handlers may record input on the host even when the canvas itself uses `pointer-events: none` to preserve links and selection.
- Use frame-rate-independent easing (for example `1 - exp(-k * dt)`), spring integration with bounded steps, or another stable method. Reset the target on `pointerleave`, `pointercancel`, and lost relevance.
- On coarse pointers or no hover, disable mouse-only response; preserve the ambient scene or its deliberate static variant. Do not capture touch scrolling, require dragging, hide the system cursor, or synthesize mouse interaction for essential content.
- Under reduced motion, disable both time-driven motion and spatial pointer motion. Updating the pointer target must not restart the loop.

## Accessibility and graceful failure

- Keep essential text, links, and controls in semantic DOM, never canvas pixels. Mark decorative canvases `aria-hidden="true"` and keep them out of the tab order. If the scene communicates information, provide a meaningful DOM equivalent.
- Reserve a stable host height/aspect ratio to avoid layout shifts. Keep sufficient contrast throughout moving frames, with a quiet zone or stable scrim if necessary. Focus indicators must remain visible.
- Respect `prefers-reduced-motion` at startup and when it changes. Show a composed static frame or static CSS/asset fallback, not an empty scene.
- For continuous automatic motion accompanying page content, provide a keyboard-accessible pause/resume control. Its label/state must reflect the actual behavior; do not offer “resume” that overrides reduced motion. A non-animated setting is a valid alternative.
- Keep a meaningful static background and DOM content visible before JavaScript and when rendering fails. Do not cover a fallback with an opaque blank canvas. Failed `getContext`, shader compile/link failure, or missing assets must not break the surrounding page.
- For WebGL context loss, prevent the default only when restoration is supported, stop work, release obsolete resources, and expose the fallback. On restoration, rebuild resources before reconciling animation eligibility. If recovery is not supported, stay on the fallback and disclose it.
- Do not add telemetry, external fonts, remote scripts, or assets by default. Preserve the project's CSP and loading conventions; use approved local assets where needed.

## Integration and cleanup

- Mount only after the DOM exists. Do not touch `window`, `document`, or canvas during module evaluation or server rendering.
- Scope listeners, drawing state, IDs, and styles per instance. Two banners must not share pointer state, pause state, or frame identifiers.
- On disposal, cancel pending frames, remove listeners (including media-query listeners), disconnect observers, and release GPU resources. Guard against late callbacks after teardown.
- In React, effect setup and cleanup must survive Strict Mode's development remount. Other frameworks should use their own lifecycle, not a React-shaped wrapper.
- Extend existing project ownership rather than creating a second animation service. Keep preview fixtures outside production routes unless requested.

## Smallest sufficient proof

Record the method and result, not just a checked box. Use browser automation or project tests where supported; source checks alone cannot establish motion quality.

| Scenario | Evidence to collect |
| --- | --- |
| Desktop and narrow viewport | No overflow/clipped content; focal scene and controls remain visible. |
| Idle animation | Compare frames at two times; intended elements move while layout stays fixed. |
| Pointer enter/move/leave | Bounded response and smooth return; links/selectable text still work. |
| Touch/coarse input | No hover dependency or scroll interception. |
| Pause and reduced motion | Stable frames; pointer movement does not animate; media-query change is honored. |
| Hidden and offscreen | No continued drawing; resume preserves explicit pause and does not create duplicate loops. |
| Resize and pixel ratio | Crisp bounded backing store, correct geometry, no stretch; paused view repaints without motion. |
| No JS / context unavailable | Designed fallback and usable semantic content remain. |
| Component mount/unmount/remount | No residual listeners/frames or double-speed animation; SSR/import and type/build checks pass. |
| Multiple components | Input, scheduler, and controls act independently. |
| WebGL, if used | Compile/link errors and context loss reveal fallback; restoration either works or remains safely static. |

For performance claims, state device/browser, viewport, duration, and measurement. Report untested cases explicitly. A successful build is not evidence of motion, accessibility, or cleanup correctness.
