# Accordion

> **When to use:** Disclose sections of content one at a time to reduce vertical density. Reach for this when the content is reference material the user dips into, not the page's primary task.
>
> **Figma:** [open in UI Kit](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=6463-9416)

> **Notes:** The Figma component exposes a single size labelled **Large (Desktop)** — corresponds to the `md` size key in `design.md`. Header is 56px tall regardless of state; the expanded version adds a content slot below a 1px divider. Container width is fluid by default (Figma frame is 860px for the spec, but the component is meant to fill its container).
>
> **Token names** below match the Figma variable names verbatim (`color/border/secondary`, `size/cornerRadius/m`, `heading/large`, etc.). Cross-reference each name against [`references/design.md`](../design.md) — every token listed here is documented there. Where Figma and design.md spell things differently (e.g. Figma `heading/large` vs. design.md `heading-lg`), the Figma name is canonical.

## Variants

| Variant | Usage |
|---|---|
| `default` | The only variant — header + optional expandable content slot. Use it for any FAQ-style or "show more details" pattern, grouped with other accordions to form a list. |

## Sizes

| Size | Header height | Title type | Header padding | Header gap | Leading icon | Container corner radius |
|---|---|---|---|---|---|---|
| `md` (Figma: "Large / Desktop") | 56px | `heading/large` — Inter SemiBold 24px | `spacing/padding/s` (8px) all sides | `spacing/stack/xs` (4px) collapsed · `spacing/padding/xs` (4px) expanded | 36×36 button hit area; chevron glyph drawn at 24×24 | `size/cornerRadius/m` (8px) |

## States

- **collapsed** — Header only. Container has a full 1px `color/border/secondary` outline; no internal divider. Chevron points **down** (`chevron_down`).
- **expanded** — Header + content slot. A 1px `color/border/secondary` divider sits between header and content. Chevron points **up** (`chevron_up`). Content slot has `spacing/padding/s` (8px) padding inside an inner 12px-rounded surface.
- **hover** — Not specified in Figma at the component level. Recommended: apply `color/surface/hover` to the header row to signal the click target.
- **focused** — Not specified in Figma. Recommended: 2px outline using `color/border/interactive` with 2px offset on the header `<button>`, for keyboard accessibility (WCAG AA target).
- **disabled** — Not specified in Figma. Recommended: title in `color/text/disabled`, chevron in `color/icon/disabled`, `cursor-not-allowed`, no expand on click, `aria-disabled` on the trigger.

## Tokens per variant × state

For each row, name the exact semantic token used on each property. Cross-namespace usage is a violation — keep `surface/*` in the surface column, `text/*` in text, etc.

| Variant | State | Surface | Text | Border | Icon | Notes |
|---|---|---|---|---|---|---|
| `default` | `collapsed` | `color/background/primary` | `color/text/primary` | `color/border/secondary` (1px outline on container) | `color/icon/primary` (`chevron_down`) | Header has no border-bottom; gap between icon and text is `spacing/stack/xs` (4px). |
| `default` | `expanded` | `color/background/primary` | `color/text/primary` | `color/border/secondary` (1px outline on container **and** 1px divider between header and content) | `color/icon/primary` (`chevron_up`) | Content slot has `spacing/padding/s` (8px) padding with an inner 12px-rounded surface. |
| `default` | `hover` | `color/surface/hover` on the header row only | `color/text/primary` | `color/border/secondary` (unchanged) | `color/icon/primary` | Hover affordance on the entire header button so the click target reads. |
| `default` | `focused` | `color/background/primary` | `color/text/primary` | `color/border/secondary` + 2px `color/border/interactive` focus ring on the header `<button>` | `color/icon/primary` | Keyboard focus must be visible; offset the ring by 2px so it doesn't crop. |
| `default` | `disabled` | `color/surface/disabled` | `color/text/disabled` | `color/border/secondary` | `color/icon/disabled` | Cursor `not-allowed`; no expand on click; `aria-disabled` on the trigger. |

## Anatomy

```
┌──────────────────────────────────────────────────────────┐  ← container
│  ┌─────┐                                                 │     border: 1px color/border/secondary
│  │  ⌄  │  License Key                                    │     radius: size/cornerRadius/m (8px)
│  └─────┘                                                 │     background: color/background/primary
└──────────────────────────────────────────────────────────┘
   36×36   heading/large · color/text/primary
   icon    title (Inter SemiBold 24px)
   ↑
   header: 56px · spacing/padding/s (8px) · spacing/stack/xs (4px) gap

── expanded adds: ───────────────────────────────────────────
   ⎯⎯⎯⎯⎯⎯⎯ 1px color/border/secondary divider ⎯⎯⎯⎯⎯⎯⎯
   ┌────────────────────────────────────────────────────┐
   │  content slot — spacing/padding/s (8px)            │
   │                  inner radius: 12px                │
   └────────────────────────────────────────────────────┘
```

## Code

### In-repo (React + Tailwind, scandit-web mapping)

