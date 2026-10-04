# Rafid WCAG Contrast Reference

Computed with the WCAG 2.1 relative-luminance formula against the **product token palette**
(`src/index.css`), which is the authoritative UI palette. The logo's print hexes
(`#29623f` / `#bc9342`) are **not** UI colors and are excluded.

## Text on light surfaces

Reference surface: `--paper #fffdf7` (ratios on `--bg #fffef9` and `--bg-2 #faf6ee` are within 0.1).

| Foreground | Ratio | Normal AA (≥4.5) | Large AA (≥3.0) | Verdict |
|---|---|---|---|---|
| `--ink` `#14110a` | 18.5:1 | ✅ | ✅ | Default body text |
| `--forest` `#0c3b2e` | 12.3:1 | ✅ | ✅ | Headings, links |
| `--forest-3` `#051d15` | 17.3:1 | ✅ | ✅ | Max-emphasis |
| `--forest-2` `#155845` | 8.2:1 | ✅ | ✅ | Safe |
| `--forest-pale` `#1f6d57` | 6.1:1 | ✅ | ✅ | Safe |
| `--ink-3` `#6e685c` | 5.4:1 | ✅ | ✅ | Captions, muted text |
| `--gold-deep` `#876530` | 5.2:1 | ✅ | ✅ | **The only text-safe gold on light** |
| `--ink-4` `#9a9486` | 3.0:1 | ❌ | ⚠️ borderline | Disabled state only |
| `--ds-gold-2` `#b8954b` | 2.8:1 | ❌ | ❌ | Decorative only |
| `--ds-gold` `#c9a961` | **2.2:1** | ❌ | ❌ | **Decorative only — never text** |

## Text on dark surfaces

| Pair | Ratio | Normal AA | Large AA | Verdict |
|---|---|---|---|---|
| `--paper` on `--forest` `#0c3b2e` | 12.3:1 | ✅ | ✅ | Default on dark |
| `--paper` on `--forest-3` `#051d15` | 17.3:1 | ✅ | ✅ | Safe |
| `--paper` on `--forest-2` `#155845` | 8.2:1 | ✅ | ✅ | Safe |
| `--paper` on `--forest-pale` `#1f6d57` | 6.1:1 | ✅ | ✅ | Safe |
| `--gold-pale` `#efe5cb` on `--forest` | 10.0:1 | ✅ | ✅ | Best gold-family text on dark |
| `--ds-gold` on `--forest-3` | 7.8:1 | ✅ | ✅ | Safe |
| `--ds-gold` on `--forest` | 5.6:1 | ✅ | ✅ | Safe |
| `--ds-gold` on `--forest-2` | 3.7:1 | ⚠️ large only | ✅ | 18px+ or bold |

## Text on gold / tinted fills

| Pair | Ratio | Normal AA | Verdict |
|---|---|---|---|
| `--forest-3` `#051d15` on `--ds-gold` `#c9a961` | 7.8:1 | ✅ | **The section-rule pill combo** |
| `--forest-3` on `--ds-gold-2` `#b8954b` | 6.2:1 | ✅ | Safe (hover state) |
| `--ink` on `--gold-pale` `#efe5cb` | 15.0:1 | ✅ | Safe |
| `--forest` on `--gold-pale` | 10.0:1 | ✅ | Safe |
| White `#ffffff` on `--ds-gold` | 2.3:1 | ❌ | **Never.** Gold pills take dark text. |

## Rules

1. **`--ds-gold #c9a961` is a decoration color, not a text color.** On any light surface it is
   2.2:1. If you need gold text on light, use `--gold-deep #876530` (5.2:1).
2. **Gold fills take `--forest-3` text**, never white. White-on-gold is 2.3:1.
3. **On any green surface, `--paper` is always safe** (6.1:1 minimum, even on the palest green).
4. `--ink-4 #9a9486` is a disabled-state color. It fails AA for body text.
5. Decorative elements (rings, leaf, wheat, dots, arcs) run at opacity `.06–.25` and are
   `aria-hidden` non-text — WCAG contrast does not apply to them. Do not "fix" their contrast;
   raising their opacity to pass a ratio breaks the design.
6. UI *components* (borders, focus rings, icons conveying meaning) need **3:1** under WCAG 1.4.11.
   `--ds-gold` at full opacity on paper is 2.2:1 — a gold hairline is decorative, but a gold
   *focus ring* is not. Use `--forest` or `--gold-deep` for focus/state indicators.
