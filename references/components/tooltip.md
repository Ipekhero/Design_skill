# Tooltip

> **TL;DR**
> - A **brief contextual hint** that appears on hover or keyboard focus of a trigger element. Used for **labelling icon-only buttons**, explaining unfamiliar terminology, or surfacing terse helper text that doesn't earn permanent screen real estate.
> - **Visually unmistakable**: brand-blue `surface/interactive` `#1047A1` background, white text, **sharp 0-radius rectangle** (NOT rounded), with a 16 × 8 px caret pointing at the trigger.
> - **One variant, no state machine.** The tooltip is presentation-only — the trigger has the state (hover/focus), the tooltip just appears or doesn't. No hover/pressed/disabled variants of the tooltip itself.
> - **2 positions in Figma — names verbatim**: `tipPosition: bottom` (tip on the bottom of the label, **tooltip sits ABOVE the trigger** pointing down) and `tipPosition: top` (tip on the top of the label, **tooltip sits BELOW the trigger** pointing up). `left` / `right` placements aren't in Figma — extend when needed.
> - **Typography is `copy/caption` 12 / 400 / 16** (Roboto in Figma → ship Inter). Padding **8px horizontal, 4px vertical**. The label wraps within its `max-width` — short tooltips fit on one line, longer ones break to two.
> - **Trigger-driven, not click-driven.** A tooltip appears on `:hover` / `:focus-visible` of the trigger after a ~500ms delay and disappears when the trigger loses hover/focus. **Don't make it click-to-open** — that's a [[popover]] (which doesn't exist as a component here yet, but the semantic distinction matters).

Figma source:
- [Tooltip (tip on top + tip on bottom)](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=10956-20525)

## When to use

| Use Tooltip when… | Use something else when… |
|---|---|
| You need to **label an icon-only button** so the user understands what it does (kebab menu, scan-icon, refresh) | The hint applies to a **filled-in field** with persistent value — use the [[text-field]] `helperText` slot |
| The text is a **brief 1–2 line clarification** (≤ 12 words ideal, 25 max) | The content runs **3+ lines** or contains links / actions — use a [[callout]] (in-flow) or a [[popover]] (click-anchored, not in scope yet) |
| The hint is **non-essential** — the UI still works if the tooltip never appears (it's an enhancement) | The information is **required to use the control** — that's missing content, not a tooltip case. Put it inline. |
| You're explaining **jargon, abbreviations, or status** ("What does *MatrixScan* mean?", "Why is this badge red?") | The element is a **link to a separate page** — link to that page with proper anchor text; don't bury the explanation in a tooltip |

## Anatomy

```
                      ╔═══════════════════════════════╗
   `tipPosition:      ║  Give tooltips meaningful     ║   ← label box: brand-blue,
   bottom`            ║  messages                     ║      0-radius rectangle,
   (tooltip ABOVE     ╚═══════════════╤═══════════════╝      8px horizontal / 4px vertical
   the trigger)                       ▼  ← tip (16 × 8 px caret)
                              [trigger]


                              [trigger]
                                       ▲  ← tip (16 × 8 px caret)
   `tipPosition:      ╔═══════════════╧═══════════════╗
   top` (tooltip      ║  Give tooltips meaningful     ║
   BELOW the          ║  messages                     ║
   trigger)           ╚═══════════════════════════════╝
```

- **Label box** — `surface/interactive` `#1047A1` brand-blue surface, white text, sharp corners (`border-radius: 0`), padded 8px horizontal × 4px vertical.
- **Tip caret** — 16 × 8 px filled triangle in the same brand blue, pointing AT the trigger. The caret is **centred on the trigger** (not on the label) — so if the label is wider than the trigger, the caret stays near the trigger's center, not the label's center.
- **Width** — tooltips read more naturally as a horizontal pill than a near-square block. Set **`min-width: 120px`** so tiny labels ("Open scanner") still feel like tooltips and not chips, and **`max-width: 320px`** so most short copy fits on one line and only genuinely long copy wraps to two. Figma's example sits at 137 px which is on the tight end — use the catalog values above in production.

## Tokens

| Property | Token | Value |
|---|---|---|
| Label surface | `color/surface/interactive` | `#1047A1` (brand blue) |
| Label text | `color/text/inverted` | `#FFFFFF` (white) |
| Text style | `copy/caption` | 12 / 400 / 16 line-height, Inter (Figma says Roboto — substitute per [[feedback-figma-font-placeholders]]) |
| Horizontal padding | `tooltip/label/padding/v` (Figma name) | **8px** — note: the Figma token name says `padding/v` but the value is applied as `px-[8px]` (horizontal). Keep as-is but document the rename. |
| Vertical padding | `tooltip/label/padding/h` (Figma name) | **4px** — same naming quirk. Applied as `py-[4px]`. |
| Corner radius | `tooltip/border/radius` | **0** (sharp rectangle, NOT rounded) |
| Tip caret size | (constant) | 16 × 8 px triangle |
| Tip caret fill | (matches surface) | `color/surface/interactive` `#1047A1` |
| Gap between trigger and tooltip | (no token — fluid) | The tip caret IS the gap — its 8px height is the visual breathing room. |

## React + Tailwind

```tsx
import { type FC, type ReactNode, useState, useRef, useEffect } from 'react';

interface TooltipProps {
  content: string;
  tipPosition?: 'bottom' | 'top';   // Figma-verbatim — see TL;DR for what each means
  delayMs?: number;                  // default 500ms; matches OS tooltip conventions
  children: ReactNode;               // the trigger
}

export const Tooltip: FC<TooltipProps> = ({
  content,
  tipPosition = 'top',
  delayMs = 500,
  children,
}) => {
  const [visible, setVisible] = useState(false);
  const timerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  const show = () => {
    if (timerRef.current) clearTimeout(timerRef.current);
    timerRef.current = setTimeout(() => setVisible(true), delayMs);
  };
  const hide = () => {
    if (timerRef.current) clearTimeout(timerRef.current);
    setVisible(false);
  };
  useEffect(() => () => { if (timerRef.current) clearTimeout(timerRef.current); }, []);

  // `tipPosition: bottom` → label appears ABOVE the trigger; tip points down.
  // `tipPosition: top`    → label appears BELOW the trigger; tip points up.
  const above = tipPosition === 'bottom';

  return (
    <span
      className="relative inline-block"
      onMouseEnter={show}
      onMouseLeave={hide}
      onFocus={show}
      onBlur={hide}
    >
      {children}
      {visible && (
        <span
          role="tooltip"
          className={`absolute left-1/2 -translate-x-1/2 z-50 pointer-events-none flex flex-col items-center ${above ? 'bottom-full mb-0' : 'top-full mt-0'}`}
        >
          {above && (
            <span className="bg-surface-interactive text-on-color text-xs leading-4 px-2 py-1 min-w-[120px] max-w-[320px] text-center whitespace-normal">
              {content}
            </span>
          )}
          <span
            className="w-0 h-0"
            style={{
              borderLeft:  '8px solid transparent',
              borderRight: '8px solid transparent',
              [above ? 'borderTop' : 'borderBottom']: '8px solid var(--color-surface-interactive)',
            }}
          />
          {!above && (
            <span className="bg-surface-interactive text-on-color text-xs leading-4 px-2 py-1 min-w-[120px] max-w-[320px] text-center whitespace-normal">
              {content}
            </span>
          )}
        </span>
      )}
    </span>
  );
};
```

Required Tailwind tokens (in `tailwind.config.js`):

```js
colors: {
  'surface-interactive': '#1047A1',
  'on-color':            '#FFFFFF',
},
```

## Standalone HTML / CSS

```html
<style>
  :root {
    --color-surface-interactive: #1047A1;
    --color-text-inverted:       #FFFFFF;
  }

  .tooltip-trigger { position: relative; display: inline-block; }

  .tooltip {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    z-index: 50;
    pointer-events: none;
    display: flex; flex-direction: column; align-items: center;
    opacity: 0;
    transition: opacity 120ms;
  }
  .tooltip-trigger:hover .tooltip,
  .tooltip-trigger:focus-within .tooltip,
  .tooltip.is-visible { opacity: 1; }

  /* `tipPosition: top` (tooltip BELOW the trigger) */
  .tooltip--top    { top: 100%; }
  /* `tipPosition: bottom` (tooltip ABOVE the trigger) */
  .tooltip--bottom { bottom: 100%; }

  .tooltip__label {
    background: var(--color-surface-interactive);
    color: var(--color-text-inverted);
    font-family: 'Inter', system-ui, sans-serif;
    font-size: 12px;
    font-weight: 400;
    line-height: 16px;
    padding: 4px 8px;
    border-radius: 0;             /* sharp corners — Figma verbatim */
    min-width: 120px;             /* keeps short labels from being a tight pill — encourages a horizontal read */
    max-width: 320px;             /* longer labels wrap only after ~50 chars */
    text-align: center;
    white-space: normal;
  }

  /* Tip caret — 16×8 triangle, same brand-blue */
  .tooltip__tip {
    width: 0; height: 0;
    border-left:  8px solid transparent;
    border-right: 8px solid transparent;
  }
  .tooltip--bottom .tooltip__tip { border-top:    8px solid var(--color-surface-interactive); }
  .tooltip--top    .tooltip__tip { border-bottom: 8px solid var(--color-surface-interactive); }
</style>

<!-- `tipPosition: top` — tooltip BELOW the trigger -->
<span class="tooltip-trigger">
  <button aria-describedby="tt-1" type="button">Trigger</button>
  <span class="tooltip tooltip--top" role="tooltip" id="tt-1">
    <span class="tooltip__tip"></span>
    <span class="tooltip__label">Give tooltips meaningful messages</span>
  </span>
</span>

<!-- `tipPosition: bottom` — tooltip ABOVE the trigger -->
<span class="tooltip-trigger">
  <button aria-describedby="tt-2" type="button">Trigger</button>
  <span class="tooltip tooltip--bottom" role="tooltip" id="tt-2">
    <span class="tooltip__label">Give tooltips meaningful messages</span>
    <span class="tooltip__tip"></span>
  </span>
</span>
```

## Composition with other components

- **Icon-only [[button]]** — the canonical use case. The button has no visible text, so the tooltip provides the label. `aria-describedby` links the button to the tooltip so screen readers announce it. The button still needs an `aria-label` for the primary name; the tooltip is supplementary.
- **[[badge]]** with an unclear status code — wrap the badge in a tooltip explaining what the code means ("E-12: device offline").
- **Truncated text in a [[list]] row or [[card]]** — wrap a long-but-clipped text node in a tooltip so the user can see the full value on hover.

## Don'ts

- **Don't put critical information in a tooltip.** Tooltips are non-essential — they don't appear on touch devices, on slow connections, or when the user hasn't hovered. If the user *needs* the text to use the UI, put it in the layout. Tooltips enhance; they don't carry load.
- **Don't make the tooltip clickable.** A tooltip with links or buttons inside it is a [[popover]] — different component, different behaviour (click-to-open, click-outside-to-close). Tooltips disappear the moment the trigger loses hover.
- **Don't use a tooltip on touch devices without a fallback.** Phones don't have hover; long-press triggers a context menu, not your tooltip. For mobile-first flows, prefer inline helper text or replace the tooltip with a `(?)` icon that opens a [[callout]] / dialog.
- **Don't write paragraphs in a tooltip.** 25 words is the hard ceiling — anything longer belongs in a [[callout]] or in-page documentation. The tooltip's 320px max-width is intentional: it forces brevity.
- **Don't add rounded corners.** The Figma spec is `border-radius: 0` — sharp rectangle. The sharpness is part of the visual identity (matches the tip caret's geometry). Rounding the corners makes the tip caret look disconnected.
- **Don't show a tooltip without a delay.** Tooltips that appear the instant the cursor enters the trigger flicker constantly as the user moves the mouse across the UI. Use a ~500ms delay before showing — matches OS-level tooltip conventions.
- **Don't recolour the tooltip surface.** It's always brand-blue `#1047A1`. There's no semantic variant ("warning tooltip" in yellow, "error tooltip" in red) — if you need that, use a [[callout]] inline. Tooltips are visually consistent so the user learns the affordance.
- **Don't use Roboto.** Figma's `copy/caption/font` reads Roboto — placeholder. Web ships Inter. Per [[feedback-figma-font-placeholders]].
