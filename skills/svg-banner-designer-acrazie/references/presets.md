# Platform Presets and Safe Zones

Standard dimensions, aspect ratios, and occlusion zones for web and social banners.

---

## Quick Reference Table

| Platform / Use Case | Recommended Size (px) | Aspect Ratio | Safe Zone & Occlusion Notes |
| :--- | :--- | :--- | :--- |
| **GitHub Repo Social Card** | `1280 × 640` | 2:1 | Keep essential text within central `1120 × 520` (80px margin all around) |
| **GitHub README Banner** | `1200 × 360` (or `1200 × 400`) | 3.33:1 / 3:1 | Full width; top/bottom 30px margin; readable on GitHub web & mobile dark/light |
| **Open Graph / Social Card** | `1200 × 630` | ~1.91:1 | Twitter/X, LinkedIn post, Slack/Discord preview; keep content within central `1040 × 540` |
| **X / Twitter Header** | `1500 × 500` | 3:1 | Avatar occludes bottom-left (~`0-380px` X, `300-500px` Y); keep main text on center/right |
| **LinkedIn Personal Header** | `1584 × 396` | 4:1 | Avatar occludes left side (~`0-350px` X, `160-396px` Y); place text and art in X: `400-1500` |
| **LinkedIn Company Banner**| `1128 × 191` | ~5.9:1 | Logo occludes bottom-left on desktop; extreme panoramic format |
| **YouTube Channel Banner** | `2560 × 1440` | 16:9 | Text/logo safe zone is strictly the central `1232 × 338` (or standard `1546 × 423`) |
| **Dev.to / Blog Hero** | `1000 × 420` | ~2.38:1 | Centered title & badges; 40px margin |
| **Substack / Newsletter** | `1100 × 220` (or `1200 × 600`) | 5:1 / 2:1 | High-density typography and clear branding |

---

## Detailed Platform Guides

### 1. GitHub Social Preview (`1280 × 640`)
- **Usage**: Repository Settings > Social preview. Appears when sharing repo links across GitHub, Twitter, Discord, etc.
- **Safe Area**: Center `1120 × 520`.
- **Layout pattern**:
  - Top-left: Project name + icon/logo.
  - Middle-left: Tagline and key selling points.
  - Bottom-left: Tech badges, pills, or release version.
  - Right 40%: Key visual motif (code snippet card, architecture diagram, 3D abstract vector, or product illustration).

### 2. GitHub README Hero Banner (`1200 × 360` or `1200 × 400`)
- **Usage**: Displayed at the top of `README.md`.
- **Theme considerations**: Render cleanly on both dark and light GitHub UI backgrounds. High-contrast dark backgrounds (`#0d1117` or `#0b0f19`) or transparent backgrounds with contrasting strokes work best.
- **Visuals**: Wide panoramic layout, centered or split (logo/tagline on the left, visual feature highlight on the right).

### 3. Open Graph / Twitter Card (`1200 × 630`)
- **Usage**: `<meta property="og:image">` and `twitter:image`.
- **Safe Area**: Margins of at least 80px horizontally and 60px vertically to prevent truncation when social apps crop preview cards to 1:1 or 16:9 thumbnails.

### 4. X / Twitter Header (`1500 × 500`)
- **Occlusion**: The circular profile picture covers a significant portion of the lower-left area (up to ~380px wide on desktop and mobile).
- **Responsive crop**: Top and bottom ~40px can be cropped on mobile viewports.
- **Composition rule**: Keep all critical text, branding, and focal points in the middle-to-right area (X coordinates between `450` and `1400`, Y coordinates between `80` and `420`).

### 5. LinkedIn Profile Header (`1584 × 396`)
- **Occlusion**: The user avatar overlaps the lower-left area (from left edge up to ~350px).
- **Composition rule**: Keep company logos, titles, and taglines positioned beyond X: 400px. An asymmetrical layout with text centered in the remaining right 70% delivers the best balance.

### 6. YouTube Channel Banner (`2560 × 1440`)
- **Multi-device clipping**:
  - TV: Full `2560 × 1440`.
  - Desktop: Central strip `2560 × 423`.
  - Tablet: Central strip `1855 × 423`.
  - Mobile & Safe Minimum: Central `1232 × 338` (or `1546 × 423`).
- **Composition rule**: Extend background patterns or artwork to the full `2560 × 1440` canvas, but place ALL critical text, logos, and taglines strictly within the central `1232 × 338` rectangle (centered at X: 1280, Y: 720).
