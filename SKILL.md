---
name: scandit-design
description: Scandit's UI Kit translated into tokens, rules, components, and icon assets — the source of truth Scandit engineers and PMs use to make prototypes look like real Scandit products. Trigger this skill whenever the user asks to build, design, generate, mock up, draft, or prototype any UI, component, page, dashboard, form, button, layout, table, modal, or visual element — even if Scandit is not explicitly named. Also trigger when the user mentions design tokens, the UI kit, Scandit brand styling, "make it look like Scandit", or when reviewing existing UI code for design-system compliance. The whole point is that prototypes across different Scandit products stay visually consistent with the production dashboard — credible, dense, and on-brand instead of looking like a generic admin template. Prefer this over generic Tailwind/Material defaults.
---

# Scandit design system

This skill is the Scandit UI Kit translated into a form Claude can use directly: design tokens, usage rules, component patterns, and 61 SVG icon assets. The intent is **prototype consistency** — when a PM mocks up a feature or an engineer scaffolds a demo, the result should sit naturally next to the production Scandit dashboard, not feel like a different product.

The visual language is **clean, minimal, information-dense, and enterprise-credible**: tinted neutrals replace pure black/white, color is reserved for state and action, typography is Inter with deliberate weights. The production reference is the React + TypeScript + Tailwind dashboard, but this skill works for any stack — standalone HTML artifacts, React components, Vue prototypes, Figma exports.

Full system lives in [`references/design.md`](references/design.md) — colors, typography, layout, elevation, shapes, components, motion. Icon catalog in [`references/icons.md`](references/icons.md) with SVGs in [`assets/icons/`](assets/icons/). Use the cheat sheet below for the 80% case; load the references when you need the long tail.

## Working modes

Most invocations are **build mode** — generating a prototype, mockup, or new component. The other two modes exist but are secondary:

- **Build** (primary) — the user wants new UI: a prototype, a page mockup, a component, a quick demo. Generate code that uses Scandit tokens, the approved icon set, and the canonical type styles from the start. Don't write generic defaults and then "convert."
- **Audit** — the user wants you to review existing UI code against the system. Follow the audit checklist; surface findings with file:line references. Don't edit unless explicitly asked.
- **Discuss** — the user is asking how the system handles something (e.g. "which surface token for a hovered selected row?"). Answer from the reference; quote token names verbatim.

If the mode isn't obvious, infer from context (empty file or "build me…" → build; existing file under review → audit; question phrasing → discuss) and state your assumption in one line so the user can redirect.

## Two ways to consume the tokens

The system is described twice in [`references/design.md`](references/design.md): once as **Figma semantic token names** (`surface/default`, `text/primary`, `border/danger`) and once as **Tailwind classes** used in the production scandit-web codebase (`bg-surface-full-primary`, `text-ntypo-primary`, etc.). Which one you reach for depends on where the output lives:

| Context | Reach for | How |
|---|---|---|
| Editing the production `scandit-web` repo | Tailwind classes from the production mapping | Import existing components from `src/components/`; use the Tailwind classes listed in the cheat sheet |
| Standalone artifact / prototype / new project | The semantic tokens themselves | Inline the hex values as CSS variables (`--surface-default: #FFFFFF` etc., pulled from `references/design.md` YAML frontmatter), then use them everywhere instead of raw hex |
| Another Scandit product (different stack) | Semantic tokens, mapped to that stack's conventions | Same — name the variables after the semantic tokens, never after the hex |

The semantic token names are the durable contract — they're what stay consistent across products. The Tailwind classes are scandit-web's specific implementation. **In a prototype, prefer semantic names** (`var(--surface-default)`, `class="bg-surface-default"`) so the prototype can later port to any Scandit product without renaming.

## The non-negotiables

These are the rules the system breaks first when something goes wrong. Internalize them — they're upstream of everything else.

### 1. Semantic tokens, never raw values

Every color, font size, radius, shadow, and spacing value in product UI must trace back to a named token. **No `[#hex]` arbitrary values. No raw `rgb()`. No `text-[14px]`.** If the value you want doesn't have a token, that's a signal the system is missing something — surface it, don't paper over it with an arbitrary value.

Primitives (`primitive/gray/100`, etc.) are also off-limits in product UI. They only exist so the system can define semantic tokens; reaching past the semantic layer breaks the contract with Figma.

**Why this matters so much:** the entire dashboard renders consistently because every component pulls from the same semantic vocabulary. A single hardcoded `#FFFFFF` in a card is an invisible bug — it looks identical today, but the next time `surface/default` shifts to a tinted off-white, that card stays stark white and pops out wrong.

