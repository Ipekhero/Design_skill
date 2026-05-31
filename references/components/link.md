# Link

> **When to use:** Inline navigation to another page or external resource. Distinct from buttons — a link **takes you somewhere**, a button **performs an action**. If the user expects to navigate (URL change, route change, new tab), it's a Link; if they expect an immediate change to the current state (save, delete, toggle), it's a Button.
>
> **Figma:** [open in UI Kit](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=418-865)

> **Notes:**
>
> - **Three visual-treatment types**, picked by where the link sits and how loud it should be:
>   - `default` — blue text (`color/text/info/default`), always underlined. The standard hyperlink for standalone navigation.
>   - `neutral` — body-text dark (`color/text/primary`), always underlined. Use **inside paragraphs** where the blue would compete with the text rhythm — visually quieter while still announcing "this is a link."
>   - `context_link` — same blue as Default but **no underline at rest**. The underline materialises on hover/pressed/disabled. Use for the "primary destination link" inside a content block (e.g. a "Read more" inside a card or a "View documentation" CTA where the surrounding container already signals interactivity).
> - **One size only** — `label/large` (16px Medium, 24px line-height, 0.25px letter-spacing). For smaller link sizes, scale via the parent's font-size (the link inherits or use it inline) — the Link component doesn't carry sm/lg variants in this Figma node.
> - **Underline is drawn as a 1px bottom border**, not via CSS `text-decoration: underline`. The border-color matches the text-color in each state, giving Figma exact control over the colour pairing.
> - **No `focused` or `visited` state in Figma.** design.md previously listed them; dropped per the no-Figma-no-token rule. Implementations should still render a visible focus ring on keyboard navigation (use `2px outline color/border/interactive offset 2px` per WCAG AA), and respect the browser's `:visited` history — but the spec is silent on visuals.
>
> **Token names** below match Figma variable names verbatim. All colour tokens are documented in `design.md` at the same hex.

## Variants

| Variant | Figma label | Default colour | Underline at rest | Use for |
|---|---|---|---|---|
| `default` | Default | `color/text/info/default` (`#1660D9` blue) | ✓ Always underlined | Standalone hyperlinks — list of links in a footer, breadcrumb-adjacent navigation, standalone CTAs that need to scream "hyperlink". |
| `neutral` | Neutral | `color/text/primary` (`#16191C` dark) | ✓ Always underlined | **Inline within body text.** Same shape as Default but the blue is suppressed so the link doesn't compete with the text rhythm — the underline still announces it's a link. |
| `context_link` | Context-link | `color/text/info/default` (`#1660D9` blue) | ✗ No underline; appears on hover/pressed/disabled | Destination-link affordance inside a contextual block (card body, dialog body, callout text). The container already implies interactivity, so the underline can fade until interaction. |

## Sizes

No size axis — Link is fixed at **`label/large`** (16px Medium / 24px lh / 0.25 ls / Inter). For smaller inline contexts, scale via the parent's `font-size` rather than introducing a new variant.

## States × Variant

The full state matrix. Text and border colours move together — the underline is always the same colour as the text.

### Default + Neutral types share the same border behavior

Both render the underline (1px bottom border) at every state including default. The only difference is the **default text colour**: `text/info/default` blue for Default, `text/primary` dark for Neutral. All other states use the same colour ladder.

| State | Text colour | Border-bottom colour | Cursor |
|---|---|---|---|
| `default` (Default type) | `color/text/info/default` (`#1660D9`) | `color/text/info/default` (`#1660D9`) | `cursor: pointer` |
| `default` (Neutral type) | `color/text/primary` (`#16191C`) | `color/text/primary` (`#16191C`) | `cursor: pointer` |
| `hover` (both) | `color/text/info/hover` (`#3683FF` — lighter sky blue) | `color/text/info/hover` (`#3683FF`) | `cursor: pointer` |
| `pressed` (both) | `color/text/info/pressed` (`#1047A1` — brand blue) | `color/text/info/pressed` (`#1047A1`) | `cursor: pointer` |
| `disabled` (both) | `color/text/disabled` (`#ACB6BF`) | `color/text/disabled` (`#ACB6BF`) | `cursor: not-allowed` |

### Context-link (underline only on interaction)

