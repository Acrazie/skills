# SVG, PNG, and favicon exports

Read this only when raster or favicon files are requested.

## Choose a renderer

Inspect available local tools before choosing commands. Prefer a renderer with reliable SVG support, such as `resvg`, `rsvg-convert`, Inkscape, Sharp, or CairoSVG. Use ImageMagick only after confirming its SVG delegate renders the source correctly.

Do not install a renderer without permission. If none exists, preserve the validated SVG and explain the smallest required dependency or command rather than faking an export.

## PNG

Render separately at each requested pixel size from the source SVG. Do not repeatedly resize a small PNG. Preserve transparency unless the user requested a background. Check actual pixel dimensions after writing.

Common web sizes include `16`, `32`, `48`, `180`, `192`, and `512`, but generate only sizes justified by the target. Pixel-hint or simplify a dedicated tiny variant when the ordinary source loses important details at 16 px.

## Favicons

A practical web favicon set can contain:

- `favicon.svg` for modern browsers
- `favicon.ico` containing 16, 32, and 48 px images for compatibility
- `apple-touch-icon.png` at 180×180 when requested
- app PNGs and a web manifest only when the consuming project needs them

Inspect existing HTML and manifest conventions before editing a project. Do not overwrite an established favicon set without confirming intended replacement.

An `.ico` file must be encoded as ICO and should contain the requested embedded sizes. Renaming a PNG to `.ico` is invalid. Validate file type and, where tooling permits, enumerate embedded frames.

## Visual checks

Render against light and dark backgrounds when transparency or `currentColor` matters. Compare target sizes at 100% scale. Check clipping, accidental blur, collapsed gaps, uneven apparent weight, and loss of the defining metaphor.
