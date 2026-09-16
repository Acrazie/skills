# SVG to Raster Exports and Validation

Read this reference only when PNG, WebP, or other raster image exports are requested.

---

## 1. Inspect Available Local Renderers

Check available CLI tools on the system before executing commands. Prefer high-fidelity SVG renderers:

1. **`resvg`** (Fastest and most accurate SVG 1.1 / static SVG renderer):
   ```bash
   resvg input.svg output.png -w 1280 -h 640
   ```
2. **`rsvg-convert`** (librsvg):
   ```bash
   rsvg-convert -w 1280 -h 640 input.svg -o output.png
   ```
3. **`inkscape`**:
   ```bash
   inkscape input.svg -o output.png -w 1280 -h 640
   ```
4. **`cairosvg`** (Python):
   ```bash
   cairosvg input.svg -o output.png -W 1280 -H 640
   ```
5. **Node.js / `@resvg/resvg-js` or `sharp`**:
   ```bash
   npx @resvg/resvg-js-cli input.svg -o output.png --width 1280
   ```

> [!NOTE]
> Do not install packages or dependencies without asking the user. If no SVG rasterizer is found on the system, preserve the validated SVG file and inform the user of the recommended command or lightweight tool (`brew install resvg` or `npm i -g @resvg/resvg-js-cli`).

---

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
