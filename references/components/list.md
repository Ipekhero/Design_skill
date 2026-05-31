# List

> **TL;DR**
> - A **List** is a vertical stack of tappable / interactive rows. Use it for navigation (drilling into a detail view), settings (with checkboxes/radios in the leading slot), or master-detail UIs (where one row is selected and its detail panel is shown elsewhere).
> - The component has two orthogonal axes:
>   - **Row type** (variant) — controls the *density and structure* of the row: `1-line`, `2-line`, `3-line`, `multi-line`, `draggable`.
>   - **Leading element** — controls what sits in the leading slot, independently of row type: `none`, `icon`, `checkbox`, `radio`, `thumbnail`.
> - **No `sizes` axis.** Row density is captured by the variant name. A `1-line` row is always 48px, a `2-line` is 72px, a `3-line` is 88px, etc.
> - **Five states per row**: `default`, `hover`, `pressed`, `selected`, `disabled`. No `focused` (keyboard focus uses `:focus-visible` outline, same call as [[menu]] / [[dropdown]]).
> - **`selected` is not in the Figma `list-item` component** — we add it ourselves for the master-detail pattern (e.g. picking a record in a sidebar so a detail panel updates). The surface token is `surface/selected` `#EFF5FA` — the same blue as [[menu]] and [[dropdown]] (NOT teal). Per [[feedback-web-uses-blue-not-teal]].
> - **Item surface tokens** map cleanly to the catalog — Figma's `surface/list-item/*` namespace uses the same hex values as the catalog `surface/default` / `surface/hover` / `surface/pressed`. No new tokens needed.
> - **Section headers** (40px tall, gray bg) live inside this component (a section header has no meaning outside a list context). The optional num-badge in a section header uses `surface/info/full` `#1660D9` — **the blue here is correct** because it's info-coded (counts of found/matched items, not the Scandit brand teal).

Figma source:
- [List items (single-item permutations)](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=6661-2262)
- [Section header](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=6669-2031)

## When to use

| Use the List when… | Use something else when… |
|---|---|
| You're showing a **vertical enumeration** of records, settings, or files that the user will read, scan, or drill into | The content is laid out as **rows of structured data with columns** — use a [[table]] (when documented) |
| Each row may navigate to a **detail view** (with a trailing `chevron_right` icon) | The list is a **floating picker** triggered by another control — use a [[menu]] (which lives inside a [[dropdown]] / kebab button) |
| The list is **persistent in the page layout** (e.g. a sidebar of records, a settings page section) | The list represents a **single-line truncated label** with no row chrome — use a [[link]] in a paragraph |
| Each row contains a **toggle, checkbox, or radio** as the leading element — settings lists | The selection is **multi-choice and lives inside a floating context** — that's a checkbox-list [[menu]] |
| You need to support **drag-to-reorder** — use the `draggable` row type | The rows are part of a long horizontally-scrollable carousel — that's a different pattern |

## Anatomy

```
┌─────────────────────────────────────────────────────────┐  ← section header (optional)
│ FOUND ITEMS                                      [ 12 ] │    surface/hover bg · label/medium · text/secondary
└─────────────────────────────────────────────────────────┘    optional info-blue num-badge

┌─────────────────────────────────────────────────────────┐
│  [leading]   Title                          [info] [>]  │  ← list item (1-line · 48px tall)
│             ──────────────────────────────────────────  │     border-bottom · border/tertiary · inset 12px left
├─────────────────────────────────────────────────────────┤
│  [thumb]    Title                                  [>]  │  ← list item (2-line · 72px tall)
│             Last Captured · Dec 12, 14:35               │     thumbnail 48×48 · body/small description
│             ──────────────────────────────────────────  │
├─────────────────────────────────────────────────────────┤
│  [thumb]    Title                                  [>]  │  ← list item (3-line · 88px tall)
│             This is a longer description that takes     │
│             up two lines                                │
│             ──────────────────────────────────────────  │
├─────────────────────────────────────────────────────────┤
│  [icon]     Title                                  [>]  │  ← list item (multi-line · variable)
│             IMEI 1     1982749283574398                 │     label/small · body-small key + value pairs
│             IMEI 2     1982749283574398                 │
│             SN         1982749283574398                 │
│             ──────────────────────────────────────────  │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│  ⋮⋮  [leading]   Title                            [info]│  ← draggable (1-line + drag handle)
│             ──────────────────────────────────────────  │     dotted_handle/horizontal · 24px
└─────────────────────────────────────────────────────────┘
```

