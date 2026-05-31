# Breadcrumbs

> **When to use:** Show the user's location in a multi-level page hierarchy. Place at the top of a content area, above the page heading. Keep paths short — 3-5 levels at most. If the path is longer, collapse middle steps behind an overflow `…` (not yet documented in Figma).
>
> **Figma:** [open in UI Kit](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=2934-6290)

> **Notes:** A single horizontal flex row composed of `_breadcrumbItem` instances. Each item has a **position** of `First`, `Middle`, or `Last` — the position drives both the leading separator (chevron or nothing) and the text colour. Figma keeps `First` + `Last` always; `Middle` items repeat between them (1–3 are shown in the documented frame via `showItem2/3/4` flags). Items have no padding; the spacing is implicit in the chevron's 20×20 box.
>
> **Chevron asset:** `chevron_right` from the approved icon set — [`assets/icons/chevron-right.svg`](../../assets/icons/chevron-right.svg). Figma's export pipeline ships **two pre-tinted PNG renders** of the chevron (one for Middle items at `color/icon/secondary`, one for the Last item's leading chevron at `color/icon/disabled`). In code, ship a **single SVG** and let the colour come from the parent text colour via `currentColor` — that way the tint comes from the namespace-correct `color/icon/*` token applied to the parent, not duplicated assets.
>
> **Token names** below match the Figma variable names verbatim (`color/text/secondary`, `body/small`, etc.). Every token is documented in [`../design.md`](../design.md) at the same hex / spec — the catalog and this file are in sync.

## Variants

| Variant | Usage |
|---|---|
| `default` | The only variant. Horizontal row of items separated by `chevron_right`. Last item is the current page and rendered with reduced emphasis. |

## Sizes

| Size | Item height | Text style | Padding | Chevron size | Gap |
|---|---|---|---|---|---|
| `md` (only documented size) | 20px (matches `body/small` line-height) | `body/small` — 14px Regular, 20px line-height, 0.25px letter-spacing | none on container or items | 20×20 (chevron glyph 20px, no padding) | 0 — the chevron's own 20px box provides the visual spacing |

## States

The position of an item drives its visual treatment — these are positional states, not interaction states.

- **default** — `First` and `Middle` positions. Item is rendered in `color/text/secondary`; preceding chevron (on Middle items only) is `color/icon/secondary`.
- **current** — `Last` position, representing the current page. Item is rendered in `color/text/disabled` (lighter, non-interactive feel); preceding chevron is `color/icon/disabled`. The current item should be marked `aria-current="page"` in code and is not focusable as a link.

## Tokens per variant × state

| Variant | State (Position) | Text | Leading separator (chevron) | Chevron colour | Notes |
|---|---|---|---|---|---|
| `default` | `default` — First | `color/text/secondary` (`#525A61`) | none | — | First item has no leading separator. |
| `default` | `default` — Middle | `color/text/secondary` (`#525A61`) | `chevron_right` 20×20 | `color/icon/secondary` (`#6C7680`) | Repeats between First and Last; 1–3 occurrences typical. |
| `default` | `current` — Last | `color/text/disabled` (`#ACB6BF`) | `chevron_right` 20×20 | `color/icon/disabled` (`#ACB6BF`) | Lighter ink on both separator and label signals "you are here". |

## Anatomy

```
   ┌──────────────┐                ┌──────────────┐                ┌──────────────┐
   │  Breadcrumb  │  ›  Breadcrumb │  ›  Breadcrumb│  ›  Breadcrumb │  ›  Breadcrumb│
   └──────────────┘   ↑            └──────────────┘                └──────────────┘
        First        chevron_right    Middle (×1–3)                      Last
        body/small    20×20                                               body/small
        text/secondary icon/secondary                                     text/disabled
                                                                          ↑
                                                                          chevron before
                                                                          Last uses
                                                                          icon/disabled
```

Items are pure-content (no padding, no border, no background). The chevron's 20×20 box is the visual separator and gap — items "touch" the chevron on both sides.

## Code

### In-repo (React + Tailwind, scandit-web mapping)

