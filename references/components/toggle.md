# Toggle

> **TL;DR**
> - A **binary on/off switch** for changes that take effect **immediately** — feature flags, mode toggles, settings rows where the user expects the action to apply on click. For values that commit on form submit (e.g. signup preferences), use [[checkbox]] instead.
> - **Same axis model as [[checkbox]] and [[radio]]**: two orthogonal axes —
>   - An interactive **state** (`default`, `hover`, `pressed`, `disabled`)
>   - A binary **value** (`switchOn: true` / `switchOn: false`)
>   Every visual variant is a (state, switchOn) pair — 4 × 2 = 8 in total.
> - **Track is always 32 × 18 px**, pill (`cornerradius/round` 999px).
> - **The knob changes size between OFF and ON** — Figma-verbatim:
>   - `switchOn: false` → 8 × 8 px brand-blue dot, left-aligned (4px from the left edge)
>   - `switchOn: true` → 14 × 14 px white circle, right-aligned (2px from the right edge)
> - **The OFF knob is brand-blue (`surface/interactive` `#1047A1`) on purpose** — it previews "this is the colour you'd see if you turned it on." It's not just a generic dot.
> - **ON track is `surface/interactive` brand-blue** (`#1047A1`) — same as [[checkbox]] / [[radio]] selected fill. Figma resolves this token correctly to blue here. Per [[feedback-web-uses-blue-not-teal]].
> - **No `focused` state** — keyboard focus follows OS-native `:focus-visible` outline. Same call as [[checkbox]] / [[radio]] / [[menu]] / [[dropdown]].

Figma source:
- [Toggle switch (4 states × 2 switchOn values)](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=10953-20508)

## When to use

