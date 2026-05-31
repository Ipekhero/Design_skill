# Badge

> **When to use:** Tag a status or count next to a label (e.g. "New", "3 issues"). Use sparingly — a row crowded with badges defeats the point. The badge is for *categorical state* visible at a glance, not for free-form annotation.
>
> **Figma:** [open in UI Kit](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=4832-11842)

> **Notes:** Five variants — Neutral, Info, Positive (= `success`), Warning, Error (= `danger`) — matching `design.md` § Components. Each variant supports an optional **leading dot** (`showDot`) for stronger state emphasis. Single size at 24px height.
>
> **Token names** below match the Figma variable names verbatim (`color/surface/danger/soft`, `size/cornerRadius/s`, `label/small`, etc.). Every token listed here is documented in [`references/design.md`](../design.md) at the same hex value — the catalog and this file are in sync.

## Variants

| Variant (`design.md` key) | Figma label | Usage |
|---|---|---|
| `neutral` | Neutral | Default tag. Use when state has no semantic charge — counts, generic categories. |
| `info` | Info | Informational status (e.g. "In review", "Beta channel"). |
| `success` | Positive | Confirmed / completed / live status (e.g. "Active", "Verified"). |
| `warning` | Warning | Soft caution (e.g. "Expiring soon", "Low confidence"). |
| `danger` | Error | Failure / critical state (e.g. "Expired", "Failed"). |

## Sizes

| Size | Natural height (hug content) | Label type | Padding | Gap (dot ↔ label) | Container radius |
|---|---|---|---|---|---|
| `md` | ~24px (matches `size/comp-height/m`) — resolved naturally from padding + line-height, not a fixed `height` | `label/small` — 12px Medium, 16px line-height, 0.25px letter-spacing, **uppercase** | `spacing/padding/s` (8px) horizontal · `spacing/padding/xs` (4px) vertical | `spacing/inline/xs` (4px) | `size/cornerRadius/s` (6px) |

> **Why hug-content, not fixed height:** Figma's auto-layout for the badge **hugs** its label vertically and horizontally. Translating that to code as `height: 24px` looks identical when the label is a single line of `label/small`, but it pins the box to the wrong shape if the label ever wraps, changes type style, or the element renders inside a tall flex row that doesn't centre it. Always set vertical padding + line-height and let the height resolve, so the badge stays centered around its glyph cap-height and adapts to content.

## States

- **default** — The only documented state. Badge is presentational only — no hover, focus, pressed, or disabled treatments. If interactivity is needed, reach for **Chip** instead.

## Tokens per variant × state

For each row, name the exact **Figma variable** used on each property. The optional dot uses the matching `color/surface/<status>/full` token.

| Variant | State | Surface (background) | Text | Dot (if `showDot`) | Notes |
|---|---|---|---|---|---|
| `neutral` | `default` | `color/surface/neutral/soft` (`#E1E7ED`) | `color/text/secondary` (`#525A61`) | `color/surface/neutral/full` (`#525A61`) | Text is `text/secondary`, NOT an `on-color` token — neutral is the only variant that uses the standard secondary text token. |
| `info` | `default` | `color/surface/info/soft` (`#D9E7FF`) | `color/text/on-color/blue` (`#1047A1`) | `color/surface/info/full` (`#1660D9`) | |
| `success` | `default` | `color/surface/success/soft` (`#CEF2DC`) | `color/text/on-color/green` (`#05612A`) | `color/surface/success/full` (`#0D853D`) | |
| `warning` | `default` | `color/surface/warning/soft` (`#FFF1CC`) | `color/text/on-color/yellow` (`#4D3800`) | `color/surface/warning/full` (`#F0BD30`) | |
| `danger` | `default` | `color/surface/danger/soft` (`#FFD9D9`) | `color/text/on-color/red` (`#AD1111`) | `color/surface/danger/full` (`#D92121`) | |
| `brand` | `default` | TODO | TODO | TODO | Not in this Figma node. |
| `new` | `default` | TODO | TODO | TODO | Not in this Figma node. |

## Anatomy

```
┌───────────────────────┐  ← container — hugs content (no fixed height)
│  ●  BADGE             │     padding: spacing/padding/xs (4px) vertical
└───────────────────────┘              spacing/padding/s  (8px) horizontal
   ↑   ↑                      radius:  size/cornerRadius/s (6px)
  6×6  label/small             gap:     spacing/inline/xs (4px)
   dot uppercase               natural height: 4 + 16 (line) + 4 = 24px
   (optional)
```

The dot is 6×6, `size/cornerRadius/round` (999px) — fully rounded. Label is always `UPPERCASE` via CSS `text-transform`, **not** capitalised in the source string.

## Code

### In-repo (React + Tailwind, scandit-web mapping)

