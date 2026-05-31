# Card

> **When to use:** Group related content into a contained surface — the dashboard's main composition unit. Pick the variant by **shape**: `Rectangle` for a row-like tile (icon · text · trailing chevron), `Square` for a compact grid tile (top icon · bottom text), `Expandable` for a Rectangle that opens to reveal more content on click.
>
> **Figma:** [open in UI Kit](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=6187-16348)

> **Notes:**
>
> - **Variants are shape-based**, not concept-based. There is no `default / interactive / elevated / bordered` axis — pick the shape that matches the content. All three variants are interactive (hover and pressed states draw a surface fill).
> - **No size axis.** Dimensions are intrinsic to each variant: Rectangle and Expandable are `343px` wide × auto height (min 72px), Square is `160px` wide × `150px` tall.
> - **Disabled state is not documented in Figma** for any card variant. Cards are presentational tiles — if you need to disable interactivity, render the card with reduced opacity and `pointer-events: none` at the application level, or replace the trailing chevron with a status badge that signals why the card isn't actionable.
> - **⚠ Brand colour divergence:** The Figma Square card renders its icon-wrapper in **teal** (`color/teal/5` background, `color/icon/brand` rendered as `#1AA1AD`). The Scandit web design system uses **brand blue** for surfaces and icons — teal is marketing-only. This card.md substitutes `color/surface/brand/softer` (`#EFF5FA`) for the wrapper and `color/icon/brand` (`#0A3390`) for the icon glyph per design.md. The Figma render should be treated as out-of-date for web product use.
>
> **Token names** below match Figma variable names verbatim. Every token is documented in [`../design.md`](../design.md) — the catalog and this file are in sync.

## Variants

| Variant | Figma label | Dimensions | Layout | Use for |
|---|---|---|---|---|
| `rectangle` | Rectangle | 343 wide × auto height (min 72px) | Horizontal row: leading element (48×48) · text wrapper (label + description) · trailing chevron_right | List of items where each row is a tappable destination — e.g. a list of projects, dashboards, scanners |
| `square` | Square | 160 × 150 | Stacked: icon-wrapper (36×36) top-left + chevron_right top-right · label + description bottom | Grid tile for shortcut / quick-action surfaces — e.g. "Start scan", "View results", "Configure device" |
| `expandable` | Expandable | 343 wide × auto, expands to 343 wide × 343+content tall when state is `expanded` | Same header as Rectangle but trailing **chevron_down** (collapsed) / **chevron_up** (expanded). Expanded reveals a content slot with a 1px divider above it. | Disclose secondary content that the user occasionally wants to see — e.g. license key value, device details, expanded analytics |

## States

- **default** — Resting state. Surface `color/surface/default` (white), 1px `color/border/tertiary` outline.
- **hover** — Surface shifts to `color/surface/hover`. Border unchanged. `cursor: pointer`.
- **pressed** — Surface shifts to `color/surface/pressed`. Border unchanged. Triggered on `:active` / pointerdown.
- **expanded** — Applies **only** to the Expandable variant. Surface returns to `color/surface/default`; chevron icon swaps from `chevron_down` to `chevron_up`; content slot (with a 1px divider above) renders below the header.

> **Disabled** and **selected** states are not in the Figma frame. If you need them, treat as application-level concerns (opacity + pointer-events for disabled; an explicit border-color or background-tint for selected).

## Common anatomy — header (Rectangle + Expandable, collapsed)

```
┌──────────────────────────────────────────────────────────────┐  width: 343px, min-height: 72px
│ ┌──────┐                                                     │  bg: surface/default
│ │      │   Label                                       ⌃     │  border: 1px solid border/tertiary
│ │      │   Short description                                 │  radius: size/cornerRadius/m (8px)
│ └──────┘                                                     │  padding: 12px vertical · 16px horizontal
└──────────────────────────────────────────────────────────────┘
   48×48     label/large + body/small               24×24
   leading   text wrapper                            trailing
   element   gap: 2px (Default) / 2px stack/xxs      icon
   radius:   between label & description             (chevron_right for Rectangle;
   cornerRadius/2xs (2px)                             chevron_down/up for Expandable)
   ↑                          ↑
   gap (header items): spacing/padding/l (16px)
```

The **leading element** is a 48×48 placeholder square with corner radius `size/cornerRadius/2xs` (2px) and background `primitive/gray/400` in the bare Figma frame — at consumption sites it's replaced with an icon, a thumbnail, an avatar, or product mark.

## Common anatomy — Square

```
┌────────────────────────┐  160 × 150
│ ┌────┐            ⌃    │  bg: surface/default
│ │ ▢  │                 │  border: 1px solid border/tertiary
│ └────┘                 │  radius: 8px
│                        │  padding: 16px
│  Card title            │  layout: column, justify-end
│  Short description     │  text aligned to bottom
└────────────────────────┘
  36×36                24×24
  icon-wrapper         chevron_right
  (top-left)           (top-right)
```

