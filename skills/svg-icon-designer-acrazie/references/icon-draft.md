# IconDraft

Use this compact notation during ideation. It is a working design recipe, not a public file format and not a substitute for the final SVG.

## Shape

```text
A — Orbit
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

Every direction in a multi-choice concept batch needs a detailed text raster. Use one shared legend before the batch rather than repeating it for every option. Default legend:

```text
. empty   # main mass   + detached/accent mass   @ explicit overlap
```

Use `.` for empty cells so canvas bounds, internal voids, and trailing space remain visible. Choose outline characters such as `/`, `\\`, `|`, `_`, and `-` only when a filled-cell raster would hide an essential thin structure.

Default square-icon preview: 28 columns by 16 rows. Monospace characters are taller than they are wide, so the wider grid compensates visually. All directions in one batch must use the same dimensions unless a different aspect ratio is intrinsic to the requested icon.

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

Treat resolution as geometric fidelity, not decorative density. Do not add texture, fake shading, or random cells merely to make a preview look detailed. ASCII still cannot validate Bézier curves, exact stroke weight, antialiasing, or optical centering. After the user narrows the field to one or two directions, SVG previews replace ASCII as the authoritative visual comparison.

## Direction quality

Directions must differ in concept or composition, not merely corner radius or stroke width. Compare meaning and small-size behavior before aesthetics. If only one credible direction exists because the user supplied strict geometry, say so and proceed instead of manufacturing alternatives.