### 2. Match the namespace to the property

Each semantic namespace is scoped to exactly one CSS property. Cross-using them is the single most common drift cause.

| Property | Use only tokens from | Example tokens |
|---|---|---|
| Text color | `text/*` | `text/primary`, `text/info/default`, `text/on-color/blue` |
| Icon fill / stroke | `icon/*` | `icon/primary`, `icon/positive`, `icon/on-color` |
| Surface fill (cards, rows, chips, button bg) | `surface/*` | `surface/default`, `surface/interactive`, `surface/success/soft` |
| Page & chrome background | `background/*` | `background/primary`, `background/brand` (sidebar) |
| Border / divider | `border/*` | `border/secondary`, `border/danger` |
| Shadow color stop | `shadows/*` | `shadows/light`, `shadows/strong` |

A success message uses `text/positive`. A success icon uses `icon/positive`. A success banner uses `surface/success/*`. Its border uses `border/success`. **Never reach across namespaces for "the same green"** — even when the hex happens to match, you're tearing the contract with Figma and future re-themes will break.

`on-color/*` tokens are the **only** correct way to color text or icons sitting on a filled semantic surface. Pick the one matching the surface's hue (text on `surface/info/full` → `text/on-color/blue`, etc.).

### 3. The action color is `surface/interactive`, not `background/brand`

The deep slate `background/brand` (`#141F2E`) is for **chrome only** — the sidebar, dark nav. The brand action color is `surface/interactive` (`#1047A1`), used for primary buttons and active states. Mixing these up makes buttons look like nav and vice versa.

### 4. Avoid pure black and white

`#000` and `#FFF` are only legitimate as `background/black` and `border/white`. Everywhere else, use the tinted neutrals (`text/primary` = `#16191C`, `surface/default` = a near-white from the palette). Pure values break the warmth of the system.

### 5. Inter, with named type styles

The font is **Inter**, full stop. Don't introduce other faces. Apply size + weight together from a named style — don't mix arbitrary `text-*` and `font-*` combos:

| Style | Tailwind | Use for |
|---|---|---|
| heading-card | `text-lg font-semibold` (18/600) | Card titles, banner headlines |
| body-card | `text-sm font-normal text-typo-secondary` (14/400) | Card subtitles, supporting copy |
| label-button | `text-base font-medium` (16/500) | Primary button labels |
| label-medium | `text-sm font-medium tracking-[0.25px]` (14/500) | Ghost button labels, secondary actions |

Headings 600, body 400, interactive labels 500 with `0.25px` tracking. `text-xs` (12px) is legacy — don't use it in new work.

### 6. Branding: the logo lives in `assets/`, never invent a placeholder

The Scandit wordmark is a static SVG at [`assets/scandit-logo.svg`](assets/scandit-logo.svg). **Always inline this asset** in chrome (top bars, auth screens, marketing surfaces) — never invent a placeholder "S" square or generic logo mark, and never substitute a different mark. The SVG is 136 × 20 at native viewBox, default fill `color/text/primary` (`#16191C`). For dark surfaces (`color/background/brand`), inline the SVG with `fill="currentColor"` and let the parent set `color: var(--text-inverted)` — don't ship a separate dark-mode asset. See `references/design.md` § Brand assets for the full guidance.

### 7. Icons: approved set first, Material Symbols Rounded as fallback

61 SVGs in [`assets/icons/`](assets/icons/) are the approved catalog (full list in [`references/icons.md`](references/icons.md)). Use one of those by default — at 24×24, colored with an `icon/*` semantic token (never `currentColor`, never hardcoded hex). Pair outline + filled variants for toggleable states.

If the icon you need genuinely doesn't exist in the approved set, source it from [Material Symbols](https://fonts.google.com/icons) with these settings — **no exceptions**: Style **Rounded**, Weight **400**, Size **24dp**, Fill 0 (outline) / 1 (active), Grade 0, Optical size 24. Download the SVG, name it kebab-case, drop it into `assets/icons/`, and document it.

## Cheat sheet — the tokens you'll use 80% of the time

### Surfaces (backgrounds of components)

