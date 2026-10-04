---
name: rafid-identity
description: >
  Apply the complete Rafid Endowments Association (جمعية رافد للأوقاف) brand identity to any design output.
  Use this skill whenever the user asks to create, design, style, or build ANYTHING for Rafid — including
  HTML pages, reports, presentations, dashboards, components, cards, flyers, certificates, social media
  posts, documents, or any visual artifact. Trigger words include: "rafid", "رافد", "brand", "brand identity",
  "Rafid style", "Rafid colors", "brand guidelines", "make it look like Rafid", "apply our brand", or any
  request to create a designed output in the context of this organization. Always use this skill before
  writing any CSS, HTML, or design code for Rafid — the color tokens, decorative patterns, logo, and layout
  rules here are authoritative and must not be improvised.
---

# Rafid Brand Identity Skill

Apply the official Rafid (رافد) visual identity to any designed output.

**The live product (`Manarat-Rafid` — منارة رافد) is the source of truth.** Colors, fonts, and
decorative elements here are ported from its design tokens (`src/index.css`) and shipped
components — not reconstructed from the PDF report. Match the product; do not improvise.

---

## Color Tokens — authoritative

```css
:root {
  /* Greens */
  --forest:      #0c3b2e;  /* PRIMARY — headers, dark sections, buttons, leaf fill on light */
  --forest-2:    #155845;  /* Hover / lifted green */
  --forest-3:    #051d15;  /* Deepest — text on gold, sidebar bars, covers */
  --forest-pale: #1f6d57;  /* Muted green — subdued accents */

  /* Golds */
  --ds-gold:     #c9a961;  /* PRIMARY ACCENT — rules, pills, rings, dots. DECORATIVE ONLY. */
  --ds-gold-2:   #b8954b;  /* Gold hover */
  --gold-pale:   #efe5cb;  /* Ring tracks, tinted fills */
  --gold-deep:   #876530;  /* The ONLY text-safe gold on light backgrounds (5.2:1) */

  /* Surfaces */
  --paper:       #fffdf7;  /* Cards, primary surface */
  --bg:          #fffef9;  /* Page background */
  --bg-2:        #faf6ee;  /* Alt section background */
  --bg-3:        #ede4d2;  /* Deepest warm surface */

  /* Text */
  --ink:         #14110a;  /* Body text — 18.5:1 on paper */
  --ink-2:       #3d3830;  /* Secondary */
  --ink-3:       #6e685c;  /* Muted / captions — 5.4:1, still AA */
  --ink-4:       #9a9486;  /* Disabled only — fails AA, never body text */
  --line:        rgba(20, 17, 10, 0.12);
}
```

**The one rule people get wrong:** `--ds-gold #c9a961` is **2.2:1 on paper** — it fails for text.
It is a decoration color. For gold *text* on a light background use `--gold-deep #876530`.
Gold text on `--forest`/`--forest-3` is fine.

### Logo hex ≠ UI hex — intentional

`assets/logo.svg` uses `#29623f` (green) and `#bc9342` (gold) — the print/logo values. The UI
palette above is deeper and softer. **Never recolor the logo to the UI tokens**, and never pull
the logo's hexes into a UI. They coexist.

---

## Typography

| Role | Token | Stack |
|------|-------|-------|
| Display / headings | `--font-display` | `"Reem Kufi", "Tajawal", sans-serif` |
| Body / UI / buttons | `--font-sans` | `"Outfit", "Tajawal", ui-sans-serif, system-ui` |
| Eyebrows, labels, stamps, numerals-in-rings | `--font-mono` | `"JetBrains Mono", "Courier New", monospace` |
| Quotes / editorial | `--font-serif` | `"Amiri", Georgia, serif` |

Tajawal carries the Arabic; Outfit carries Latin/numerals in body text.

**Mono is a brand signal, not a code font.** Eyebrows, identity stamps, section labels, and
ring captions are all mono with wide tracking (`1.2px`–`2px`) and uppercase for Latin. Using a
sans there loses the Rafid feel.

```html
<link href="https://fonts.googleapis.com/css2?family=Reem+Kufi:wght@400..700&family=Tajawal:wght@400;500;700;900&family=Outfit:wght@400..700&family=JetBrains+Mono:wght@400;500&family=Amiri:ital@0;1&display=swap" rel="stylesheet"/>
```

Dates are **Hijri primary**, Gregorian secondary. Arabic output uses Arabic-Indic numerals
(`٠١٢٣٤٥٦٧٨٩`) in Arabic-language contexts.

