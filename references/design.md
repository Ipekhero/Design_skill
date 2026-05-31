---

version: alpha
name: Scandit web
description: >-
  Design system for the Scandit web — a React + TypeScript +
  Tailwind single-page app for technical users managing SDK licenses,
  projects, and analytics. Web-mode tokens from the Scandit UI Kit.
colors:
  # ─────────────────────────────────────────────────────────
  # Primitives — raw foundation palette
  # Semantic tokens below reference these. When adding new
  # semantic tokens, reuse a primitive instead of introducing
  # a new hex.
  # ─────────────────────────────────────────────────────────

  # Gray (true neutral)
  "primitive/gray/50": "#F7F7F7"
  "primitive/gray/100": "#F3F5F8"
  "primitive/gray/200": "#E1E7ED"
  "primitive/gray/300": "#C7CFD6"
  "primitive/gray/400": "#ACB6BF"
  "primitive/gray/500": "#6C7680"
  "primitive/gray/600": "#525A61"
  "primitive/gray/700": "#292E33"
  "primitive/gray/900": "#16191C"

  # Slate (cool, blue-tinted gray — chrome & selected states)
  "primitive/slate/200": "#A3B3C8"
  "primitive/slate/500": "#374E6D"
  "primitive/slate/700": "#25364D"
  "primitive/slate/900": "#141F2E"

  # Blue (brand & info)
  "primitive/blue/50": "#F0F6FA"
  "primitive/blue/100": "#EFF5FA"
  "primitive/blue/200": "#E3E8EE"
  "primitive/blue/300": "#CDDFF1"
  "primitive/blue/400": "#C4CFDD"
  "primitive/blue/500": "#1660D9"
  "primitive/blue/600": "#1047A1"
  "primitive/blue/700": "#065DB8"
  "primitive/blue/800": "#0A3390"
  "primitive/blue/900": "#063073"

  # Sky (lighter info accents)
  "primitive/sky/100": "#ECF3FF"
  "primitive/sky/200": "#D9E7FF"
  "primitive/sky/300": "#B2D0FF"
  "primitive/sky/400": "#3683FF"

  # Green (success)
  "primitive/green/100": "#E6F9EE"
  "primitive/green/200": "#CEF2DC"
  "primitive/green/300": "#A1E5BC"
  "primitive/green/600": "#0D853D"
  "primitive/green/900": "#03401B"

  # Yellow (warning & highlight)
  "primitive/yellow/100": "#FFF8E5"
  "primitive/yellow/200": "#FFF1CC"
  "primitive/yellow/300": "#FFE7A6"
  "primitive/yellow/500": "#FFD300"
  "primitive/yellow/600": "#F0BD30"
  "primitive/yellow/900": "#4D3800"

  # Red (danger)
  "primitive/red/100": "#FFE8E8"
  "primitive/red/200": "#FFD9D9"
  "primitive/red/300": "#FFB8B8"
  "primitive/red/400": "#FF9494"
  "primitive/red/600": "#D92121"
  "primitive/red/900": "#800606"

  # Teal (brand secondary — marketing accent & teal brand outline)
  "primitive/teal/400": "#2EC1CE"
  "primitive/teal/600": "#077F8A"
  "primitive/teal/900": "#055961"

  # Purple (new / beta)
  "primitive/purple/600": "#8E22E0"

  # Pink (interaction emphasis)
  "primitive/pink/600": "#C21D90"

  # Pure
  "primitive/white": "#FFFFFF"
  "primitive/black": "#000000"

  # Alpha primitives — overlays & ambient elevation
  "primitive/black-alpha/10": "#0000001A"
  "primitive/black-alpha/25": "#00000040"
  "primitive/black-alpha/40": "#00000066"
  "primitive/black-alpha/50": "#00000080"
  "primitive/white-alpha/10": "#FFFFFF1A"

  # ─────────────────────────────────────────────────────────
  # Semantic — Figma variable names (verbatim)
  # ─────────────────────────────────────────────────────────

  # Background — page and chrome backgrounds
  "background/primary": "#FFFFFF"
  "background/secondary": "#F7F7F7"
  "background/brand": "#141F2E"
  "background/black": "#000000"
  "background/overlay dark": "#00000040"
  "background/overlay darker": "#00000066"

  # Surface — neutral states
  "surface/default": "#FFFFFF"
  "surface/hover": "#F3F5F8"
  "surface/pressed": "#E1E7ED"
  "surface/selected": "#EFF5FA"
  "surface/selected hover": "#F3F5F8"
  "surface/disabled": "#E1E7ED"

  # Surface — interactive (primary action)
  "surface/interactive": "#1047A1"
  "surface/interactive hover": "#1660D9"
  "surface/interactive pressed": "#063073"

  # Surface — brand ramp (blue)
  "surface/brand/full": "#1047A1"
  "surface/brand/subdued": "#C4CFDD"
  "surface/brand/soft": "#E3E8EE"
  "surface/brand/softer": "#EFF5FA"

  # Surface — info ramp (blue)
  "surface/info/full": "#1660D9"
  "surface/info/subdued": "#B2D0FF"
  "surface/info/soft": "#D9E7FF"
  "surface/info/softer": "#ECF3FF"

  # Surface — success ramp (green)
  "surface/success/full": "#0D853D"
  "surface/success/subdued": "#A1E5BC"
  "surface/success/soft": "#CEF2DC"
  "surface/success/softer": "#E6F9EE"

  # Surface — warning ramp (yellow)
  "surface/warning/full": "#F0BD30"
  "surface/warning/subdued": "#FFE7A6"
  "surface/warning/soft": "#FFF1CC"
  "surface/warning/softer": "#FFF8E5"

  # Surface — danger ramp (red)
  "surface/danger/full": "#D92121"
  "surface/danger/subdued": "#FFB8B8"
  "surface/danger/soft": "#FFD9D9"
  "surface/danger/softer": "#FFE8E8"

  # Surface — neutral ramp (gray)
  "surface/neutral/dark": "#292E33"
  "surface/neutral/full": "#525A61"
  "surface/neutral/subdued": "#C7CFD6"
  "surface/neutral/soft": "#E1E7ED"
  "surface/neutral/softer": "#F3F5F8"

  # Surface — sidebar item (lives on background/brand)
  "surface/sidebar-item/hover": "#FFFFFF1A"
  "surface/sidebar-item/pressed": "#25364D"
  "surface/sidebar-item/selected": "#374E6D"

  # Text
  "text/primary": "#16191C"
  "text/secondary": "#525A61"
  "text/disabled": "#ACB6BF"
  "text/inverted": "#FFFFFF"
  "text/highlight": "#FFD300"
  "text/brand": "#0A3390"
  "text/brand dark": "#055961"
  "text/positive": "#0D853D"
  "text/warning": "#F0BD30"
  "text/danger": "#D92121"
  "text/new": "#8E22E0"
  "text/interaction": "#C21D90"

  # Text — info (link states)
  "text/info/default": "#1660D9"
  "text/info/hover": "#3683FF"
  "text/info/pressed": "#1047A1"

  # Text — on-color (4.5:1 contrast pairs)
  "text/on-color/blue": "#063073"
  "text/on-color/yellow": "#4D3800"
  "text/on-color/green": "#03401B"
  "text/on-color/red": "#800606"

  # Border
  "border/primary": "#525A61"
  "border/secondary": "#C7CFD6"
  "border/tertiary": "#E1E7ED"
  "border/interactive": "#16191C"
  "border/white": "#FFFFFF"
  "border/highlight": "#FFD300"
  "border/selected": "#A3B3C8"
  "border/brand": "#077F8A"
  "border/info": "#1660D9"
  "border/success": "#0D853D"
  "border/warning": "#F0BD30"
  "border/danger": "#D92121"
  "border/danger-light": "#FF9494"
  "border/transparent-25": "#00000040"

  # Border — notification (lighter ramp for Alert outlines)
  "border/notification/neutral": "#C7CFD6"
  "border/notification/info": "#B2D0FF"
  "border/notification/warning": "#FFE7A6"
  "border/notification/success": "#A1E5BC"
  "border/notification/error": "#FFB8B8"

  # Icon
  "icon/primary": "#16191C"
  "icon/secondary": "#6C7680"
  "icon/on-color": "#FFFFFF"
  "icon/disabled": "#ACB6BF"
  "icon/highlight": "#FFD300"
  "icon/brand": "#0A3390"
  "icon/brand dark": "#077F8A"
  "icon/info": "#3683FF"
  "icon/positive": "#0D853D"
  "icon/warning": "#F0BD30"
  "icon/danger": "#D92121"

  # Shadow color stops
  "shadows/light": "#00000040"
  "shadows/strong": "#00000080"