- **Padding** — every row uses `spacing/padding/m` (12px) on all four sides.
- **Gap between leading element and content** — `spacing/padding/m` (12px).
- **Gap between trailing items** (info text + chevron) — `spacing/padding/s` (8px).
- **Bottom border** — 1px `color/border/tertiary` (`#E1E7ED`), inset 12px from the left so it never touches the leading element block.

## Variants (row type)

The variant controls **vertical content structure**, not the leading element.

| Variant | Min height | Title | Description | Multi-line info | When to use |
|---|---:|---|---|---|---|
| `1-line` | `48px` (`comp-height/2xl`) | `body/medium` | — | — | Plain enumeration: settings rows, simple navigation list, "Recents" |
| `2-line` | `72px` (`comp-height/5xl`) | `body/medium` | `body/small` · `text/secondary` (1 line) | — | Title + metadata: file list (name + modified date), records (name + status) |
| `3-line` | `88px` | `body/medium` | `body/small` · `text/secondary` (up to 2 lines, wraps) | — | Title + longer description: notification rows, search results with snippets |
| `multi-line` | `104px+` (variable) | `body/medium` | — | 2–6 rows of `label/small` key + value pairs (`spacing/inline/l` 16px gap) | Structured records: a captured item with IMEI 1 / IMEI 2 / SN / model fields |
| `draggable` | `48px` | `body/medium` | — | — | Reorderable rows (sortable settings, custom column orders). Prepends a `dotted_handle/horizontal` 24×24 drag affordance before the leading slot |

## Leading element (orthogonal axis)

The leading slot is independent from the row type. Some combinations are not valid (see *Validity* column).

| Leading | Width | Element | Validity |
|---|---:|---|---|
| `none` | — | (no leading slot, content butts up against the 12px left padding) | all row types |
| `icon` | 24px | A 24×24 icon from the [[icons]] catalog, colour `icon/primary` (`#16191C`). **MUST** come from [`references/icons.md`](../icons.md) — never use an icon outside the approved set. If you need a new glyph, add it to `icons.md` first (Material Symbols Rounded / 400 / 24dp), drop the SVG into `assets/icons/`, then reference it here. See "Icon sourcing rule" below. | all row types |
| `checkbox` | 20px (inside 24px slot) | Standard [[checkbox]] component, follows its own state machine independently of the row's hover/pressed/selected | all row types |
| `radio` | 20px (inside 24px slot) | Standard [[radio]] component | all row types |
| `thumbnail` | 48px | A 48×48 image with 4px corner radius. Falls back to `color/gray/30` (`#ACB6BF`) placeholder if the image is missing | **only `2-line`, `3-line`, `multi-line`** — the 48px thumbnail doesn't fit a 48px-tall row |

## States

| State | Trigger | Surface | Text · title | Text · description | Icon (leading + trailing) | Cursor |
|---|---|---|---|---|---|---|
| `default` | Resting | `surface/default` (`#FFFFFF`) | `text/primary` (`#16191C`) | `text/secondary` (`#525A61`) | `icon/primary` / `icon/secondary` | `pointer` (when row is interactive) |
| `hover` | Pointer over row | `surface/hover` (`#F3F5F8`) | `text/primary` | `text/secondary` | unchanged | `pointer` |
| `pressed` | Active click | `surface/pressed` (`#E1E7ED`) | `text/primary` | `text/secondary` | unchanged | `pointer` |
| `selected` | Master-detail current row, sidebar current entry | **`surface/selected` (`#EFF5FA` — brand blue softer)** ← per the web colour rule | `text/primary` | `text/secondary` | unchanged | `pointer` |
| `disabled` | Row not actionable in current context | `surface/default` (no fill change) | `text/disabled` (`#ACB6BF`) | `text/disabled` | `icon/disabled` (`#ACB6BF`) | `not-allowed` |

`selected + hover` uses `surface/selected hover` (`#F3F5F8`) — matches the [[menu]] convention.

## Icon sourcing rule