---

## Official Logo

`assets/logo.svg` — `viewBox="0 0 596.52 631.78"`, two fills: `.cls-1 #29623f` (letterforms),
`.cls-2 #bc9342` (leaf/plant accent). **Always use the file.** Never recreate, recolor, or stretch it.

- Pair with the full name: **جمعية رافد للأوقاف بمنطقة مكة المكرمة**
- License **ترخيص رقم: 1937** in small muted text beneath
- Top-right in RTL layouts (leading edge), followed by a hairline rule
- Minimum clear space = height of the ر glyph; minimum width 80px
- On a forest background: invert `.cls-1` to `#fffdf7`, keep `.cls-2` gold

Artifacts/emails cannot load external files — read `assets/logo.svg` and inline the SVG.

---

## Decorative Elements

**Full source for all 14 → `references/decorative-elements.md`. Read it before decorating anything.**

The two motifs that carry the brand:

- **The leaf** — a specific two-lobe organic shape (`assets/leaf.svg`, `viewBox 0 0 1383 1161`).
  A generic teardrop is **not** the Rafid leaf. Bleed it off an edge at `opacity .08–.13`.
- **Concentric rings** — `radii = 40 + 30i`, stroke 1.5, innermost `opacity .1`, −25% per ring.
  Anchored so a corner crops them.

Supporting: wheat silhouette · wheat bookmark panel · diagonal dot array · gold arc ·
sidebar bar · section divider · section rule · identity stamp · progress ring.

Three hard rules:

1. **Max 3 decorations per card** — one large bleeding shape, one ring cluster, one small accent.
2. **Decorations are textures, not illustrations.** Opacity `.06–.25`. If a shape reads clearly
   as a shape at a glance, it is too strong.
3. Everything decorative gets `pointer-events:none`, `user-select:none`, `aria-hidden="true"`,
   and lives inside an `overflow:hidden` parent.

### Most-used snippets

**Section divider** — between every major section:
```html
<div aria-hidden="true" style="display:flex;align-items:center;gap:12px;width:100%">
  <div style="flex:1;height:1px;background:#c9a961;opacity:.22"></div>
  <div style="display:flex;align-items:center;gap:6px">
    <div style="width:5px;height:5px;border-radius:50%;background:#c9a961;opacity:.5"></div>
    <div style="width:10px;height:10px;border-radius:50%;border:1.5px solid #c9a961;opacity:.7"></div>
    <div style="width:5px;height:5px;border-radius:50%;background:#c9a961;opacity:.5"></div>
  </div>
  <div style="flex:1;height:1px;background:#c9a961;opacity:.22"></div>
</div>
```

**Section rule** — every section header (gold-FILLED pill, then a line to the edge):
```html
<div style="display:flex;align-items:center;gap:16px;margin-bottom:40px">
  <div style="display:inline-flex;align-items:center;gap:12px;border-radius:9999px;background:#c9a961;
              padding:6px 18px 6px 6px;flex-shrink:0">
    <span style="width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;
                 background:rgba(255,255,255,.22);color:#051d15;font-size:14px;flex-shrink:0">◉</span>
    <span style="font-family:'Reem Kufi','Tajawal',sans-serif;font-weight:700;font-size:13px;color:#051d15">اسم القسم</span>
  </div>
  <div style="flex:1;height:1.5px;background:#c9a961;opacity:.25"></div>
</div>
```

**Concentric rings** — corner texture:
```html
<svg viewBox="0 0 200 200" width="150" height="150" aria-hidden="true"
     style="position:absolute;top:-40px;inset-inline-end:-40px;pointer-events:none">
  <circle cx="100" cy="100" r="40"  fill="none" stroke="#c9a961" stroke-width="1.5" opacity=".100"/>
  <circle cx="100" cy="100" r="70"  fill="none" stroke="#c9a961" stroke-width="1.5" opacity=".075"/>
  <circle cx="100" cy="100" r="100" fill="none" stroke="#c9a961" stroke-width="1.5" opacity=".050"/>
  <circle cx="100" cy="100" r="130" fill="none" stroke="#c9a961" stroke-width="1.5" opacity=".025"/>
</svg>
```

---

## Layout Rules

- **Direction**: RTL always (`dir="rtl"`). Logical properties only — `inset-inline-start/end`,
  `padding-inline-*`, `margin-inline-*`. Never bare `left`/`right` in layout.
