# Button

> **When to use:** The primary affordance for an action. One **primary** button per view; **secondary** for supporting actions; **ghost** for low-emphasis or icon-only triggers. Reach for the `danger` style on Primary (or Secondary, when documented) only when the action is **irreversible** — delete, remove, revoke, archive.
>
> **Figma:** Primary — [open in UI Kit](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=175-1266) · Secondary — [open in UI Kit](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=184-902) · Ghost — [open in UI Kit](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=364-1297)

> **Notes:**
>
> - **Primary supports two styles** via a `style` prop: `Standard` (brand action) and `Danger` (irreversible action). Standard renders with the brand-blue interactive surface; Danger renders red.
> - Each variant supports an optional leading **icon** (`showIcon`). With-icon variants use **asymmetric horizontal padding** (tighter on the icon side, wider on the label side) so the label remains visually centred against the icon.
> - **Icons must come from `assets/icons/`** following the approved set in [`../icons.md`](../icons.md). For the demo code below, Standard buttons use [`check`](../../assets/icons/check.svg) and Danger buttons use [`delete`](../../assets/icons/delete.svg). Inline the SVG with `fill="currentColor"` so the path inherits the button's text colour (no need for per-state icon colour overrides). If your action's icon isn't in the approved set, source it from Material Symbols Rounded 400 24dp and add it to `assets/icons/`.
> - **Hierarchy rule:** one primary per view. If a layout needs two equally-weighted actions, the cancel/dismiss action is always Ghost or Secondary, never a second Primary.
>
> **Token names** below match the Figma variable names verbatim (`color/surface/interactive`, `label/large`, etc.). Every token is documented in [`../design.md`](../design.md).
>
> **⚠ Figma vs. design.md divergence on primary surface colour:**
> The Figma Primary frame currently renders the Standard style with `color/surface/interactive` set to `#16191C` (near-black). **design.md is canonical here** — primary buttons use `#1047A1` (Scandit brand blue) per [`../design.md`](../design.md) § Colors. Treat the Figma render as out-of-date / experimental until the design team confirms a brand-action recolor. All code examples below use the **blue** values from design.md.

## Variants

| Variant | Usage |
|---|---|
| `primary` | The view's main action. Filled surface, high contrast. One per view. Supports `Standard` (blue) and `Danger` (red) styles. |
| `secondary` | Supporting actions paired with a Primary (e.g. **Cancel** beside **Save**), or stand-alone medium-emphasis triggers. Outlined surface (1px border on white). Supports `Standard` (gray border + dark text) and `Danger` (red border + red text) styles. |
| `ghost` | Low-emphasis or icon-only actions (kebab menus, dismiss buttons, inline row actions, toolbar triggers). No border or fill at rest — surface materialises only on hover and pressed. Supports `Standard` (dark text) and `Danger` (red text) styles. |

## Styles (apply to Primary; possibly extended to others later)

| Style | Usage |
|---|---|
| `standard` | Default brand action. Blue surface. |
| `danger` | Irreversible action (delete, remove). Red surface. Use sparingly — once per view at most. |

## Sizes

Same scale across all variants. Each size has its own height, label type, horizontal padding (with and without icon), gap, icon size, and corner radius.

| Size (`design.md`) | Figma label | Height | Label type | H-padding (no icon) | H-padding (with icon: left / right) | Gap (icon ↔ label) | Icon size | Corner radius |
|---|---|---|---|---|---|---|---|---|
| `md` (default) | "Default" | `size/comp-height/xl` (40px) | `label/large` — 16px Medium, 24px lh, 0.25px ls | `spacing/padding/xl` (24px) both sides | `spacing/padding/l` (16px) left · `spacing/padding/xl` (24px) right | `spacing/padding/s` (8px) | 24×24 | `button/border/radius` (8px, aliased to `size/cornerRadius/m`) |
| `sm` | "S" | `size/comp-height/l` (32px) | `label/medium` — 14px Medium, 20px lh, 0.25px ls | `spacing/padding/m` (12px) both sides | `spacing/padding/s` (8px) left · `spacing/padding/m` (12px) right | `spacing/padding/xs` (4px) | 20×20 (`size/icon/s` — value 20px, key marked "(tbd)" in Figma) | `size/cornerRadius/s` (6px) |

## States

- **default** — Resting state. Filled surface in the variant's primary colour, label in `color/text/inverted` (white).
- **hover** — Surface darkens (or shifts to the hover token of the matching ramp). Cursor: `pointer`.
- **pressed** — Surface deepens further. Triggered on `:active` / pointerdown.
- **disabled** — Surface flattens to `color/surface/disabled` (grey), label to `color/text/disabled`, icon to `color/icon/disabled`. Not focusable; `aria-disabled` on the element.