Every icon rendered inside a list item — the **leading `icon`** slot, the **trailing `chevron_right`** / **`info_circle`** indicators, the **`drag_handle`** on draggable rows — **MUST come from the approved set in [`references/icons.md`](../icons.md)**. This is non-negotiable:

1. **Pick from the catalog.** Browse [`icons.md`](../icons.md) for an existing entry that matches the action's meaning (not just its shape). For example, prefer `chevron_right` for "navigate to detail view" and `arrow_triangle_right` only when you explicitly want the chunky filled triangle (Dropdown trigger affordance).
2. **Copy the SVG verbatim.** Read the matching `assets/icons/<name>.svg` file and copy the `d=` path *byte-for-byte*. Never hand-type, normalize, or "compress" path data — even visually identical paths (e.g. `M5 15C…` vs `M5.00004 15C…`) drift from the asset and silently degrade icon parity across the system. Per [[feedback-icon-paths-from-assets]].
3. **If you need a glyph that isn't catalogued**, do NOT inline a new SVG into the component file. Instead: source it from Material Symbols (Rounded / 400 / 24dp), drop the SVG into `assets/icons/<kebab-name>.svg`, add a row to `icons.md` under the right category, *then* reference it from this component. The catalog is the single source of truth.
4. **For prototype HTML pages** (test pages, demo files), the recommended pattern is a single `<svg><defs><symbol id="i-<name>">…verbatim path…</symbol></defs></svg>` block at the top of the document, then `<svg viewBox="0 0 24 24"><use href="#i-<name>"/></svg>` everywhere the icon appears. This guarantees every instance is byte-identical to the asset and makes the icon set auditable in one place. See [`workspace/iteration-1/list-test.html`](../../workspace/iteration-1/list-test.html) for an example.

The same rule applies to every component (Menu, Dropdown, Card, Button, etc.) — list.md just spells it out because Lists are the densest consumer of icons in the system (every row potentially has 2–3 of them).

## Container

The List container itself is **minimal**. It's a vertical flex stack of `list-item` children with optional `section-header` rows interspersed. No background, no padding, no border. The visual chrome lives entirely on the items (the bottom border separator).

| Property | Value |
|---|---|
| Background | `surface/default` (the parent page surface) |
| Padding | `0` |
| Border / radius | none (items render their own bottom border) |

The list typically sits inside a [[card]] (with its 16px radius) or a page section. If you want the list itself to be the visual chrome, wrap it in a card.

## Section header

A 40px-tall row above a group of items. **Lives inside this component because it has no meaning outside a list.**

| Property | Value |
|---|---|
| Height | `40px` (`comp-height/xl`) |
| Background | `color/surface/hover` (`#F3F5F8`) — a soft gray to separate the group from the rows below |
| Padding | `0 16px` (`spacing/padding/l`) |
| Title | `label/medium` (14/500/20/0.25) · `color/text/secondary` (`#525A61`) |
| Trailing num-badge | Optional. Pill — `color/surface/info/full` (`#1660D9`) bg, `color/text/inverted` (`#FFFFFF`) text, `label/medium` (14/500/20/0.25), 20px tall, padding 0 6px, radius 999. **Blue is correct** here — it's an info-coded count (number of records found, matched, etc.). |

Use section headers to group items by category (e.g. "Found items" + "Missing items"), by time bucket ("Today", "This week"), or by source ("Local files", "Cloud").

## Token matrix (item background by state)

The variant doesn't change the surface — only the row's internal layout. So this is a single column repeated five times across the variants.

| State | All five variants |
|---|---|
| `default` | `color/surface/default` (`#FFFFFF`) |
| `hover` | `color/surface/hover` (`#F3F5F8`) |
| `pressed` | `color/surface/pressed` (`#E1E7ED`) |
| `selected` | `color/surface/selected` (`#EFF5FA`) |
| `selected + hover` | `color/surface/selected hover` (`#F3F5F8`) |
| `disabled` | `color/surface/default` (`#FFFFFF`) — surface unchanged; only the text/icon colours change |

### Label colour

| State | Title | Description / multi-line value |
|---|---|---|
| `default`, `hover`, `pressed`, `selected` | `color/text/primary` (`#16191C`) | `color/text/secondary` (`#525A61`) |
| `disabled` | `color/text/disabled` (`#ACB6BF`) | `color/text/disabled` |

### Leading + trailing icon colour

