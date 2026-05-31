# Menu

> **TL;DR**
> - A **Menu** is a floating list of selectable items shown in a popover above other content — used inside Dropdowns, overflow (`menu_dots_vertical`) buttons, right-click context menus, and "more actions" affordances.
> - A Menu is composed of two parts: the **container** (the floating white surface) and one-or-more **menu items** (the rows). Items are the only things with state; the container is always the same colour, radius, and shadow.
> - **Four item variants** based on what sits in the leading slot:
>   - `standard` — text only, no leading element
>   - `with-icon` — 24×24 icon in the leading slot (`icon/primary`)
>   - `checkbox` — multi-select rows (the menu becomes a checklist)
>   - `radio` — single-select rows (the menu becomes a choice picker)
> - **Two sizes** — `lg` (40px / `comp-height/xl`) for default product menus, `sm` (32px / `comp-height/l`) for compact menus inside dense surfaces (e.g. dropdowns inside data tables).
> - **Five states per item** — `default`, `hover`, `pressed`, `selected`, `disabled`. No `focused` state (matches the [[dropdown]] decision — a keyboard-focus ring is the responsibility of the trigger, not the menu items).
> - **The selected item uses brand-blue softer (`#EFF5FA`)**, NOT Figma's teal `list item/selected` (`#E7F7F9`) — see [[feedback-web-uses-blue-not-teal]]. The Figma library uses teal here purely because teal is its accent in the brand identity; the production web design system substitutes brand blue.
> - **All tokens align with `design.md`** — Menu items reuse the standard `surface/hover`, `surface/pressed`, `surface/selected` row tokens (the same family used by [[list]], [[chip]], [[dropdown]]). No new component-specific surface tokens are needed.

Figma source:
- [Menu items (single-item permutations)](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=6481-8736)
- [Menu containers (full assembled menus)](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=6481-8758)

## When to use

| Use the Menu when… | Use something else when… |
|---|---|
| The trigger opens a **floating list** of options (Dropdown, more-actions button, kebab menu, right-click context menu) | The list is **persistent in the page layout** — that's a [[list]], not a menu |
| You need to pick **one** option from a small set (1–8 items) → `radio` variant | You need to choose from a long scrollable set (>20 items) → use a [[dropdown]] with a search filter |
| You need to toggle **multiple** options at once → `checkbox` variant | The actions live in the page itself (a toolbar or page header) — use [[button]]s, not a menu |
| The menu represents **navigation between pages or views** | Use the [[sidebar]] or top-nav, not a menu |
| The actions need an **icon affordance** to distinguish them visually → `with-icon` variant | The icon would be purely decorative — keep the menu items as `standard` (text only) |

## Anatomy

```
┌───────────────────────────────────────────────┐  ← Container
│                                               │    bg: surface/default (#FFFFFF)
│  ┌─────────────────────────────────────────┐  │    radius: cornerradius/s (4px)
│  │ [leading]  Menu item label   [trailing] │  │    shadow: shadow-lg (Elevation/2)
│  └─────────────────────────────────────────┘  │    padding-y: 8px (lg) / 4px (sm)
│  ┌─────────────────────────────────────────┐  │
│  │ [leading]  Menu item label   [trailing] │  │  ← Menu item (40px lg / 32px sm)
│  └─────────────────────────────────────────┘  │    bg: per state (default/hover/pressed/selected)
│  ┌─────────────────────────────────────────┐  │    padding-x: 12px (spacing/padding/m)
│  │ [leading]  Menu item label   [trailing] │  │    gap: 8px (spacing/padding/s)
│  └─────────────────────────────────────────┘  │    text: body/medium · text/primary
│                                               │
└───────────────────────────────────────────────┘
```

- **Leading slot** (24px square) — empty (`standard`), an `icon/primary` 24×24 icon (`with-icon`), a 20×20 checkbox (`checkbox`), or a 20×20 radio button (`radio`).
- **Label** — `body/medium` (16/400/24/0.25), colour `text/primary` (or `text/disabled` when the item is disabled).
- **Trailing slot** (optional) — typically the `num-badge` neutral pill (e.g. unread count next to "Inbox"). Renders inside the row with the standard 20px badge spec.

## Variants

Item type lives in the leading slot. **All four variants share the same surface tokens, sizes, and states** — only the leading content differs.