> **Implementation gotcha:** `:hover` / `:active` selectors are more specific than `[disabled]`. **Guard interactive states with `:not([disabled])`** (or `pointer-events: none` on the disabled style) — otherwise a disabled button still picks up the hover/pressed background when the cursor passes over it. The standalone code blocks below all use `:not([disabled]):not(.is-disabled)` on the hover/active selectors for this reason.

> Figma does not draw `focused` or `loading` states at this node. The current YAML omits both — add them back to design.md when those frames exist in Figma.

## Tokens per style × state — Primary

The load-bearing reference. Each row names the exact Figma variable used. Sizes only affect dimensions (height, padding, radius), not colours — so this matrix is size-agnostic.

### Style: Standard

> Surface uses the design.md blue values for `surface/interactive*`, **not** the Figma render's near-black.

| State | Surface | Label text | Icon | Notes |
|---|---|---|---|---|
| `default` | `color/surface/interactive` (`#1047A1`, design.md canonical) | `color/text/inverted` (`#FFFFFF`) | `color/icon/on-color` (`#FFFFFF`) | |
| `hover` | `color/surface/interactive hover` (`#1660D9`, design.md canonical) | `color/text/inverted` | `color/icon/on-color` | `cursor: pointer` |
| `pressed` | `color/surface/interactive pressed` (`#063073`, design.md canonical) | `color/text/inverted` | `color/icon/on-color` | |
| `disabled` | `color/surface/disabled` (`#E1E7ED`) | `color/text/disabled` (`#ACB6BF`) | `color/icon/disabled` (`#ACB6BF`) | `aria-disabled="true"` |

### Style: Danger

| State | Surface | Label text | Icon | Notes |
|---|---|---|---|---|
| `default` | `color/surface/danger/full` (`#D92121`) | `color/text/inverted` (`#FFFFFF`) | `color/icon/on-color` (`#FFFFFF`) | Reuses the general danger ramp's `full` step. |
| `hover` | `color/surface/button-danger/primary/hover` (`#F24949`) | `color/text/inverted` | `color/icon/on-color` | New button-specific token. |
| `pressed` | `color/surface/button-danger/primary/pressed` (`#AD1111`) | `color/text/inverted` | `color/icon/on-color` | New button-specific token. Same hex as `color/text/on-color/red`. |
| `disabled` | `color/surface/disabled` (`#E1E7ED`) | `color/text/disabled` (`#ACB6BF`) | `color/icon/disabled` (`#ACB6BF`) | Disabled is style-agnostic — same as Standard. |

## Anatomy — Primary (md size, with icon)

```
┌─────────────────────────────────────┐  ← height: size/comp-height/xl (40px)
│ ┌──────┐                            │     radius: button/border/radius (8px)
│ │  ✓   │  Primary                   │     surface: variant + state token
│ └──────┘                            │
└─────────────────────────────────────┘
   ↑     ↑           ↑
   24×24 8px gap     label/large
   icon  (padding/s) text-inverted
   ↑                                      ↑
   pl: 16px (padding/l)                   pr: 24px (padding/xl)
   asymmetric: tighter on icon side
```

## Code — Primary

### In-repo (React + Tailwind, scandit-web mapping)

```tsx
type PrimaryStyle = 'standard' | 'danger';
type ButtonSize = 'md' | 'sm';

type PrimaryButtonProps = React.ButtonHTMLAttributes<HTMLButtonElement> & {
  style?: PrimaryStyle;
  size?: ButtonSize;
  leadingIcon?: React.ReactNode;
};

const STYLES: Record<PrimaryStyle, string> = {
  standard:
    // surface/interactive (#1047A1 — design.md canonical, not Figma's #16191C)
    'bg-surface-full-primary text-white ' +
    'hover:bg-surface-full-primary-hover ' +
    'active:bg-surface-full-primary-active ' +
    'disabled:bg-configurator-gray-10 disabled:text-configurator-gray-30',
  danger:
    'bg-[#D92121] text-white ' +
    'hover:bg-[#F24949] ' +
    'active:bg-[#AD1111] ' +
    'disabled:bg-configurator-gray-10 disabled:text-configurator-gray-30',
};

const SIZES: Record<ButtonSize, { base: string; withIcon: string; noIcon: string }> = {
  md: {
    base: 'h-10 rounded-lg text-base font-medium tracking-[0.25px] leading-6', // 40px, label/large
    withIcon: 'pl-4 pr-6 gap-2',  // 16/24/8
    noIcon: 'px-6',               // 24
  },
  sm: {
    base: 'h-8 rounded-md text-sm font-medium tracking-[0.25px] leading-5',   // 32px, label/medium
    withIcon: 'pl-2 pr-3 gap-1',  // 8/12/4
    noIcon: 'px-3',               // 12
  },
};

export function PrimaryButton({
  style = 'standard',
  size = 'md',
  leadingIcon,
  children,
  ...rest
}: PrimaryButtonProps) {
  const s = SIZES[size];
  return (
    <button
      {...rest}
      className={[
        'inline-flex items-center justify-center transition-colors',
        s.base,
        leadingIcon ? s.withIcon : s.noIcon,
        STYLES[style],
      ].join(' ')}
    >
      {leadingIcon && <span aria-hidden="true" className={size === 'md' ? 'size-6' : 'size-5'}>{leadingIcon}</span>}
      <span>{children}</span>
    </button>
  );
}
```