```tsx
import { ChevronDownIcon, ChevronUpIcon } from '@/icons';

type AccordionProps = {
  title: string;
  defaultExpanded?: boolean;
  children: React.ReactNode;
};

export function Accordion({ title, defaultExpanded = false, children }: AccordionProps) {
  const [expanded, setExpanded] = React.useState(defaultExpanded);
  const headerId = React.useId();
  const panelId = React.useId();

  return (
    <div className="bg-white border border-configurator-gray-20 rounded-lg overflow-hidden">
      <button
        id={headerId}
        type="button"
        aria-expanded={expanded}
        aria-controls={panelId}
        onClick={() => setExpanded((v) => !v)}
        className={[
          'flex w-full h-14 items-center gap-1 px-2',
          'text-ntypo-primary text-2xl font-semibold text-left',
          'hover:bg-configurator-gray-5',
          'focus:outline-none focus-visible:ring-2 focus-visible:ring-newblue-darker focus-visible:ring-offset-2',
          expanded ? 'border-b border-configurator-gray-20' : '',
        ].join(' ')}
      >
        <span className="size-9 grid place-items-center text-ntypo-primary">
          {expanded ? <ChevronUpIcon className="size-6" /> : <ChevronDownIcon className="size-6" />}
        </span>
        <span className="flex-1">{title}</span>
      </button>
      {expanded && (
        <div id={panelId} role="region" aria-labelledby={headerId} className="p-2">
          <div className="rounded-[12px]">{children}</div>
        </div>
      )}
    </div>
  );
}
```

### Standalone artifact (prototype)

```html
<style>
  :root {
    --background-primary: #FFFFFF;
    --surface-hover:      #F3F5F8;
    --surface-disabled:   #E1E7ED;
    --text-primary:       #16191C;
    --text-disabled:      #ACB6BF;
    --border-secondary:   #C7CFD6;
    --border-interactive: #16191C;
    --icon-primary:       #16191C;
    --icon-disabled:      #ACB6BF;
  }
  .accordion {
    background: var(--background-primary);
    border: 1px solid var(--border-secondary);
    border-radius: 8px;
    overflow: hidden;
    font-family: Inter, system-ui, sans-serif;
  }
  .accordion__header {
    display: flex; align-items: center; gap: 4px;
    width: 100%; height: 56px;
    padding: 8px;
    background: transparent;
    border: 0;
    color: var(--text-primary);
    font-size: 24px;
    font-weight: 600;
    text-align: left;
    cursor: pointer;
  }
  .accordion__header:hover { background: var(--surface-hover); }
  .accordion__header:focus-visible {
    outline: 2px solid var(--border-interactive);
    outline-offset: 2px;
  }
  .accordion__header[aria-expanded="true"] {
    border-bottom: 1px solid var(--border-secondary);
  }
  .accordion__header[aria-disabled="true"] {
    background: var(--surface-disabled);
    color: var(--text-disabled);
    cursor: not-allowed;
  }
  .accordion__icon {
    width: 36px; height: 36px;
    display: grid; place-items: center;
    color: var(--icon-primary);
  }
  .accordion__header[aria-disabled="true"] .accordion__icon { color: var(--icon-disabled); }
  .accordion__content { padding: 8px; }
  .accordion__inner   { border-radius: 12px; }
</style>

<div class="accordion">
  <button class="accordion__header" aria-expanded="false" aria-controls="acc-license-key">
    <span class="accordion__icon" aria-hidden="true">
      <!-- chevron_down when collapsed; swap glyph to chevron_up when aria-expanded="true" -->
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none"
           stroke="currentColor" stroke-width="2"
           stroke-linecap="round" stroke-linejoin="round">
        <polyline points="6 9 12 15 18 9"/>
      </svg>
    </span>
    <span style="flex: 1">License Key</span>
  </button>
  <div id="acc-license-key" class="accordion__content" hidden>
    <div class="accordion__inner">
      <!-- content -->
    </div>
  </div>
</div>
```

## Don'ts

- **Don't use an accordion for a single item.** One disclosable section is just a Card with a collapse — use Card instead. Accordions earn their complexity by managing multiple sections.
- **Don't open all sections by default.** Defeats the purpose. If everything matters at once, use a plain stacked layout.
- **Don't nest accordions.** Information hierarchy collapses on itself; users lose track of where they are.
- **Don't use accordions for primary navigation.** Use Sidebar or Tabs. Accordions are for *content* disclosure, not wayfinding.
- **Don't change the chevron to a `+ / -`, arrow, or custom glyph.** The Figma spec uses `chevron_down` / `chevron_up` from the approved icon set — pairing outline glyphs for state is the system convention (same pattern as Toggle, Visibility, etc.).
- **Don't put the chevron on the right.** Figma places it leading-left at 36×36 with `icon/primary` color. Keep it consistent with the documented anatomy.
- **Don't apply a shadow to the container.** Accordions sit flat on the page; elevation is reserved for cards, popovers, and modals.