typography:
  heading-xl:
    fontFamily: Inter
    fontSize: 30px
    fontWeight: 600
    lineHeight: 1.2
  heading-lg:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
  heading-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
  heading-sm:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
  body-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
  label-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 500
    letterSpacing: 0.25px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 500
    letterSpacing: 0.25px
  caption-xs:
    fontFamily: Inter
    fontSize: 10px
    fontWeight: 400


spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  sidebar: 300px
  content-max: 1650px
  dialog: 704px
  dialog-xl-width: 749px
  dialog-xl-height: 765px


rounded:
  sm: 4px
  md: 6px
  lg: 8px
  xl: 10px
  2xl: 16px
  full: 9999px


components:
  # Each component enumerates its variants, sizes, and states.
  # Detailed token bindings (backgroundColor, padding, etc.) live
  # in per-component .md files alongside this one.

  accordion:
    variants: [default]
    sizes: [md]
    states: [collapsed, expanded, hover, focused, disabled]

  badge:
    variants: [neutral, info, success, warning, danger, brand, new]
    sizes: [sm, md]
    states: [default]

  branding:
    variants: [logo, wordmark, lockup]
    sizes: [sm, md, lg]
    states: [default, inverted]

  button:
    variants: [primary, secondary, ghost, destructive]
    sizes: [sm, md, lg]
    states: [default, hover, focused, pressed, disabled, loading]

  breadcrumbs:
    variants: [default]
    sizes: [md]
    states: [default, hover, current, truncated]

  callout:
    variants: [info, success, warning, danger, neutral]
    sizes: [md]
    states: [default, dismissible]

  card:
    variants: [default, interactive, elevated, bordered]
    sizes: [sm, md, lg]
    states: [default, hover, pressed, selected, disabled]

  checkbox:
    variants: [default]
    sizes: [sm, md]
    states: [unchecked, checked, indeterminate, hover, focused, disabled, error]

  chip:
    variants: [neutral, filter, choice, action]
    sizes: [sm, md]
    states: [default, hover, focused, selected, disabled, removable]

  dialog:
    variants: [default, alert, confirmation, fullscreen]
    sizes: [md, lg, xl]
    states: [open, closing]

  dropdown:
    variants: [single-select, multi-select, with-search]
    sizes: [sm, md, lg]
    states: [default, hover, focused, open, filled, disabled, error]

  link:
    variants: [default, inline, standalone, external]
    sizes: [sm, md, lg]
    states: [default, hover, focused, pressed, visited, disabled]

  list:
    variants: [default, with-actions, with-icons, interactive]
    sizes: [sm, md, lg]
    states: [default, hover, focused, selected, disabled]

  menu:
    variants: [default, with-icons, with-shortcuts, contextual]
    sizes: [md]
    states: [default, hover, focused, selected, disabled]

  progress:
    variants: [linear, circular]
    sizes: [sm, md, lg]
    states: [indeterminate, determinate, complete, error]

  radio:
    variants: [default]
    sizes: [sm, md]
    states: [unchecked, checked, hover, focused, disabled, error]

  search:
    variants: [default, with-suggestions, with-filters]
    sizes: [sm, md, lg]
    states: [default, hover, focused, filled, disabled]

  sidebar:
    variants: [default, collapsed]
    sizes: [default]
    states: [default, scrolled]

  text-field:
    variants: [default, with-label, with-helper, with-icon, textarea]
    sizes: [sm, md, lg]
    states: [default, hover, focused, filled, error, disabled, read-only]

  toggle:
    variants: [default]
    sizes: [sm, md]
    states: [off, on, hover, focused, disabled]

  tree-view:
    variants: [default, with-icons, with-actions]
    sizes: [md]
    states: [default, hover, focused, selected, expanded, collapsed, disabled]
