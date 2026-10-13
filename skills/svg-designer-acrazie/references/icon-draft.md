# IconDraft

Use this optional vocabulary only when compact geometry comparison helps. It is
not a public file format or required preview medium. Concepts may use prose,
wireframes, ASCII or an independently approved comparison sheet. They are not
execution or export approval. Reuse the elected direction; changed scope/assets
still need their affected approvals. No fixed question fields, charset interview
or concept count is required.

## Shape

```text
Option 1 — Orbit
meaning: continuity + moment of insight
recipe: ring c(11,13) r7 gap=NE; spark c(18,6) size=4
style: outline; stroke=2; caps=round
benefit: distinct silhouette, clear focal point
risk@16: ring gap may close
```

Coordinates assume the stated grid, normally `grid: 24`. Omit coordinates when relationships such as `inside`, `overlap`, `cutout`, `above`, or `NE` communicate the idea more cheaply.

Useful vocabulary:

- primitives: `line`, `polyline`, `rect`, `roundrect`, `circle`, `ring`, `arc`, `dot`, `spark`, `chevron`
- operations: `cutout`, `gap`, `merge`, `overlap`, `mask`
- placement: `N`, `NE`, `E`, `SE`, `S`, `SW`, `W`, `NW`, `center`, `inside`, `outside`
- treatments: `outline`, `filled`, `duotone`, `sharp`, `round`, `monoline`

This vocabulary is descriptive, not a parser grammar. Prefer words over pseudo-syntax when pseudo-syntax would become longer or ambiguous.

## Detailed ASCII rasters

If ASCII is useful or requested, use a readable geometric raster. Choose a fitting charset and explain it only when needed; ask the user only for a material visual preference. The alphabet below is an example, not a required convention:

```text
. empty   # main mass   + detached/accent mass   @ explicit overlap
```

Size rasters so the direction can actually be judged: no horizontal scrolling (vertical scrolling is acceptable). Use one shared legend for the batch only when the chosen charset needs explaining.

One option is `.` for empty cells so canvas bounds, internal voids, and trailing space remain visible. Choose outline characters such as `/`, `\\`, `|`, `_`, and `-` only when a filled-cell raster would hide an essential thin structure.

Default to a raster large enough to judge the direction; never cap it at 28 columns by 16 rows. Monospace characters are taller than they are wide, so compensate aspect accordingly. All directions in one batch must use the same dimensions unless a different aspect ratio is intrinsic to the requested icon.

Construct the recipe and normalized geometry first, then map that same topology onto the raster. Do not improvise an unrelated ASCII silhouette after writing the description. The raster must show:

- outer contour and relative mass
- internal negative-space geometry
- intentional cuts and openings
- detached or second-color pieces
- major overlaps and depth order

Example, shortened only for documentation:

```text
......##########......
....##############....
...#####......#####...
..#####........++++...
..####.........+++++..
...#####......+++++...
....############......
......########........
```

Treat resolution as geometric fidelity, not decorative density. Do not add texture, fake shading, or random cells merely to make a preview look detailed. ASCII still cannot validate Bézier curves, exact stroke weight, antialiasing, or optical centering. A rendered SVG comparison requires its own applicable approval; whichever preview is used, source inspection alone does not certify visual quality.

## Direction quality

Directions must differ in topology — element count, void shape, and balance — not merely corner radius, stroke width, or a satellite on the same form. Compare meaning and small-size behavior before aesthetics. If only one credible direction exists because the user supplied strict geometry, say so and proceed instead of manufacturing alternatives.
