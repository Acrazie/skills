---
name: svg-icon-designer-acrazie
description: Design original SVG logos and icons through compact concept drafts, then produce clean vector markup and requested PNG or favicon exports. Use for individual marks, small sets, app symbols, and favicons; not for editing raster artwork and not for producing ASCII art as the deliverable.
---

# SVG Icon Designer / Acrazie

Turn an icon or logo idea into a readable SVG without spending tokens on premature polished variants. ASCII rasters are geometry previews for comparing directions, not the product. The deliverable is general-purpose vector markup in the visual language the user elected.

## Intake

Infer constraints already present. Ask only unanswered questions that materially change the design, usually one to three at a time:

- intended meaning, product context, and target audience
- symbols or visual clichés to use or avoid
- style or existing icon family to match
- target sizes, color behavior, and required files

Interview progressively. Do not block ideation on details that can safely remain provisional. If the request is already precise, begin directly.

For abstract personal marks that should follow the user's curated logo taste, read [references/curated-abstract-marks.md](references/curated-abstract-marks.md). Treat that reference as optional visual vocabulary, not a default style for unrelated icon work.

When the user explicitly requests the Acrazie retro-tech wordmark language or its orange-to-violet palette, read [references/visual-identity.md](references/visual-identity.md). Remix its principles into original lettering; never trace the supplied references.

Once intake context is refined (meaning, audience, sizes known), read [references/inspiration-library.md](references/inspiration-library.md) alongside the interview to propose ideas. Use it strictly as creativity fuel: extract construction rules, never reproduce a linked logo.

## Concept phase

Unless the user requests immediate production or supplies a locked design, offer two to three genuinely different directions in compact `IconDraft` notation. Read [references/icon-draft.md](references/icon-draft.md) for its syntax and selection rules. Sample at least two different inspiration families per batch. Cap ASCII-forward *final* styles at one unless the user explicitly requests an ASCII or pixel-block mark. After the interview, re-read the When to use entries and shortlist the families that fit the user's own nuanced wording rather than forcing keyword matches.

Whenever presenting multiple visual directions, include one large, detailed ASCII geometry preview for every direction unless the user explicitly opts out. The raster is a stand-in for topology, not a preview of an ASCII logo. Build every raster from the same normalized geometry described by its recipe rather than drawing a loosely related symbol. Size rasters so the direction can actually be judged: no horizontal scrolling (vertical scrolling is acceptable). Choose the charset and any legend in the interview — never impose a default alphabet or symbol set. Show outer contour, internal voids, cuts, overlap, detached fragments, and relative scale. Never present ASCII as evidence of Bézier quality, antialiasing, exact stroke weight, or optical balance.

For each direction, include:

- short name and intended metaphor
- detailed ASCII geometry preview (charset chosen in the interview)
- geometric recipe
- distinguishing benefit
- likely risk at the smallest target size
- any shape that reads as a rendering bug at small size must be removed or made explicit

Ask the user to select, reject, or combine directions. Preserve prior decisions. Do not generate any SVG before the user explicitly elects a direction, unless the user explicitly wants a comparison sheet.

When source logos are supplied as taste references, extract shared design principles and remix them into new topology. Do not trace, closely reproduce, or merely recolor a reference mark.

## SVG production

Create vector markup directly; do not invoke raster image generation for code-native icons. Build the SVG from the elected geometry. Do not reduce it to a generic pictogram, and do not default the deliverable to an ASCII or pixel-block logo unless that language was elected.

- Use a deliberate `viewBox`, normally `0 0 24 24` unless target or family dictates another grid; use a large grid (512 units or more) when the detail requires it.
- Keep geometry editable and concise. Prefer primitives when they communicate structure; use paths when they improve output.
- Avoid scripts, external resources, embedded raster data, editor metadata, invisible objects, and arbitrary precision.
- Define `fill`, `stroke`, line caps, and joins explicitly. Prefer `currentColor` for adaptable monochrome icons unless fixed branding requires colors.
- Check clear space, optical centering, stroke consistency, negative space, and recognition at target sizes.
- Determine whether usage is decorative or meaningful before adding accessibility markup. Do not hard-code an unsuitable label.
- Preserve sharp features and intentional asymmetry; do not mechanically normalize geometry.

When comparison helps, create a minimal local HTML contact sheet that renders candidates large at the actual target sizes. Do not treat source-code inspection alone as visual validation.

Deliver the result as a large visual preview plus what to keep or adjust in plain language. Report generated paths, dimensions, and any converter dependency used only when requested.

## Refinement

Translate feedback into explicit changes: silhouette, metaphor, proportion, stroke, corner treatment, or color. Show only variants needed to resolve the current decision. When offering multiple refinement variants, give each variant a detailed ASCII raster under the same rules as the concept phase. Keep one canonical source SVG after approval unless variants were requested.

## Export and validation

Always keep the source SVG. Generate PNG or favicon assets only when requested. Read [references/exports.md](references/exports.md) before raster or favicon work.

Validate observable results:

- SVG parses as XML and has no broken references.
- Artwork fits the `viewBox` without accidental clipping.
- Rendered icon remains legible at every requested size.
- PNG dimensions and transparency match the request.
- ICO is a real multi-size ICO when requested, not a renamed PNG.

Report generated paths, dimensions, and any converter dependency used only when requested. Do not install dependencies or overwrite unrelated assets without permission.