### Standalone artifact (prototype)

```html
<style>
  :root {
    --color-surface-interactive:                 #1047A1;  /* design.md canonical (NOT Figma's #16191C) */
    --color-surface-interactive-hover:           #1660D9;
    --color-surface-interactive-pressed:         #063073;
    --color-surface-danger-full:                 #D92121;
    --color-surface-button-danger-primary-hover: #F24949;
    --color-surface-button-danger-primary-pressed:#AD1111;
    --color-surface-disabled:                    #E1E7ED;
    --color-text-inverted:                       #FFFFFF;
    --color-text-disabled:                       #ACB6BF;
    --color-icon-on-color:                       #FFFFFF;
    --color-icon-disabled:                       #ACB6BF;
  }

  .btn {
    display: inline-flex; align-items: center; justify-content: center;
    border: 0; cursor: pointer;
    font-family: Inter, system-ui, sans-serif;
    font-weight: 500; letter-spacing: 0.25px;
    color: var(--color-text-inverted);
    transition: background-color 120ms;
  }
  .btn:disabled {
    background: var(--color-surface-disabled) !important;
    color: var(--color-text-disabled);
    cursor: not-allowed;
  }
  .btn:disabled .btn__icon { color: var(--color-icon-disabled); }

  /* Sizes */
  .btn--md { height: 40px; border-radius: 8px; font-size: 16px; line-height: 24px; padding: 0 24px; }
  .btn--md.btn--with-icon { padding: 0 24px 0 16px; gap: 8px; }
  .btn--md .btn__icon { width: 24px; height: 24px; }

  .btn--sm { height: 32px; border-radius: 6px; font-size: 14px; line-height: 20px; padding: 0 12px; }
  .btn--sm.btn--with-icon { padding: 0 12px 0 8px; gap: 4px; }
  .btn--sm .btn__icon { width: 20px; height: 20px; }

  /* Style: Standard (blue per design.md) */
  .btn--primary.btn--standard          { background: var(--color-surface-interactive); }
  .btn--primary.btn--standard:hover    { background: var(--color-surface-interactive-hover); }
  .btn--primary.btn--standard:active   { background: var(--color-surface-interactive-pressed); }

  /* Style: Danger (red) */
  .btn--primary.btn--danger            { background: var(--color-surface-danger-full); }
  .btn--primary.btn--danger:hover      { background: var(--color-surface-button-danger-primary-hover); }
  .btn--primary.btn--danger:active     { background: var(--color-surface-button-danger-primary-pressed); }

  .btn__icon { color: var(--color-icon-on-color); display: inline-grid; place-items: center; }
</style>

<button class="btn btn--md btn--primary btn--standard">Primary</button>
<button class="btn btn--md btn--primary btn--standard btn--with-icon">
  <span class="btn__icon" aria-hidden="true">
    <!-- assets/icons/check.svg — fill="currentColor" inherits button text colour --><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M9.55 15.15 18.025 6.675c.2-.2.433-.3.7-.3s.5.1.7.3c.2.2.3.438.3.713 0 .274-.1.512-.3.712L10.25 17.3c-.2.2-.433.3-.7.3-.267 0-.5-.1-.7-.3L4.55 13c-.2-.2-.296-.438-.288-.713.009-.275.113-.512.313-.712s.438-.3.713-.3c.275 0 .512.1.712.3l3.55 3.575Z"/></svg>
  </span>
  Primary
</button>

<button class="btn btn--md btn--primary btn--danger">Delete</button>
<button class="btn btn--md btn--primary btn--danger btn--with-icon">
  <span class="btn__icon" aria-hidden="true">
    <!-- assets/icons/delete.svg --><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M7 21c-.55 0-1.02-.196-1.413-.588C5.196 20.02 5 19.55 5 19V6c-.283 0-.52-.096-.713-.288C4.096 5.521 4 5.283 4 5c0-.283.096-.521.288-.713C4.479 4.096 4.717 4 5 4h4c0-.283.096-.521.288-.713C9.479 3.096 9.717 3 10 3h4c.283 0 .521.096.713.288.191.191.287.43.287.712h4c.283 0 .521.096.713.288.191.191.287.43.287.712 0 .283-.096.521-.288.713C19.521 5.904 19.283 6 19 6v13c0 .55-.196 1.02-.588 1.413C18.02 20.804 17.55 21 17 21H7Zm10-15H7v13h10V6ZM10 17c.283 0 .521-.096.713-.288.191-.191.287-.43.287-.712V9c0-.283-.096-.521-.288-.713C10.521 8.096 10.283 8 10 8c-.283 0-.521.096-.713.288C9.096 8.479 9 8.717 9 9v7c0 .283.096.521.288.713.191.191.43.287.712.287Zm4 0c.283 0 .521-.096.713-.288.191-.191.287-.43.287-.712V9c0-.283-.096-.521-.288-.713C14.521 8.096 14.283 8 14 8c-.283 0-.521.096-.713.288C13.096 8.479 13 8.717 13 9v7c0 .283.096.521.288.713.191.191.43.287.712.287Z"/></svg>
  </span>
  Delete
</button>

<button class="btn btn--sm btn--primary btn--standard">Primary S</button>
<button class="btn btn--md btn--primary btn--standard" disabled>Primary</button>
```