| Variant | Leading slot | Typical use |
|---|---|---|
| `standard` | (empty) | Plain text actions: "Edit", "Duplicate", "Delete" |
| `with-icon` | 24×24 icon (`icon/primary`) | Icon-prefixed actions: "Settings" + gear icon, "Share" + share icon |
| `checkbox` | 20×20 checkbox | Multi-select lists: "Show completed tasks", "Notify me by email" |
| `radio` | 20×20 radio button | Single-select pickers: sort order, view density, theme |

## Sizes

| Token | Height | Padding-x | Gap | When to use |
|---|---:|---:|---:|---|
| `lg` | **40px** (`size/comp-height/xl`) | 12px (`spacing/padding/m`) | 8px (`spacing/padding/s`) | Default product menus, kebab menus on cards |
| `sm` | **32px** (`size/comp-height/l`) | 12px (`spacing/padding/m`) | 8px (`spacing/padding/s`) | Compact menus inside dense surfaces — dropdowns embedded in data-table cells, in-row overflow menus |

The container's vertical padding scales with the item size: `lg` menu uses `spacing/padding/s` (8px) top + bottom, `sm` menu uses `spacing/padding/xs` (4px). This keeps the visual gap above the first row and below the last row proportional to the row height.

## States (per item)

| State | Trigger | Surface | Label colour | Cursor |
|---|---|---|---|---|
| `default` | Resting | `surface/default` (`#FFFFFF`) | `text/primary` (`#16191C`) | `pointer` |
| `hover` | Pointer over row | `surface/hover` (`#F3F5F8`) | `text/primary` | `pointer` |
| `pressed` | Active click | `surface/pressed` (`#E1E7ED`) | `text/primary` | `pointer` |
| `selected` | Currently-chosen value (radio, current view, etc.) | **`surface/selected` (`#EFF5FA` — brand blue softer)** ← per the web colour rule, NOT Figma's teal `list item/selected` `#E7F7F9` | `text/primary` | `pointer` |
| `disabled` | Action unavailable (e.g. "Delete" with nothing selected) | `surface/default` (no fill change) | `text/disabled` (`#ACB6BF`) | `not-allowed` |

`selected` can combine with `hover`/`pressed` — `surface/selected hover` (`#F3F5F8`) covers the hover-over-already-selected case (e.g. mousing over the current sort option in a radio menu).

## Container spec

The container is **identical across all four variants and both sizes**. It does not have its own state machine — the container is always white, 4px corners, with `shadow-lg` (Elevation/2 directional).

| Token | Value | Notes |
|---|---|---|
| Background | `color/surface/default` (`#FFFFFF`) | |
| Corner radius | `size/cornerradius/s` (`4px`) | |
| Shadow | `shadow-lg` (Elevation/2) — `0 1px 2px 0 rgba(0,0,0,0.30), 0 2px 6px 2px rgba(0,0,0,0.15)` | Two-layer directional drop shadow; floats above page content |
| Vertical padding | `spacing/padding/s` (8px) for `lg`, `spacing/padding/xs` (4px) for `sm` | |
| Horizontal padding | `0` | Each item carries its own 12px horizontal padding so the hover/pressed fill stretches edge-to-edge |
| Min width | Content-driven; Figma reference frames are 343px (lg) and 200px (sm) but real menus should be **fluid** within their trigger — match the trigger width for Dropdown menus, sit at content width for context menus |

## Token matrix (item background by variant × state)

The variant doesn't change the surface — only the leading content. So this is a single column repeated four times:

| State | All four variants (`standard`, `with-icon`, `checkbox`, `radio`) |
|---|---|
| `default` | `color/surface/default` (`#FFFFFF`) |
| `hover` | `color/surface/hover` (`#F3F5F8`) |
| `pressed` | `color/surface/pressed` (`#E1E7ED`) |
| `selected` | `color/surface/selected` (`#EFF5FA`) |
| `selected + hover` | `color/surface/selected hover` (`#F3F5F8`) |
| `disabled` | `color/surface/default` (`#FFFFFF`) — surface unchanged; only the label colour changes |

### Label colour

| State | Token |
|---|---|
| `default`, `hover`, `pressed`, `selected` | `color/text/primary` (`#16191C`) |
| `disabled` | `color/text/disabled` (`#ACB6BF`) |

### Leading icon colour (`with-icon` variant only)

| State | Token |
|---|---|
| `default`, `hover`, `pressed`, `selected` | `color/icon/primary` (`#16191C`) |
| `disabled` | `color/icon/disabled` (`#ACB6BF`) |

## React + Tailwind