The Square card's **icon-wrapper** is `36×36`, `border-radius: 4px`, with the brand-blue soft surface (per the web brand rule — substitutes Figma's teal `color/teal/5`):
- Background: `color/surface/brand/softer` (`#EFF5FA`)
- Inner glyph: 24×24 icon in `color/icon/brand` (`#0A3390`) — typically a `scan` or product-specific icon

## Tokens per variant × state

The colour tokens that change per state are surface + border. Text and icon colours stay constant per variant (only the chevron glyph changes for Expandable).

### Rectangle

| State | Surface | Border | Label text | Description text | Trailing icon |
|---|---|---|---|---|---|
| `default` | `color/surface/default` (`#FFFFFF`) | `color/border/tertiary` (`#E1E7ED`) | `color/text/primary` (`#16191C`) — `label/large` 16/24/0.25 | `color/text/secondary` (`#525A61`) — `body/small` 14/20/0.25 | `chevron_right` 24×24 in `color/icon/secondary` (`#6C7680`) |
| `hover` | `color/surface/hover` (`#F3F5F8`) | `color/border/tertiary` (unchanged) | `color/text/primary` | `color/text/secondary` | `chevron_right` in `color/icon/secondary`. `cursor: pointer`. |
| `pressed` | `color/surface/pressed` (`#E1E7ED`) | `color/border/tertiary` | `color/text/primary` | `color/text/secondary` | Trailing chevron typically suppressed at pressed in Figma; keep visible in code for layout stability |

### Square

| State | Surface | Border | Label text | Description text | Icon-wrapper bg | Icon glyph | Trailing icon |
|---|---|---|---|---|---|---|---|
| `default` | `color/surface/default` (`#FFFFFF`) | `color/border/tertiary` | `color/text/primary` — `label/large` | `color/text/secondary` — `body/small` | `color/surface/brand/softer` (`#EFF5FA`) ← substituted for Figma teal | `color/icon/brand` (`#0A3390`) ← blue per design.md, NOT Figma's #1AA1AD teal | `chevron_right` 24×24 `color/icon/secondary` |
| `hover` | `color/surface/hover` (`#F3F5F8`) | `color/border/tertiary` | same as default | same as default | same as default | same as default | same as default |
| `pressed` | `color/surface/pressed` (`#E1E7ED`) | `color/border/tertiary` | same as default | same as default | same as default | same as default | same as default |

### Expandable

| State | Surface | Border | Trailing icon | Notes |
|---|---|---|---|---|
| `default` | `color/surface/default` (`#FFFFFF`) | `color/border/tertiary` | `chevron_down` 24×24 in `color/icon/secondary` | Header only — no content slot rendered. |
| `hover` | `color/surface/hover` (`#F3F5F8`) | `color/border/tertiary` | `chevron_down` (unchanged) | `cursor: pointer`. |
| `pressed` | `color/surface/pressed` (`#E1E7ED`) | `color/border/tertiary` | `chevron_down` (unchanged) | |
| `expanded` | `color/surface/default` (`#FFFFFF`) | `color/border/tertiary` | `chevron_up` 24×24 in `color/icon/secondary` | Adds a 1px `color/border/tertiary` divider below the header, then a content slot. |

## Code

### In-repo (React + Tailwind, scandit-web mapping)