| State | Text colour | Border-bottom colour | Cursor |
|---|---|---|---|
| `default` | `color/text/info/default` (`#1660D9`) | **none** — no underline at rest | `cursor: pointer` (implied by parent) |
| `hover` | `color/text/info/hover` (`#3683FF`) | `color/text/info/hover` (`#3683FF`) — underline appears | `cursor: pointer` |
| `pressed` | `color/text/info/pressed` (`#1047A1`) | `color/text/info/pressed` (`#1047A1`) — underline | `cursor: pointer` |
| `disabled` | `color/text/disabled` (`#ACB6BF`) | `color/text/disabled` (`#ACB6BF`) — underline | `cursor: not-allowed` |

## Anatomy

```
  Default / Neutral (always underlined)
  ┌─────────┐
  │  link   │   text-color: variant default
  ├─────────┤   border-bottom: 1px solid (text-color)
                font: label/large (16px Medium / 24px lh / 0.25 ls)


  Context-link (default — no underline)
  ┌─────────┐
  │  link   │   text-color: text/info/default
  └─────────┘   border-bottom: none

  Context-link (hover/pressed/disabled — underline appears)
  ┌─────────┐
  │  link   │   text-color: state colour
  ├─────────┤   border-bottom: 1px solid (state colour)
```

The Link is **inline** content — it doesn't reserve its own block. In a paragraph it flows with the surrounding text; standalone, it's a single line that's as wide as its label.

## Code

### In-repo (React + Tailwind, scandit-web mapping)

```tsx
type LinkVariant = 'default' | 'neutral' | 'context_link';

type LinkProps = React.AnchorHTMLAttributes<HTMLAnchorElement> & {
  variant?: LinkVariant;
  disabled?: boolean;
};

const VARIANT_STYLES: Record<LinkVariant, string> = {
  default:
    // default text + always-underline + colour ladder for hover/active
    'text-newblue-darker border-b border-newblue-darker ' +     // color/text/info/default → also #1660D9 if not aliased
    'hover:text-[#3683FF] hover:border-[#3683FF] ' +            // color/text/info/hover
    'active:text-surface-full-primary active:border-surface-full-primary ' + // color/text/info/pressed → #1047A1
    'aria-disabled:text-configurator-gray-30 aria-disabled:border-configurator-gray-30 aria-disabled:cursor-not-allowed',
  neutral:
    'text-ntypo-primary border-b border-ntypo-primary ' +
    'hover:text-[#3683FF] hover:border-[#3683FF] ' +
    'active:text-surface-full-primary active:border-surface-full-primary ' +
    'aria-disabled:text-configurator-gray-30 aria-disabled:border-configurator-gray-30 aria-disabled:cursor-not-allowed',
  context_link:
    // no border at rest; appears on hover
    'text-newblue-darker border-b border-transparent ' +
    'hover:text-[#3683FF] hover:border-[#3683FF] ' +
    'active:text-surface-full-primary active:border-surface-full-primary ' +
    'aria-disabled:text-configurator-gray-30 aria-disabled:border-configurator-gray-30 aria-disabled:cursor-not-allowed',
};

export function Link({ variant = 'default', disabled, children, ...rest }: LinkProps) {
  return (
    <a
      {...rest}
      aria-disabled={disabled || undefined}
      tabIndex={disabled ? -1 : rest.tabIndex}
      onClick={disabled ? (e) => e.preventDefault() : rest.onClick}
      className={[
        'inline-block text-base font-medium tracking-[0.25px] leading-6',  // label/large
        'no-underline',                                                     // we draw the underline via border-b
        'focus-visible:outline focus-visible:outline-2 focus-visible:outline-newblue-darker focus-visible:outline-offset-2',
        VARIANT_STYLES[variant],
      ].join(' ')}
    >
      {children}
    </a>
  );
}
```

### Standalone artifact (prototype)