- **Radius**: sharp/flat aesthetic. Cards 12–16px · pills 9999px · buttons 8px.
  No 24px+ blobs on layout boxes.
- **Shadows**: barely there — `0 2px 12px rgba(20,17,10,.07)`, or `0 4px 20px rgba(20,17,10,.12)` on images.
- **Spacing**: 8px multiples.
- **Grid**: 2-column content; 1-column centered for stat/impact pages.
- **Responsive**: every fixed size needs a mobile step — `px-4 sm:px-8 lg:px-20`,
  `grid-cols-1 sm:grid-cols-2 lg:grid-cols-3`, `text-[32px] lg:text-[56px]`. No horizontal overflow.

---

## HTML Boilerplate

```html
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>رافد — [Title]</title>
<link href="https://fonts.googleapis.com/css2?family=Reem+Kufi:wght@400..700&family=Tajawal:wght@400;500;700;900&family=Outfit:wght@400..700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet"/>
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --forest:#0c3b2e; --forest-2:#155845; --forest-3:#051d15; --forest-pale:#1f6d57;
  --ds-gold:#c9a961; --ds-gold-2:#b8954b; --gold-pale:#efe5cb; --gold-deep:#876530;
  --paper:#fffdf7; --bg:#fffef9; --bg-2:#faf6ee; --bg-3:#ede4d2;
  --ink:#14110a; --ink-2:#3d3830; --ink-3:#6e685c;
  --line:rgba(20,17,10,.12);
  --font-display:"Reem Kufi","Tajawal",sans-serif;
  --font-sans:"Outfit","Tajawal",ui-sans-serif,system-ui,sans-serif;
  --font-mono:"JetBrains Mono","Courier New",monospace;
}
body{font-family:var(--font-sans);background:var(--bg);color:var(--ink);direction:rtl;line-height:1.7;overflow-x:hidden}
h1,h2,h3{font-family:var(--font-display)}
.eyebrow{font-family:var(--font-mono);font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--ink-3)}
</style>
</head>
<body>

<header style="padding:16px 32px;position:relative">
  <div style="display:flex;align-items:center;gap:16px;justify-content:flex-end">
    <div style="text-align:end">
      <div style="font-family:var(--font-display);font-weight:700;color:var(--forest);font-size:14px">جمعية رافد للأوقاف بمنطقة مكة المكرمة</div>
      <div style="font-family:var(--font-mono);font-size:10px;letter-spacing:1px;color:var(--ink-3)">ترخيص رقم: 1937</div>
    </div>
    <!-- inline assets/logo.svg here (external files are blocked in artifacts/email) -->
  </div>
  <div style="height:1px;background:var(--ds-gold);opacity:.45;margin-top:8px"></div>
</header>

<main style="max-width:1100px;margin:0 auto;padding:32px;position:relative">
  <!-- content -->
</main>

</body>
</html>
```

---

## Quality Checklist

- [ ] `dir="rtl"` on `<html>`; logical properties throughout — no bare `left`/`right`
- [ ] Reem Kufi (display) + Tajawal/Outfit (body) + JetBrains Mono (labels) loaded
- [ ] Colors from the token block — `#0c3b2e` / `#c9a961`, **not** the logo's `#29623f` / `#bc9342`
- [ ] No `--ds-gold` text on a light background — use `--gold-deep #876530`
- [ ] Logo inlined from `assets/logo.svg`, never redrawn, never recolored
- [ ] The real leaf (`assets/leaf.svg`) used — not a generic teardrop
- [ ] Concentric rings use `radii = 40 + 30i`, stroke 1.5, fading −25% per ring
- [ ] ≤ 3 decorations per card; all at opacity `.06–.25`
- [ ] All decoration is `pointer-events:none` + `aria-hidden="true"` inside `overflow:hidden`
- [ ] Section divider between major sections; gold-filled pill rule on each section header
- [ ] Dates Hijri-primary; Arabic-Indic numerals in Arabic copy
- [ ] Mobile breakpoints on every fixed size; no horizontal scroll

---

## Further Reference

→ `references/decorative-elements.md` — all 14 elements, real SVG source, card recipes
→ `references/wcag-contrast.md` — contrast table for the token palette
→ `assets/logo.svg` — official logo (print hexes `#29623f` + `#bc9342`)
→ `assets/leaf.svg` — the real Rafid leaf (`viewBox 0 0 1383 1161`)
→ `assets/wheat.svg` — wheat icon (`viewBox 0 0 17.37 17.37`)