---

# Design System 

> Source of truth for design tokens, component patterns, and visual language. Conforms to the [DESIGN.md format spec](https://github.com/google-labs-code/design.md).
>
> **Figma UI Kit:** [`UI-Kit`](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit) · **Mode:** Web only · **Tailwind config:** `tailwind.config.js`

---

## Overview

The Scandit SDK Dashboard is a React + TypeScript single-page application styled with Tailwind CSS. The visual language is **clean, minimal, and information-dense** — optimised for technical users managing SDK licenses, projects, and analytics.

The system favours **enterprise trust** over flourish: the checkout flow handles legally-binding orders, so every interaction should feel deliberate and clear. Layouts are dense but never crowded; colour is reserved for state, action, and brand emphasis. Pure black and white are avoided in favour of tinted neutrals.

- **Users:** Scandit customers, product managers, technical-user personas, enterprises — the UI must look credible and enterprise-grade.
- **Brand:** Scandit — brand blue (`#1047A1`), flat / minimal corporate, Inter typeface.
- **Personality:** Bold, fast, actionable. Data-forward, results-oriented.
- **Aesthetic:** Blend of warm / approachable and technical. Generous whitespace, no gradients, no flashy effects.
- **Principles:** Credible at a glance · Density with breathing room · Scandit DNA throughout.
- **Accessibility:** WCAG AA target.

**Voice:** Pragmatic, precise, technical. The UI gets out of the way so engineers can do their work.

---

## Colors

All values below are the canonical Figma `Web` mode tokens. Where the Tailwind config diverges, the Figma value wins — code should be updated to match. Divergences are flagged with **⚠** and listed under [Known divergences](#known-divergences).

The palette is anchored by a deep brand blue (`#1047A1`) for action, a slate chrome (`#141F2E`) for navigation, and a near-black ink (`#16191C`) for body text. Semantic ramps (info, success, warning, danger) each provide four steps — **full → subdued → soft → softer** — for use across alerts, banners, badges, and inline status.

Colors are organised in two layers:

1. **Primitives** — the raw foundation palette (hues × lightness steps). Use these only when defining new semantic tokens.
2. **Semantic** — Figma variable names (`background/…`, `surface/…`, `text/…`, `border/…`, `icon/…`). Use these in components and product UI.

#### Usage rules — match the property to its namespace

Each semantic namespace is scoped to one property. Cross-using namespaces (e.g. applying a `surface/*` value to text, or a `text/*` value to a background) breaks the token contract and will drift from Figma.

| Property | Use only tokens from | Examples |
|---|---|---|
| **Text colour** | `text/*` | Body, headings, labels, links, error messages — `text/primary`, `text/secondary`, `text/info/default`, `text/on-color/blue` |
| **Icon fill / stroke** | `icon/*` | All SVG and icon-font colour — `icon/primary`, `icon/positive`, `icon/on-color` |
| **Surface fill** | `surface/*` | Card / row / chip / button backgrounds — `surface/default`, `surface/interactive`, `surface/success/soft` |
| **Page & chrome background** | `background/*` | Body, sidebar, modal scrim — `background/primary`, `background/brand`, `background/overlay dark` |
| **Border / divider** | `border/*` | Input outlines, card edges, list separators — `border/secondary`, `border/danger`, `border/notification/info` |
| **Shadow colour stop** | `shadows/*` | Box-shadow colour only — `shadows/light`, `shadows/strong` |

A few corollaries:

- A text colour never names a background, and a surface colour never names text — even if the hex happens to match.
- Status colour comes from the matching namespace for the property: a success message uses `text/positive`, a success icon uses `icon/positive`, a success banner uses `surface/success/*`, its border uses `border/success`. Don't reach across namespaces for "the same green."
- `on-color` tokens (`text/on-color/*`, `icon/on-color`) are the only legitimate way to colour text or icons that sit on a filled semantic surface. Pick the one matching the surface's hue.
- Primitives (`primitive/*`) are never used directly in product UI — only when defining a new semantic token.

### Primitives

The foundation palette. Each step is named `primitive/<hue>/<step>`, where `<step>` follows a 50–900 lightness scale (lower = lighter). Steps that aren't currently used in any semantic token are omitted — extend the scale only when you need a new semantic.

> Hex values live in the YAML frontmatter. The tables below document which semantic tokens each primitive backs.

#### Gray (true neutral)

| Token | Used in |
|---|---|
| `primitive/gray/50` | `background/secondary` |
| `primitive/gray/100` | `surface/hover`, `surface/selected hover`, `surface/neutral/softer` |
| `primitive/gray/200` | `surface/pressed`, `surface/disabled`, `surface/neutral/soft`, `border/tertiary` |
| `primitive/gray/300` | `surface/neutral/subdued`, `border/secondary`, `border/notification/neutral` |
| `primitive/gray/400` | `text/disabled`, `icon/disabled` |
| `primitive/gray/500` | `icon/secondary` |
| `primitive/gray/600` | `text/secondary`, `surface/neutral/full`, `border/primary` |
| `primitive/gray/700` | `surface/neutral/dark` |
| `primitive/gray/900` | `text/primary`, `icon/primary`, `border/interactive` |

#### Slate (cool, blue-tinted gray — chrome & selected states)

| Token | Used in |
|---|---|
| `primitive/slate/200` | `border/selected` |
| `primitive/slate/500` | `surface/sidebar-item/selected` |
| `primitive/slate/700` | `surface/sidebar-item/pressed` |
| `primitive/slate/900` | `background/brand` |

#### Blue (brand & info)

| Token | Used in |
|---|---|
| `primitive/blue/50` | Legacy `newblue-lighter` |
| `primitive/blue/100` | `surface/selected`, `surface/brand/softer` |
| `primitive/blue/200` | `surface/brand/soft` |
| `primitive/blue/300` | Legacy `newblue-light` |
| `primitive/blue/400` | `surface/brand/subdued` |
| `primitive/blue/500` | `surface/interactive hover`, `surface/info/full`, `text/info/default`, `border/info` |
| `primitive/blue/600` | `surface/interactive`, `surface/brand/full`, `text/info/pressed` |
| `primitive/blue/700` | Legacy `newblue-dark` |
| `primitive/blue/800` | `text/brand`, `icon/brand` |
| `primitive/blue/900` | `surface/interactive pressed`, `text/on-color/blue` |

#### Sky (lighter info accents)

| Token | Used in |
|---|---|
| `primitive/sky/100` | `surface/info/softer` |
| `primitive/sky/200` | `surface/info/soft` |
| `primitive/sky/300` | `surface/info/subdued`, `border/notification/info` |
| `primitive/sky/400` | `text/info/hover`, `icon/info` |

#### Green (success)

| Token | Used in |
|---|---|
| `primitive/green/100` | `surface/success/softer` |
| `primitive/green/200` | `surface/success/soft` |
| `primitive/green/300` | `surface/success/subdued`, `border/notification/success` |
| `primitive/green/600` | `surface/success/full`, `text/positive`, `icon/positive`, `border/success` |
| `primitive/green/900` | `text/on-color/green` |

#### Yellow (warning & highlight)

| Token | Used in |
|---|---|
| `primitive/yellow/100` | `surface/warning/softer` |
| `primitive/yellow/200` | `surface/warning/soft` |
| `primitive/yellow/300` | `surface/warning/subdued`, `border/notification/warning` |
| `primitive/yellow/500` | `text/highlight`, `icon/highlight`, `border/highlight` |
| `primitive/yellow/600` | `surface/warning/full`, `text/warning`, `icon/warning`, `border/warning` |
| `primitive/yellow/900` | `text/on-color/yellow` |

#### Red (danger)

| Token | Used in |
|---|---|
| `primitive/red/100` | `surface/danger/softer` |
| `primitive/red/200` | `surface/danger/soft` |
| `primitive/red/300` | `surface/danger/subdued`, `border/notification/error` |
| `primitive/red/400` | `border/danger-light` |
| `primitive/red/600` | `surface/danger/full`, `text/danger`, `icon/danger`, `border/danger` |
| `primitive/red/900` | `text/on-color/red` |

#### Teal (brand secondary)

| Token | Used in |
|---|---|
| `primitive/teal/400` | Legacy `teal-scandit` (marketing accent) |
| `primitive/teal/600` | `border/brand`, `icon/brand dark` |
| `primitive/teal/900` | `text/brand dark` |

#### Accents

| Token | Used in |
|---|---|
| `primitive/purple/600` | `text/new` (beta / new labels) |
| `primitive/pink/600` | `text/interaction` (rare emphasis) |

#### Pure & alpha

| Token | Used in |
|---|---|
| `primitive/white` | `background/primary`, `surface/default`, `text/inverted`, `icon/on-color`, `border/white` |
| `primitive/black` | `background/black` |
| `primitive/black-alpha/10` | Reserved |
| `primitive/black-alpha/25` | `background/overlay dark`, `border/transparent-25`, `shadows/light` |
| `primitive/black-alpha/40` | `background/overlay darker` |
| `primitive/black-alpha/50` | `shadows/strong` |
| `primitive/white-alpha/10` | `surface/sidebar-item/hover` |

> **Note:** The primitive set above is **derived from the semantic tokens** currently in the system. If the Figma `Primitives` collection defines a canonical scale (with steps that don't yet map to a semantic), update this section to match Figma — Figma is the source of truth for the primitive layer.

### Background

| Figma token | Tailwind class | Usage |
|---|---|---|
| `background/primary` | `bg-white` | Default page background |
| `background/secondary` | — | Page background variant (cards on cards) |
| `background/brand` | `bg-navbar-bg` | Sidebar / dark chrome |
| `background/black` | `bg-black` | Pure black surfaces |
| `background/overlay dark` | — | Modal scrim (light) |
| `background/overlay darker` | — | Modal scrim (heavy) |

### Surface — neutral states

| Figma token | Tailwind class | Usage |
|---|---|---|
| `surface/default` | `bg-white` | Card / list / form background |
| `surface/hover` | `bg-configurator-gray-5` | Row / chip hover |
| `surface/pressed` | `bg-configurator-gray-10` | Row / chip active |
| `surface/selected` | `bg-surface-soft-brand` | Selected row / chip |
| `surface/selected hover` | `bg-configurator-gray-5` | Hover on selected |
| `surface/disabled` | `bg-configurator-gray-10` | Disabled background |

### Surface — interactive (primary action)

Primary blue button. **`surface/interactive` is the brand colour for actions** (not the slate `background/brand` used in chrome).

| Figma token | Tailwind class | Usage |
|---|---|---|
| `surface/interactive` | `bg-surface-full-primary` | Primary button default |
| `surface/interactive hover` | `bg-surface-full-primary-hover` | Primary button hover |
| `surface/interactive pressed` | `bg-surface-full-primary-active` | Primary button pressed |

### Surface — semantic ramps

Each semantic colour comes with a 4-step ramp: **full** (solid) → **subdued** → **soft** → **softer** (lightest tint).

#### Brand (blue)

| Figma token | Tailwind class |
|---|---|
| `surface/brand/full` | `bg-surface-full-primary` |
| `surface/brand/subdued` | `bg-surface-subdued-brand` |
| `surface/brand/soft` | — |
| `surface/brand/softer` | `bg-surface-soft-brand` |

#### Info (blue)

| Figma token | Tailwind class |
|---|---|
| `surface/info/full` | `bg-surface-full-info` |
| `surface/info/subdued` | `bg-surface-subdued-info` |
| `surface/info/soft` | `bg-surface-soft-info` |
| `surface/info/softer` | — |

#### Success (green)

| Figma token | Tailwind class |
|---|---|
| `surface/success/full` | `bg-surface-full-positive` |
| `surface/success/subdued` | `bg-surface-subdued-positive` |
| `surface/success/soft` | `bg-surface-soft-positive` |
| `surface/success/softer` | — |

#### Warning (yellow)

| Figma token | Tailwind class |
|---|---|
| `surface/warning/full` | `bg-surface-full-warning` |
| `surface/warning/subdued` | `bg-surface-subdued-warning` |
| `surface/warning/soft` | `bg-surface-soft-warning` |
| `surface/warning/softer` | — |

#### Danger (red)

| Figma token | Tailwind class |
|---|---|
| `surface/danger/full` | `bg-surface-full-error` |
| `surface/danger/subdued` | `bg-surface-subdued-error` |
| `surface/danger/soft` | `bg-surface-soft-error` |
| `surface/danger/softer` | — |

#### Neutral (gray)

| Figma token | Tailwind class |
|---|---|
| `surface/neutral/dark` | — |
| `surface/neutral/full` | `bg-ntypo-secondary` |
| `surface/neutral/subdued` | `bg-configurator-gray-20` |
| `surface/neutral/soft` | `bg-configurator-gray-10` |
| `surface/neutral/softer` | `bg-configurator-gray-5` |

### Sidebar item

Lives on the dark `background/brand`.

| Figma token | Tailwind class | State |
|---|---|---|
| (transparent) | — | Default |
| `surface/sidebar-item/hover` | `bg-navbar-hover` | Hover |
| `surface/sidebar-item/pressed` | `bg-navbar-pressed` | Active / pressed |
| `surface/sidebar-item/selected` | `bg-navbar-selected` | Selected |

Item anatomy: `h-12 px-3 mx-3 rounded-lg gap-3` · icon `24×24` · text 16px `tracking-[0.25px]` (body/medium). Selected items use 600 / semibold; all other states use 400 / regular. (Figma node `10221:26594`.)

### Text

| Figma token | Tailwind class | Usage |
|---|---|---|
| `text/primary` | `text-ntypo-primary` ⚠ | Primary body / headings |
| `text/secondary` | `text-ntypo-secondary` | Supporting text, labels |
| `text/disabled` | `text-configurator-gray-30` | Disabled labels |
| `text/inverted` | `text-white` | Text on dark surfaces |
| `text/highlight` | — | AR / highlight emphasis |
| `text/brand` | `text-newblue-darker` | Brand-coloured text (slate blue) |
| `text/brand dark` | — | Teal-on-light emphasis |
| `text/positive` | `text-surface-full-positive` | Success messages |
| `text/warning` | `text-ntypo-warning` | Warning messages |
| `text/danger` | `text-ntypo-danger` | Error messages |
| `text/new` | — | "New" / beta labels |
| `text/interaction` | — | Interaction-state emphasis (rare) |

#### Text — info (link states)

| Figma token | Tailwind class |
|---|---|
| `text/info/default` | `text-ntypo-interactive` |
| `text/info/hover` | `text-ntypo-interactive-hover` |
| `text/info/pressed` | `text-ntypo-interactive-active` |

#### Text on color (4.5:1 contrast pairs)

| Figma token | Use against |
|---|---|
| `text/on-color/blue` | Blue subdued/soft backgrounds |
| `text/on-color/yellow` | Yellow subdued/soft backgrounds |
| `text/on-color/green` | Green subdued/soft backgrounds |
| `text/on-color/red` | Red subdued/soft backgrounds |

### Border

| Figma token | Tailwind class | Usage |
|---|---|---|
| `border/primary` | `border-ntypo-secondary` | Strong dividers / checkboxes |
| `border/secondary` | `border-configurator-gray-20` | Default input / card border |
| `border/tertiary` | `border-configurator-gray-10` | Subtle dividers / list separators |
| `border/interactive` | — | Toggle / button outline |
| `border/white` | `border-white` | Border on dark surfaces |
| `border/highlight` | — | AR highlight |
| `border/selected` | — | Selected card outline |
| `border/brand` | — | Teal brand outline |
| `border/info` | `border-surface-full-info` | Info border |
| `border/success` | `border-surface-full-positive` | Success border |
| `border/warning` | `border-surface-full-warning` | Warning border |
| `border/danger` | `border-surface-full-error` | Error border |
| `border/danger-light` | — | Soft error outline |
| `border/transparent-25` | — | Subtle outline on imagery |

A lighter ramp of border tokens — `border/notification/{neutral,info,warning,success,error}` — exists for `Alert` outlines; values are in the YAML frontmatter.

### Icon

| Figma token | Tailwind class | Usage |
|---|---|---|
| `icon/primary` | `text-ntypo-primary` ⚠ | Primary iconography |
| `icon/secondary` | — | Subtle / trailing icons |
| `icon/on-color` | `text-white` | Icons on filled surfaces |
| `icon/disabled` | `text-configurator-gray-30` | Disabled icons |
| `icon/highlight` | — | AR / highlight |
| `icon/brand` | `text-newblue-darker` | Brand icons |
| `icon/brand dark` | — | Teal brand icons |
| `icon/info` | — | Info icons |
| `icon/positive` | `text-surface-full-positive` | Success icons |
| `icon/warning` | `text-ntypo-warning` | Warning icons |
| `icon/danger` | `text-ntypo-danger` | Error icons |

### Project-specific (legacy) tokens

These Tailwind classes appear in code but do not match the Figma Web tokens. Prefer the Figma equivalents above when adding new work.

| Tailwind class | Hex | Notes |
|---|---|---|
| `teal-scandit` | `#2EC1CE` | Marketing brand accent — used sparingly in trial-related UI |
| `card-border` | `#E0E9F4` | Card outline — closest Figma equivalent is `border/secondary` (#C7CFD6) |
| `newblue-dark` | `#065DB8` | Used for some link copy — Figma equivalent is `text/info/default` (#1660D9) |
| `newblue-light` | `#CDDFF1` | Light blue tint — no exact Figma equivalent |
| `newblue-lighter` | `#F0F6FA` | Lightest blue background — no exact Figma equivalent |

### Known divergences

- **`text/primary` / `icon/primary`**: Figma is `#16191C` (gray/90). Tailwind's `ntypo-primary` resolves to `colors.neutral[90]` = `#1A1A1A`. Visually almost identical but tokens should be aligned — update `tailwind.config.js` to point `ntypo-primary` at `#16191C` when feasible.
- **Pure black/white**: Figma uses tinted neutrals everywhere — avoid `#000` / `#FFF` outside `background/black` and `border/white`.

---

## Typography

> **Figma:** [Typography page](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=63-383)

**Font:** Inter (`font-inter`) — the sole typeface for all dashboard UI. Headlines use the **600/semibold** weight to feel institutional without being heavy; body copy is **400/regular** for sustained readability in dense tabular UIs; interactive labels are **500/medium** with a `0.25px` tracking adjustment to feel decisive without shouting.

### Size scale

| Class | Size | Token | Usage |
|-------|------|-------|-------|
| `text-xxs` | 10px | `caption-xs` | Fine print, badges |
| `text-xs` | 12px | `body-sm` | Legacy — do not use in new work |
| `text-sm` | 14px | `body-md` / `label-md` | Body text, form labels, subtitles |
| `text-base` | 16px | `body-lg` / `label-lg` | Default body, primary button label |
| `text-lg` | 18px | `heading-sm` | Card titles, banner headlines |
| `text-xl` | 20px | `heading-md` | Section headings |
| `text-2xl` | 24px | `heading-lg` | Page sub-headings |
| `text-3xl` | 30px | `heading-xl` | Page headings |

### Named type styles

Canonical pairings to use across components. Apply both size and weight together — do not mix.

| Style | Tailwind classes | px / weight | Figma token | Usage |
|---|---|---|---|---|
| **heading-card** | `text-lg font-semibold` | 18px / 600 | `heading/small` | Card titles, banner headlines |
| **body-card** | `text-sm font-normal text-typo-secondary` | 14px / 400 | `body/small` | Card subtitles, banner sublines |
| **label-button** | `text-base font-medium` | 16px / 500 | `label/xl` | Primary button labels |
| **label-medium** | `text-sm font-medium tracking-[0.25px]` | 14px / 500 | `label/medium` | Ghost button labels, secondary actions |

---

## Layout

> **Figma:** [Size and Spacing page](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=57-2)

The dashboard uses a **fixed left sidebar (300px) + fluid main content (max 1650px)** model. Spacing follows the Tailwind 4px scale; the named tokens in the frontmatter (`xs` 4 → `2xl` 48) cover the canonical steps. Cards have generous internal padding (`24px` default) to keep dense tables breathable.

### Layout tokens

| Token | Value | Usage |
|-------|-------|-------|
| `w-sidebar-width` / `ml-sidebar-width` | `300px` | Fixed nav sidebar |
| `max-w-siteContent` | `1650px` | Main content max-width |
| `w-dialog` / `h-dialog` | `704px` | Standard modal size |
| `w-dialogXl` / `h-dialogXl` | `749px / 765px` | Large modal |
| `z-popover` | `70` | Popover z-index |

### Breakpoints

| Name | Min-width | Notes |
|------|-----------|-------|
| `sm` | `640px` | Mobile landscape |
| `md` | `768px` | Tablet |
| `lg` | `1024px` | Sidebar becomes fixed |
| `xl` | `1280px` | Desktop |
| `2xl` | `1440px` | Wide desktop |

---

## Elevation & Depth

> **Figma:** [Elevation page](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=10-2)

Elevation is **subtle and ambient**, never directional. All shadows are pure-vertical (offset 0, varying blur) at low opacity (`rgba(27,32,38,0.08)`) so cards lift off the page without casting harsh edges. Modals and popovers use heavier scrims (`rgba(0,0,0,0.25)`–`0.40`) defined under [Background](#background).

| Class | Value | Usage |
|-------|-------|-------|
| `shadow` | `0 0 4px 0 rgba(27,32,38,0.08)` | Resting card lift |
| `shadow-md` | `0 0 8px 0 rgba(27,32,38,0.08)` | Hovered card, sticky header |
| `shadow-lg` | `0 0 16px 0 rgba(27,32,38,0.08)` | Popover, dropdown |
| `shadow-xl` | `0 0 32px 0 rgba(27,32,38,0.08)` | Modal dialog |

Shadow colour stops (Figma): `shadows/light` `rgba(0,0,0,0.25)` · `shadows/strong` `rgba(0,0,0,0.5)`.

---

## Shapes

Corner radii are **measured and modest** — sharp enough to feel engineered, soft enough to feel current. Buttons and sidebar items use `8px` (`rounded-lg`); inputs use a tighter `4px`; cards step up to `16px` for a clear container hierarchy; chips are fully pill-shaped.

| Class | Value | Usage |
|-------|-------|-------|
| `rounded` | `4px` | Input fields |
| `rounded-6` | `6px` | Small surface accents |
| `rounded-lg` | `8px` | Buttons, sidebar items |
| `rounded-10` | `10px` | Medium containers |
| `rounded-2xl` | `16px` | Cards |
| `rounded-full` | `9999px` | Chips, avatars |

---

## Components

High-level overview of every component in the system. Each entry links to its Figma page; detailed token bindings (variant × size × state) live in the per-component `.md` files alongside this document, and variant/size/state enumerations are in the YAML `components:` block above.

| Component | When to use | Figma |
|---|---|---|
| **Accordion** | Disclose sections of content one at a time to reduce vertical density. | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=2934-5760) |
| **Badge** | Tag a status or count next to a label (e.g. "New", "3 issues"). | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=4832-11808) |
| **Branding** | Place the Scandit identity in the chrome and on auth / marketing surfaces. | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=2934-5540) |
| **Button** | The primary affordance for an action. One primary button per view; ghost for secondary navigation. | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=2803-4942) |
| **Breadcrumbs** | Show the user's location in a multi-level page hierarchy. | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=2934-6290) |
| **Callout** | Inline status message tied to a section (info, success, warning, danger). | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=7031-931) |
| **Card** | Group related content into a contained surface — the dashboard's main composition unit. | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=2803-4467) |
| **Checkbox** | Multi-select binary input. Use in forms, filters, and table-row selection. | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=4788-86) |
| **Chip** | Compact tag for features, filters, or selectable options on cards. | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=4397-3636) |
| **Dialog** | Modal interruption requiring confirmation, input, or critical info. Use only when blocking is justified. | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=2934-5695) |
| **Dropdown** | Single- or multi-select picker for a finite, pre-defined option list. | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=2934-5921) |
| **Link** | Inline navigation to another page or external resource. Distinct from buttons. | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=2934-5429) |
| **List** | Ordered enumeration of items with optional leading / trailing affordances. | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=3152-150) |
| **Menu** | Floating action list triggered by a control (kebab, "more", contextual right-click). | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=5992-5045) |
| **Progress** | Communicate loading, completion percentage, or a long-running task. | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=4995-7653) |
| **Radio** | Single-select from 2–5 mutually exclusive options. Prefer Dropdown beyond that. | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=4788-85) |
| **Search** | Input field for querying a dataset. Pair with suggestions or filters where relevant. | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=4052-3806) |
| **Sidebar** | Primary left-rail navigation on `background/brand`. Fixed at `lg` and above. | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=2934-5545) |
| **Text Field** | Free-text input for forms. Default to single-line; use textarea variant for multi-line. | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=5294-1106) |
| **Toggle** | Immediate on/off binary control. Use when the change takes effect instantly, not for forms. | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=2934-5542) |
| **Tree view** | Hierarchical navigation through nested data (folders, org structures, scan-result trees). | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=6639-1940) |