## Secondary

The outlined sibling of Primary. Same dimensions, padding, label type, and icon sizes as Primary — the difference is the **surface + border** treatment. Secondary uses a transparent / light fill with a 1px border in the variant colour. Pairs cleanly with Primary as the secondary action in a button group.

### Anatomy difference vs. Primary

- **Border:** `button/border/secondary/width` (1px) solid in `color/border/primary` (Standard) or `color/border/danger` (Danger). Border colour does **not** shift with hover / pressed — only the surface does.
- **Surface:** White by default (`color/surface/default`); shifts subtly on hover / pressed using the matching ramp's softer tints.
- **Disabled:** Border is **removed entirely** when disabled. The button collapses to a flat `color/surface/disabled` block with `color/text/disabled` label — same disabled treatment as Primary, so visually they're indistinguishable when disabled. This is intentional.

### Tokens per style × state — Secondary

#### Style: Standard

| State | Surface | Border (1px) | Label text | Icon | Notes |
|---|---|---|---|---|---|
| `default` | `color/surface/default` (`#FFFFFF`) | `color/border/primary` (`#525A61`) | `color/text/primary` (`#16191C`) | `color/icon/primary` (`#16191C`) | |
| `hover` | `color/surface/hover` (`#F3F5F8`) | `color/border/primary` (unchanged) | `color/text/primary` | `color/icon/primary` | `cursor: pointer` |
| `pressed` | `color/surface/pressed` (`#E1E7ED`) | `color/border/primary` (unchanged) | `color/text/primary` | `color/icon/primary` | |
| `disabled` | `color/surface/disabled` (`#E1E7ED`) | **none** (border removed) | `color/text/disabled` (`#ACB6BF`) | `color/icon/disabled` (`#ACB6BF`) | `aria-disabled="true"` |

#### Style: Danger

> Figma defines `color/surface/button-danger/secondary/{default,hover,pressed}` as a separate namespace, but every value reuses existing `surface/*` tokens — no new colour tokens needed. The Figma aliases and the design.md tokens they map to are noted in the Notes column.

| State | Surface | Border (1px) | Label text | Icon | Notes |
|---|---|---|---|---|---|
| `default` | `color/surface/default` (`#FFFFFF`) | `color/border/danger` (`#D92121`) | `color/text/danger` (`#D92121`) | `color/icon/danger` (`#D92121`) | Figma alias: `button-danger/secondary/default` → same as `surface/default`. |
| `hover` | `color/surface/danger/softer` (`#FFE8E8`) | `color/border/danger` (unchanged) | `color/text/danger` | `color/icon/danger` | Figma alias: `button-danger/secondary/hover` → same as `surface/danger/softer`. |
| `pressed` | `color/surface/danger/soft` (`#FFD9D9`) | `color/border/danger` (unchanged) | `color/text/danger` | `color/icon/danger` | Figma alias: `button-danger/secondary/pressed` → same as `surface/danger/soft`. |
| `disabled` | `color/surface/disabled` (`#E1E7ED`) | **none** | `color/text/disabled` | `color/icon/disabled` | Same as Standard disabled — style is collapsed. |

