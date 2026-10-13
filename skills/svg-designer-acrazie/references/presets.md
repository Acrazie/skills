# Platform Formats and Safe Zones

Use this reference to identify target constraints, not to select authoritative dimensions from a static table. Platform requirements, preview crops and avatar placement can change. Confirm the intended surface and current requirements from official documentation or the actual target UI before production; record the source, date and applicability. User-supplied dimensions settle the requested canvas, not compatibility with a platform.

## Target-specific checks

| Surface | What to establish before claiming compatibility |
| :--- | :--- |
| GitHub repository social preview | Accepted upload dimensions, aspect ratio, file limits and previews on relevant sharing surfaces. |
| GitHub README banner | Approved canvas, available content width, mobile scaling and light/dark background readability. There is no universal README banner size. |
| Open Graph / social preview | Requirements of each requested consumer, not only one assumed card ratio; inspect actual crop behavior. |
| X / Twitter header | Accepted canvas, desktop/mobile crops and actual avatar occlusion bounds. |
| LinkedIn personal or company header | Correct surface, upload constraints, responsive crops and avatar/logo occlusion. Do not transfer personal-header bounds to company pages. |
| YouTube channel banner | Accepted canvas and the current critical-content safe area across the requested TV, desktop, tablet and mobile views. Resolve differing measurements before production. |
| Blog / newsletter hero | Constraints of the actual theme, template or publishing platform and its responsive image handling. |

## Composition and validation

- Derive margins and essential-content bounds from the verified crop and placement. Treat occlusion coordinates as target-specific measurements, not universal constants.
- Keep essential branding visible across the approved views. Optional background artwork may extend beyond a crop; unintended clipping of text, strokes or focal content must be resolved.
- Use the entrypoint's content rules. Taglines, badges, code cards or feature lists are not implied by a platform choice; include them only when requested.
- Test readability, contrast and font rendering at actual display sizes and relevant backgrounds. A static wireframe cannot certify crop or safe-zone compliance.
- For YouTube, record one applicable canvas and safe-area definition from verified requirements instead of offering incompatible rectangles as interchangeable minima. Confirm it with the target preview where available.
- If official requirements or the target preview are unavailable, preserve an approved draft and disclose the missing compatibility check. Do not label historical dimensions as current, silently choose between conflicting measurements or claim validation from the SVG canvas alone.
