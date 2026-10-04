# Rafid Decorative Elements — Authoritative SVG Reference

Every element below is **ported from the live Rafid product** (`Manarat-Rafid`), not redrawn.
Source of truth in the app:

| Element | App source |
|---|---|
| Leaf (organic, real) | `src/assets/leaf_background.tsx` · `src/assets/leafs_clean.svg` |
| Wheat (icon) | `src/assets/wheat.svg` |
| Wheat bookmark panel | `src/assets/wheat_bookmark.tsx` |
| Concentric rings, section divider, identity stamp, bookmark panel, section rule | `src/components/sections/home/primitives.tsx` |
| Dots, arc, small leaf, wheat silhouette, sidebar bar, card recipes | `src/components/sections/lectures/CardDecorations.tsx` |
| Progress ring | `src/components/sections/lectures/trackVisuals.tsx` |

Bundled files: `assets/leaf.svg`, `assets/wheat.svg`, `assets/logo.svg`.
Artifacts and emailed HTML **cannot load external files** — inline the snippets below instead.

---

## Palette used in every snippet

```
--forest      #0c3b2e   --ds-gold    #c9a961   (decorative gold — NOT text-safe on paper)
--forest-2    #155845   --ds-gold-2  #b8954b
--forest-3    #051d15   --gold-deep  #876530   (text-safe gold on paper — 5.2:1)
--forest-pale #1f6d57   --gold-pale  #efe5cb
--paper       #fffdf7   --ink        #14110a   --ink-3  #6e685c
--bg-2        #faf6ee   --line       rgba(20,17,10,.12)
```

Decoration opacities are low by design (0.06–0.25). These are **textures**, not illustrations —
if a decoration is legible as a shape at a glance, it is too strong.

---

## 1. Leaf — the real Rafid leaf ★ primary motif

Two-lobe organic leaf. This is the actual brand shape — **never** substitute a generic teardrop
for it in a hero, cover, or full-bleed context. `viewBox="0 0 1383 1161"`, single path, single fill.