| State | Token |
|---|---|
| `default`, `hover`, `pressed`, `selected` | `color/icon/primary` (`#16191C`) for the leading; `color/icon/secondary` (`#525A61`) for the trailing `chevron_right` |
| `disabled` | `color/icon/disabled` (`#ACB6BF`) |

## React + Tailwind

```tsx
import { type ReactNode } from 'react';

type RowType    = '1-line' | '2-line' | '3-line' | 'multi-line' | 'draggable';
type LeadingKey = 'none' | 'icon' | 'checkbox' | 'radio' | 'thumbnail';

interface ListItemProps {
  type?: RowType;
  selected?: boolean;
  disabled?: boolean;
  leading?: ReactNode;          // pre-rendered: icon / checkbox / radio / 48×48 <img>
  title: string;
  description?: string;          // 2-line / 3-line
  info?: { label: string; value: string }[];   // multi-line
  trailingInfo?: string;         // small grey "5 modules"
  trailingIcon?: ReactNode;      // chevron_right | info_circle | (omit)
  draggable?: boolean;           // forces the dotted handle
  onClick?: () => void;
  divider?: boolean;             // default true; last row should pass false
}

export function ListItem({
  type = '1-line',
  selected = false,
  disabled = false,
  leading,
  title,
  description,
  info = [],
  trailingInfo,
  trailingIcon,
  draggable = false,
  onClick,
  divider = true,
}: ListItemProps) {
  const minHeight = {
    '1-line':     'min-h-12',     // 48
    '2-line':     'min-h-[72px]',
    '3-line':     'min-h-[88px]',
    'multi-line': 'min-h-[104px]',
    'draggable':  'min-h-12',
  }[type];

  const surface = disabled
    ? 'bg-white cursor-not-allowed'
    : selected
      ? 'bg-surface-selected hover:bg-surface-selected-hover active:bg-surface-pressed cursor-pointer'
      : 'bg-white hover:bg-surface-hover active:bg-surface-pressed cursor-pointer';

  const titleColor = disabled ? 'text-disabled' : 'text-primary';
  const descColor  = disabled ? 'text-disabled' : 'text-secondary';

  return (
    <div
      role={onClick ? 'button' : undefined}
      tabIndex={onClick && !disabled ? 0 : undefined}
      onClick={disabled ? undefined : onClick}
      className={`flex flex-col items-stretch overflow-hidden ${surface}`}
    >
      <div className={`flex items-${type === '1-line' || type === 'draggable' ? 'center' : 'start'} gap-3 p-3 ${minHeight}`}>
        {(draggable || type === 'draggable') && (
          <span className="size-6 shrink-0 text-icon-secondary cursor-grab" aria-hidden="true">{/* dotted_handle */}</span>
        )}
        {leading && <span className="shrink-0">{leading}</span>}

        <div className="flex-1 min-w-0 flex flex-col">
          <p className={`text-base leading-6 tracking-[0.25px] ${titleColor} truncate`}>{title}</p>
          {description && (
            <p className={`text-sm leading-5 tracking-[0.25px] ${descColor} ${type === '2-line' ? 'truncate' : 'line-clamp-2'}`}>
              {description}
            </p>
          )}
          {type === 'multi-line' && info.length > 0 && (
            <div className="flex flex-col gap-1 mt-1">
              {info.map(row => (
                <div key={row.label} className="flex items-center gap-4">
                  <span className="w-16 text-xs leading-4 tracking-[0.25px] font-medium text-secondary">{row.label}</span>
                  <span className="text-sm text-primary">{row.value}</span>
                </div>
              ))}
            </div>
          )}
        </div>

        <div className="flex items-center gap-2 shrink-0">
          {trailingInfo && <span className="text-sm text-secondary whitespace-nowrap">{trailingInfo}</span>}
          {trailingIcon}
        </div>
      </div>
      {divider && <div className="ml-3 h-px bg-border-tertiary" />}
    </div>
  );
}

export function SectionHeader({ title, count }: { title: string; count?: number }) {
  return (
    <div className="flex items-center gap-2 h-10 px-4 bg-surface-hover">
      <span className="flex-1 text-sm font-medium leading-5 text-secondary">{title}</span>
      {count != null && (
        <span className="inline-flex items-center justify-center min-w-5 h-5 px-1.5 rounded-full bg-info-full text-xs font-medium text-white leading-5">
          {count}
        </span>
      )}
    </div>
  );
}
```

