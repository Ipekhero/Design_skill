d# Chip

> **When to use:** Help people enter information or filter content. Two types based on the user's intent:
> - **Filter** — toggleable. Tap to select / deselect. Used in filter bars, faceted search, tag filtering. Can be single- or multi-select.
> - **Input** — represents an item the user has entered (a tag, an email recipient, a selected option in a multi-picker). Tap the trailing × to remove the chip permanently — reverting requires an action elsewhere.
>
> **Figma:** [open in UI Kit](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=4397-3636)

> **Notes:**
>
> - **Two types, 5 states each:** Filter and Input. States are `default · hover · selected · selected_hover · disabled`. There's no `pressed` — hover acts as the active-interaction state because chips are too small for a meaningful pressed shift.
> - **Pill-shaped** (`size/cornerRadius/round`, 999px) — always. The chip never gets squared corners.
> - **32px tall**, single-line label only. If the label is too long, truncate with ellipsis — never wrap or stack.
> - **⚠ Selected colour divergence:** Figma renders the Selected state with `color/surface/chip/selected: #16191C` (near-black). The Scandit web design system substitutes **brand blue** (`color/surface/interactive: #1047A1`) per the web colour rule — same precedent as the Primary Button decision. The Figma render should be treated as out-of-date for web product use.
> - **No new tokens added to design.md** — chip reuses existing tokens: default surface = `background/secondary`, selected surface = `surface/interactive`, disabled surface = `surface/disabled`. The Figma `color/surface/chip/*` namespace is documented inline as Figma-side aliases.
> - **Icons:** Filter selected uses leading [`check`](../../assets/icons/check.svg) at 20×20; Input selected uses trailing [`close_small`](../../assets/icons/close-small.svg) at 20×20. Both inherit colour from the chip's text colour (`color/text/inverted` = white when selected).

## Variants

| Variant | Figma label | Usage |
|---|---|---|
| `filter` | Filter | Toggleable filter chip. Tap to select / deselect. Selected state adds a leading 20×20 `check`. Used in filter bars and faceted search. Filter Chips can be set for single-selection or multi-selection (the component is agnostic — the parent group manages the policy). |
| `input` | Input | Represents an entered or selected item with a trailing 20×20 `close_small` for removal. Tapping the × is destructive — it removes the chip permanently. Reverting requires an action elsewhere (e.g. re-typing the value or selecting it again from a list). |

## Sizes

No size axis — chip is fixed at **32px tall** (`size/comp-height/l`). If a more compact tag is needed, use **Badge** instead (24px, label-only, no interactive states).

## States

- **default** — Resting unselected state. Outlined chip: pale gray surface + 1px border.
- **hover** — Unselected hover. Surface shifts slightly darker; border unchanged. `cursor: pointer`.
- **selected** — Filled chip. Brand blue surface, white label, leading or trailing icon depending on type. **No border** (the colored surface is the edge).
- **selected_hover** — Selected + hover. Surface shifts to the interactive-hover step (lighter blue). Icon and text colours unchanged. `cursor: pointer`.
- **disabled** — Pale gray surface (no border), dim text. Not interactive. `cursor: not-allowed`. Applies to both Filter and Input types regardless of selected state.

## Tokens per type × state

The colour matrix. Text and icon colours on the **selected** states use `color/text/inverted` / white; unselected uses `color/text/primary`.

### Filter

| State | Surface | Border (1px) | Text | Leading icon |
|---|---|---|---|---|
| `default` | `background/secondary` (`#F7F7F7`) ← Figma alias: `color/surface/chip/default` | `color/border/secondary` (`#C7CFD6`) | `color/text/primary` (`#16191C`) | — |
| `hover` | `#E6E6E6` ← Figma alias: `color/surface/chip/hover`. Doesn't match design.md's `surface/hover` (`#F3F5F8`) — chip-specific value, inlined for now. | `color/border/secondary` (unchanged) | `color/text/primary` | — |
| `selected` | `color/surface/interactive` (`#1047A1`) ← BLUE per design.md, NOT Figma's near-black `#16191C` | **none** | `color/text/inverted` (`#FFFFFF`) | [`check`](../../assets/icons/check.svg) 20×20, `color/icon/on-color` (white) |
| `selected_hover` | `color/surface/interactive hover` (`#1660D9`) | **none** | `color/text/inverted` | `check` 20×20, white |
| `disabled` | `#E6E6E6` ← Figma alias: `color/surface/chip/disabled` (same hex as `chip/hover`). Surface stays put across hover/disabled; the disabled signal is the dim text colour. | **none** | `color/text/disabled` (`#ACB6BF`) | — |