```tsx
import { type ReactNode } from 'react';

type ItemVariant = 'standard' | 'with-icon' | 'checkbox' | 'radio';
type ItemSize    = 'lg' | 'sm';
type ItemState   = 'default' | 'selected';   // hover/pressed handled by :hover/:active

interface MenuItemProps {
  variant?: ItemVariant;
  size?: ItemSize;
  state?: ItemState;
  disabled?: boolean;
  leading?: ReactNode;          // for `with-icon`: a 24×24 icon. for `checkbox`/`radio`: the input.
  trailing?: ReactNode;         // optional badge or shortcut
  onClick?: () => void;
  children: ReactNode;
}

export function MenuItem({
  variant = 'standard',
  size = 'lg',
  state = 'default',
  disabled = false,
  leading,
  trailing,
  onClick,
  children,
}: MenuItemProps) {
  const sizeClass = size === 'lg' ? 'h-10' : 'h-8';

  const surface = disabled
    ? 'bg-white cursor-not-allowed'
    : state === 'selected'
      ? 'bg-surface-selected hover:bg-surface-selected-hover active:bg-surface-pressed cursor-pointer'
      : 'bg-white hover:bg-surface-hover active:bg-surface-pressed cursor-pointer';

  const labelColor = disabled ? 'text-disabled' : 'text-primary';

  return (
    <button
      type="button"
      role="menuitem"
      aria-disabled={disabled || undefined}
      onClick={disabled ? undefined : onClick}
      className={`flex items-center gap-2 w-full px-3 ${sizeClass} ${surface} text-left transition-colors`}
    >
      {(variant === 'with-icon' || variant === 'checkbox' || variant === 'radio') && (
        <span className="flex items-center justify-center w-6 shrink-0">{leading}</span>
      )}
      <span className={`flex-1 min-w-0 text-base leading-6 tracking-[0.25px] ${labelColor} truncate`}>
        {children}
      </span>
      {trailing && <span className="flex items-center shrink-0">{trailing}</span>}
    </button>
  );
}

interface MenuProps {
  size?: ItemSize;
  children: ReactNode;
}

export function Menu({ size = 'lg', children }: MenuProps) {
  const padding = size === 'lg' ? 'py-2' : 'py-1';
  return (
    <div
      role="menu"
      className={`bg-white rounded-sm shadow-lg overflow-hidden ${padding} min-w-[200px]`}
    >
      {children}
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
  'text-primary':           '#16191C',
  'text-disabled':          '#ACB6BF',
  'icon-primary':           '#16191C',
  'icon-disabled':          '#ACB6BF',
},
boxShadow: {
  lg: '0 1px 2px 0 rgba(0,0,0,0.30), 0 2px 6px 2px rgba(0,0,0,0.15)',
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
    --color-text-primary:           #16191C;
    --color-text-disabled:          #ACB6BF;
    --color-icon-primary:           #16191C;
    --color-icon-disabled:          #ACB6BF;

    --size-comp-height-l:  32px;
    --size-comp-height-xl: 40px;
    --size-cornerradius-s: 4px;
    --spacing-padding-xs:  4px;
    --spacing-padding-s:   8px;
    --spacing-padding-m:   12px;

    --shadow-lg: 0 1px 2px 0 rgba(0,0,0,0.30), 0 2px 6px 2px rgba(0,0,0,0.15);
  }

  /* ─── Container ─── */
  .menu {
    background: var(--color-surface-default);
    border-radius: var(--size-cornerradius-s);
    box-shadow: var(--shadow-lg);
    padding: var(--spacing-padding-s) 0;     /* lg */
    overflow: hidden;
    min-width: 200px;
    display: flex;
    flex-direction: column;
  }
  .menu--sm { padding: var(--spacing-padding-xs) 0; }

  /* ─── Item ─── */
  .menu-item {
    display: flex;
    align-items: center;
    gap: var(--spacing-padding-s);
    width: 100%;
    padding: 0 var(--spacing-padding-m);
    height: var(--size-comp-height-xl);              /* lg */
    background: var(--color-surface-default);
    border: 0;
    cursor: pointer;
    text-align: left;
    transition: background 80ms;
  }
  .menu-item--sm { height: var(--size-comp-height-l); }

  .menu-item__label {
    flex: 1 1 0;
    min-width: 0;
    font-family: 'Inter', system-ui, sans-serif;
    font-size: 16px;
    font-weight: 400;
    line-height: 24px;
    letter-spacing: 0.25px;
    color: var(--color-text-primary);
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .menu-item__leading {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 24px;
    flex-shrink: 0;
  }

  .menu-item__trailing { flex-shrink: 0; }

  /* ─── State ladder (guard against disabled/selected variants) ─── */
  .menu-item:not(.menu-item--disabled):not(.menu-item--selected):hover,
  .menu-item.is-hover { background: var(--color-surface-hover); }

  .menu-item:not(.menu-item--disabled):not(.menu-item--selected):active,
  .menu-item.is-pressed { background: var(--color-surface-pressed); }

  /* ─── Selected (and selected + hover) ─── */
  .menu-item--selected { background: var(--color-surface-selected); }
  .menu-item--selected:not(.menu-item--disabled):hover,
  .menu-item--selected.is-hover { background: var(--color-surface-selected-hover); }
  .menu-item--selected:not(.menu-item--disabled):active,
  .menu-item--selected.is-pressed { background: var(--color-surface-pressed); }

  /* ─── Disabled — wins over everything ─── */
  .menu-item--disabled,
  .menu-item.is-disabled {
    cursor: not-allowed;
    background: var(--color-surface-default);
  }
  .menu-item--disabled .menu-item__label,
  .menu-item.is-disabled .menu-item__label { color: var(--color-text-disabled); }
</style>

<!-- Example: large menu with one icon item, one selected radio item, one disabled standard item -->
<div class="menu" role="menu">
  <button class="menu-item" role="menuitem">
    <span class="menu-item__leading">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
        <!-- settings.svg path here -->
      </svg>
    </span>
    <span class="menu-item__label">Settings</span>
  </button>
  <button class="menu-item menu-item--selected" role="menuitemradio" aria-checked="true">
    <span class="menu-item__leading"><!-- radio (filled) --></span>
    <span class="menu-item__label">Sort by date</span>
  </button>
  <button class="menu-item menu-item--disabled" role="menuitem" aria-disabled="true">
    <span class="menu-item__label">Delete (nothing selected)</span>
  </button>
</div>
```