| Use Toggle when… | Use something else when… |
|---|---|
| The change applies **immediately** on click (feature flag, dark mode, notification on/off) | The change commits on submit (signup form) → [[checkbox]] |
| The control represents a **binary state** that fits "on/off" / "enabled/disabled" / "active/inactive" semantics | The choice is between named alternatives → [[radio]] (3+ options) or a [[chip]] group |
| You want a **visually prominent** affordance for an instantly-applied setting (the switch's animation reads as "I just did something") | The choice is one item in a long list of comparable booleans → use [[list]] with `checkbox` leading element instead — checkboxes scan better when stacked |
| The setting **doesn't have intermediate states** (no "partial / indeterminate") | Three-state semantics ("yes / no / not set") → [[checkbox]] with an indeterminate value |

## Anatomy

```
switchOn: false          switchOn: true

  ╭────────────────╮       ╭══════════════╮
  │ •              │       │       ◯◯◯    │
  ╰────────────────╯       ╰══════════════╯

  • track: 32 × 18 pill
  • OFF knob: 8 × 8 blue dot, 4px from left
  • ON  knob: 14 × 14 white circle, 2px from right
```

The knob position AND size shift on toggle — not just position. This is intentional: it signals "the value is now committed" (the thumb fills the track more emphatically when active).

## States

### `switchOn: false` (outlined track, small blue knob)

| State | Track surface | Border | Knob | Cursor |
|---|---|---|---|---|
| `default` | `surface/default` `#FFFFFF` | 1px `border/primary` `#525A61` | 8 × 8 `surface/interactive` `#1047A1` (brand-blue dot, left) | `pointer` |
| `hover` | `surface/hover` `#F3F5F8` | 1px `border/primary` (unchanged) | unchanged | `pointer` |
| `pressed` | `surface/pressed` `#E1E7ED` | 1px `border/primary` (unchanged) | unchanged | `pointer` |
| `disabled` | `surface/disabled` `#E1E7ED` | **none** (no border) | 8 × 8 `surface/default` (**white**, blue hint dropped — see notes) | `not-allowed` |

### `switchOn: true` (filled brand-blue track, large white knob)

| State | Track surface | Border | Knob | Cursor |
|---|---|---|---|---|
| `default` | **`surface/interactive` `#1047A1`** (brand blue) | none | 14 × 14 `surface/default` `#FFFFFF` (right) | `pointer` |
| `hover` | `surface/interactive hover` `#1660D9` | none | unchanged | `pointer` |
| `pressed` | `surface/interactive pressed` `#063073` | none | unchanged | `pointer` |
| `disabled` | `surface/disabled` `#E1E7ED` | none | 14 × 14 `surface/default` (white) | `not-allowed` |

Notes:
- **OFF disabled drops the blue hint dot** — the knob becomes white. The disabled state mutes everything to gray-and-white, which makes "this control is locked" read clearly even at a glance. The blue dot returns the moment the toggle is re-enabled.
- **ON disabled and OFF disabled look almost identical** (gray track + white knob) — only the knob *position* (and size) differ to preserve the toggle's current value visually. The surrounding label colour going to `text/disabled` does the heavy lifting of communicating "locked."
- The track has **no border in any ON state** (the brand-blue surface provides the edge). The 1px `border/primary` is OFF-only.

## Toggle row (control + label)

The bare toggle is most commonly wrapped in a clickable row with a text label and (optionally) a short description. The wrapper provides:
- A **larger hit target** (the whole row toggles, not just the 32 × 18 track)
- **Vertical alignment** of the track + label + helper text
- Optional **status text** beside the toggle ("On" / "Off") for accessibility

| Property | Value |
|---|---|
| Layout | `display: flex`, `align-items: center`, `gap: 12px` (`spacing/padding/m`), label on the LEFT, toggle on the RIGHT |
| Cursor | `pointer` (when not disabled), `not-allowed` (when disabled) |
| Label typography | `body/medium` (16/400/24/0.25) · `text/primary` (`#16191C`) |
| Description typography | `body/small` (14/400/20/0.25) · `text/secondary` (`#525A61`) |
| Label colour when disabled | `text/disabled` (`#ACB6BF`) |

Placing the toggle on the **right** matches mobile/iOS conventions and is the most common layout — the label tells you what the setting is; the toggle is the affordance.

## React + Tailwind

```tsx
import { type FC, type InputHTMLAttributes } from 'react';

interface ToggleProps extends Omit<InputHTMLAttributes<HTMLInputElement>, 'type' | 'size'> {
  switchOn: boolean;
  disabled?: boolean;
  label?: string;
  description?: string;
  onToggle?: (next: boolean) => void;
  className?: string;
}

export const Toggle: FC<ToggleProps> = ({
  switchOn,
  disabled = false,
  label,
  description,
  onToggle,
  className,
  ...inputProps
}) => {
  const trackClass = disabled
    ? 'bg-surface-disabled border-0'
    : switchOn
      ? 'bg-surface-interactive border-0 hover:bg-surface-interactive-hover active:bg-surface-interactive-pressed'
      : 'bg-white border border-border-primary hover:bg-surface-hover active:bg-surface-pressed';

  const knobBase = 'absolute rounded-full transition-all duration-150';
  const knobClass = switchOn
    ? `${knobBase} bg-white right-[2px] top-1/2 -translate-y-1/2 size-[14px]`
    : disabled
      ? `${knobBase} bg-white left-[5px] top-[5px] size-2`
      : `${knobBase} bg-surface-interactive left-[4px] top-[4px] size-2`;

  return (
    <label
      className={`flex items-center justify-between gap-3 ${disabled ? 'cursor-not-allowed' : 'cursor-pointer'} ${className ?? ''}`}
    >
      {(label || description) && (
        <div className="flex flex-col">
          {label && <span className={`text-base leading-6 tracking-[0.25px] ${disabled ? 'text-disabled' : 'text-primary'}`}>{label}</span>}
          {description && <span className={`text-sm leading-5 tracking-[0.25px] ${disabled ? 'text-disabled' : 'text-secondary'}`}>{description}</span>}
        </div>
      )}
      <span className={`relative shrink-0 w-8 h-[18px] rounded-full transition-colors ${trackClass}`}>
        <input
          type="checkbox"
          role="switch"
          checked={switchOn}
          disabled={disabled}
          onChange={e => onToggle?.(e.target.checked)}
          className="sr-only"
          {...inputProps}
        />
        <span aria-hidden="true" className={knobClass} />
      </span>
    </label>
  );
};
```

Required Tailwind tokens (in `tailwind.config.js`):

```js
colors: {
  'surface-hover':               '#F3F5F8',
  'surface-pressed':             '#E1E7ED',
  'surface-disabled':            '#E1E7ED',
  'surface-interactive':         '#1047A1',
  'surface-interactive-hover':   '#1660D9',
  'surface-interactive-pressed': '#063073',
  'border-primary':              '#525A61',
  'text-primary':                '#16191C',
  'text-secondary':              '#525A61',
  'text-disabled':               '#ACB6BF',
},
```

## Standalone HTML / CSS

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
    --color-text-primary:                #16191C;
    --color-text-secondary:              #525A61;
    --color-text-disabled:               #ACB6BF;
    --size-cornerradius-round:           999px;
    --spacing-padding-m:                 12px;
  }

  .toggle {
    display: inline-flex;
    align-items: center;
    justify-content: space-between;
    gap: var(--spacing-padding-m);
    cursor: pointer;
    user-select: none;
    font-family: 'Inter', system-ui, sans-serif;
  }
  .toggle--disabled { cursor: not-allowed; }

  .toggle__label {
    font-size: 16px; font-weight: 400; line-height: 24px; letter-spacing: 0.25px;
    color: var(--color-text-primary);
  }
  .toggle__description {
    font-size: 14px; font-weight: 400; line-height: 20px; letter-spacing: 0.25px;
    color: var(--color-text-secondary);
  }
  .toggle--disabled .toggle__label,
  .toggle--disabled .toggle__description { color: var(--color-text-disabled); }

  .toggle__input {
    position: absolute;
    width: 1px; height: 1px;
    padding: 0; margin: -1px;
    overflow: hidden; clip: rect(0, 0, 0, 0);
    white-space: nowrap; border: 0;
  }

  /* Track — OFF default */
  .toggle__track {
    position: relative;
    width: 32px; height: 18px;
    box-sizing: border-box;
    background: var(--color-surface-default);
    border: 1px solid var(--color-border-primary);
    border-radius: var(--size-cornerradius-round);
    flex-shrink: 0;
    transition: background-color 80ms, border-color 80ms;
  }

  /* OFF hover / pressed — track tints, border stays */
  .toggle:not(.toggle--disabled):hover .toggle__track:not(.toggle__track--on),
  .toggle__track:not(.toggle__track--on).is-hover {
    background: var(--color-surface-hover);
  }
  .toggle:not(.toggle--disabled):active .toggle__track:not(.toggle__track--on),
  .toggle__track:not(.toggle__track--on).is-pressed {
    background: var(--color-surface-pressed);
  }

  /* ON — brand-blue track, no border */
  .toggle__track--on {
    background: var(--color-surface-interactive);
    border-color: transparent;
  }
  .toggle:not(.toggle--disabled):hover .toggle__track--on,
  .toggle__track--on.is-hover {
    background: var(--color-surface-interactive-hover);
  }
  .toggle:not(.toggle--disabled):active .toggle__track--on,
  .toggle__track--on.is-pressed {
    background: var(--color-surface-interactive-pressed);
  }

  /* Disabled — both ON and OFF show gray track, no border */
  .toggle__track--disabled {
    background: var(--color-surface-disabled) !important;
    border-color: transparent !important;
  }

  /* Knob — OFF (8×8 brand-blue dot, left) */
  .toggle__knob {
    position: absolute;
    background: var(--color-surface-interactive);
    border-radius: var(--size-cornerradius-round);
    transition: left 150ms, right 150ms, width 150ms, height 150ms, background 80ms;
    width: 8px; height: 8px;
    left: 4px; top: 4px;
    right: auto;
  }

  /* Knob — ON (14×14 white circle, right) */
  .toggle__track--on .toggle__knob {
    width: 14px; height: 14px;
    left: auto;
    right: 2px;
    top: 50%;
    transform: translateY(-50%);
    background: var(--color-surface-default);
  }

  /* Knob — disabled (white, both ON and OFF) */
  .toggle__track--disabled .toggle__knob { background: var(--color-surface-default); }
  .toggle__track--disabled:not(.toggle__track--on) .toggle__knob {
    left: 5px; top: 5px;          /* slightly centered when disabled OFF */
  }
