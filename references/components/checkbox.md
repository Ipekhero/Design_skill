# Checkbox

> **When to use:** Multi-select binary input. Use in forms, filters, and table-row selection where the user picks **zero, one, or several** items from a set. For mutually-exclusive choices (pick exactly one), use **Radio**. For instant-effect on/off toggles, use **Toggle**.
>
> **Figma:** [open in UI Kit](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=10930-19359)

> **Notes:**
>
> - The Checkbox has **two orthogonal axes**: an interactive **state** (`default`, `hover`, `pressed`, `disabled`) and a selection **checked** value (`no`, `yes`, `indeterminate`). Every visual variant is a (state, checked) pair — 4 × 3 = 12 in total. Both axes are documented separately in design.md.
> - **Two visual modes** based on the `checked` value:
>   - `checked: no` → **outlined box** (white surface + 2px `color/border/primary` outline)
>   - `checked: yes` or `indeterminate` → **filled box** (interactive blue surface + white glyph, no border)
> - Use the **indeterminate** state when a parent checkbox controls a group of children and some — but not all — of them are checked (e.g. table "select all" header when half the rows are picked).
> - All tokens align with `design.md` verbatim. No divergences. Brand blue (`color/surface/interactive`) is used for the checked surface per the web colour rule.

## Anatomy

```
  Unchecked (no)               Checked (yes)              Indeterminate
  ┌──────────┐                 ┌──────────┐               ┌──────────┐
  │░░░░░░░░░░│  2px border     │██████████│  filled blue  │██████████│  filled blue
  │░░░░░░░░░░│  border/primary │██  ✓  ██│  white check  │██   ━   ██│  white minus
  │░░░░░░░░░░│  white surface  │██████████│   16×16       │██████████│   16×16
  └──────────┘                 └──────────┘               └──────────┘
   20×20 box                    20×20 box                  20×20 box
   radius:                      radius:                    radius:
   size/cornerRadius/xs (4px)   size/cornerRadius/xs       size/cornerRadius/xs
```

The box is **always 20×20** with 4px corner radius. The inner glyph (check or minus) is **16×16**, centered. Outlined boxes carry a 2px border in `color/border/primary`; filled boxes have no border (the colored surface alone provides the edge).

## Variants

| Variant | Usage |
|---|---|
| `default` | The only variant. No size or style alternatives at this Figma node. |

## Sizes

No size axis — the checkbox is fixed at **20×20**. If you need a larger touch target, wrap the box in a larger clickable label/row; don't scale the box itself.

## States × Checked — the 12-cell matrix

The full cartesian product. Surface and border change per `(state, checked)` pair; the inner glyph's colour changes only between active states and disabled.

### `checked: no` (outlined box, no glyph)

| State | Surface | Border (2px solid) | Glyph |
|---|---|---|---|
| `default` | `color/surface/default` (`#FFFFFF`) | `color/border/primary` (`#525A61`) | — |
| `hover` | `color/surface/hover` (`#F3F5F8`) | `color/border/primary` (unchanged) | — |
| `pressed` | `color/surface/pressed` (`#E1E7ED`) | `color/border/primary` (unchanged) | — |
| `disabled` | `color/surface/disabled` (`#E1E7ED`) | **none** (border removed when disabled) | — |

### `checked: yes` (filled box, 16×16 check glyph)

| State | Surface | Border | Glyph (16×16 `check`) |
|---|---|---|---|
| `default` | `color/surface/interactive` (`#1047A1`) | none | `color/icon/on-color` (`#FFFFFF`) |
| `hover` | `color/surface/interactive hover` (`#1660D9`) | none | `color/icon/on-color` (white) |
| `pressed` | `color/surface/interactive pressed` (`#063073`) | none | `color/icon/on-color` (white) |
| `disabled` | `color/surface/disabled` (`#E1E7ED`) | none | `color/icon/disabled` (`#ACB6BF`) |

### `checked: indeterminate` (filled box, 16×16 minus glyph)

| State | Surface | Border | Glyph (16×16 `minus`) |
|---|---|---|---|
| `default` | `color/surface/interactive` (`#1047A1`) | none | `color/icon/on-color` (`#FFFFFF`) |
| `hover` | `color/surface/interactive hover` (`#1660D9`) | none | `color/icon/on-color` (white) |
| `pressed` | `color/surface/interactive pressed` (`#063073`) | none | `color/icon/on-color` (white) |
| `disabled` | `color/surface/disabled` (`#E1E7ED`) | none | `color/icon/disabled` (`#ACB6BF`) |