| Need | Token | Tailwind |
|---|---|---|
| Default card / form | `surface/default` | `bg-white` |
| Page background | `background/primary` | `bg-white` |
| Sidebar / dark chrome | `background/brand` | `bg-navbar-bg` |
| Row hover | `surface/hover` | `bg-configurator-gray-5` |
| Row pressed | `surface/pressed` | `bg-configurator-gray-10` |
| Selected row | `surface/selected` | `bg-surface-soft-brand` |
| Disabled | `surface/disabled` | `bg-configurator-gray-10` |
| Primary button | `surface/interactive` | `bg-surface-full-primary` |
| Primary button hover | `surface/interactive hover` | `bg-surface-full-primary-hover` |

### Status surfaces (4-step ramps: full → subdued → soft → softer)

For a banner, badge, or callout, pick the ramp step that matches the emphasis:
- **full** — the solid status color (icons, button-like elements)
- **subdued** — medium emphasis
- **soft** — banner / callout background
- **softer** — lightest tint, ambient highlight

Examples: `surface/info/soft` (`bg-surface-soft-info`), `surface/success/soft` (`bg-surface-soft-positive`), `surface/warning/soft` (`bg-surface-soft-warning`), `surface/danger/soft` (`bg-surface-soft-error`).

### Text

| Need | Token | Tailwind |
|---|---|---|
| Primary body / headings | `text/primary` | `text-ntypo-primary` |
| Secondary (labels, helper) | `text/secondary` | `text-ntypo-secondary` |
| Disabled | `text/disabled` | `text-configurator-gray-30` |
| Inverted (on dark) | `text/inverted` | `text-white` |
| Link default | `text/info/default` | `text-ntypo-interactive` |
| Success message | `text/positive` | `text-surface-full-positive` |
| Warning message | `text/warning` | `text-ntypo-warning` |
| Error message | `text/danger` | `text-ntypo-danger` |

### Borders

| Need | Token | Tailwind |
|---|---|---|
| Default input / card | `border/secondary` | `border-configurator-gray-20` |
| Subtle divider | `border/tertiary` | `border-configurator-gray-10` |
| Strong divider | `border/primary` | `border-ntypo-secondary` |
| Status (info/success/warning/danger) | `border/{info|success|warning|danger}` | `border-surface-full-{info|positive|warning|error}` |

### Shape & elevation

| Need | Tailwind |
|---|---|
| Input | `rounded` (4px) |
| Button, sidebar item | `rounded-lg` (8px) |
| Card | `rounded-2xl` (16px) |
| Chip, avatar | `rounded-full` |
| Resting card | `shadow` |
| Sticky header, hover card | `shadow-md` |
| Popover, dropdown | `shadow-lg` |
| Modal | `shadow-xl` |

Shadows are pure-vertical, ambient, low-opacity — never directional.

### Layout

- Sidebar fixed `w-sidebar-width` (300px) at `lg+`, fluid main with `max-w-siteContent` (1650px).
- Cards: `24px` internal padding default. Dense but never crowded — let tables breathe.
- Spacing follows the Tailwind 4px scale; reach for the named tokens (`xs` 4 → `2xl` 48).

## Build mode workflow

When generating new UI:

1. **Plan the composition first.** Identify: which container (card, dialog, banner, plain section); which atoms (button + variant, input, dropdown, etc.); what state colors apply. List them mentally before writing markup.
2. **Reach for the cheat sheet.** For colors, work down from namespace → semantic token → value/class. If a token isn't in the cheat sheet, look it up in [`references/design.md`](references/design.md) — don't guess.
3. **Use the named type styles.** Don't compose `text-base` and `font-medium` separately — apply a named pairing.
4. **Source icons from `assets/icons/` first.** Inline the SVG (artifact) or reference the asset path (in-repo). If the icon genuinely isn't there, add it via Material Symbols Rounded 400 24dp and flag it.
5. **Components: re-use, don't re-invent.** The system has 20+ components (Button, Card, Dialog, Dropdown, Toggle, etc.). **Before building a specific atom, open the matching `references/components/<component>.md` file** — it has the exact variant × state token bindings, sizes, and code patterns that aren't in the global design.md. In the scandit-web repo, import the existing atom from `src/components/`; in a prototype, replicate the anatomy documented in the per-component file.
6. **One primary button per view.** Multiple primaries dilute hierarchy; use ghost (`label-medium`) for secondary actions.

### Prototype / artifact recipe (the common case)

Most prototypes are standalone HTML or a single React file with no scandit-web codebase nearby. Set them up like this:

1. **Declare the token layer first.** At the top of the artifact, inline a `:root` block with the semantic tokens you'll use as CSS variables — pull hex values from `references/design.md` YAML frontmatter. Name the variables after the **semantic** tokens (`--surface-default`, `--text-primary`, `--border-secondary`), not the primitives or hexes. This is the durable contract.
2. **Load Inter.** Use `@import url('https://rsms.me/inter/inter.css')` or the Google Fonts CDN. Set it as the body font.
3. **Inline the icons you need** from `assets/icons/` as SVG — don't fetch externally. Size 24×24 by default (16 in dense UIs, 20 inline), color via `currentColor` from a parent that sets an `icon/*` token value, or set `stroke`/`fill` explicitly to a token var.
4. **Keep the look:** tinted neutrals, no gradients, no flashy effects, ambient pure-vertical shadows, modest radii (4 input / 8 button / 16 card / pill chip).
5. **Stay disciplined.** Even in a 50-line prototype: no raw hex outside the `:root` block, no `#000`/`#FFF` in product UI, namespace match on every property.

A prototype that follows these five steps will sit naturally next to a real Scandit dashboard. A prototype that doesn't, won't — even if it looks "fine" in isolation.

## Audit mode workflow

When reviewing existing UI code:

1. **Hardcoded values.** Grep for `#[0-9a-fA-F]{3,8}`, `rgb(`, `text-\[`, `bg-\[`, `border-\[`. Each hit is a finding.
2. **Pure black/white in product UI.** Flag any `bg-black`, `bg-white`, `text-black`, `text-white`, `#000`, `#FFF` that aren't `background/black` (rare) or `border/white` (on dark surfaces).
3. **Cross-namespace usage.** `bg-text-*`, `text-surface-*`, `border-text-*` patterns indicate someone reached across namespaces for the same hex. Flag.
4. **Primitive usage.** `primitive/*` tokens in product UI (not in `tailwind.config.js` or token definitions) is a violation.
5. **Off-system icons.** Imports from `lucide`, `react-icons`, `heroicons`, inline SVGs not from `assets/icons/`, or Material Symbols configured with anything other than Rounded/400/24dp.
6. **Loose typography.** `text-xs` in new code is legacy. Arbitrary `text-[Npx]`. Type pairings that don't match the named styles.
7. **Hierarchy.** Multiple primary buttons in one view. Sidebar items missing the `h-12 px-3 mx-3 rounded-lg gap-3` anatomy.
8. **Known divergences.** `ntypo-primary` resolves to `#1A1A1A` in Tailwind but Figma is `#16191C` — note as known. Legacy classes (`teal-scandit`, `card-border`, `newblue-dark`, etc.) are flagged in `references/design.md` § Project-specific (legacy) tokens — prefer Figma equivalents in new work.

Report findings as a list with file:line references and the specific token/class that should be used instead. Don't auto-fix unless the user asks.

## Do's and Don'ts (the condensed version)

- **Do** trace every color/spacing/radius value to a token.
- **Do** match property → namespace (text→`text/*`, icon→`icon/*`, etc.).
- **Do** use named type styles together (size + weight + tracking as a unit).
- **Do** use `on-color/*` tokens for text/icons on filled semantic surfaces.
- **Do** reach for the approved icon set first; Material Symbols Rounded 400 24dp for anything missing.
- **Don't** cross namespaces, even when hexes match.
- **Don't** use primitives directly in product UI.
- **Don't** use `#000` / `#FFF` outside the two legitimate cases.
- **Don't** use `text-xs` (12px) in new work — legacy.
- **Don't** introduce directional shadows or bouncy motion — elevation is pure-vertical, motion is functional.
- **Don't** duplicate components — wrap or extend the shared atom.

## When you need more depth

| You're looking for | Open |
|---|---|
| Full color tables (primitives, semantic ramps, legacy mappings, divergences) | [`references/design.md`](references/design.md) § Colors |
| Full type scale & components | [`references/design.md`](references/design.md) § Typography |
| Layout, breakpoints, spacing scale | [`references/design.md`](references/design.md) § Layout |
| Shadows, radii, motion | [`references/design.md`](references/design.md) § Elevation / Shapes / Motion |
| Full component catalog (when to use which) | [`references/design.md`](references/design.md) § Components |
| Variant × state token bindings for a specific component | [`references/components/<component>.md`](references/components/) (e.g. `button.md`, `dialog.md`) |
| Icon catalog + per-icon Tailwind keys | [`references/icons.md`](references/icons.md) |
| Raw SVG icon assets | [`assets/icons/`](assets/icons/) |

The user is Scandit's design owner — they care about getting this right, and they will spot incorrect tokens. When in doubt, look it up rather than guess.