</style>

<!-- ON -->
<label class="toggle">
  <span class="toggle__label">Email notifications</span>
  <span class="toggle__track toggle__track--on">
    <input type="checkbox" role="switch" checked class="toggle__input">
    <span class="toggle__knob" aria-hidden="true"></span>
  </span>
</label>

<!-- OFF -->
<label class="toggle">
  <span class="toggle__label">Daily summary</span>
  <span class="toggle__track">
    <input type="checkbox" role="switch" class="toggle__input">
    <span class="toggle__knob" aria-hidden="true"></span>
  </span>
</label>

<!-- Disabled -->
<label class="toggle toggle--disabled">
  <span class="toggle__label">SMS alerts (requires mobile app)</span>
  <span class="toggle__track toggle__track--disabled">
    <input type="checkbox" role="switch" disabled class="toggle__input">
    <span class="toggle__knob" aria-hidden="true"></span>
  </span>
</label>
```

## Don'ts

- **Don't use Toggle for form fields that submit on save.** A toggle says "I just applied this change." If the change only takes effect on form submit, use [[checkbox]] — the visual idiom matches the commitment model.
- **Don't render Toggle without a label.** A 32×18 track sitting alone has no semantic meaning. Always pair it with a label that says what it controls. Screen readers announce the toggle as "switch, on/off" — but sighted users need the label too.
- **Don't put the toggle on the LEFT of the label.** The conventional layout (matching iOS, Android, GitHub, Slack) is **label-left, toggle-right** — the label tells you what; the toggle is the affordance. Reversing this confuses scanning.
- **Don't recolour the OFF knob.** The 8×8 brand-blue dot is a *preview hint* of the ON colour — it intentionally tells the user "this is what it'll look like." Using `text/secondary` or `text/primary` for the dot drops that affordance.
- **Don't animate the knob with a long duration.** 150ms feels instant; >300ms feels sluggish. The user already knows they clicked; the animation just confirms it.
- **Don't add an `indeterminate` state.** A toggle is strictly binary. If you have three states (yes/no/not-yet-decided), that's a different control — use [[radio]] with three options.
- **Don't use Toggle for destructive actions.** "Delete account" with a toggle is dangerous — the user can tap it accidentally and trigger an irreversible action. Use a [[button]] (which makes the user click+confirm) for any action that can't be cleanly reversed.
- **Don't add a `focused` state with its own background colour.** Keyboard focus follows the OS-native `:focus-visible` outline. Same call as [[checkbox]] / [[radio]] / [[menu]] / [[dropdown]].