### Input

| State | Surface | Border (1px) | Text | Trailing icon |
|---|---|---|---|---|
| `default` | `background/secondary` (`#F7F7F7`) | `color/border/secondary` (`#C7CFD6`) | `color/text/primary` (`#16191C`) | — |
| `hover` | `#E6E6E6` ← Figma alias: `color/surface/chip/hover`. Doesn't match design.md's `surface/hover` (`#F3F5F8`) — chip-specific value, inlined for now. | `color/border/secondary` (unchanged) | `color/text/primary` | — |
| `selected` | `color/surface/interactive` (`#1047A1`) ← BLUE | **none** | `color/text/inverted` (`#FFFFFF`) | [`close_small`](../../assets/icons/close-small.svg) 20×20, `color/icon/on-color` (white) |
| `selected_hover` | `color/surface/interactive hover` (`#1660D9`) | **none** | `color/text/inverted` | `close_small` 20×20, white |
| `disabled` | `#E6E6E6` ← Figma alias: `color/surface/chip/disabled`. Same hex as Filter's chip/disabled. | **none** | `color/text/disabled` (`#ACB6BF`) | — |

## Anatomy

```
  Filter (default)              Filter (selected)            Input (selected)
  ┌────────────────┐            ┌─────────────────┐          ┌────────────────┐
  │░░░░░  Chip  ░░░│  outlined  │██  ✓  Chip   ██│  filled  │██   Chip   × ██│  filled
  └────────────────┘  pill      └─────────────────┘  pill    └────────────────┘  pill
     32px tall                     32px tall                    32px tall
     px: 12px (m)                  pl: 8px (s), pr: 12px (m)    pl: 12px (m), pr: 4px (xs)
                                   gap: 4px (xs) icon ↔ label   gap: 4px (xs) label ↔ icon
                                   leading: check 20×20         trailing: close_small 20×20
```

Common to all states: `height: 32px`, `border-radius: 999px` (`size/cornerRadius/round`), label is `body/small` — 14px Regular, 20px line-height, 0.25px letter-spacing.

The icon's **20×20 box** sits inside the chip's 32px height with `items-center` alignment. The Input chip's trailing × has a **48×48 invisible tap-area** (centered on the 20px icon) so the destructive action is easier to hit precisely.

## Code

### In-repo (React + Tailwind, scandit-web mapping)

```tsx
import { CheckIcon, CloseSmallIcon } from '@/icons';

type ChipType = 'filter' | 'input';
type ChipProps = {
  type: ChipType;
  label: string;
  selected?: boolean;
  disabled?: boolean;
  onToggle?: () => void;        // filter: toggles selected
  onRemove?: () => void;        // input: removes the chip permanently
};

export function Chip({ type, label, selected, disabled, onToggle, onRemove }: ChipProps) {
  const isFilled = !disabled && selected;
  const handleClick = type === 'filter' ? onToggle : undefined; // input chip's surface isn't tappable; the × is

  return (
    <span
      className={[
        'inline-flex items-center h-8 rounded-full text-sm tracking-[0.25px] leading-5 whitespace-nowrap',
        // unselected (outlined)
        !isFilled && !disabled && [
          'bg-configurator-gray-5 text-ntypo-primary border border-configurator-gray-20',
          type === 'filter' && 'cursor-pointer hover:bg-configurator-gray-5',
        ].filter(Boolean).join(' '),
        // selected (filled, BLUE per design.md — NOT Figma's near-black)
        isFilled && [
          'bg-surface-full-primary text-white border-0',
          'hover:bg-surface-full-primary-hover cursor-pointer',
        ].join(' '),
        // disabled
        disabled && 'bg-configurator-gray-10 text-configurator-gray-30 border-0 cursor-not-allowed',
        // padding: filter selected has leading icon; input selected has trailing icon
        !isFilled && 'px-3',
        isFilled && type === 'filter' && 'gap-1 pl-2 pr-3',
        isFilled && type === 'input'  && 'gap-1 pl-3 pr-1',
      ].filter(Boolean).join(' ')}
      onClick={handleClick}
      role={type === 'filter' ? 'checkbox' : undefined}
      aria-checked={type === 'filter' ? !!selected : undefined}
      aria-disabled={disabled || undefined}
    >
      {isFilled && type === 'filter' && <CheckIcon className="size-5" aria-hidden="true" />}
      <span>{label}</span>
      {isFilled && type === 'input' && (
        <button
          type="button"
          aria-label={`Remove ${label}`}
          disabled={disabled}
          onClick={(e) => { e.stopPropagation(); onRemove?.(); }}
          className="size-5 inline-grid place-items-center rounded-full"
        >
          <CloseSmallIcon className="size-5" aria-hidden="true" />
        </button>
      )}
    </span>
  );
}
```

