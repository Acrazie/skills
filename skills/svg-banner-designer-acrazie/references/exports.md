# SVG to Raster Exports and Validation

Read this reference only when PNG, WebP, or other raster image exports are requested.

---

## 1. Approved local export

Export only requested formats/dimensions to approved exact paths. Prefer an already
installed renderer with suitable SVG support: resvg, librsvg, Inkscape, Sharp or
CairoSVG. Verify its installed version, supported options and current documentation
before constructing commands; tool names are candidates, not certified recipes or
performance rankings. Do not run `npx` or similar download-capable wrappers as a
substitute for installation permission. Preserve source SVG and transparency unless
an approved background is requested.

No renderer means a disclosed export blocker, not a renamed file or fabricated
preview. Propose separately approved installation only if needed. Conversion must
not implicitly fetch external resources, write outside agreed paths or execute
untrusted SVG scripts. Inspect source, fonts and external references before rendering.

## 2. macOS Built-in Inspection

On macOS systems, verify output dimensions using `sips`:
```bash
sips -g pixelWidth -g pixelHeight output.png
```

---

## 3. Quality and Validation Checklist

Before finalizing output:

1. **XML Validity**: Ensure `<svg>` tags match, namespaces (`xmlns="http://www.w3.org/2000/svg"`) are defined, and attributes are properly quoted.
2. **ViewBox & Bounds**: Confirm artwork stays strictly within `0 0 W H` without clipping drop-shadows or glow halos.
3. **Font Rendering**: When non-standard fonts are used, ensure robust fallback stacks (`system-ui, -apple-system, "Segoe UI", Roboto, sans-serif` or `ui-monospace, monospace`), or embed paths for critical custom lettering.
4. **Export Dimensions**: Validate that the exported PNG matches the required platform dimensions (or 2x for high-DPI retina display).