### Anatomy — Secondary (md size, with icon)

```
┌─────────────────────────────────────┐  ← height: size/comp-height/xl (40px)
│ ┌──────┐                            │     radius: button/border/radius (8px)
│ │  ✓   │  Secondary                 │     surface: surface/default (white default)
│ └──────┘                            │     border:  1px solid border/primary
└─────────────────────────────────────┘            (or border/danger for Danger style)
   ↑     ↑           ↑
   24×24 8px gap     label/large
   icon  (padding/s) text/primary (or text/danger)
   ↑                                      ↑
   pl: 16px (padding/l)                   pr: 24px (padding/xl)
   asymmetric: tighter on icon side
```

### Code — Secondary

#### In-repo (React + Tailwind, scandit-web mapping)

```tsx
type SecondaryStyle = 'standard' | 'danger';

type SecondaryButtonProps = React.ButtonHTMLAttributes<HTMLButtonElement> & {
  style?: SecondaryStyle;
  size?: ButtonSize;     // reuse ButtonSize from Primary section
  leadingIcon?: React.ReactNode;
};

const SECONDARY_STYLES: Record<SecondaryStyle, string> = {
  standard:
    'bg-white text-ntypo-primary border border-ntypo-secondary ' +
    'hover:bg-configurator-gray-5 ' +
    'active:bg-configurator-gray-10 ' +
    'disabled:bg-configurator-gray-10 disabled:text-configurator-gray-30 disabled:border-transparent',
  danger:
    'bg-white text-ntypo-danger border border-ntypo-danger ' +
    'hover:bg-surface-softer-error ' +
    'active:bg-surface-soft-error ' +
    'disabled:bg-configurator-gray-10 disabled:text-configurator-gray-30 disabled:border-transparent',
};

export function SecondaryButton({
  style = 'standard',
  size = 'md',
  leadingIcon,
  children,
  ...rest
}: SecondaryButtonProps) {
  const s = SIZES[size];   // SIZES from Primary section above
  return (
    <button
      {...rest}
      className={[
        'inline-flex items-center justify-center transition-colors',
        s.base,
        leadingIcon ? s.withIcon : s.noIcon,
        SECONDARY_STYLES[style],
      ].join(' ')}
    >
      {leadingIcon && <span aria-hidden="true" className={size === 'md' ? 'size-6' : 'size-5'}>{leadingIcon}</span>}
      <span>{children}</span>
    </button>
  );
}
```

#### Standalone artifact (prototype)

```html
<style>
  /* Assumes the Primary :root token block is already declared earlier.
     Add these additional vars if the prototype is Secondary-only. */
  :root {
    --color-surface-default:    #FFFFFF;
    --color-surface-hover:      #F3F5F8;
    --color-surface-pressed:    #E1E7ED;
    --color-surface-danger-soft:   #FFD9D9;
    --color-surface-danger-softer: #FFE8E8;
    --color-border-primary:     #525A61;
    --color-border-danger:      #D92121;
    --color-text-primary:       #16191C;
    --color-text-danger:        #D92121;
    --color-icon-primary:       #16191C;
    --color-icon-danger:        #D92121;
    --button-border-secondary-width: 1px;
  }

  /* Style: Standard (gray border + dark text) */
  .btn--secondary.btn--standard {
    background: var(--color-surface-default);
    color: var(--color-text-primary);
    border: var(--button-border-secondary-width) solid var(--color-border-primary);
  }
  .btn--secondary.btn--standard:hover  { background: var(--color-surface-hover); }
  .btn--secondary.btn--standard:active { background: var(--color-surface-pressed); }

  /* Style: Danger (red border + red text) */
  .btn--secondary.btn--danger {
    background: var(--color-surface-default);
    color: var(--color-text-danger);
    border: var(--button-border-secondary-width) solid var(--color-border-danger);
  }
  .btn--secondary.btn--danger:hover    { background: var(--color-surface-danger-softer); }
  .btn--secondary.btn--danger:active   { background: var(--color-surface-danger-soft); }

  /* Disabled — border removed, surface flattens to disabled gray */
  .btn--secondary:disabled {
    background: var(--color-surface-disabled);
    color: var(--color-text-disabled);
    border-color: transparent;
    cursor: not-allowed;
  }
  .btn--secondary:disabled .btn__icon { color: var(--color-icon-disabled); }

  /* Icon colour follows text colour for Secondary (currentColor on the SVG) */
  .btn--secondary.btn--standard .btn__icon { color: var(--color-icon-primary); }
  .btn--secondary.btn--danger   .btn__icon { color: var(--color-icon-danger); }
</style>

<button class="btn btn--md btn--secondary btn--standard">Cancel</button>
<button class="btn btn--md btn--secondary btn--standard btn--with-icon">
  <span class="btn__icon" aria-hidden="true">
    <!-- assets/icons/check.svg — fill="currentColor" inherits button text colour --><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M9.55 15.15 18.025 6.675c.2-.2.433-.3.7-.3s.5.1.7.3c.2.2.3.438.3.713 0 .274-.1.512-.3.712L10.25 17.3c-.2.2-.433.3-.7.3-.267 0-.5-.1-.7-.3L4.55 13c-.2-.2-.296-.438-.288-.713.009-.275.113-.512.313-.712s.438-.3.713-.3c.275 0 .512.1.712.3l3.55 3.575Z"/></svg>
  </span>
  Confirm
</button>

<button class="btn btn--md btn--secondary btn--danger">Remove</button>
<button class="btn btn--sm btn--secondary btn--standard">Cancel</button>
<button class="btn btn--md btn--secondary btn--standard" disabled>Disabled</button>
```