```tsx
import { ChevronRightIcon, ChevronDownIcon, ChevronUpIcon } from '@/icons';

type CardVariant = 'rectangle' | 'square' | 'expandable';

type CardProps = {
  variant: CardVariant;
  label: string;
  description?: string;
  leading?: React.ReactNode;       // 48×48 element for rectangle/expandable; 36×36 icon for square
  expanded?: boolean;              // expandable only
  onToggle?: () => void;           // expandable only
  onClick?: () => void;            // rectangle/square
  children?: React.ReactNode;      // expandable's content slot
};

const cardBase =
  // bg + border unchanged across hover/pressed for border-tertiary
  'rounded-lg border border-configurator-gray-10 bg-white ' +
  'hover:bg-configurator-gray-5 active:bg-configurator-gray-10';

export function Card(p: CardProps) {
  if (p.variant === 'square') {
    return (
      <button
        type="button"
        onClick={p.onClick}
        className={[cardBase, 'flex flex-col justify-end gap-4 p-4 w-[160px] h-[150px] text-left'].join(' ')}
      >
        <div className="flex items-center justify-between w-full">
          <div className="size-9 rounded grid place-items-center bg-surface-soft-brand">
            {/* 24×24 icon — use color/icon/brand (#0A3390 deep blue). Do NOT use Figma's teal #1AA1AD. */}
            <span className="size-6 text-newblue-darker">{p.leading}</span>
          </div>
          <ChevronRightIcon className="size-6 text-ntypo-secondary" />
        </div>
        <div className="flex flex-col">
          <span className="text-base font-medium tracking-[0.25px] leading-6 text-ntypo-primary">{p.label}</span>
          {p.description && <span className="text-sm tracking-[0.25px] leading-5 text-ntypo-secondary">{p.description}</span>}
        </div>
      </button>
    );
  }

  // rectangle + expandable share the header
  const isExpandable = p.variant === 'expandable';
  const TrailingIcon = isExpandable
    ? (p.expanded ? ChevronUpIcon : ChevronDownIcon)
    : ChevronRightIcon;

  return (
    <div className={[cardBase, 'w-[343px] min-h-[72px] flex flex-col'].join(' ')}>
      <button
        type="button"
        onClick={isExpandable ? p.onToggle : p.onClick}
        className="flex items-center gap-4 px-4 py-3 text-left"
      >
        <div className="size-12 rounded-sm shrink-0 bg-configurator-gray-30">{p.leading}</div>
        <div className="flex-1 min-w-0 flex flex-col gap-[2px]">
          <span className="text-base font-medium tracking-[0.25px] leading-6 text-ntypo-primary truncate">{p.label}</span>
          {p.description && (
            <span className="text-sm tracking-[0.25px] leading-5 text-ntypo-secondary truncate">{p.description}</span>
          )}
        </div>
        <TrailingIcon className="size-6 text-ntypo-secondary shrink-0" />
      </button>
      {isExpandable && p.expanded && (
        <>
          <div className="h-px bg-configurator-gray-10" />
          <div className="p-4">{p.children}</div>
        </>
      )}
    </div>
  );
}
```

### Standalone artifact (prototype)