```tsx
import { ChevronRightIcon } from '@/icons';

type Crumb = { label: string; href?: string };
type BreadcrumbsProps = { items: Crumb[] };

export function Breadcrumbs({ items }: BreadcrumbsProps) {
  return (
    <nav aria-label="Breadcrumb">
      <ol className="flex items-center text-sm tracking-[0.25px]">
        {items.map((item, i) => {
          const isLast = i === items.length - 1;
          return (
            <li key={i} className="flex items-center">
              {i > 0 && (
                <ChevronRightIcon
                  aria-hidden="true"
                  className={
                    isLast
                      ? 'size-5 text-configurator-gray-30'   // color/icon/disabled
                      : 'size-5 text-ntypo-secondary'        // color/icon/secondary — verify Tailwind key
                  }
                />
              )}
              {isLast ? (
                <span aria-current="page" className="text-configurator-gray-30">
                  {item.label}
                </span>
              ) : (
                <a href={item.href} className="text-ntypo-secondary hover:text-ntypo-primary">
                  {item.label}
                </a>
              )}
            </li>
          );
        })}
      </ol>
    </nav>
  );
}
```

### Standalone artifact (prototype)

```html
<style>
  :root {
    --color-text-secondary: #525A61;   /* default + middle item label */
    --color-text-disabled:  #ACB6BF;   /* current (last) item label */
    --color-icon-secondary: #6C7680;   /* default separator chevron */
    --color-icon-disabled:  #ACB6BF;   /* separator before current item */
  }
  .crumbs {
    display: flex; align-items: center;
    margin: 0; padding: 0;
    list-style: none;
    font-family: Inter, system-ui, sans-serif;
    font-size: 14px;            /* body/small */
    line-height: 20px;
    letter-spacing: 0.25px;
  }
  .crumbs__item { display: flex; align-items: center; }
  .crumbs__link {
    color: var(--color-text-secondary);
    text-decoration: none;
  }
  .crumbs__link:hover { color: var(--color-text-primary, #16191C); text-decoration: underline; }
  .crumbs__current {
    color: var(--color-text-disabled);
  }
  .crumbs__sep {
    width: 20px; height: 20px;
    color: var(--color-icon-secondary);
    display: inline-block;
  }
  .crumbs__item:last-child .crumbs__sep { color: var(--color-icon-disabled); }
</style>

<nav aria-label="Breadcrumb">
  <ol class="crumbs">
    <li class="crumbs__item">
      <a href="/" class="crumbs__link">Workspace</a>
    </li>
    <li class="crumbs__item">
      <span class="crumbs__sep" aria-hidden="true">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none"
             stroke="currentColor" stroke-width="2"
             stroke-linecap="round" stroke-linejoin="round">
          <polyline points="9 18 15 12 9 6"/>
        </svg>
      </span>
      <a href="/projects" class="crumbs__link">Projects</a>
    </li>
    <li class="crumbs__item">
      <span class="crumbs__sep" aria-hidden="true">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none"
             stroke="currentColor" stroke-width="2"
             stroke-linecap="round" stroke-linejoin="round">
          <polyline points="9 18 15 12 9 6"/>
        </svg>
      </span>
      <span class="crumbs__current" aria-current="page">Warehouse pilot — Zurich DC</span>
    </li>
  </ol>
</nav>
```

## Don'ts

- **Don't link the current page.** The last item should be plain text marked `aria-current="page"`, not an anchor. Linking the current page is a usability anti-pattern (the user is already there) and the visual treatment (`color/text/disabled` + `color/icon/disabled`) reinforces non-interactivity.
- **Don't substitute a different separator** (slash, arrow, `›` HTML entity rendered as text). The system uses the `chevron_right` icon at exactly 20×20 — anything else breaks alignment with the 20px line-height baseline.
- **Don't introduce padding or borders on items.** Items are pure inline content; spacing comes from the chevron's own bounding box. Adding padding shifts the alignment and breaks the "flush against the chevron" look.
- **Don't use breadcrumbs for navigation outside a hierarchy.** They communicate parent → child → current. For peer navigation, use Tabs. For deep nested data, use Tree view.
- **Don't put more than 5 levels visible.** Beyond that, collapse middle steps behind an overflow `…` — but this pattern isn't documented in Figma yet, so flag it to the design owner before implementing.
- **Don't reach for `color/text/primary` on any item.** The whole row sits at `text/secondary` (and `text/disabled` for current). Using primary text makes breadcrumbs compete with the page heading directly below them.