## Ghost

The least-emphasis button. **No background, no border at rest** — the button reads as text until a hover or pressed state fills it in. Same dimensions as Primary and Secondary, but **tighter horizontal padding** when there's no icon (it has to feel light against page content, not like a hidden button).

### Anatomy difference vs. Secondary

- **No border at any state.** Ghost never gets a 1px outline; the touch target is delimited by padding + on-state surface fill.
- **Default state has no surface fill** (fully transparent). Hover fills the surface to the variant's softer ramp step; pressed darkens one step further. Same hover/pressed surface tokens as Secondary.
- **No-icon horizontal padding is tighter for Standard than for Danger.** Standard gets `spacing/padding/l` (16px), Danger gets `spacing/padding/xl` (24px). This is **intentional** — Danger buttons get more breathing room as a subtle hesitation hint before an irreversible click.
- **Disabled state for Danger is undocumented in Figma.** By convention it collapses to the same disabled treatment as Standard Ghost: transparent surface, label and icon turn `color/text/disabled` / `color/icon/disabled` gray. No red text on disabled.

### Sizes — Ghost-specific padding

Ghost has its own padding tokens for the S size, which alias existing spacing values:

| Token | Value | Aliases to |
|---|---|---|
| `button/padding/ghost/left-icon` | 8px | `spacing/padding/s` (left padding when an icon leads, S size) |
| `button/padding/ghost/h` | 12px | `spacing/padding/m` (horizontal padding both sides when no icon, S size; right padding when icon leads, S size) |

For Default size, Ghost reuses the standard `spacing/padding/{l,xl}` family — see the size table below.

| Size | Height | Label | Icon | Padding (no icon) | Padding (with icon: left / right) | Gap (icon ↔ label) | Corner radius |
|---|---|---|---|---|---|---|---|
| `md` (Default) — Standard | 40px (`size/comp-height/xl`) | `label/large` 16/24/0.25 | 24×24 | `spacing/padding/l` (16px) both sides | `spacing/padding/l` (16px) left · `spacing/padding/xl` (24px) right | `spacing/padding/s` (8px) | `button/border/radius` (8px) |
| `md` (Default) — Danger | 40px | `label/large` | 24×24 | `spacing/padding/xl` (24px) both sides | `spacing/padding/l` (16px) left · `spacing/padding/xl` (24px) right | `spacing/padding/s` (8px) | `button/border/radius` (8px) |
| `sm` (S) | 32px (`size/comp-height/l`) | `label/medium` 14/20/0.25 | 20×20 | `spacing/padding/m` (12px) both sides | `button/padding/ghost/left-icon` (8px) left · `button/padding/ghost/h` (12px) right | `spacing/inline/xs` (4px) | `size/cornerRadius/s` (6px) |

### Tokens per style × state — Ghost

#### Style: Standard

| State | Surface | Label text | Icon | Notes |
|---|---|---|---|---|
| `default` | **transparent** (no fill) | `color/text/primary` (`#16191C`) | `color/icon/primary` (`#16191C`) | Reads as styled text until hovered. |
| `hover` | `color/surface/hover` (`#F3F5F8`) | `color/text/primary` | `color/icon/primary` | Surface materialises; `cursor: pointer`. |
| `pressed` | `color/surface/pressed` (`#E1E7ED`) | `color/text/primary` | `color/icon/primary` | |
| `disabled` | **transparent** (no fill) | `color/text/disabled` (`#ACB6BF`) | `color/icon/disabled` (`#ACB6BF`) | `aria-disabled="true"`. Looks like dimmed plain text. |