```tsx
type BadgeVariant = 'neutral' | 'info' | 'success' | 'warning' | 'danger';

const VARIANT_STYLES: Record<BadgeVariant, { wrap: string; text: string; dot: string }> = {
  neutral: {
    wrap: 'bg-configurator-gray-10',               // color/surface/neutral/soft
    text: 'text-ntypo-secondary',                  // color/text/secondary
    dot:  'bg-ntypo-secondary',                    // color/surface/neutral/full
  },
  info: {
    wrap: 'bg-surface-soft-info',                  // color/surface/info/soft
    text: 'text-newblue-darker',                   // color/text/on-color/blue
    dot:  'bg-surface-full-info',                  // color/surface/info/full
  },
  success: {
    wrap: 'bg-surface-soft-positive',              // color/surface/success/soft
    text: 'text-[#05612A]',                        // color/text/on-color/green
    dot:  'bg-surface-full-positive',              // color/surface/success/full
  },
  warning: {
    wrap: 'bg-surface-soft-warning',               // color/surface/warning/soft
    text: 'text-[#4D3800]',                        // color/text/on-color/yellow
    dot:  'bg-surface-full-warning',               // color/surface/warning/full
  },
  danger: {
    wrap: 'bg-surface-soft-error',                 // color/surface/danger/soft
    text: 'text-[#AD1111]',                        // color/text/on-color/red
    dot:  'bg-surface-full-error',                 // color/surface/danger/full
  },
};

type BadgeProps = {
  variant?: BadgeVariant;
  showDot?: boolean;
  children: React.ReactNode;
};

export function Badge({ variant = 'neutral', showDot = false, children }: BadgeProps) {
  const s = VARIANT_STYLES[variant];
  return (
    <span
      className={[
        // hug content: no fixed height, py-1 + leading-4 resolves to ~24px
        'inline-flex items-center gap-1 px-2 py-1 rounded-md',
        'text-xs font-medium tracking-[0.25px] uppercase leading-4 whitespace-nowrap',
        s.wrap,
        s.text,
      ].join(' ')}
    >
      {showDot && <span aria-hidden="true" className={['size-1.5 rounded-full', s.dot].join(' ')} />}
      {children}
    </span>
  );
}
```

### Standalone artifact (prototype)

```html
<style>
  :root {
    /* Surface — variant background (color/surface/<variant>/soft) */
    --color-surface-neutral-soft: #E1E7ED;
    --color-surface-info-soft:    #D9E7FF;
    --color-surface-success-soft: #CEF2DC;
    --color-surface-warning-soft: #FFF1CC;
    --color-surface-danger-soft:  #FFD9D9;

    /* Surface — dot (color/surface/<variant>/full) */
    --color-surface-neutral-full: #525A61;
    --color-surface-info-full:    #1660D9;
    --color-surface-success-full: #0D853D;
    --color-surface-warning-full: #F0BD30;
    --color-surface-danger-full:  #D92121;

    /* Text — variant label */
    --color-text-secondary:       #525A61;
    --color-text-on-color-blue:   #1047A1;
    --color-text-on-color-green:  #05612A;
    --color-text-on-color-yellow: #4D3800;
    --color-text-on-color-red:    #AD1111;
  }

  .badge {
    /* hug content — natural height = 4 + 16 + 4 = 24px (matches size/comp-height/m) */
    display: inline-flex; align-items: center; gap: 4px;     /* spacing/inline/xs */
    padding: 4px 8px;                                        /* spacing/padding/xs vertical · spacing/padding/s horizontal */
    border-radius: 6px;                                      /* size/cornerRadius/s */
    font-family: Inter, system-ui, sans-serif;
    font-size: 12px; font-weight: 500;                       /* label/small */
    line-height: 16px; letter-spacing: 0.25px;
    text-transform: uppercase; white-space: nowrap;
  }
  .badge__dot {
    width: 6px; height: 6px; border-radius: 999px;           /* size/cornerRadius/round */
  }

  /* Variants */
  .badge--neutral { background: var(--color-surface-neutral-soft); color: var(--color-text-secondary); }
  .badge--neutral .badge__dot { background: var(--color-surface-neutral-full); }

  .badge--info    { background: var(--color-surface-info-soft);    color: var(--color-text-on-color-blue); }
  .badge--info    .badge__dot { background: var(--color-surface-info-full); }

  .badge--success { background: var(--color-surface-success-soft); color: var(--color-text-on-color-green); }
  .badge--success .badge__dot { background: var(--color-surface-success-full); }

  .badge--warning { background: var(--color-surface-warning-soft); color: var(--color-text-on-color-yellow); }
  .badge--warning .badge__dot { background: var(--color-surface-warning-full); }

  .badge--danger  { background: var(--color-surface-danger-soft);  color: var(--color-text-on-color-red); }
  .badge--danger  .badge__dot { background: var(--color-surface-danger-full); }
</style>

<span class="badge badge--neutral"><span class="badge__dot" aria-hidden="true"></span>Neutral</span>
<span class="badge badge--info"><span class="badge__dot" aria-hidden="true"></span>Info</span>
<span class="badge badge--success"><span class="badge__dot" aria-hidden="true"></span>Active</span>
<span class="badge badge--warning"><span class="badge__dot" aria-hidden="true"></span>Expiring</span>
<span class="badge badge--danger"><span class="badge__dot" aria-hidden="true"></span>Expired</span>
```

## Don'ts

- **Don't use a badge for an interactive control.** Badges are presentational; use **Chip** when the user needs to click, dismiss, or toggle.
- **Don't reach across namespaces for "the same green".** A success-coloured icon is `color/icon/positive`, a success-coloured text is `color/text/positive`, a success **badge** is `color/surface/success/soft` + `color/text/on-color/green`. Never substitute one for another.
- **Don't put more than one badge per row item.** A row with three badges fights for attention with itself. Pick the one signal that matters most.
- **Don't lowercase the label.** Badges are uppercase by spec — use `text-transform: uppercase` in CSS, not in the source string. Keeping the source mixed-case preserves searchability and screen-reader pronunciation.
- **Don't use the dot variant in a dense data table.** The dot is for emphasis; a column of badges with dots looks like Christmas lights. Reserve dots for cards, modals, and standalone status displays.
- **Don't repurpose the badge for counts > 99.** Numeric counters that grow are a different pattern — consider a chip or a dedicated counter component to avoid badge truncation.