Required Tailwind tokens (in `tailwind.config.js`):

```js
colors: {
  'surface-hover':          '#F3F5F8',
  'surface-pressed':        '#E1E7ED',
  'surface-selected':       '#EFF5FA',
  'surface-selected-hover': '#F3F5F8',
  'border-tertiary':        '#E1E7ED',
  'info-full':              '#1660D9',
  'text-primary':           '#16191C',
  'text-secondary':         '#525A61',
  'text-disabled':          '#ACB6BF',
  'icon-primary':           '#16191C',
  'icon-secondary':         '#525A61',
  'icon-disabled':          '#ACB6BF',
},
```

## Standalone HTML / CSS

```html
<style>
  :root {
    --color-surface-default:        #FFFFFF;
    --color-surface-hover:          #F3F5F8;
    --color-surface-pressed:        #E1E7ED;
    --color-surface-selected:       #EFF5FA;
    --color-surface-selected-hover: #F3F5F8;
    --color-surface-info-full:      #1660D9;

    --color-text-primary:           #16191C;
    --color-text-secondary:         #525A61;
    --color-text-disabled:          #ACB6BF;
    --color-text-inverted:          #FFFFFF;

    --color-icon-primary:           #16191C;
    --color-icon-secondary:         #525A61;
    --color-icon-disabled:          #ACB6BF;

    --color-border-tertiary:        #E1E7ED;

    --spacing-padding-s:  8px;
    --spacing-padding-m:  12px;
    --spacing-padding-l:  16px;
    --spacing-inline-l:   16px;
    --size-cornerradius-xs:    4px;
    --size-cornerradius-round: 999px;
  }

  /* ─── Container ─── */
  .list { display: flex; flex-direction: column; background: var(--color-surface-default); }

  /* ─── Section header ─── */
  .section-header {
    display: flex; align-items: center; gap: var(--spacing-padding-s);
    height: 40px;
    padding: 0 var(--spacing-padding-l);
    background: var(--color-surface-hover);
  }
  .section-header__title {
    flex: 1; font-family: 'Inter', system-ui, sans-serif;
    font-size: 14px; font-weight: 500; line-height: 20px; letter-spacing: 0.25px;
    color: var(--color-text-secondary);
  }
  .section-header__count {
    display: inline-flex; align-items: center; justify-content: center;
    min-width: 20px; height: 20px; padding: 0 6px;
    background: var(--color-surface-info-full);
    color: var(--color-text-inverted);
    font-size: 14px; font-weight: 500; line-height: 20px; letter-spacing: 0.25px;
    border-radius: var(--size-cornerradius-round);
  }

  /* ─── List item ─── */
  .list-item {
    display: flex; flex-direction: column;
    background: var(--color-surface-default);
    cursor: pointer;
    transition: background 80ms;
  }
  .list-item__content {
    display: flex; align-items: center; gap: var(--spacing-padding-m);
    padding: var(--spacing-padding-m);
    width: 100%;
  }
  .list-item--2-line .list-item__content,
  .list-item--3-line .list-item__content,
  .list-item--multi-line .list-item__content { align-items: flex-start; }
  .list-item--1-line     { min-height: 48px; }
  .list-item--2-line     { min-height: 72px; }
  .list-item--3-line     { min-height: 88px; }
  .list-item--multi-line { min-height: 104px; }
  .list-item--draggable  { min-height: 48px; }

  .list-item__leading {
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
    color: var(--color-icon-primary);
  }

  .list-item__body {
    flex: 1 1 0; min-width: 0;
    display: flex; flex-direction: column;
  }
  .list-item__title {
    font-family: 'Inter', system-ui, sans-serif;
    font-size: 16px; font-weight: 400; line-height: 24px; letter-spacing: 0.25px;
    color: var(--color-text-primary);
    overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
  }
  .list-item__description {
    font-family: inherit;
    font-size: 14px; font-weight: 400; line-height: 20px; letter-spacing: 0.25px;
    color: var(--color-text-secondary);
  }
  .list-item--2-line .list-item__description {
    overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
  }
  .list-item--3-line .list-item__description {
    display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;
    overflow: hidden;
  }
  .list-item__info-rows {
    display: flex; flex-direction: column; gap: 4px;
    margin-top: 4px;
  }
  .list-item__info-row {
    display: flex; align-items: center; gap: var(--spacing-inline-l);
    width: 100%;
  }
  .list-item__info-label {
    width: 64px;
    font-size: 12px; font-weight: 500; line-height: 16px; letter-spacing: 0.25px;
    color: var(--color-text-secondary);
  }
  .list-item__info-value {
    font-size: 14px; line-height: 20px;
    color: var(--color-text-primary);
  }

  .list-item__trailing {
    display: flex; align-items: center; gap: var(--spacing-padding-s);
    flex-shrink: 0;
  }
  .list-item__trailing-info {
    font-size: 14px; line-height: 20px; color: var(--color-text-secondary);
    white-space: nowrap;
  }

  .list-item__handle {
    width: 24px; height: 24px;
    color: var(--color-icon-secondary);
    flex-shrink: 0;
    cursor: grab;
  }

  /* ─── Border ─── */
  .list-item__divider {
    height: 1px;
    background: var(--color-border-tertiary);
    margin-left: var(--spacing-padding-m);
  }
  .list-item--no-divider .list-item__divider { display: none; }

  /* ─── State ladder — guard against disabled/selected ─── */
  .list-item:not(.list-item--disabled):not(.list-item--selected):hover,
  .list-item.is-hover { background: var(--color-surface-hover); }
  .list-item:not(.list-item--disabled):not(.list-item--selected):active,
  .list-item.is-pressed { background: var(--color-surface-pressed); }

  /* selected */
  .list-item--selected { background: var(--color-surface-selected); }
  .list-item--selected:not(.list-item--disabled):hover,
  .list-item--selected.is-hover { background: var(--color-surface-selected-hover); }
  .list-item--selected:not(.list-item--disabled):active,
  .list-item--selected.is-pressed { background: var(--color-surface-pressed); }

  /* disabled — wins */
  .list-item--disabled, .list-item.is-disabled { cursor: not-allowed; background: var(--color-surface-default); }
  .list-item--disabled .list-item__title,
  .list-item--disabled .list-item__description,
  .list-item--disabled .list-item__info-label,
  .list-item--disabled .list-item__info-value,
  .list-item--disabled .list-item__trailing-info,
  .list-item.is-disabled .list-item__title,
  .list-item.is-disabled .list-item__description { color: var(--color-text-disabled); }
  .list-item--disabled .list-item__leading,
  .list-item.is-disabled .list-item__leading { color: var(--color-icon-disabled); }
</style>
```