### Standalone artifact (prototype)

```html
<style>
  :root {
    --color-surface-default-chip:        #F7F7F7;   /* background/secondary — Figma calls it color/surface/chip/default */
    --color-surface-chip-hover:          #E6E6E6;   /* chip-specific hover (NOT surface/hover #F3F5F8) — also used for chip disabled */
    --color-surface-interactive:         #1047A1;   /* BLUE per design.md, NOT Figma's near-black */
    --color-surface-interactive-hover:   #1660D9;
    --color-surface-chip-disabled:       #E6E6E6;   /* same hex as chip-hover — Figma uses one shared chip-specific gray */
    --color-border-secondary:            #C7CFD6;
    --color-text-primary:                #16191C;
    --color-text-inverted:               #FFFFFF;
    --color-text-disabled:               #ACB6BF;
  }

  .chip {
    display: inline-flex; align-items: center;
    height: 32px;
    border-radius: 999px;                /* size/cornerRadius/round */
    font-family: Inter, system-ui, sans-serif;
    font-size: 14px; line-height: 20px;  /* body/small */
    letter-spacing: 0.25px;
    white-space: nowrap;
    background: var(--color-surface-default-chip);
    border: 1px solid var(--color-border-secondary);
    color: var(--color-text-primary);
    padding: 0 12px;
    transition: background-color 120ms;
    cursor: pointer;
  }
  .chip:not(.is-disabled):not([disabled]):hover { background: var(--color-surface-chip-hover); }

  .chip--selected {
    background: var(--color-surface-interactive);
    color: var(--color-text-inverted);
    border: 0;
    gap: 4px;                            /* spacing/padding/xs */
  }
  .chip--selected:not(.is-disabled):not([disabled]):hover { background: var(--color-surface-interactive-hover); }

  /* Filter selected: leading check, asymmetric padding (pl 8 / pr 12) */
  .chip--filter.chip--selected   { padding: 0 12px 0 8px; }
  /* Input selected: trailing close, asymmetric padding (pl 12 / pr 4) */
  .chip--input.chip--selected    { padding: 0 4px 0 12px; }

  .chip__icon { width: 20px; height: 20px; display: inline-grid; place-items: center; color: currentColor; }

  /* Input × button — invisible 48×48 tap area for accessible click target */
  .chip__remove {
    width: 20px; height: 20px;
    display: inline-grid; place-items: center;
    background: transparent; border: 0; padding: 0;
    color: inherit; cursor: pointer;
    border-radius: 999px;
    position: relative;
  }
  .chip__remove::before {
    content: '';
    position: absolute; inset: -14px;     /* extends to 48×48 */
  }

  .chip[disabled], .chip.is-disabled {
    background: var(--color-surface-chip-disabled);
    color: var(--color-text-disabled);
    border: 0;
    cursor: not-allowed;
  }
</style>

<!-- Filter (default + selected) -->
<span class="chip chip--filter" role="checkbox" aria-checked="false">Active</span>
<span class="chip chip--filter chip--selected" role="checkbox" aria-checked="true">
  <span class="chip__icon" aria-hidden="true">
    <!-- assets/icons/check.svg -->
    <svg viewBox="0 0 24 24" fill="currentColor"><path d="M9.55 15.15 18.025 6.675c.2-.2.433-.3.7-.3s.5.1.7.3c.2.2.3.438.3.713 0 .274-.1.512-.3.712L10.25 17.3c-.2.2-.433.3-.7.3-.267 0-.5-.1-.7-.3L4.55 13c-.2-.2-.296-.438-.288-.713.009-.275.113-.512.313-.712s.438-.3.713-.3c.275 0 .512.1.712.3l3.55 3.575Z"/></svg>
  </span>
  Active
</span>

<!-- Input (default + selected) -->
<span class="chip chip--input">jane@scandit.com</span>
<span class="chip chip--input chip--selected">
  jane@scandit.com
  <button class="chip__remove" type="button" aria-label="Remove jane@scandit.com">
    <!-- assets/icons/close-small.svg — exact path copied from the asset file -->
    <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20">
      <path d="M12 13.4L9.08325 16.325C8.89875 16.5083 8.664 16.6 8.379 16.6C8.094 16.6 7.85933 16.5083 7.675 16.325C7.49167 16.1417 7.4 15.9083 7.4 15.625C7.4 15.3417 7.49167 15.1083 7.675 14.925L10.6 12L7.675 9.10825C7.49167 8.92375 7.4 8.689 7.4 8.404C7.4 8.119 7.49167 7.88433 7.675 7.7C7.85833 7.51667 8.09167 7.425 8.375 7.425C8.65833 7.425 8.89167 7.51667 9.075 7.7L12 10.625L14.8917 7.7C15.0762 7.51667 15.311 7.425 15.596 7.425C15.881 7.425 16.1157 7.51667 16.3 7.7C16.5 7.9 16.6 8.1375 16.6 8.4125C16.6 8.6875 16.5 8.91667 16.3 9.1L13.375 12L16.3 14.9167C16.4833 15.1012 16.575 15.336 16.575 15.621C16.575 15.906 16.4833 16.1407 16.3 16.325C16.1 16.525 15.8625 16.625 15.5875 16.625C15.3125 16.625 15.0833 16.525 14.9 16.325L12 13.4Z"/>
    </svg>
  </button>
</span>

<!-- Disabled -->
<span class="chip chip--filter is-disabled" aria-disabled="true">Archived</span>
```