```html
<style>
  :root {
    --color-surface-default:        #FFFFFF;
    --color-surface-hover:          #F3F5F8;
    --color-surface-pressed:        #E1E7ED;
    --color-surface-brand-softer:   #EFF5FA;   /* used as Square icon-wrapper bg (NOT teal #E7F7F9) */
    --color-border-tertiary:        #E1E7ED;
    --color-text-primary:           #16191C;
    --color-text-secondary:         #525A61;
    --color-icon-secondary:         #6C7680;
    --color-icon-brand:             #0A3390;   /* brand blue per design.md (NOT Figma's teal #1AA1AD) */
    --color-gray-primitive-400:     #ACB6BF;   /* used by the bare LeadingElement placeholder */
  }

  /* ─── Card base ─── */
  .card {
    background: var(--color-surface-default);
    border: 1px solid var(--color-border-tertiary);
    border-radius: 8px;            /* size/cornerRadius/m */
    font-family: Inter, system-ui, sans-serif;
    color: var(--color-text-primary);
    cursor: pointer;
    transition: background-color 120ms;
  }
  .card:hover  { background: var(--color-surface-hover); }
  .card:active { background: var(--color-surface-pressed); }
  .card[disabled], .card.is-disabled { opacity: 0.5; pointer-events: none; }

  /* ─── Rectangle (and Expandable header) ─── */
  .card--rectangle, .card--expandable {
    width: 343px;
    min-height: 72px;
    display: flex; flex-direction: column;
  }
  .card__header {
    display: flex; align-items: center; gap: 16px;   /* spacing/padding/l */
    padding: 12px 16px;                              /* spacing/padding/m vertical · l horizontal */
    width: 100%;
    text-align: left;
    background: transparent;
    border: 0; color: inherit; font: inherit;
    cursor: inherit;
  }
  .card__leading {
    width: 48px; height: 48px; flex-shrink: 0;
    border-radius: 2px;                              /* size/cornerRadius/2xs */
    background: var(--color-gray-primitive-400);
  }
  .card__text {
    flex: 1; min-width: 0;
    display: flex; flex-direction: column; gap: 2px; /* spacing/stack/xxs */
  }
  .card__label {
    font-size: 16px; font-weight: 500; line-height: 24px; letter-spacing: 0.25px;  /* label/large */
    color: var(--color-text-primary);
    overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
  }
  .card__desc {
    font-size: 14px; font-weight: 400; line-height: 20px; letter-spacing: 0.25px;  /* body/small */
    color: var(--color-text-secondary);
    overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
  }
  .card__trailing {
    width: 24px; height: 24px; flex-shrink: 0;
    color: var(--color-icon-secondary);
  }

  /* ─── Expandable extras ─── */
  .card--expandable .card__divider {
    height: 1px; background: var(--color-border-tertiary);
  }
  .card--expandable .card__content {
    padding: 16px;
  }

  /* ─── Square ─── */
  .card--square {
    width: 160px; height: 150px;
    display: flex; flex-direction: column; justify-content: space-between;
    padding: 16px;
    text-align: left;
  }
  .card--square .card__top {
    display: flex; align-items: center; justify-content: space-between;
  }
  .card--square .card__icon-wrapper {
    width: 36px; height: 36px;
    border-radius: 4px;
    background: var(--color-surface-brand-softer);   /* blue per design.md, NOT teal */
    display: grid; place-items: center;
  }
  .card--square .card__icon-glyph {
    width: 24px; height: 24px;
    color: var(--color-icon-brand);                  /* blue per design.md */
  }
  .card--square .card__bottom {
    display: flex; flex-direction: column;
  }
</style>

<!-- Rectangle -->
<a class="card card--rectangle" href="#">
  <span class="card__header">
    <span class="card__leading"></span>
    <span class="card__text">
      <span class="card__label">Warehouse pilot — Zurich DC</span>
      <span class="card__desc">12 scanners · last sync 2 minutes ago</span>
    </span>
    <span class="card__trailing">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <path d="M9.4 18 8 16.6l4.6-4.6L8 7.4 9.4 6l6 6-6 6Z"/>
      </svg>
    </span>
  </span>
</a>

<!-- Square (note: blue icon-wrapper, not teal) -->
<a class="card card--square" href="#">
  <span class="card__top">
    <span class="card__icon-wrapper">
      <!-- assets/icons/scan.svg — fill="currentColor" inherits color/icon/brand -->
      <span class="card__icon-glyph">
        <svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <path d="M3 8V5q0-.825.588-1.412Q4.175 3 5 3h3v2H5v3H3Zm0 13v-3h2v3H3Zm5 0v-2h3v2H8Zm8 0v-2h3v-3h2v3q0 .825-.588 1.413Q19.825 21 19 21h-3Zm3-13V5h-3V3h3q.825 0 1.413.588Q21 4.175 21 5v3h-2Z"/>
        </svg>
      </span>
    </span>
    <span class="card__trailing">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <path d="M9.4 18 8 16.6l4.6-4.6L8 7.4 9.4 6l6 6-6 6Z"/>
      </svg>
    </span>
  </span>
  <span class="card__bottom">
    <span class="card__label">Start scan</span>
    <span class="card__desc">Open the scanner</span>
  </span>
</a>

<!-- Expandable (collapsed) -->
<details class="card card--expandable">
  <summary class="card__header" style="list-style: none; cursor: pointer;">
    <span class="card__leading"></span>
    <span class="card__text">
      <span class="card__label">License key</span>
      <span class="card__desc">AmGq·BvJp·KZ4d·R2sM</span>
    </span>
    <span class="card__trailing">
      <!-- chevron_down — swap to chevron_up when [open] -->
      <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <path d="m12 15-6-6 1.4-1.4 4.6 4.6 4.6-4.6L18 9l-6 6Z"/>
      </svg>
    </span>
  </summary>
  <div class="card__divider"></div>
  <div class="card__content">
    <!-- Expanded content goes here -->
  </div>
</details>
```

## Don'ts

- **Don't render the Square card's icon-wrapper in teal.** Use the brand-blue tokens (`color/surface/brand/softer` + `color/icon/brand`). The Figma file shows teal, but the web design system uses blue — design.md is canonical. Teal is for marketing surfaces only.
- **Don't reach for a different chevron per variant.** Rectangle uses `chevron_right` (drill-in). Square uses `chevron_right` top-right. Expandable uses `chevron_down` (collapsed) and `chevron_up` (expanded). Other glyphs (arrow, caret) break the system's "drill-in vs disclosure" affordance contract.
- **Don't put a Card inside a Card.** Hover/pressed states stack and the visual hierarchy collapses. Use a List inside the Card instead.
- **Don't change the dimensions per breakpoint.** Rectangle/Expandable are 343 wide; Square is 160 wide. If you need a wider tile, that's a different pattern (consider a full-width section header).
- **Don't omit the description on a Rectangle card if there's room.** The Figma layout reserves space for it — collapsing to label-only changes the row's vertical rhythm. If you really have no description, render an empty `<span>` for the slot so the layout stays consistent.
- **Don't add a shadow.** Cards sit flat on the page; elevation is reserved for popovers, dropdowns, and modals. The 1px `color/border/tertiary` outline is the only separation needed.
- **Don't auto-expand all Expandable cards on load.** They default to collapsed. If the user reliably needs the content visible, choose a Rectangle (no toggle) or render the section without a Card wrapper.
- **Don't use a Card for a list of items where each row IS the content.** Cards are tile-shaped destinations — they take the user somewhere. For inline content rows (like a table row), use the List or Table pattern.