## Icon glyphs

The checked and indeterminate variants use approved icons from the catalog at 16×16 (not the standard 24×24 — the smaller `size/icon/s` variant fits the 20×20 box correctly).

- **Checked (yes):** [`check`](../../assets/icons/check.svg)
- **Checked (indeterminate):** [`minus`](../../assets/icons/minus.svg) — the same minus icon used elsewhere for decrement / "remove from set" semantics

## Code

### In-repo (React + Tailwind, scandit-web mapping)

```tsx
import { CheckIcon, MinusIcon } from '@/icons';

type CheckedValue = boolean | 'indeterminate';
type CheckboxProps = {
  checked: CheckedValue;
  onChange: (next: boolean) => void;   // 'indeterminate' resolves to true on click
  disabled?: boolean;
  'aria-label'?: string;
};

export function Checkbox({ checked, onChange, disabled, ...rest }: CheckboxProps) {
  const isFilled = checked === true || checked === 'indeterminate';
  const isIndeterminate = checked === 'indeterminate';

  return (
    <button
      type="button"
      role="checkbox"
      aria-checked={isIndeterminate ? 'mixed' : checked}
      disabled={disabled}
      onClick={() => onChange(!checked || isIndeterminate)}
      className={[
        'size-5 rounded shrink-0',
        'inline-flex items-center justify-center transition-colors',
        'focus:outline-none focus-visible:ring-2 focus-visible:ring-surface-full-primary focus-visible:ring-offset-2',
        // Outlined variant (checked=no) — surface + 2px border
        !isFilled && !disabled && [
          'bg-white border-2 border-ntypo-secondary',
          'hover:bg-configurator-gray-5',
          'active:bg-configurator-gray-10',
        ].join(' '),
        // Filled variant (checked=yes/indeterminate) — interactive surface + white glyph
        isFilled && !disabled && [
          'bg-surface-full-primary border-0 text-white',
          'hover:bg-surface-full-primary-hover',
          'active:bg-surface-full-primary-active',
        ].join(' '),
        // Disabled — both checked-states collapse to the same disabled style
        disabled && (isFilled
          ? 'bg-configurator-gray-10 border-0 text-configurator-gray-30'
          : 'bg-configurator-gray-10 border-0'),
        disabled && 'cursor-not-allowed',
      ].filter(Boolean).join(' ')}
      {...rest}
    >
      {isIndeterminate ? (
        <MinusIcon className="size-4" aria-hidden="true" />
      ) : checked === true ? (
        <CheckIcon className="size-4" aria-hidden="true" />
      ) : null}
    </button>
  );
}
```

### Standalone artifact (prototype)