## Don'ts

- **Don't use teal for the selected row.** Same call as [[menu]] and [[dropdown]]. The web design system substitutes `surface/selected: #EFF5FA` (brand blue softer) for Figma's teal `list item/selected` `#E7F7F9`. Per [[feedback-web-uses-blue-not-teal]].
- **Don't put a 48×48 thumbnail in a 1-line row.** The row is 48px tall — the thumbnail equals the entire row height, leaving no padding. Promote to 2-line (72px) or 3-line (88px) when you need a thumbnail.
- **Don't omit the chevron_right when the row navigates somewhere.** The chevron is the user's signal that tapping the row opens a detail view. A row with no trailing affordance reads as a leaf (settings toggle, label).
- **Don't add a `focused` state with its own background colour.** Keyboard focus is the OS-native `:focus-visible` outline ring. Same call as [[menu]] / [[dropdown]].
- **Don't draw a divider after the last row in a section.** Drop the bottom border on the last item to avoid a stray line touching the bottom of the card or section.
- **Don't mix row types in a single list.** A list of records should be all-2-line or all-3-line — alternating heights breaks the rhythm and makes the list look broken. Section headers are the right tool to group items of the same type with different metadata.
- **Don't hand-type icon SVGs.** Copy paths verbatim from `assets/icons/<name>.svg`. Per [[feedback-icon-paths-from-assets]].
- **Don't use Roboto.** Figma's `body/medium/font` reads `Roboto` — this is a placeholder. Web ships Inter. Per [[feedback-figma-font-placeholders]].
- **Don't substitute teal for the section header num-badge.** The num-badge here is `surface/info/full` `#1660D9` — informational blue, not the teal brand colour. Figma renders this in the correct colour because it's already coded as `info`, not `brand`.
