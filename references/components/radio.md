# Radio

> **TL;DR**
> - The Radio Button has **two orthogonal axes** — same model as [[checkbox]]:
>   - An interactive **state** (`default`, `hover`, `pressed`, `disabled`)
>   - A selection **value** (`selected: yes`, `selected: no`)
>   Every visual variant is a (state, selected) pair — 4 × 2 = 8 in total.
> - **Two visual modes** based on the `selected` value:
>   - `selected: no` → **outlined ring** (white surface + 2px `color/border/primary` outline)
>   - `selected: yes` → **filled circle** (interactive blue surface + small white inner dot, no border)
> - The ring is **always 20×20**. The inner dot is **10×10**, centered.
> - **Brand blue (`color/surface/interactive` `#1047A1`) is used for the selected fill, NOT Figma's dark `#16191C`**. This is the same call as [[checkbox]] — sibling controls must look consistent. Per [[feedback-web-uses-blue-not-teal]] (the catch-all rule that the web design system substitutes its catalogued token values whenever they diverge from the Figma library).
> - When **unselected**, the **border colour stays constant** across `default` / `hover` / `pressed` (always `border/primary` `#525A61`). The ring's **inner fill** changes — `surface/default` white → `surface/hover` `#F3F5F8` → `surface/pressed` `#E1E7ED`. When **selected**, the fill drives the state — the blue gets lighter on hover (`surface/interactive hover`), darker on pressed (`surface/interactive pressed`).
> - **No `focused` state** — keyboard focus follows the OS-native `:focus-visible` outline (matches [[menu]] / [[dropdown]] / [[checkbox]]).
> - **No `error` state** — if a radio is in an invalid state (required field, none selected), the error treatment lives on the surrounding **form group** (red label, helper text, group border), not on the radio ring. The radio itself is just a value control.

Figma source:
- [Radio button (8 state × selected combinations)](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=5833-17675)
- [Radio item (control + label)](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=6766-3055)

## When to use

| Use Radio when… | Use something else when… |
|---|---|
| The user must pick **exactly one** of **2–5 mutually exclusive options** | The user picks **0–many** → [[checkbox]] |
| The options need to be **scannable in parallel** (all visible at once) | More than **5 options** → use a [[dropdown]] with a single-select menu |
| The choice is a **persistent value** (form field) | The choice is a **transient action** (e.g. picking a sort order in a popover) — use a [[menu]]'s `radio` variant |
| The choice is settled and **not part of an inline picker** | The radio is **inside a floating menu** — that pattern lives in [[menu]] (`radio` variant), not here |

If you find yourself with more than 5 options, the radio group becomes a wall of circles. Switch to a [[dropdown]] with single-select semantics.

## Anatomy

```
selected: no            selected: yes
                        
   ╭──────╮               ╭──────╮
  │░░░░░░░░│  ← outlined  │██████│  ← filled blue (surface/interactive)
  │░░░░░░░░│    20×20     │██▓▓██│  ← 10×10 white inner dot
  │░░░░░░░░│    2px border│██████│
   ╰──────╯               ╰──────╯
```

- **Ring** is always 20 × 20 px, perfect circle (`cornerradius/round` 999px).
- **Outlined ring** (`selected: no`) carries a 2 px border in `color/border/primary`.
- **Filled ring** (`selected: yes`) has **no border** — the blue surface alone provides the edge.
- The inner dot is 10 × 10 px, centered, `color/icon/on-color` (white).

## Tokens per (state, selected) pair

The full cartesian product. Surface and border change per `(state, selected)`; the inner dot is always `icon/on-color` (white) when `selected: yes` and absent when `selected: no` (except in `disabled` — see notes).

### `selected: no` (outlined ring, no dot)

| State | Surface (ring background) | Border | Notes |
|---|---|---|---|
| `default` | `color/surface/default` (`#FFFFFF`) | 2 px `color/border/primary` (`#525A61`) | |
| `hover` | `color/surface/hover` (`#F3F5F8`) | 2 px `color/border/primary` (unchanged) | The ring's **inner fill** tints to the gray hover tone; the border stays constant. This is how Figma signals interactivity on unselected radios — picked up at the ring itself rather than relying purely on the surrounding row. |
| `pressed` | `color/surface/pressed` (`#E1E7ED`) | 2 px `color/border/primary` (unchanged) | Same pattern — fill darkens to the gray pressed tone; border unchanged. |
| `disabled` | `color/surface/disabled` (`#E1E7ED`) — solid fill, no border | none | The ring becomes a flat gray disc. No dot. |

### `selected: yes` (filled circle, 10×10 white inner dot)