---

## Do's and Don'ts

- **Do** trace every colour and spacing value back to a token. No `[#hex]` arbitrary values in new code.
- **Do** use semantic tokens (`surface-*`, `ntypo-*`) rather than raw palette values.
- **Do** keep shared UI in `src/components/`; page-specific UI in `src/app-components/`.
- **Do** use `surface/interactive` (`#1047A1`) for primary actions — reserve `background/brand` (`#141F2E`) for chrome.
- **Do** apply size and weight together from a named type style — don't mix.
- **Do** match the token namespace to the property: text uses `text/*`, icons use `icon/*`, surfaces use `surface/*`, borders use `border/*`, page chrome uses `background/*`, shadows use `shadows/*`.
- **Do** colour text or icons on filled semantic surfaces with the matching `on-color` token (`text/on-color/blue`, `icon/on-color`).
- **Don't** cross namespaces — never colour text with a `surface/*` value or fill a background with a `text/*` value, even if the hex matches.
- **Don't** use a primitive (`primitive/*`) directly in product UI. Primitives only define semantic tokens.
- **Don't** reach across namespaces for "the same green" — a success message is `text/positive`, a success banner is `surface/success/*`, its border is `border/success`.
- **Don't** reference iOS/Android platform tokens. Web mode only.
- **Don't** use pure `#000` / `#FFF` outside `background/black` and `border/white` — prefer tinted neutrals.
- **Don't** use `text-xs` (12px) in new work — it's legacy.
- **Don't** duplicate components — extend or wrap the shared atom.
- **Don't** introduce directional shadows — elevation is pure-vertical at low opacity.