## Composition with other components

- **Dropdown** opens its menu using this exact spec — the dropdown's open state (`state=selected`) renders a Menu container below the trigger, sized to match. See [[dropdown]] for the full open/close behaviour and trigger ↔ menu width matching.
- **Overflow / kebab buttons** (`menu_dots_vertical` icon button) open a context menu with these same items. The button is responsible for positioning (`popper.js` / floating-ui); the menu is just rendered with this component.
- **Right-click context menus** use the same Menu. The trigger and positioning are different (mouse coords + native `contextmenu` event), but the visual spec is identical.

## Don'ts

- **Don't use teal for the selected item.** Figma library shows `list item/selected: #E7F7F9` (teal). The web design system substitutes `surface/selected: #EFF5FA` (brand blue softer). Per [[feedback-web-uses-blue-not-teal]]. The teal value is purely a Figma library token for the marketing-tinted UI Kit — it must not ship to production.
- **Don't add `focused` as a separate state with its own colour.** Keyboard focus on a menu item should follow the OS-native focus ring (`:focus-visible` outline). Adding a dedicated `focused` background colour duplicates state and conflicts with `hover` when keyboard and mouse both target the same row. (Same call as [[dropdown]].)
- **Don't omit `disabled` from the state machine.** Figma's menu items node doesn't render a disabled state, but real product menus need one ("Delete" with nothing selected, "Save" with no changes, etc.). Use `text/disabled` for the label and `cursor: not-allowed` — leave the surface white.
- **Don't draw dividers between every item.** The default menu has no separators. Use dividers only when the menu has **logically grouped sections** (e.g. file actions vs. share actions vs. destructive actions) — and use a single 1px `border/tertiary` rule with 4px vertical padding around it.
- **Don't render checkbox / radio items without the actual control in the leading slot.** A "Show details" menu item with no checkbox visible is just a confusing toggle button. Always render the 20×20 checkbox or 20×20 radio so the multi-/single-select affordance is clear.
- **Don't hand-type icon SVGs for the `with-icon` variant.** Copy paths verbatim from `assets/icons/<name>.svg`. Per [[feedback-icon-paths-from-assets]].
- **Don't use Roboto.** Figma's `body/medium/font` reads `Roboto` — this is a placeholder. Web ships Inter. Per [[feedback-figma-font-placeholders]].
- **Don't stretch the menu wider than its content needs.** For Dropdown menus, match the trigger width via `min-width`. For context menus, let `width: max-content` size to the longest label. Don't hardcode 343px just because Figma's reference frame is 343px.