| State | Surface (ring fill) | Inner dot | Notes |
|---|---|---|---|
| `default` | **`color/surface/interactive` (`#1047A1` — brand blue)** ← NOT Figma's dark `#16191C` | `color/icon/on-color` (`#FFFFFF`) | |
| `hover` | `color/surface/interactive hover` (`#1660D9`) | `color/icon/on-color` (white) | The fill brightens to the brand-blue lighter shade. |
| `pressed` | `color/surface/interactive pressed` (`#063073`) | `color/icon/on-color` (white) | The fill darkens to the brand-blue pressed shade. |
| `disabled` | `color/surface/disabled` (`#E1E7ED`) | `color/icon/on-color` (white) | Gray fill, white dot. The dot is the only signal that the radio is still "selected" — surrounding form context should make the disabled state clear. |

## Radio item (control + label)

The radio control is most commonly wrapped in a clickable row with a text label. The wrapper provides:
- **Hover / pressed feedback** for unselected states (since the ring itself doesn't change)
- A **larger hit target** (the whole row is clickable, not just the 20×20 circle)
- **Vertical alignment** of the ring + label

| Property | Value |
|---|---|
| Layout | `display: flex`, `align-items: center`, `gap: 8px` (`spacing/padding/s`) |
| Cursor | `pointer` (when not disabled), `not-allowed` (when disabled) |
| Label typography | `body/medium` (16/400/24/0.25) · `color/text/primary` (`#16191C`) |
| Label colour when disabled | `color/text/disabled` (`#ACB6BF`) |
| Min hit-target height | **24px** — the label height ensures the row covers WCAG SC 2.5.5 even though the ring is only 20px |

For a **radio group** (the typical use case), wrap multiple radio items in a `role="radiogroup"` container with a group label. Use 8px gap between items (`spacing/padding/s`) for tight stacks, 16px for breathing room.

## React + Tailwind

```tsx
import { type FC, type InputHTMLAttributes } from 'react';

type RadioState = 'default' | 'hover' | 'pressed' | 'disabled';

interface RadioProps extends Omit<InputHTMLAttributes<HTMLInputElement>, 'type' | 'size'> {
  selected: boolean;
  disabled?: boolean;
  label?: string;
  className?: string;
}

export const Radio: FC<RadioProps> = ({
  selected,
  disabled = false,
  label,
  className,
  ...inputProps
}) => {
  const ringFill = disabled
    ? 'bg-surface-disabled border-0'
    : selected
      ? 'bg-surface-interactive border-0 hover:bg-surface-interactive-hover active:bg-surface-interactive-pressed'
      : 'bg-white border-2 border-border-primary';

  return (
    <label
      className={`inline-flex items-center gap-2 ${disabled ? 'cursor-not-allowed' : 'cursor-pointer'} ${className ?? ''}`}
    >
      <input
        type="radio"
        checked={selected}
        disabled={disabled}
        className="sr-only peer"
        {...inputProps}
      />
      <span
        aria-hidden="true"
        className={`relative size-5 rounded-full transition-colors ${ringFill}`}
      >
        {selected && (
          <span
            className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 size-[10px] rounded-full bg-on-color"
          />
        )}
      </span>
      {label && (
        <span className={`text-base leading-6 tracking-[0.25px] ${disabled ? 'text-disabled' : 'text-primary'}`}>
          {label}
        </span>
      )}
    </label>
  );
};
```

Required Tailwind tokens (in `tailwind.config.js`):

```js
colors: {
  'surface-disabled':            '#E1E7ED',
  'surface-interactive':         '#1047A1',
  'surface-interactive-hover':   '#1660D9',
  'surface-interactive-pressed': '#063073',
  'border-primary':              '#525A61',
  'text-primary':                '#16191C',
  'text-disabled':               '#ACB6BF',
  'on-color':                    '#FFFFFF',
},
```

## Standalone HTML / CSS

```html
<style>
  :root {
    --color-surface-default:            #FFFFFF;
    --color-surface-hover:              #F3F5F8;
    --color-surface-pressed:            #E1E7ED;
    --color-surface-disabled:           #E1E7ED;
    --color-surface-interactive:        #1047A1;     /* BRAND BLUE, not Figma's dark #16191C */
    --color-surface-interactive-hover:  #1660D9;
    --color-surface-interactive-pressed:#063073;
    --color-border-primary:             #525A61;
    --color-text-primary:               #16191C;
    --color-text-disabled:              #ACB6BF;
    --color-icon-on-color:              #FFFFFF;
    --size-cornerradius-round:          999px;
    --spacing-padding-s:                8px;
  }

  /* ─── Radio item (control + label wrapper) ─── */
  .radio-item {
    display: inline-flex;
    align-items: center;
    gap: var(--spacing-padding-s);
    cursor: pointer;
    user-select: none;
    font-family: 'Inter', system-ui, sans-serif;
  }
  .radio-item--disabled { cursor: not-allowed; }

  .radio-item__label {
    font-size: 16px;
    font-weight: 400;
    line-height: 24px;
    letter-spacing: 0.25px;
    color: var(--color-text-primary);
  }
  .radio-item--disabled .radio-item__label { color: var(--color-text-disabled); }

  /* visually hide the native input but keep it accessible to assistive tech */
  .radio-item__input {
    position: absolute;
    width: 1px; height: 1px;
    padding: 0; margin: -1px;
    overflow: hidden; clip: rect(0, 0, 0, 0);
    white-space: nowrap; border: 0;
  }

  /* ─── Ring ─── */
  .radio {
    position: relative;
    width: 20px; height: 20px;
    box-sizing: border-box;
    background: var(--color-surface-default);
    border: 2px solid var(--color-border-primary);
    border-radius: var(--size-cornerradius-round);
    flex-shrink: 0;
    transition: background-color 80ms;
  }

  /* Selected = filled blue, no border */
  .radio--selected {
    background: var(--color-surface-interactive);
    border-color: var(--color-surface-interactive);
  }
  .radio--selected::after {
    content: '';
    position: absolute;
    top: 50%; left: 50%;
    width: 10px; height: 10px;
    transform: translate(-50%, -50%);
    border-radius: var(--size-cornerradius-round);
    background: var(--color-icon-on-color);
  }

  /* UNSELECTED hover/pressed — inner fill tints, border stays constant. Guarded against disabled. */
  .radio-item:not(.radio-item--disabled):hover .radio:not(.radio--selected),
  .radio:not(.radio--selected).is-hover {
    background: var(--color-surface-hover);
  }
  .radio-item:not(.radio-item--disabled):active .radio:not(.radio--selected),
  .radio:not(.radio--selected).is-pressed {
    background: var(--color-surface-pressed);
  }

  /* SELECTED hover/pressed — fill recolours to brand-blue lighter/darker. */
  .radio-item:not(.radio-item--disabled):hover .radio--selected,
  .radio--selected.is-hover {
    background: var(--color-surface-interactive-hover);
    border-color: var(--color-surface-interactive-hover);
  }
  .radio-item:not(.radio-item--disabled):active .radio--selected,
  .radio--selected.is-pressed {
    background: var(--color-surface-interactive-pressed);
    border-color: var(--color-surface-interactive-pressed);
  }

  /* Disabled — solid gray fill, no border, dot still shows when selected */
  .radio--disabled {
    background: var(--color-surface-disabled);
    border-color: var(--color-surface-disabled);
  }
  .radio--disabled.radio--selected::after {
    background: var(--color-icon-on-color);
  }
</style>

<!-- Selected: yes -->
<label class="radio-item">
  <input type="radio" name="example" class="radio-item__input" checked>
  <span class="radio radio--selected" aria-hidden="true"></span>
  <span class="radio-item__label">Selected option</span>
</label>

<!-- Selected: no -->
<label class="radio-item">
  <input type="radio" name="example" class="radio-item__input">
  <span class="radio" aria-hidden="true"></span>
  <span class="radio-item__label">Unselected option</span>
</label>

<!-- Disabled, selected -->
<label class="radio-item radio-item--disabled">
  <input type="radio" name="example" class="radio-item__input" disabled checked>
  <span class="radio radio--selected radio--disabled" aria-hidden="true"></span>
  <span class="radio-item__label">Disabled, selected</span>
</label>
```

## Don'ts

- **Don't use Figma's dark `#16191C` for the selected fill.** The web design system substitutes brand blue (`color/surface/interactive` `#1047A1`) per the web colour rule — same as [[checkbox]]. Visit [[feedback-web-uses-blue-not-teal]] for the broader pattern.
- **Don't change the border colour of an unselected radio on hover/pressed.** The border stays `border/primary` constant. The interactivity feedback comes from tinting the **inner fill** of the ring (`surface/hover` / `surface/pressed`) — not from recolouring the border. The surrounding label/row may ALSO show its own hover background; the ring's inner fill is a complementary signal at the control itself.
- **Don't use radio buttons for "yes/no" decisions.** Two-option choices read better as a [[toggle]] (switch) or two [[button]]s when the choice triggers an action. Radios shine when the user is *comparing* 3+ options in parallel.
- **Don't omit the `name=` attribute on `<input type="radio">`.** Two radios with the same `name` form a mutually-exclusive group at the platform level (selecting one deselects the other). Without `name`, both can be selected at once and you lose native keyboard navigation between them (arrow keys).
- **Don't render a focused `:focus` ring with a custom colour.** Use `:focus-visible` with the OS-native outline (already provided by browser defaults on the `<input>`). Same call as [[menu]] / [[dropdown]] / [[checkbox]].
- **Don't put more than 5 radios in a group.** Switch to a [[dropdown]] with single-select semantics. A wall of 8 circles is harder to scan than a labelled dropdown.
- **Don't use Roboto.** Figma's `body/medium/font` reads Roboto — placeholder. Web ships Inter. Per [[feedback-figma-font-placeholders]].
- **Don't draw an error state on the ring itself.** If a required radio group has no selection, the error treatment goes on the **group's label** (red text, error helper text below) — not on the radio rings. The radio is just a value control; the validation lives at the group level.