#### Style: Danger

> Surface tokens reuse the same `surface/danger/softer` / `surface/danger/soft` values Secondary uses for its Danger hover/pressed states. Figma exposes them under `button-danger/secondary/{hover,pressed}` aliases — no new tokens added.

| State | Surface | Label text | Icon | Notes |
|---|---|---|---|---|
| `default` | **transparent** (no fill) | `color/text/danger` (`#D92121`) | `color/icon/danger` (`#D92121`) | Figma also exposes `button/label/color/ghost/danger` as an alias for the same `#D92121` value — design.md keeps a single source via `color/text/danger`. |
| `hover` | `color/surface/danger/softer` (`#FFE8E8`) | `color/text/danger` | `color/icon/danger` | Figma alias: `button-danger/secondary/hover`. |
| `pressed` | `color/surface/danger/soft` (`#FFD9D9`) | `color/text/danger` | `color/icon/danger` | Figma alias: `button-danger/secondary/pressed`. |
| `disabled` | **transparent** (no fill) | `color/text/disabled` | `color/icon/disabled` | Not drawn in Figma; inherits Standard Ghost's disabled treatment. No red text on disabled. |

### Anatomy — Ghost (md size, Standard, no icon — narrower than Primary/Secondary)

```
┌───────────────────────┐  ← height: size/comp-height/xl (40px)
│       Ghost           │     surface: transparent at rest
└───────────────────────┘     radius:  button/border/radius (8px)
  ↑                   ↑       no border (any state)
  px: 16px (padding/l)
  ↑ Standard only ↑
  Danger uses 24px (padding/xl) for visual hesitation
```

### Code — Ghost

#### In-repo (React + Tailwind, scandit-web mapping)

```tsx
type GhostStyle = 'standard' | 'danger';

type GhostButtonProps = React.ButtonHTMLAttributes<HTMLButtonElement> & {
  style?: GhostStyle;
  size?: ButtonSize;
  leadingIcon?: React.ReactNode;
};

const GHOST_STYLES: Record<GhostStyle, string> = {
  standard:
    'bg-transparent text-ntypo-primary ' +
    'hover:bg-configurator-gray-5 ' +
    'active:bg-configurator-gray-10 ' +
    'disabled:bg-transparent disabled:text-configurator-gray-30',
  danger:
    'bg-transparent text-ntypo-danger ' +
    'hover:bg-surface-softer-error ' +
    'active:bg-surface-soft-error ' +
    'disabled:bg-transparent disabled:text-configurator-gray-30',
};

// Ghost's no-icon padding is style-aware (Standard tighter than Danger).
// With-icon padding matches the Primary/Secondary asymmetric pattern.
const GHOST_PADDING = {
  md: {
    standard: { noIcon: 'px-4',     withIcon: 'pl-4 pr-6 gap-2' },   // 16/-/16+24/8
    danger:   { noIcon: 'px-6',     withIcon: 'pl-4 pr-6 gap-2' },   // 24/-/16+24/8
  },
  sm: {
    standard: { noIcon: 'px-3',     withIcon: 'pl-2 pr-3 gap-1' },   // 12/-/8+12/4
    danger:   { noIcon: 'px-3',     withIcon: 'pl-2 pr-3 gap-1' },   // 12/-/8+12/4  (S size shares Standard padding)
  },
};

export function GhostButton({
  style = 'standard',
  size = 'md',
  leadingIcon,
  children,
  ...rest
}: GhostButtonProps) {
  const s = SIZES[size]; // SIZES.base only — drop SIZES.withIcon/noIcon, we use GHOST_PADDING
  const pad = GHOST_PADDING[size][style];
  return (
    <button
      {...rest}
      className={[
        'inline-flex items-center justify-center transition-colors',
        s.base,
        leadingIcon ? pad.withIcon : pad.noIcon,
        GHOST_STYLES[style],
      ].join(' ')}
    >
      {leadingIcon && <span aria-hidden="true" className={size === 'md' ? 'size-6' : 'size-5'}>{leadingIcon}</span>}
      <span>{children}</span>
    </button>
  );
}
```

#### Standalone artifact (prototype)