---

## Motion

> **Figma:** [Motion page](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=8398-6551)

Motion is **functional, not decorative**. Entrances fade in with a short translate; state transitions use `transition-colors` only. No bounce, no overshoot.

| Class | Value |
|-------|-------|
| `animate-fadeIn` | `fadeIn 0.3s ease-out` — opacity + translateY(12px→0) |
| `animate-fadeSlideIn` | `fadeSlideIn 350ms ease-out` — opacity + translateY(8px→0) |

---

## Figma UI Kit — Page Index

Every page in the [UI Kit](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit) is linked below.

**Foundations**

| Page | Figma |
|------|-------|
| Icons | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=136-70) |
| Colors | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=5-2) |
| Size and Spacing | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=57-2) |
| Typography | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=63-383) |
| Elevation | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=10-2) |
| Motion | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=8398-6551) |

**Components**

| Page | YAML key | Figma |
|------|----------|-------|
| Accordion | `accordion` | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=2934-5760) |
| Badge | `badge` | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=4832-11808) |
| Branding | `branding` | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=2934-5540) |
| Buttons | `button` | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=2803-4942) |
| Breadcrumbs | `breadcrumbs` | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=2934-6290) |
| Callout | `callout` | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=7031-931) |
| Cards | `card` | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=2803-4467) |
| Checkbox | `checkbox` | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=4788-86) |
| Chips | `chip` | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=4397-3636) |
| Dialogs | `dialog` | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=2934-5695) |
| Dropdown | `dropdown` | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=2934-5921) |
| Link | `link` | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=2934-5429) |
| Lists | `list` | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=3152-150) |
| Menu | `menu` | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=5992-5045) |
| Progress | `progress` | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=4995-7653) |
| Radio Button | `radio` | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=4788-85) |
| Search | `search` | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=4052-3806) |
| Sidebar | `sidebar` | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=2934-5545) |
| Text Fields | `text-field` | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=5294-1106) |
| Toggle Switch | `toggle` | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=2934-5542) |
| Tree View | `tree-view` | [open](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=6639-1940) |