## Chip Group

A thin layout wrapper that arranges chips in a row with consistent gaps. Two flavours match the chip types: **Filter Chips group** (toggleable filter bar) and **Input Chips group** (removable tag list).

### Anatomy

```
┌────────────────────────────────────────────────────────────────────────┐
│ ┌────┐  ┌─────┐  ┌────┐  ┌────┐  ┌────┐                                 │  Filter Chips group
│ │Chip│  │✓Chip│  │Chip│  │Chip│  │Chip│  …                              │  flex row, wrap on overflow
│ └────┘  └─────┘  └────┘  └────┘  └────┘                                 │  gap: 8px (spacing/padding/s)
└────────────────────────────────────────────────────────────────────────┘
```

- **Layout:** `display: flex; flex-wrap: wrap; gap: 8px` (`spacing/padding/s`).
- **No surface or border of its own.** It's a layout wrapper — the visual is entirely the chips inside.
- **Filter Chips group:** the parent decides single-select (only one chip can be selected at a time) vs multi-select (any combination). The Chip atom doesn't know — it just renders the selected state passed by the parent.
- **Input Chips group:** typically renders a list of items the user has entered or picked. The chips are usually all in `selected` state by default (they're displayed because they're "in" the set); the user removes individual ones via their × buttons.

### Code

```tsx
type ChipGroupProps = { children: React.ReactNode };

export function ChipGroup({ children }: ChipGroupProps) {
  return (
    <div role="group" className="flex flex-wrap gap-2">
      {children}
    </div>
  );
}
```

```html
<div role="group" style="display: flex; flex-wrap: wrap; gap: 8px;">
  <span class="chip chip--filter chip--selected" role="checkbox" aria-checked="true">
    <span class="chip__icon">…check…</span>
    Active
  </span>
  <span class="chip chip--filter" role="checkbox" aria-checked="false">Expired</span>
  <span class="chip chip--filter" role="checkbox" aria-checked="false">Pending</span>
</div>
```

## Don'ts

- **Don't use a Chip for a non-interactive status indicator.** Chips are interactive (toggle or remove). For read-only status, use **Badge** — same pill-ish shape, but presentational only and uppercase by spec.
- **Don't render the Selected chip in near-black.** Figma shows `#16191C`, but the Scandit web design system uses brand blue (`color/surface/interactive` = `#1047A1`). design.md is canonical here — same precedent as the Primary Button.
- **Don't put a chip in a tight column or a data table cell.** They need horizontal room to wrap. For inline status in tables, use Badge.
- **Don't make the chip label more than 1-2 words.** Truncate to ellipsis at the container edge. If you need to convey a longer phrase, the chip isn't the right primitive — use a List or a Card.
- **Don't substitute a different icon.** Filter selected uses `check` 20×20. Input selected uses `close_small` 20×20. Other glyphs (×, dot, custom) break the system's "you can recognise the affordance at a glance" contract.
- **Don't fire `onToggle` from the Input chip's surface.** The Input chip is selected by virtue of being displayed — its surface isn't tappable. Only the trailing × fires `onRemove`. (For a tappable Input, you want a Filter chip.)
- **Don't wrap the chip's label onto two lines.** The chip is single-line and 32px tall. If you have more to say, drop down to a List item with a chip as one of its facets.
- **Don't omit `aria-checked` on Filter chips.** Filter is semantically a checkbox-like control — screen readers need the state.
- **Don't omit the descriptive `aria-label` on Input chip's × button.** Just "Remove" is opaque — "Remove jane@scandit.com" makes the destructive target clear before the user fires it.