```html
<style>
  /* Assumes Primary/Secondary root vars are already in scope.
     Ghost adds no new colour vars — reuses surface/hover, surface/pressed,
     surface/danger/softer, surface/danger/soft, text/danger, etc. */

  /* Style: Standard (dark text, no fill at rest) */
  .btn--ghost.btn--standard {
    background: transparent;
    color: var(--color-text-primary);
    border: 0;
  }
  .btn--ghost.btn--standard:hover  { background: var(--color-surface-hover); }
  .btn--ghost.btn--standard:active { background: var(--color-surface-pressed); }

  /* Style: Danger (red text, no fill at rest) */
  .btn--ghost.btn--danger {
    background: transparent;
    color: var(--color-text-danger);
    border: 0;
  }
  .btn--ghost.btn--danger:hover    { background: var(--color-surface-danger-softer); }
  .btn--ghost.btn--danger:active   { background: var(--color-surface-danger-soft); }

  /* Disabled — transparent surface, dimmed label */
  .btn--ghost:disabled {
    background: transparent;
    color: var(--color-text-disabled);
    cursor: not-allowed;
  }
  .btn--ghost:disabled .btn__icon { color: var(--color-icon-disabled); }

  /* Icon colour follows label colour */
  .btn--ghost.btn--standard .btn__icon { color: var(--color-icon-primary); }
  .btn--ghost.btn--danger   .btn__icon { color: var(--color-icon-danger); }

  /* Ghost-specific no-icon padding — Standard tighter, Danger wider for hesitation */
  .btn--md.btn--ghost.btn--standard:not(.btn--with-icon) { padding: 0 16px; }
  .btn--md.btn--ghost.btn--danger:not(.btn--with-icon)   { padding: 0 24px; }
  .btn--sm.btn--ghost:not(.btn--with-icon)               { padding: 0 12px; }

  /* With-icon padding follows the standard asymmetric pattern across styles */
  .btn--md.btn--ghost.btn--with-icon { padding: 0 24px 0 16px; gap: 8px; }
  .btn--sm.btn--ghost.btn--with-icon { padding: 0 12px 0 8px;  gap: 4px; }
</style>

<button class="btn btn--md btn--ghost btn--standard">Ghost</button>
<button class="btn btn--md btn--ghost btn--standard btn--with-icon">
  <span class="btn__icon" aria-hidden="true">
    <!-- assets/icons/check.svg — fill="currentColor" inherits button text colour --><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M9.55 15.15 18.025 6.675c.2-.2.433-.3.7-.3s.5.1.7.3c.2.2.3.438.3.713 0 .274-.1.512-.3.712L10.25 17.3c-.2.2-.433.3-.7.3-.267 0-.5-.1-.7-.3L4.55 13c-.2-.2-.296-.438-.288-.713.009-.275.113-.512.313-.712s.438-.3.713-.3c.275 0 .512.1.712.3l3.55 3.575Z"/></svg>
  </span>
  Ghost
</button>

<button class="btn btn--md btn--ghost btn--danger">Remove</button>
<button class="btn btn--sm btn--ghost btn--standard">Cancel</button>
<button class="btn btn--md btn--ghost btn--standard" disabled>Disabled</button>
```

## Don'ts

- **Don't put more than one primary button per view.** If two actions feel equally important, the secondary one is **Secondary** or **Ghost**, never a second Primary. Two primaries flatten the hierarchy and force the user to decide.
- **Don't use `danger` for non-destructive actions.** Red triggers a visceral "stop and think" — reserve it for actions you can't undo (delete, remove, revoke, archive). Save/Update/Confirm is **Standard**.
- **Don't apply `surface/interactive` blue to non-interactive surfaces.** It's a *colour with meaning* — clickable action. Filling a stat card or chrome with `surface/interactive` makes that surface look clickable when it isn't.
- **Don't use Figma's `#16191C` near-black as the primary surface.** design.md is canonical here — primary is `#1047A1` (brand blue). If the Figma file shows black, that's a render-side experiment, not the spec.
- **Don't substitute a different corner radius.** `md` = 8px, `sm` = 6px — both come from the corner-radius scale. Inflating to 12px makes buttons look like cards; flattening to 4px makes them look like inputs.
- **Don't omit the disabled `aria-disabled` attribute.** Visual disabling alone isn't accessible. Screen readers need the attribute; keyboard users need the element to be unfocusable (also: don't fire `onClick` while disabled).
- **Don't put a destructive icon (trash, x-circle) on a Standard primary.** Icon and surface must agree on intent. Delete buttons render with the `danger` style + a delete glyph; a trash icon on a blue button reads as a UI bug.