```html
<style>
  :root {
    --color-surface-default:             #FFFFFF;
    --color-surface-hover:               #F3F5F8;
    --color-surface-pressed:             #E1E7ED;
    --color-surface-disabled:            #E1E7ED;
    --color-surface-interactive:         #1047A1;
    --color-surface-interactive-hover:   #1660D9;
    --color-surface-interactive-pressed: #063073;
    --color-border-primary:              #525A61;
    --color-icon-on-color:               #FFFFFF;
    --color-icon-disabled:               #ACB6BF;
  }

  .checkbox {
    width: 20px; height: 20px; flex-shrink: 0;
    display: inline-flex; align-items: center; justify-content: center;
    border-radius: 4px;                  /* size/cornerRadius/xs */
    padding: 0; cursor: pointer;
    background: var(--color-surface-default);
    border: 2px solid var(--color-border-primary);
    transition: background-color 120ms;
    color: var(--color-icon-on-color);   /* glyph colour (currentColor) */
  }
  .checkbox > svg { width: 16px; height: 16px; }

  /* Outlined (unchecked) hover / pressed */
  .checkbox[aria-checked="false"]:not(:disabled):not(.is-disabled):hover,
  .checkbox[aria-checked="false"].is-hover    { background: var(--color-surface-hover); }
  .checkbox[aria-checked="false"]:not(:disabled):not(.is-disabled):active,
  .checkbox[aria-checked="false"].is-pressed  { background: var(--color-surface-pressed); }

  /* Filled (checked / indeterminate) */
  .checkbox[aria-checked="true"],
  .checkbox[aria-checked="mixed"] {
    background: var(--color-surface-interactive);
    border: 0;
  }
  .checkbox[aria-checked="true"]:not(:disabled):not(.is-disabled):hover,
  .checkbox[aria-checked="true"].is-hover,
  .checkbox[aria-checked="mixed"]:not(:disabled):not(.is-disabled):hover,
  .checkbox[aria-checked="mixed"].is-hover    { background: var(--color-surface-interactive-hover); }
  .checkbox[aria-checked="true"]:not(:disabled):not(.is-disabled):active,
  .checkbox[aria-checked="true"].is-pressed,
  .checkbox[aria-checked="mixed"]:not(:disabled):not(.is-disabled):active,
  .checkbox[aria-checked="mixed"].is-pressed  { background: var(--color-surface-interactive-pressed); }

  /* Disabled — surface flattens; border removed for unchecked too */
  .checkbox:disabled,
  .checkbox.is-disabled {
    background: var(--color-surface-disabled);
    border: 0;
    color: var(--color-icon-disabled);
    cursor: not-allowed;
  }
</style>

<!-- Unchecked -->
<button class="checkbox" type="button" role="checkbox" aria-checked="false" aria-label="Item"></button>

<!-- Checked -->
<button class="checkbox" type="button" role="checkbox" aria-checked="true" aria-label="Item">
  <!-- assets/icons/check.svg -->
  <svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <path d="M9.55 15.15 18.025 6.675c.2-.2.433-.3.7-.3s.5.1.7.3c.2.2.3.438.3.713 0 .274-.1.512-.3.712L10.25 17.3c-.2.2-.433.3-.7.3-.267 0-.5-.1-.7-.3L4.55 13c-.2-.2-.296-.438-.288-.713.009-.275.113-.512.313-.712s.438-.3.713-.3c.275 0 .512.1.712.3l3.55 3.575Z"/>
  </svg>
</button>

<!-- Indeterminate -->
<button class="checkbox" type="button" role="checkbox" aria-checked="mixed" aria-label="Item">
  <!-- assets/icons/minus.svg -->
  <svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <path d="M6 13q-.425 0-.713-.288Q5 12.425 5 12q0-.425.288-.713Q5.575 11 6 11h12q.425 0 .713.288.287.287.287.712 0 .425-.287.713Q18.425 13 18 13H6Z"/>
  </svg>
</button>

<!-- Disabled (any checked state) -->
<button class="checkbox" type="button" role="checkbox" aria-checked="true" disabled aria-label="Item">
  <svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <path d="M9.55 15.15 18.025 6.675c.2-.2.433-.3.7-.3s.5.1.7.3c.2.2.3.438.3.713 0 .274-.1.512-.3.712L10.25 17.3c-.2.2-.433.3-.7.3-.267 0-.5-.1-.7-.3L4.55 13c-.2-.2-.296-.438-.288-.713.009-.275.113-.512.313-.712s.438-.3.713-.3c.275 0 .512.1.712.3l3.55 3.575Z"/>
  </svg>
</button>
```

## Don'ts

- **Don't use a Checkbox for mutually-exclusive choices.** That's what **Radio** is for. Checkboxes communicate "pick any combination, including none" — Radio communicates "pick exactly one".
- **Don't use a Checkbox for instant-effect toggles** like "Notifications on/off" or "Dark mode". Those are **Toggle** affordances — the state change applies immediately. Checkboxes belong in forms where the change applies on submit, or in selection contexts (filters, table rows).
- **Don't scale the box up.** It's fixed at 20×20. If you need a larger hit target, wrap the box in a label / row that's larger and clickable.
- **Don't draw a border on the filled (checked) variant.** The 2px outline is for the outlined (unchecked) state only — the filled state uses its surface colour as the edge.
- **Don't use `indeterminate` as a real value.** It's a **display** state for "some children checked" — the underlying data is still boolean. On click, an indeterminate checkbox should resolve to either `true` or `false` based on the application logic (typically: clicking the parent in indeterminate state checks all children).
- **Don't omit `aria-checked="mixed"`** for the indeterminate state — screen readers need it to communicate the partial-selection meaning. Without it, the checkbox just announces as unchecked.
- **Don't put a Checkbox in a Dialog without a label nearby.** A floating 20×20 box with no context is meaningless — pair it with a label (clickable, ideally wrapping both) so the user knows what they're toggling.