```html
<style>
  :root {
    --color-text-info-default:  #1660D9;
    --color-text-info-hover:    #3683FF;
    --color-text-info-pressed:  #1047A1;
    --color-text-primary:       #16191C;
    --color-text-disabled:      #ACB6BF;
  }

  .link {
    display: inline-block;
    font-family: Inter, system-ui, sans-serif;
    font-size: 16px; font-weight: 500; line-height: 24px; letter-spacing: 0.25px;  /* label/large */
    text-decoration: none;                       /* we draw the underline via border-b */
    border-bottom: 1px solid transparent;        /* reserve space so layout doesn't shift between states */
    cursor: pointer;
    transition: color 120ms, border-color 120ms;
  }
  .link:focus-visible {
    outline: 2px solid var(--color-text-info-default);
    outline-offset: 2px;
  }

  /* Default + Neutral — always show the underline (default state colours differ; hover/active/disabled ladder is shared) */
  .link--default { color: var(--color-text-info-default); border-bottom-color: var(--color-text-info-default); }
  .link--neutral { color: var(--color-text-primary);      border-bottom-color: var(--color-text-primary); }

  /* Context-link — no underline at rest; the border is transparent (kept for layout stability), only colour changes on interaction */
  .link--context_link { color: var(--color-text-info-default); border-bottom-color: transparent; }
  .link--context_link:not([aria-disabled="true"]):not(.is-disabled):hover,
  .link--context_link.is-hover,
  .link--context_link:not([aria-disabled="true"]):not(.is-disabled):active,
  .link--context_link.is-pressed   { border-bottom-color: var(--color-text-info-hover); }
  .link--context_link:not([aria-disabled="true"]):not(.is-disabled):active,
  .link--context_link.is-pressed   { border-bottom-color: var(--color-text-info-pressed); }
  .link--context_link[aria-disabled="true"],
  .link--context_link.is-disabled  { border-bottom-color: var(--color-text-disabled); }

  /* Shared state ladder for all variants (hover/pressed/disabled colour) */
  .link:not([aria-disabled="true"]):not(.is-disabled):hover,
  .link.is-hover    { color: var(--color-text-info-hover); border-bottom-color: var(--color-text-info-hover); }
  .link:not([aria-disabled="true"]):not(.is-disabled):active,
  .link.is-pressed  { color: var(--color-text-info-pressed); border-bottom-color: var(--color-text-info-pressed); }

  /* Disabled overrides everything else (specificity needs to win over the colour-specific rules) */
  .link[aria-disabled="true"],
  .link.is-disabled {
    color: var(--color-text-disabled);
    border-bottom-color: var(--color-text-disabled);
    cursor: not-allowed;
  }
</style>

<!-- Default (blue, always underlined) -->
<a href="#" class="link link--default">View documentation</a>

<!-- Neutral (dark, always underlined — for use inside body text) -->
<p>For details, see the
  <a href="#" class="link link--neutral">License usage report</a>
  in the admin console.</p>

<!-- Context-link (no underline at rest, appears on hover) -->
<a href="#" class="link link--context_link">Read more →</a>

<!-- Disabled -->
<a href="#" class="link link--default is-disabled" aria-disabled="true" tabindex="-1">Unavailable on trial</a>
```

## Don'ts

- **Don't use `text-decoration: underline`** — the Link uses a 1px `border-bottom` whose colour exactly tracks the text colour in each state. CSS `text-decoration` has less control over the line colour and offset, and the visual line position will not match Figma. The border approach also lets `Context-link` toggle the underline by changing border-color rather than toggling a different property family.
- **Don't substitute a button for a link** (or vice versa). A link **navigates** (URL changes); a button **acts** (state changes in place). If your "link" doesn't change the URL or open a new tab, it's a Button. If your "button" navigates somewhere, it's a Link.
- **Don't use `default` (blue) inside body paragraphs.** The blue competes with the paragraph's reading rhythm. Use `neutral` inline — same affordance, quieter.
- **Don't render `context_link` outside a contextual block.** Without the surrounding card / dialog / callout to signal "this is interactive", the no-underline default state reads as plain text. Use `default` for standalone hyperlinks.
- **Don't omit a visible focus ring for keyboard users.** Figma doesn't draw `focused`, but WCAG AA requires it. Use `outline: 2px solid color/text/info/default` with 2px offset; don't rely on the underline alone (some browsers suppress it on focus).
- **Don't link "click here" / "read more" with no context.** The link text should describe its destination so screen readers can announce it. "View the License usage report" is good; "Click here" is unintelligible out of context.
- **Don't apply hover colour shifts to `disabled`.** The disabled state must stay flat at `text/disabled`. The `:not([aria-disabled="true"])` guards in the standalone code enforce this.
- **Don't use Link styles for navigation chrome.** The sidebar, top nav, and tab affordances are their own components — they have their own hover treatments, selected states, and chrome-specific colour ramps. Link is for inline / standalone hyperlinks within content.