Inline (fill + opacity set by the caller; the file's own default tint is `#c8b98a`):

```html
<svg viewBox="0 0 1383 1161" width="360" aria-hidden="true"
     style="position:absolute;bottom:-40px;inset-inline-start:-40px;opacity:.12;transform:rotate(345deg);pointer-events:none;user-select:none">
  <path fill="#0c3b2e" d="m157.3 13.6c-7.6 7.6-18.7 19.7-24.7 26.9-5.9 7.2-15.8 20-22 28.5-6.2 8.5-13.1 18.2-15.3 21.5-2.2 3.3-8.2 13-13.3 21.5-5.1 8.5-14.8 26.8-21.6 40.5-6.7 13.8-14.5 30.8-17.4 38-2.9 7.2-7.9 20.9-11.2 30.5-3.2 9.6-7.4 22.7-9.3 29-1.8 6.3-5.4 20.3-7.8 31-2.5 10.7-5.5 24.9-6.7 31.5-1.1 6.6-2.7 16.5-3.6 22-0.8 5.5-2.4 18.1-3.5 28-1.4 12.4-2.2 28.4-2.6 51-0.4 21.2-0.2 39.8 0.6 52 0.6 10.4 1.9 25.5 2.7 33.5 0.8 8 2.6 21.9 4 31 1.4 9.1 3.8 22.6 5.4 30 1.5 7.4 4.2 19.6 5.9 27 1.8 7.4 4.8 18.9 6.7 25.5 2 6.6 6.4 20.5 9.9 31 3.4 10.5 8.2 23.7 10.5 29.5 2.3 5.8 6.2 15.2 8.7 21 2.5 5.8 8.1 17.7 12.4 26.5 4.2 8.8 10.8 21.4 14.5 28 3.7 6.6 9.4 16.5 12.7 22 3.3 5.5 10 16.1 15 23.5 4.9 7.4 13.5 19.6 19.1 27 5.5 7.4 13.4 17.5 17.6 22.5 4.1 5 11.9 13.9 17.5 19.9 5.5 6.1 15 16 21 22 6.1 6.1 16.4 15.8 23 21.6 6.6 5.8 15.4 13.3 19.5 16.6 4.1 3.3 12 9.4 17.5 13.6 5.5 4.1 17.2 12.2 26 18 8.8 5.8 22.5 14.2 30.5 18.6 8 4.4 15.9 8.4 17.5 8.8 2.8 0.6 3.7 0 14.4-11.2 6.2-6.6 16.3-17.8 22.4-24.9 6.1-7.1 15.4-18.9 20.8-26 5.3-7.1 12.8-17.7 16.6-23.5 3.9-5.8 11.1-17.3 16-25.5 5-8.3 13.1-23.1 18.1-33 5-9.9 11.8-24.3 15.2-32 3.4-7.7 8.8-21 12-29.5 3.1-8.5 6.9-19.1 8.3-23.5 1.4-4.4 3.6-11.8 5-16.5 1.4-4.7 4.2-14.8 6.1-22.5 1.9-7.7 5.1-21.9 7-31.5 1.9-9.6 4.4-23.6 5.6-31 1.1-7.4 2.6-20.1 3.5-28.3 0.8-8.1 2-22.7 2.6-32.5 0.7-10.7 0.9-29.9 0.6-48.7-0.4-17-1.1-35.7-1.7-41.5-0.6-5.8-2-17.7-3.1-26.5-1.1-8.8-3.1-22.8-4.5-31-1.3-8.3-3.6-20.6-5-27.5-1.4-6.9-4.1-18.4-6-25.5-1.8-7.1-5.1-19.1-7.4-26.5-2.3-7.4-6.2-19.6-8.6-27-2.5-7.4-7.2-20-10.4-28-3.2-8-7.7-18.8-10-24-2.3-5.2-7.2-15.6-10.8-23-3.6-7.4-9.5-18.7-13-25-3.6-6.3-9.6-16.9-13.5-23.5-3.9-6.6-11.8-19-17.6-27.5-5.7-8.5-15.1-21.6-20.9-29-5.7-7.4-15.9-19.8-22.6-27.5-6.8-7.7-19.2-21-27.7-29.6-8.5-8.5-22.2-21.3-30.4-28.3-8.3-7.1-21.1-17.4-28.5-23.1-7.4-5.6-19.4-14.1-26.5-18.7-7.2-4.7-16.6-10.7-21-13.3-4.4-2.6-13.1-7.4-19.2-10.7l-11.3-6.1zm1026.3 340.5c-11 0.4-28.1 1.4-38 2.3-9.9 0.9-24.8 2.6-33 3.6-8.3 1.1-17.7 2.5-21 3.1-3.3 0.5-14.8 2.8-25.5 5-10.8 2.2-25.8 5.6-33.5 7.6-7.7 1.9-20.6 5.5-28.5 7.9-8 2.5-21.3 6.8-29.5 9.6-8.3 2.8-23.4 8.3-33.5 12.3-10.2 4-26.6 11-36.5 15.5-9.9 4.5-25.2 11.9-34 16.5-8.8 4.5-20 10.6-24.8 13.4-4.8 2.8-12.4 7.3-17 9.9-4.5 2.7-12.3 7.4-17.2 10.4-5 3.1-17.4 11.3-27.5 18.3-10.2 7-23 16.2-28.5 20.4-5.5 4.2-14.8 11.4-20.5 16-5.8 4.6-17 14.1-25 21-8 6.9-21.2 19.1-29.4 27.1-8.2 8-17.5 17.2-20.6 20.5-3.2 3.3-10.6 11.4-16.6 18.1-6 6.6-13.6 15.2-17 19-3.3 3.8-9.6 11.4-14.1 16.9-4.4 5.5-12 15.4-17 22-4.9 6.6-13.3 18.3-18.5 26-5.2 7.7-12.2 18.3-15.5 23.5-3.3 5.2-10.2 16.7-15.3 25.5-5.1 8.8-13.7 24.5-19.1 35-5.4 10.4-13.7 28-18.5 39-4.7 11-10.2 24-12.2 29-1.9 4.9-6.1 16.9-9.4 26.5-3.3 9.6-7.5 22.9-9.4 29.5-2 6.6-5.3 18.7-7.4 27-2.1 8.2-5.2 21.7-6.9 30-1.6 8.2-3.9 20.6-5 27.5-1.2 6.9-3 20.4-4.1 30-1.1 9.6-2.5 24.9-3.1 34-0.6 9.1-0.9 29.8-0.8 46 0.3 26.1 0.6 29.9 2.1 32.3 1 1.5 3.2 3.1 5 3.7 1.8 0.5 12.5 2.9 23.8 5.4 11.2 2.5 27.4 5.6 36 7 8.5 1.4 24.5 3.5 35.5 4.6 11 1.2 28.1 2.5 38 3 9.9 0.5 29.2 0.7 43 0.4 13.7-0.2 26.1-0.6 27.5-0.8 1.3-0.2 7.2-0.7 13-1.1 5.7-0.3 18.3-1.5 28-2.6 9.6-1.1 21.7-2.6 27-3.4 5.2-0.9 14.4-2.4 20.5-3.6 6-1.1 16.1-3.1 22.5-4.5 6.3-1.4 17.5-4.1 25-6.1 7.4-1.9 20-5.4 28-7.8 7.9-2.4 21-6.6 29-9.3 7.9-2.7 22.3-8 32-11.7 9.6-3.7 23.5-9.5 31-12.8 7.4-3.4 20.9-9.8 30-14.3 9-4.4 24.8-12.8 35-18.6 10.1-5.8 24.5-14.2 32-18.8 7.4-4.6 18.2-11.5 24-15.3 5.7-3.9 15.4-10.6 21.5-15 6-4.4 17.3-13 25-19.1 7.7-6.1 18.5-14.9 24-19.5 5.5-4.7 13.8-11.9 18.5-15.9 4.6-4.1 14.7-13.6 22.3-21.1 7.7-7.5 19.4-19.5 26.1-26.6 6.7-7.2 15.5-16.8 19.7-21.5 4.1-4.7 11.7-13.7 17-20 5.2-6.3 12.9-16 17-21.5 4.1-5.5 10.9-14.7 15-20.5 4.1-5.8 11.3-16.4 16-23.5 4.7-7.2 10.6-16.4 13-20.5 2.5-4.1 8.2-13.8 12.6-21.5 4.4-7.7 11.4-20.5 15.6-28.5 4.2-8 10.6-21 14.2-29 3.7-8 9.8-22.4 13.7-32 3.9-9.6 10.1-26.7 13.8-38 3.8-11.3 8.5-26.4 10.5-33.5 2-7.2 5.2-19.3 7.1-27 1.9-7.7 4.7-21 6.4-29.5 1.6-8.5 3.9-21.8 5-29.5 1.1-7.7 2.9-22.6 4-33 1.3-12.1 2.3-29.6 2.6-48 0.3-16 0.2-34-0.3-40.2-0.7-9.1-1.2-11.6-2.8-13.3-1.1-1.1-4.7-2.7-8-3.6-3.3-0.8-12.1-2.8-19.5-4.5-7.5-1.7-18-3.9-23.5-4.9-5.5-1-16.6-2.8-24.5-3.9-8-1.1-22.2-2.8-31.5-3.7-9.4-0.9-27.8-1.9-41-2.3-13.2-0.3-33-0.3-44 0z"/>
</svg>
```

**Placement rules (from the live cards):**

| Context | fill | opacity | rotation | size |
|---|---|---|---|---|
| Light card (cream/clay/paper) | `#0c3b2e` | `.11 – .13` | `345°` / `350°` / `-8°` | 36–44 units wide, bleeding off a corner |
| Forest card (dark bg) | `#ffffff` | `.08 – .09` | `352°` / `15°` | 40 units wide, bleeding off a corner |

Always bleed it off an edge (negative inset). A fully-contained leaf reads as clip-art.

**React (in-app):** `import LeafBackground from "@/assets/leaf_background"` → `<LeafBackground fill={...} className="absolute ..." />`

---

## 2. Small Leaf / Teardrop — secondary accent

Simplified two-path leaf for tight spots (badges, small card corners) where the real leaf's
detail would be lost. **Not** a replacement for #1 at large sizes.

```html
<svg viewBox="0 0 100 130" width="72" aria-hidden="true"
     style="position:absolute;opacity:1;pointer-events:none">
  <path d="M 50 8 Q 88 28 86 70 Q 84 108 50 122 Q 18 108 14 70 Q 12 28 50 8Z"
        stroke="#0c3b2e" stroke-width="1.5" fill="none" opacity=".25"/>
  <path d="M 50 30 Q 72 48 70 72 Q 68 96 50 106 Q 32 96 30 72 Q 28 48 50 30Z"
        fill="#0c3b2e" opacity=".18"/>
</svg>
```

---

## 3. Concentric Rings ★ core motif

The circular motif. Two calibrated variants — use them, don't invent radii.

**Corner variant** — anchored so the card's `overflow:hidden` crops it. Rings fade outward.
`radii = 40 + 30i`, stroke 1.5, innermost opacity `0.1`, each outer ring −25%.

```html
<svg viewBox="0 0 200 200" width="150" height="150" aria-hidden="true"
     style="position:absolute;top:-40px;inset-inline-end:-40px;pointer-events:none;user-select:none">
  <circle cx="100" cy="100" r="40"  fill="none" stroke="#c9a961" stroke-width="1.5" opacity=".100"/>
  <circle cx="100" cy="100" r="70"  fill="none" stroke="#c9a961" stroke-width="1.5" opacity=".075"/>
  <circle cx="100" cy="100" r="100" fill="none" stroke="#c9a961" stroke-width="1.5" opacity=".050"/>
  <circle cx="100" cy="100" r="130" fill="none" stroke="#c9a961" stroke-width="1.5" opacity=".025"/>
</svg>
```

On a forest background swap the stroke to `rgba(255,253,247,0.9)` and keep the same opacities.

**Edge variant** — centre pinned off the top edge, denser rings. `radii = [26,46,66,86]`,
opacity `0.14 − 0.027i`.

```html
<svg viewBox="0 0 100 100" width="80" height="80" aria-hidden="true"
     style="position:absolute;top:0;inset-inline-end:0;pointer-events:none">
  <circle cx="100" cy="0" r="26" fill="none" stroke="#c9a961" stroke-width="1.1" opacity=".140"/>
  <circle cx="100" cy="0" r="46" fill="none" stroke="#c9a961" stroke-width="1.1" opacity=".113"/>
  <circle cx="100" cy="0" r="66" fill="none" stroke="#c9a961" stroke-width="1.1" opacity=".086"/>
  <circle cx="100" cy="0" r="86" fill="none" stroke="#c9a961" stroke-width="1.1" opacity=".059"/>
</svg>
```

**React:** `<ConcentricRings color="var(--ds-gold)" rings={4} opacity={0.1} className="absolute -top-10 -end-10 w-[150px] h-[150px]" />`

---

## 4. Wheat — silhouette and icon

The wheat stalk is the growth/harvest half of the brand metaphor (leaf = the other half).

**4a. Procedural wheat silhouette** — the version used on cards. Stalk + crown + 6 paired grains
+ two ground leaves. Very low opacity (0.09–0.12).

```html
<svg viewBox="60 100 150 500" width="44" height="112" aria-hidden="true"
     style="position:absolute;pointer-events:none;user-select:none">
  <line x1="175" y1="590" x2="175" y2="132" stroke="#c9a961" stroke-width="2" opacity=".12" stroke-linecap="round"/>
  <ellipse cx="175" cy="112" rx="5" ry="16" fill="#c9a961" opacity=".12"/>
  <!-- 6 rows × 2 grains, mirrored at ±48° -->
  <g transform="rotate(-48 175 148)"><ellipse cx="175" cy="130" rx="5.5" ry="18" fill="#c9a961" opacity=".09"/></g>
  <g transform="rotate( 48 175 148)"><ellipse cx="175" cy="130" rx="5.5" ry="18" fill="#c9a961" opacity=".09"/></g>
  <g transform="rotate(-48 175 180)"><ellipse cx="175" cy="162" rx="5.5" ry="18" fill="#c9a961" opacity=".09"/></g>
  <g transform="rotate( 48 175 180)"><ellipse cx="175" cy="162" rx="5.5" ry="18" fill="#c9a961" opacity=".09"/></g>
  <g transform="rotate(-48 175 212)"><ellipse cx="175" cy="194" rx="5.5" ry="18" fill="#c9a961" opacity=".09"/></g>
  <g transform="rotate( 48 175 212)"><ellipse cx="175" cy="194" rx="5.5" ry="18" fill="#c9a961" opacity=".09"/></g>
  <g transform="rotate(-48 175 244)"><ellipse cx="175" cy="226" rx="5.5" ry="18" fill="#c9a961" opacity=".09"/></g>
  <g transform="rotate( 48 175 244)"><ellipse cx="175" cy="226" rx="5.5" ry="18" fill="#c9a961" opacity=".09"/></g>
  <g transform="rotate(-48 175 276)"><ellipse cx="175" cy="258" rx="5.5" ry="18" fill="#c9a961" opacity=".09"/></g>
  <g transform="rotate( 48 175 276)"><ellipse cx="175" cy="258" rx="5.5" ry="18" fill="#c9a961" opacity=".09"/></g>
  <g transform="rotate(-48 175 308)"><ellipse cx="175" cy="290" rx="5.5" ry="18" fill="#c9a961" opacity=".09"/></g>
  <g transform="rotate( 48 175 308)"><ellipse cx="175" cy="290" rx="5.5" ry="18" fill="#c9a961" opacity=".09"/></g>
  <path d="M175 455 C156 446 134 434 126 416 C143 422 164 434 175 444 Z" fill="#0c3b2e" opacity=".10"/>
  <path d="M175 518 C194 507 214 493 220 474 C206 480 186 494 175 507 Z" fill="#0c3b2e" opacity=".10"/>
</svg>
```

Rows are at `y = 148, 180, 212, 244, 276, 308`; each grain sits at `y − 18` and is rotated ±48°
about its row centre. Keep that rhythm if you rebuild it.

**4b. Detailed wheat icon** — `assets/wheat.svg`, `viewBox="0 0 17.37 17.37"`, 13 paths,
a single stalk with grains fanning to one side. Use inside the bookmark panel (#5) or as a
watermark. Recolor by replacing `fill:#030104` with a brand hex.

---

## 5. Wheat Bookmark Panel

Tall rounded "bookmark" slab in forest green, with the wheat icon clipped inside at 25% gold.
From the report's page-side panels. `viewBox="0 0 300 700"`.

```html
<svg viewBox="0 0 300 700" width="220" fill="none" aria-hidden="true">
  <defs>
    <clipPath id="wb-clip">
      <path d="M40 20 H190 C250 20 280 70 280 130 V560 C280 640 230 690 180 690 H170 C120 690 70 650 70 580 V120 C70 60 45 35 40 20 Z"/>
    </clipPath>
  </defs>
  <path d="M40 20 H190 C250 20 280 70 280 130 V560 C280 640 230 690 180 690 H170 C120 690 70 650 70 580 V120 C70 60 45 35 40 20 Z"
        fill="#0c3b2e"/>
  <g clip-path="url(#wb-clip)">
    <!-- assets/wheat.svg paths, placed and scaled: -->
    <g fill="#D4A843" opacity="0.25"
       transform="translate(180, 350) scale(-33, 33) rotate(-20) translate(-8.685, -8.685)">
      <!-- paste the 13 <path> children of assets/wheat.svg here -->
    </g>
  </g>
</svg>
```

The `scale(-33, 33)` mirrors the wheat horizontally — that mirroring is intentional in the
original and reads correctly in RTL. Keep it.

**React:** `import WheatBookmark from "@/assets/wheat_bookmark"`

---

## 6. Bookmark Panel (plain)

Half-stadium forest panel that bleeds off the inline-start edge. Report pages 14 & 19.
Desktop only — hide below `lg`.

```html
<div aria-hidden="true"
     style="position:absolute;top:0;bottom:0;inset-inline-start:0;width:26%;
            background:#0c3b2e;border-radius:9999px 0 0 9999px"></div>
```

The two large corner radii meet and form one continuous convex arc. Do not soften to a
small radius — the full semicircle *is* the shape.

---

## 7. Section Divider ★ use between every major section

Gold hairline, broken at centre by a dot–ring–dot ornament. This replaced the old solid
gradient bar and is the current divider everywhere in the product.

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

Inverted (on forest bg): rule `rgba(200,185,138,.35)` @ `.22`, ornament `rgba(200,185,138,.50)`.

---

## 8. Section Rule (gold pill + extending line) ★ every section header

Gold-**filled** capsule with a translucent circular icon well, then a gold line running to the
edge. Note: filled gold, not an outlined pill.

```html
<div style="display:flex;align-items:center;gap:16px;margin-bottom:40px">
  <div style="display:inline-flex;align-items:center;gap:12px;border-radius:9999px;background:#c9a961;
              padding-inline-start:6px;padding-inline-end:18px;padding-top:6px;padding-bottom:6px;flex-shrink:0">
    <span style="width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;
                 background:rgba(255,255,255,.22);color:#051d15;font-size:14px;line-height:1;flex-shrink:0">◉</span>
    <span style="font-family:'Reem Kufi','Tajawal',sans-serif;font-weight:700;font-size:13px;
                 color:#051d15;letter-spacing:-.2px">اسم القسم</span>
  </div>
  <div style="flex:1;height:1.5px;background:#c9a961;opacity:.25"></div>
</div>
```

Text is `--forest-3 #051d15` on gold — 7.8:1, safe. Never white-on-gold (2.4:1).

---

## 9. Identity Stamp (masthead)

Two mono lines split by a gold hairline. The formal identity block from the report.

```html
<div style="display:inline-flex;flex-direction:column;gap:6px">
  <span style="font-family:'JetBrains Mono',monospace;font-size:14px;letter-spacing:1.8px;line-height:1;color:#14110a">
    منارة رافد · ١٤٤٧هـ / 2026
  </span>
  <div style="height:1px;width:100%;background:#c9a961;opacity:.45"></div>
  <span style="font-family:'JetBrains Mono',monospace;font-size:13px;letter-spacing:1.2px;line-height:1;color:#6e685c">
    بإشراف جمعية رافد للأوقاف · رؤية ٢٠٣٠
  </span>
</div>
```

Inverted: line1 `#c9a961`, rule @ `.35`, line2 `rgba(255,253,247,.52)`.

---

## 10. Diagonal Dot Array

Gold dots fading along the diagonal. Corner accent.

```html
<!-- Small 3×3 (48px) — wrapper opacity .85 -->
<svg viewBox="0 0 48 48" width="48" height="48" aria-hidden="true" style="opacity:.85;position:absolute;pointer-events:none">
  <circle cx="8"  cy="8"  r="3.5" fill="#c9a961" opacity=".9"/>
  <circle cx="24" cy="8"  r="3.5" fill="#c9a961" opacity=".6"/>
  <circle cx="40" cy="8"  r="3.5" fill="#c9a961" opacity=".35"/>
  <circle cx="8"  cy="24" r="3.5" fill="#c9a961" opacity=".6"/>
  <circle cx="24" cy="24" r="3.5" fill="#c9a961" opacity=".4"/>
  <circle cx="40" cy="24" r="3.5" fill="#c9a961" opacity=".2"/>
  <circle cx="8"  cy="40" r="3.5" fill="#c9a961" opacity=".35"/>
  <circle cx="24" cy="40" r="3.5" fill="#c9a961" opacity=".2"/>
  <circle cx="40" cy="40" r="3.5" fill="#c9a961" opacity=".1"/>
</svg>

<!-- Large 4×4 (80px) — wrapper opacity .75, r=4, step 20 -->
<svg viewBox="0 0 80 80" width="80" height="80" aria-hidden="true" style="opacity:.75;position:absolute;pointer-events:none">
  <circle cx="10" cy="10" r="4" fill="#c9a961" opacity=".9"/>  <circle cx="30" cy="10" r="4" fill="#c9a961" opacity=".7"/>
  <circle cx="50" cy="10" r="4" fill="#c9a961" opacity=".45"/> <circle cx="70" cy="10" r="4" fill="#c9a961" opacity=".2"/>
  <circle cx="10" cy="30" r="4" fill="#c9a961" opacity=".7"/>  <circle cx="30" cy="30" r="4" fill="#c9a961" opacity=".5"/>
  <circle cx="50" cy="30" r="4" fill="#c9a961" opacity=".3"/>  <circle cx="70" cy="30" r="4" fill="#c9a961" opacity=".12"/>
  <circle cx="10" cy="50" r="4" fill="#c9a961" opacity=".45"/> <circle cx="30" cy="50" r="4" fill="#c9a961" opacity=".3"/>
  <circle cx="50" cy="50" r="4" fill="#c9a961" opacity=".15"/> <circle cx="70" cy="50" r="4" fill="#c9a961" opacity=".06"/>
  <circle cx="10" cy="70" r="4" fill="#c9a961" opacity=".2"/>  <circle cx="30" cy="70" r="4" fill="#c9a961" opacity=".12"/>
  <circle cx="50" cy="70" r="4" fill="#c9a961" opacity=".06"/> <circle cx="70" cy="70" r="4" fill="#c9a961" opacity=".03"/>
</svg>
```

---

## 11. Gold Arc + Terminal Dot

Single curved stroke with a dot at the end. Runs across the top of a card, full width.

```html
<svg viewBox="0 0 400 80" aria-hidden="true"
     style="position:absolute;top:-4px;inset-inline:0;width:100%;height:56px;overflow:visible;pointer-events:none">
  <path d="M 10 65 Q 200 -5 390 50" stroke="#c9a961" stroke-width="2" fill="none" opacity=".4"/>
  <circle cx="390" cy="50" r="4" fill="#c9a961" opacity=".4"/>
</svg>
```

---

## 12. Sidebar Bar

Thin deep-forest bar on the inline-start edge of a card. Signature of the "forest" card tone.

```html
<div aria-hidden="true"
     style="position:absolute;top:0;inset-inline-start:0;width:5px;height:100%;
            background:#051d15;opacity:.55;border-start-end-radius:4px;border-end-end-radius:4px"></div>
```

Full-page variant (report pages): width `28px`, no opacity.

---

## 13. Progress Ring

Circular progress with a count in the middle. Track = `--gold-pale`, fill = `--forest`.
Rotated −90° so it fills from 12 o'clock.

```html
<div style="position:relative;width:62px;height:62px">
  <svg width="62" height="62" style="display:block;transform:rotate(-90deg)">
    <circle cx="31" cy="31" r="28" fill="none" stroke="#efe5cb" stroke-width="6"/>
    <!-- circumference = 2πr = 175.9; offset = C × (1 − value/total) -->
    <circle cx="31" cy="31" r="28" fill="none" stroke="#0c3b2e" stroke-width="6" stroke-linecap="round"
            stroke-dasharray="175.9" stroke-dashoffset="70.4"
            style="transition:stroke-dashoffset .5s ease"/>
  </svg>
  <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
    <b style="color:#0c3b2e;font-size:18px;line-height:1">٣<span style="opacity:.45;font-size:.7em"> / ٥</span></b>
    <small style="margin-top:2px;font-family:'JetBrains Mono',monospace;letter-spacing:1px;font-size:8px;color:#6e685c">لقاء</small>
  </div>
</div>
```

`r = (size − stroke) / 2`. Numerals are Arabic-Indic (`٠١٢٣٤٥٦٧٨٩`) in Arabic output.

---

## 14. Rounded Image Frame

All photos live in a frame. No raw images.

```html
<div style="border-radius:16px;overflow:hidden;box-shadow:0 4px 20px rgba(20,17,10,.12)">
  <img src="..." alt="..." style="width:100%;display:block"/>
</div>

<!-- Gold double-border -->
<div style="border-radius:18px;padding:3px;background:#c9a961">
  <div style="border-radius:15px;overflow:hidden;border:2px solid #fffdf7">
    <img src="..." alt="..." style="width:100%;display:block"/>
  </div>
</div>
```

---

## Card Decoration Recipes ★ how elements actually combine

**The rule the product follows: exactly 3 decorations per card, no more.** One large bleeding
shape + one ring cluster + one small accent. Copy a recipe rather than improvising a new mix.

Card tones and their recipes (from `CardDecorations.tsx`):

| Tone | Background | Decoration 1 | Decoration 2 | Decoration 3 |
|---|---|---|---|---|
| **clay** | light warm | Leaf `#0c3b2e` @ .12, bottom-start, rot 345° | Rings gold, top-end corner | Dots small, top-start |
| **gold** | light gold | Wheat silhouette, top-end | Rings gold, bottom-end corner | Small leaf, bottom-start, rot 170° |
| **paper** | `#fffdf7` | Leaf `#0c3b2e` @ .13, bottom-end, rot −8° | Gold arc across top | Rings green, bottom-start corner |
| **forest** | `#0c3b2e` | Sidebar bar | Rings white, top-end corner | Leaf `#ffffff` @ .09, bottom-start, rot 352° |

Per-topic assignment used in the lecture cards:

```
fiqh-waqf → clay      management → gold        history     → paper    innovation → forest
investment → forest   society    → paper       legislation → clay     applied-studies → gold
```

Every decoration carries `pointer-events:none` and `user-select:none`, and the card is
`overflow:hidden` so corner shapes crop cleanly.

---

## Composition Order (background → foreground)

1. Surface — `--paper` / `--bg-2` / `--forest`, radius 12–16px, `overflow:hidden`
2. Sidebar bar (forest tone only)
3. Large bleeding shape — real leaf (#1) or wheat silhouette (#4a)
4. Concentric rings (#3) in the opposite corner
5. Small accent — dots (#10), arc (#11), or small leaf (#2)
6. Content
7. Section divider (#7) before the next section
