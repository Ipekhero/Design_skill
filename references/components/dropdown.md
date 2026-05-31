# Dropdown

> **When to use:** Picker for a finite, pre-defined option list. The visible trigger looks like a styled text field with a trailing arrow; tapping the trigger opens a menu below (or above, if there's no room) containing the options. Use over Radio when the list is **>5 items**, and over a search field when the options are **enumerable and short** (≤30 items typically).
>
> **Figma:** [open in UI Kit](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=10940-19946)

> **Notes:**
>
> - **Two layout variants** (Figma "layout" axis):
>   - `vertical` — label on top, dropdown below (standard form layout). Available in both `sm` and `lg` sizes.
>   - `horizontal` — label inline on the left, dropdown to the right. Available in `sm` size only; total width 286px (label 120px + gap 16px + dropdown 150px).
> - **Two sizes:** `lg` (Large, 48px height — available for `vertical` only) and `sm` (Small, 32px height — available for both layouts).
> - **9 states** including 3 error variants (Error / Error Hover / Error Selected). The state model is the same shape as Text Field's form-component state set, reused here for consistency.
> - **Sub-elements:** optional `label` (with optional mandatory `*`), the `Dropdown wrapper` (trigger), optional leading `book` icon (Large vertical only), the input text, trailing arrow (`arrow_triangle_down` closed / `arrow_triangle_up` open), and optional helper text below.
> - **Menu:** opens when `state = selected`, floats below the trigger with `shadow-lg` (directional Elevation/2), white surface, 4px corners, 4px or 8px vertical padding. Menu items are 32px (sm) or 40px (lg) tall, full-width, with `body/medium` text. The currently-selected item gets a **brand-blue softer** surface (`color/surface/brand/softer` `#EFF5FA`) — **not** Figma's teal `list item/selected` `#E7F7F9`, per the web colour rule.
> - **⚠ Token decisions for this component:**
>   - **Form-component surfaces (`color/surface/formcomp/*`)** are inlined here only. They're not added to design.md. Reuse pattern: `formcomp/default` = `surface/default`, `formcomp/error` = `surface/danger/softer`, `formcomp/disabled` = `surface/hover` (`#F3F5F8` — NOT `surface/disabled` `#E1E7ED`), `formcomp/hover` = a translucent `rgba(0,0,0,0.05)` overlay (new, no existing equivalent).
>   - **Helper-text typography** uses Figma `body/xs` (12px / 400 / 16 lh / 0.25 ls). Inlined here; not in design.md typography (closest existing: `label/small` is 12px Medium, `body/small` is 14px Regular — neither matches).
>
> **Token names** below match Figma variable names verbatim. Where chip-style `formcomp/*` aliases are noted, they're informational; the actual code references the existing design.md token they map to.

## Variants

| Variant | Figma label | Layout | Available sizes |
|---|---|---|---|
| `vertical` | Vertical | Label stacked above the dropdown (column flex) | `sm` (200px wide, 32px tall) · `lg` (329px wide, 48px tall) |
| `horizontal` | Horizontal | Label inline left of the dropdown (row flex, items-center) | `sm` only (286px total: 120px label + 16px gap + 150px dropdown) |

## Sizes

| Size | Figma label | Trigger height | Trigger radius | Input text | Trailing arrow | Trailing-arrow button |
|---|---|---|---|---|---|---|
| `sm` | Small | `size/comp-height/l` (32px) | `size/cornerRadius/xs` (4px) | `body/medium` (16px / 400 / 24 lh / 0.25 ls) | `arrow_triangle_down` / `up` 20×20 | 24×24 button, `size/cornerRadius/s` (6px) |
| `lg` | Large | `size/comp-height/2xl` (48px) | `size/cornerRadius/xs` (4px) | `body/medium` | `arrow_triangle_down` / `up` 24×24 | 32×32 button, `button/border/radius` (8px) |

Right padding of the trigger is **`spacing/padding/xs` (4px) for `sm`** and **`spacing/padding/s` (8px) for `lg`** — tighter for sm so the trailing arrow button hugs the right edge. Left padding is always `spacing/padding/m` (12px). When a leading `book` icon is present (lg only), the gap from icon to text is `spacing/padding/m` (12px); without an icon, the gap collapses to 0.

The leading icon is **24×24 button surround / 20×20 glyph**, only documented for `lg vertical` at this Figma node. In `assets/icons/` the canonical example is [`book`](../../assets/icons/book.svg) (sm-icon variant). For a "what library?" dropdown, this is the right glyph; for other dropdowns, swap the leading glyph to whatever fits the field semantics.

## States

| State | Surface | Border | Notes |
|---|---|---|---|
| `default` | `color/surface/formcomp/default` (`#FFFFFF` — = `surface/default`) | 1px `color/border/secondary` (`#C7CFD6`) | Placeholder shown in `color/text/secondary`. |
| `hover` | `color/surface/formcomp/default` + 1px `color/surface/formcomp/hover` overlay (`rgba(0,0,0,0.05)`) | 1px `color/border/secondary` (unchanged) | The hover is a translucent overlay layered over the default surface — `cursor: pointer`. |
| `selected` | `color/surface/formcomp/default` | **2px** `color/border/interactive` (`#16191C` — near-black, matches design.md `border/interactive`) | Menu opens below. Trailing arrow swaps to `arrow_triangle_up`. |
| `filled` | `color/surface/formcomp/default` | 1px `color/border/secondary` | Same as default but text uses `color/text/primary` (`#16191C`) instead of placeholder secondary. |
| `read_only` | `color/surface/formcomp/default` | **no border** | Text in `color/text/primary`. Cursor is the default arrow (not interactive). Trailing arrow shown but greyed. Label in `color/text/secondary`. |
| `disabled` | `color/surface/formcomp/disabled` (`#F3F5F8` — = `surface/hover`) | **no border** | Text + label + icon all in `color/text/disabled` (`#ACB6BF`). `cursor: not-allowed`. |
| `error` | `color/surface/formcomp/error` (`#FFE8E8` — = `surface/danger/softer`) | 1px `color/border/danger` (`#D92121`) | Helper text (below) is rendered in `color/text/danger`. |
| `error_hover` | `color/surface/formcomp/error` + `formcomp/hover` overlay | 1px `color/border/danger` | Same overlay pattern as `hover` but on the error surface. |
| `error_selected` | `color/surface/formcomp/error` | **2px** `color/border/danger` | Menu opens. Same border colour as error states, doubled in width. |

## Label

Position depends on the `layout` variant.

- **Vertical:** label stacked above the trigger, `padding-bottom: spacing/padding/xs` (4px).
- **Horizontal:** label inline left, fixed `width: 120px`, no right padding (the 16px gap between label and trigger is on the parent flex).

| Property | Token | Value |
|---|---|---|
| Text style | `label/medium` | 14px / Medium (500) / 20px lh / 0.25 ls / Inter |
| Colour (default / hover / filled / selected / error states) | `color/text/secondary` | `#525A61` |
| Colour (read_only) | `color/text/secondary` | `#525A61` |
| Colour (disabled) | `color/text/disabled` | `#ACB6BF` |
| Mandatory marker | `*` in `color/text/danger` (`#D92121`), inline after label | size renders ~9px in Figma (visually small superscript-style) |

## Helper text

Optional. Sits below the trigger (Vertical) or after the dropdown wrapper (Horizontal small).

| Property | Token | Value |
|---|---|---|
| Text style | `body/xs` (new — inlined) | 12px / Regular (400) / 16px lh / 0.25 ls / Inter |
| Colour (default / hover / filled states) | `color/text/primary` | `#16191C` |
| Colour (error / error_hover states) | `color/text/danger` | `#D92121` |
| Padding above | `spacing/padding/xs` (4px) | |

## Trigger anatomy (Vertical Large, default state, with leading icon and helper text)

```
  Label  *                                           ← label/medium · text/secondary · 4px bottom padding
  ┌────────────────────────────────────────────────────┐  ← trigger: 329px × 48px
  │  📖  Input                                  ⌄     │     bg: surface/formcomp/default (white)
  └────────────────────────────────────────────────────┘     border: 1px border/secondary (#C7CFD6)
   ↑    ↑                                      ↑            radius: 4px (cornerRadius/xs)
   20×20 body/medium                           32×32        padding: 12px left / 8px right
   book  text/secondary (placeholder)          icon-only    inner: 12px gap (icon ↔ text)
   icon  text/primary (filled)                 button       arrow 24×24
                                                            radius 8px (cornerRadius/m)
  Helper text                                              ← body/xs · text/primary · 4px top padding
```

## Menu (when `selected`)

Floats below the trigger, **full width of the trigger**, with directional shadow. Menu items are 32px tall (sm) or 40px (lg), full-width, hover highlights the row.

| Property | Token | Value |
|---|---|---|
| Surface | `color/surface/default` | `#FFFFFF` |
| Corner radius | `size/cornerRadius/s` | 4px (slightly smaller than the trigger's 4px to keep the menu tight) |
| Padding (top + bottom) | `spacing/padding/xs` (4px) for `sm`, `spacing/padding/s` (8px) for `lg` | |
| Item height | `sm` → 32px (`size/comp-height/l`), `lg` → 40px (`size/comp-height/xl`) | |
| Item padding | `spacing/padding/m` (12px) horizontal · `spacing/padding/s` (8px) gap | |
| Item text | `body/medium` (16px / 400 / 24 lh / 0.25 ls) | colour `color/text/primary` |
| Item — default surface | `list item/default` (= `color/surface/default`, `#FFFFFF`) | |
| Item — selected surface | **`color/surface/brand/softer`** (`#EFF5FA`) ← BLUE per the web rule, **NOT** Figma's teal `list item/selected` (`#E7F7F9`) | |
| Item — hover surface | `color/surface/hover` (`#F3F5F8`) | |
| Menu shadow | `shadow-lg` (now directional per design.md update) — Figma Elevation/2: `0 1px 2px 0 rgba(0,0,0,0.30), 0 2px 6px 2px rgba(0,0,0,0.15)` | |

## Code

### In-repo (React + Tailwind, scandit-web mapping)

```tsx
import { ArrowTriangleDownIcon, ArrowTriangleUpIcon, BookIcon } from '@/icons';

type DropdownProps = {
  layout?: 'vertical' | 'horizontal';
  size?: 'sm' | 'lg';
  state?: 'default' | 'hover' | 'selected' | 'filled' | 'read_only' | 'disabled' | 'error' | 'error_hover' | 'error_selected';
  label?: string;
  mandatory?: boolean;
  helperText?: string;
  placeholder?: string;
  value?: string;
  leadingIcon?: React.ReactNode;
  options: { value: string; label: string }[];
  selectedValue?: string;
  onOpen?: () => void;
  onSelect?: (value: string) => void;
};

// Form-component surface tokens (inlined — not added to design.md catalog)
const SURFACES = {
  default:  'bg-white',
  hover:    'bg-white before:absolute before:inset-[-1px] before:bg-black/[0.05] before:pointer-events-none',
  selected: 'bg-white border-2 border-[#16191C]',     // border/interactive
  filled:   'bg-white',
  read_only:'bg-white border-0',
  disabled: 'bg-configurator-gray-5 border-0',        // surface/hover hex doubles as formcomp/disabled
  error:    'bg-surface-softer-error border-ntypo-danger',
  error_hover:    'bg-surface-softer-error border-ntypo-danger before:absolute before:inset-[-1px] before:bg-black/[0.05]',
  error_selected: 'bg-surface-softer-error border-2 border-ntypo-danger',
};

// ... (full implementation; see chip / button patterns for the structure)
```

### Standalone artifact (prototype)

```html
<style>
  :root {
    /* Form-component surface tokens — inlined; not in design.md catalog */
    --color-surface-formcomp-default:  #FFFFFF;
    --color-surface-formcomp-error:    #FFE8E8;        /* = surface/danger/softer */
    --color-surface-formcomp-disabled: #F3F5F8;        /* = surface/hover (NOT surface/disabled #E1E7ED) */
    --color-surface-formcomp-hover:    rgba(0, 0, 0, 0.05);

    --color-border-secondary:          #C7CFD6;
    --color-border-interactive:        #16191C;        /* matches design.md border/interactive (near-black) */
    --color-border-danger:             #D92121;

    --color-text-primary:              #16191C;
    --color-text-secondary:            #525A61;
    --color-text-disabled:             #ACB6BF;
    --color-text-danger:               #D92121;

    --color-icon-primary:              #16191C;
    --color-icon-secondary:            #6C7680;
    --color-icon-disabled:             #ACB6BF;

    --color-surface-default:           #FFFFFF;
    --color-surface-hover:             #F3F5F8;
    --color-surface-brand-softer:      #EFF5FA;        /* menu selected item — BLUE, NOT teal #E7F7F9 */

    /* shadow-lg (now directional per design.md update) */
    --shadow-popover: 0 1px 2px 0 rgba(0, 0, 0, 0.30), 0 2px 6px 2px rgba(0, 0, 0, 0.15);
  }

  /* Wrapper layout — Vertical (column) or Horizontal (row inline) */
  .dropdown { display: flex; font-family: Inter, system-ui, sans-serif; position: relative; }
  .dropdown--vertical   { flex-direction: column; align-items: flex-start; }
  .dropdown--horizontal { flex-direction: row; align-items: center; gap: 16px; }

  .dropdown--vertical.dropdown--lg { width: 329px; }
  .dropdown--vertical.dropdown--sm { width: 200px; }
  .dropdown--horizontal.dropdown--sm { width: 286px; }

  /* Label */
  .dropdown__label {
    display: inline-flex; align-items: center;
    font-size: 14px; font-weight: 500; line-height: 20px; letter-spacing: 0.25px;
    color: var(--color-text-secondary);
  }
  .dropdown--vertical .dropdown__label { padding-bottom: 4px; }
  .dropdown--horizontal .dropdown__label { width: 120px; }
  .dropdown__mandatory { color: var(--color-text-danger); margin-left: 2px; font-weight: 500; }

  /* Trigger (the dropdown wrapper) */
  .dropdown__trigger {
    display: flex; align-items: center;
    padding: 0 8px 0 12px;
    border: 1px solid var(--color-border-secondary);
    border-radius: 4px;                                     /* size/cornerRadius/xs */
    background: var(--color-surface-formcomp-default);
    cursor: pointer;
    color: var(--color-text-secondary);
    position: relative;
    width: 100%;
  }
  .dropdown--lg .dropdown__trigger { height: 48px; padding-right: 8px; }
  .dropdown--sm .dropdown__trigger { height: 32px; padding-right: 4px; }
  .dropdown--horizontal .dropdown__trigger { width: 150px; }

  /* Inner content */
  .dropdown__content { flex: 1; display: flex; align-items: center; min-width: 0; gap: 12px; padding: 4px 0; }
  .dropdown--sm .dropdown__content { gap: 0; }
  .dropdown__leading-icon { width: 20px; height: 20px; flex-shrink: 0; color: var(--color-icon-primary); }
  .dropdown__input {
    flex: 1; min-width: 0;
    font-size: 16px; font-weight: 400; line-height: 24px; letter-spacing: 0.25px;
    overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
  }
  .dropdown__trigger--filled .dropdown__input,
  .dropdown__trigger--read_only .dropdown__input { color: var(--color-text-primary); }

  /* Trailing arrow icon-only button */
  .dropdown__arrow-btn {
    display: inline-grid; place-items: center;
    background: transparent; border: 0; padding: 0; cursor: pointer;
    color: var(--color-icon-primary);
  }
  .dropdown--lg .dropdown__arrow-btn { width: 32px; height: 32px; border-radius: 8px; }
  .dropdown--sm .dropdown__arrow-btn { width: 24px; height: 24px; border-radius: 6px; }
  .dropdown--lg .dropdown__arrow-btn svg { width: 24px; height: 24px; }
  .dropdown--sm .dropdown__arrow-btn svg { width: 20px; height: 20px; }

  /* State modifiers */
  .dropdown__trigger--hover::after,
  .dropdown__trigger--error_hover::after {
    content: ''; position: absolute; inset: -1px;
    background: var(--color-surface-formcomp-hover);
    pointer-events: none; border-radius: inherit;
  }
  .dropdown__trigger--selected,
  .dropdown__trigger--error_selected {
    border-width: 2px;
  }
  .dropdown__trigger--selected { border-color: var(--color-border-interactive); }
  .dropdown__trigger--error,
  .dropdown__trigger--error_hover,
  .dropdown__trigger--error_selected {
    background: var(--color-surface-formcomp-error);
    border-color: var(--color-border-danger);
  }
  .dropdown__trigger--read_only,
  .dropdown__trigger--disabled { border: 0; cursor: default; }
  .dropdown__trigger--read_only { cursor: default; }
  .dropdown__trigger--disabled {
    background: var(--color-surface-formcomp-disabled);
    cursor: not-allowed;
    color: var(--color-text-disabled);
  }
  .dropdown__trigger--disabled .dropdown__input,
  .dropdown__trigger--disabled .dropdown__arrow-btn,
  .dropdown__trigger--disabled .dropdown__leading-icon { color: var(--color-text-disabled); }

  /* Helper text */
  .dropdown__helper {
    padding-top: 4px;
    font-size: 12px; font-weight: 400; line-height: 16px; letter-spacing: 0.25px;
    color: var(--color-text-primary);
  }
  .dropdown__helper--error { color: var(--color-text-danger); }

  /* Menu */
  .dropdown__menu {
    position: absolute;
    background: var(--color-surface-default);
    border-radius: 4px;
    box-shadow: var(--shadow-popover);
    z-index: 10;
    list-style: none; margin: 0;
    overflow: hidden;
    width: 100%;
  }
  .dropdown--lg .dropdown__menu { padding: 8px 0; }
  .dropdown--sm .dropdown__menu { padding: 4px 0; }

  /* Position the menu below the trigger */
  .dropdown--vertical .dropdown__menu { top: calc(100% + 4px); left: 0; }
  .dropdown--horizontal .dropdown__menu { top: calc(100% + 4px); left: 136px; width: 150px; }

  .dropdown__menu-item {
    display: flex; align-items: center;
    padding: 0 12px;
    font-size: 16px; font-weight: 400; line-height: 24px; letter-spacing: 0.25px;
    color: var(--color-text-primary);
    cursor: pointer;
    background: transparent;
    border: 0; text-align: left; width: 100%;
  }
  .dropdown--lg .dropdown__menu-item { height: 40px; }
  .dropdown--sm .dropdown__menu-item { height: 32px; }
  .dropdown__menu-item:hover { background: var(--color-surface-hover); }
  .dropdown__menu-item--selected {
    background: var(--color-surface-brand-softer);   /* BLUE per web rule — NOT teal #E7F7F9 */
  }
</style>

<!-- Vertical · Large · default -->
<div class="dropdown dropdown--vertical dropdown--lg">
  <label class="dropdown__label" for="dd-1">Library</label>
  <div class="dropdown__trigger dropdown__trigger--default" id="dd-1" tabindex="0">
    <div class="dropdown__content">
      <span class="dropdown__leading-icon" aria-hidden="true">
        <!-- assets/icons/book.svg — exact path -->
        <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20">…book path…</svg>
      </span>
      <span class="dropdown__input">Input</span>
    </div>
    <button class="dropdown__arrow-btn" type="button" aria-label="Open menu">
      <!-- assets/icons/arrow-triangle-down.svg — exact path -->
      <svg viewBox="0 0 24 24" fill="currentColor">…arrow path…</svg>
    </button>
  </div>
</div>

<!-- … other state variants follow the same pattern with state modifier classes … -->
```

> The SVG paths shown above are placeholders. When rendering, **read the exact path from the matching `assets/icons/<name>.svg` file** and inline it byte-for-byte.

## Don'ts

- **Don't use Dropdown for ≤5 options** that are mutually exclusive — use **Radio** instead. Radio shows all options inline so the user doesn't need an extra click to see them.
- **Don't use Dropdown for a long searchable list** (>30 options) — use a search-driven combobox instead. The Dropdown's menu doesn't support filtering.
- **Don't render the selected menu item in teal.** Figma shows `list item/selected: #E7F7F9` (teal); the web design system uses **brand blue softer** (`color/surface/brand/softer` `#EFF5FA`) per the web colour rule.
- **Don't reuse `surface/disabled`** (`#E1E7ED`) for the disabled dropdown surface. Form components use a **lighter** disabled (`#F3F5F8` = `surface/hover`) so they stand out less. This is a form-specific quirk; don't try to "fix" it by aligning to `surface/disabled`.
- **Don't omit the `*` on a mandatory field.** Required-field marker is the smallest red asterisk after the label — without it, the user has to discover the requirement by hitting an error on submit.
- **Don't widen the Horizontal label slot past 120px.** It's a fixed alignment; widening it shifts every horizontal-layout dropdown out of alignment with the rest of the form.
- **Don't change the trigger corner radius.** All form components share `size/cornerRadius/xs` (4px). The Text Field, Search input, and Dropdown wrapper all match.
- **Don't omit the keyboard focus ring.** Figma doesn't draw `focused` explicitly, but WCAG AA requires a visible focus state. Mirror the `selected` border treatment (2px `border/interactive`) when the trigger has keyboard focus.
- **Don't render the Read-only state in `text/disabled`.** Read-only ≠ disabled — read-only text is *intentional final state* (`text/primary`), disabled means *currently unavailable* (`text/disabled` grey). Confusing them tells the user the field is broken when it's actually just frozen.
