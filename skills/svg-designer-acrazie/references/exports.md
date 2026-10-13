# SVG, Raster and Favicon Exports

Read this only for requested raster or favicon files. Common export authority and
validation apply to icons and banners; select the checks fitting the approved target.

## Authority and renderer

Use only approved formats, dimensions and exact output/replacement paths. Inspect
installed renderer/version and current version-matched command documentation before
execution. Candidates include resvg, librsvg, Inkscape, Sharp and CairoSVG; no tool
is mandatory or certified by this list. Use ImageMagick only after verifying its
actual SVG delegate. Do not install a renderer without separate permission.
Download-capable wrappers such as `npx` are not an installation bypass.

Inspect source, fonts and external resources before conversion. Do not execute
untrusted scripts, fetch private/external resources, write outside approved paths
or weaken CSP implicitly. Preserve source SVG and transparency unless an approved
background is requested. No suitable renderer means a disclosed export blocker,
not a renamed file or fabricated preview.

## Raster files

Render each requested size from the canonical SVG instead of repeatedly scaling a
small PNG. Verify format support and actual pixel dimensions after writing. Test
font fallback and, where applicable, light/dark backgrounds or `currentColor`.
A high-DPI variant is a requested output decision, not an automatic multiplier.
Do not generate a default set of sizes or formats from a remembered platform recipe.

## Favicons and application assets

Only for a favicon/app-icon target, inspect the actual HTML/manifest conventions.
Select SVG, ICO, touch icon or application PNGs from the consuming project's needs.
Application markup/manifest changes and replacement of an existing set require their
own scoped realization approval; export permission does not authorize integration.

An ICO must be encoded as ICO and contain the requested embedded sizes. Renaming a
PNG to `.ico` is invalid. Verify real file type and enumerate embedded frames when
tooling supports it. Simplify or pixel-hint a dedicated tiny variant only when the
ordinary source loses essential topology at the actual smallest target size.

## Final evidence

Verify XML/namespace, viewBox, transformed bounds, strokes, font rendering and absence
of unintended clipping. Check gaps, apparent weight and defining metaphor for small
marks; check text hierarchy, actual crop and safe-area applicability for banners.
Validate actual raster dimensions and preserved transparency. Separate checks passed,
failed, unavailable and not executed. Local exports do not prove deployment, device
coverage or acceptance by a live platform.
