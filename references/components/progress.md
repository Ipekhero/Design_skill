# Progress

> **TL;DR**
> - Two visually distinct variants that do **different jobs**:
>   - **`linear`** — a horizontal pill bar that communicates *how much* of a known total is done. Always **determinate** (0–100% value). Renders in **success green** (`surface/success/full` `#0D853D`) because semantically "filling up the bar" reads as a positive accumulation.
>   - **`circular`** — a 24×24 ring that communicates *that something is happening*. Can be **determinate** (with a known value, drawn as an arc filling the ring) OR **indeterminate** (a small arc spinning around the ring forever, used when the total isn't known). Renders in **neutral dark** (`icon/primary` `#16191C`) because semantically it reads as "task in progress" — not necessarily a positive accumulation.
> - **No sizes axis.** Linear is one height (8px bar in a 16px container, fluid width). Circular is one size (24×24).
> - **Linear has an optional value label** — right-aligned `body/small` text reading "XX %", default on.
> - **Circular has an optional stop affordance** — a small dark filled square in the center, signalling "tap to interrupt". Default off.
> - **Colour split is intentional** — keep linear green and circular dark. Don't recolour them to "match" — and don't introduce semantic colour variants (blue / red / etc.). The progress bar exists to show *value*, not status; status belongs in a [[callout]].
> - **Indeterminate is circular-only.** Linear progress with an unknown total is a non-sensical UI — if you don't know the total, use a circular spinner.

Figma source:
- [Linear progress (12/25/40/50/75/85/100% sample states)](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=6614-679)
- [Circular progress (25%, 25% stop, 75%, 75% stop, 100%)](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=4995-7636)

## When to use

| Use Progress when… | Use something else when… |
|---|---|
| You have a **task with a known % done** (file upload, batch processing, multi-step wizard) → `linear` | The task is instant — don't show progress at all. A spinner that flashes for 200ms is just visual noise. |
| You want to show that **something is loading right now**, value unknown → `circular indeterminate` | You're communicating a *result* (success / failure) — use a [[callout]] |
| The user can **cancel the in-flight task** → `circular` with `stoppable` | The progress is part of a multi-step wizard nav — use the wizard's step indicator, not a progress bar |
| You're showing **completion towards a goal** (license usage, quota fill, gamification) → `linear` | The "progress" is qualitative (e.g. "ready / setup needed / not started") — that's a [[badge]] |

## Variants

| Variant | Container | Track | Progress fill | Optional extras |
|---|---|---|---|---|
| `linear` | Height `comp-height/s` (16px). Padding 0. Fluid width (bar grows with container). | `surface/disabled` `#E1E7ED` (gray). Pill (`cornerradius/round` 999px). Height 8px (`comp-height/2xs`). | `surface/success/full` `#0D853D` (green). Pill. Width = `value%` of track. | Right-aligned `body/small` label "XX %" (40px wide, 8px gap from bar). |
| `circular` | 24×24 square. | 20×20 circle (2px inset on all sides), stroke 2px `surface/neutral/subdued` `#C7CFD6` (gray), no fill. | Same 20×20 circle, stroke 2px `icon/primary` `#16191C` (dark), drawn as an arc via `stroke-dasharray` or rotating in indeterminate mode. | Center stop button — 6×6 `icon/primary` (#16191C) filled square, `cornerradius/2xs` (1px), positioned 9px from top-left of the 24×24 container. |

## Modes

| Mode | Applies to | Behaviour |
|---|---|---|
| `determinate` | `linear` (always) · `circular` (when a `value` is provided) | Bar / arc reflects a 0–100% value. No animation. |
| `indeterminate` | `circular` only | A small ~25% arc rotates 360° continuously (1.4s linear infinite). Indicates "something is happening, total unknown." |

## Anatomy

### Linear

```
┌──────────────────────────────────────────────────────┐  16px tall container
│                                                      │  display: flex; gap: 8px; align-items: center
│  ╭─────────────────────╮ ╭─────────────────╮         │
│  │█████░░░░░░░░░░░░░░░░│ │░░░░░░░░░░░░░░░░░│  XX %   │  ← bar (8px tall, pill, fluid width)
│  ╰─────────────────────╯ ╰─────────────────╯         │     filled portion = success/full · track = disabled
│                                                      │     label (optional, 40px wide, body/small, right-aligned)
└──────────────────────────────────────────────────────┘
```

### Circular

```
        ╭─────────────────╮              24×24 outer container
        │     ╭──────╮    │              20×20 ring inside (2px inset)
        │   ╭╯      ╰╮    │              stroke: 2px gray track + 2px dark arc
        │  │   ╔══╗  │    │              stoppable: 6×6 dark filled square center
        │  │   ║▓▓║  │    │              (rounded 1px, indicates "tap to stop")
        │   ╰╮      ╭╯    │
        │     ╰──────╯    │
        ╰─────────────────╯
```

## Tokens

### Linear

| Property | Token | Value |
|---|---|---|
| Container height | `size/comp-height/s` | `16px` |
| Bar height | `size/comp-height/2xs` | `8px` |
| Bar corner radius | `size/cornerradius/round` | `999px` |
| Track surface | `color/surface/disabled` | `#E1E7ED` |
| Fill surface | `color/surface/success/full` | `#0D853D` |
| Gap (bar ↔ label) | `spacing/padding/s` | `8px` |
| Label typography | `body/small` (14/400/20/0.25) · `color/text/primary` `#16191C` | |
| Label width | fixed `44px` (no-wrap so "100 %" fits on one line), right-aligned, `body/small` | |

### Circular

| Property | Token | Value |
|---|---|---|
| Container size | n/a (raw `24px`) | `24×24` |
| Ring outer diameter | n/a (raw `20px`) | `20px` (2px inset) |
| Ring stroke | `size/border/wide` | `2px` |
| Track stroke colour | `color/surface/neutral/subdued` (Figma label: `default/subdued` — same hex) | `#C7CFD6` |
| Arc stroke colour | `color/icon/primary` | `#16191C` |
| Stop button size | n/a | `6×6` |
| Stop button colour | `color/icon/primary` | `#16191C` |
| Stop button corner radius | `size/cornerradius/2xs` | `1px` |
| Indeterminate animation | rotation `360deg` linear infinite | duration `1.4s` |

## React + Tailwind

```tsx
import { type FC } from 'react';

interface LinearProgressProps {
  value: number;              // 0–100
  showValue?: boolean;        // default true
  className?: string;
  ariaLabel?: string;
}

export const LinearProgress: FC<LinearProgressProps> = ({
  value,
  showValue = true,
  className,
  ariaLabel = 'Progress',
}) => {
  const pct = Math.max(0, Math.min(100, value));
  return (
    <div
      className={`flex items-center gap-2 h-4 ${className ?? ''}`}
      role="progressbar"
      aria-valuenow={pct}
      aria-valuemin={0}
      aria-valuemax={100}
      aria-label={ariaLabel}
    >
      <div className="flex-1 h-2 bg-surface-disabled rounded-full overflow-hidden">
        <div
          className="h-2 bg-success-full rounded-full transition-[width] duration-200"
          style={{ width: `${pct}%` }}
        />
      </div>
      {showValue && (
        <span className="w-11 text-right text-sm leading-5 tracking-[0.25px] text-primary tabular-nums whitespace-nowrap">
          {Math.round(pct)} %
        </span>
      )}
    </div>
  );
};

interface CircularProgressProps {
  value?: number;             // 0–100. Omit for indeterminate.
  indeterminate?: boolean;    // default false (only valid when value is omitted)
  stoppable?: boolean;        // default false. Renders the center stop square.
  onStop?: () => void;        // optional callback when the stop button is clicked
  ariaLabel?: string;
}

export const CircularProgress: FC<CircularProgressProps> = ({
  value,
  indeterminate = value === undefined,
  stoppable = false,
  onStop,
  ariaLabel = 'Loading',
}) => {
  const r = 9;                              // 20px ring → r=9, stroke=2, fits inside 24×24
  const circ = 2 * Math.PI * r;             // ≈ 56.55
  const pct = value !== undefined ? Math.max(0, Math.min(100, value)) : 25;
  const dashoffset = indeterminate ? circ * 0.75 : circ - (circ * pct) / 100;

  return (
    <div className="relative size-6" role="progressbar" aria-valuenow={indeterminate ? undefined : pct} aria-valuemin={0} aria-valuemax={100} aria-label={ariaLabel}>
      <svg className="absolute inset-0 size-full" viewBox="0 0 24 24">
        {/* Track */}
        <circle cx="12" cy="12" r={r} stroke="var(--color-surface-neutral-subdued)" strokeWidth="2" fill="none" />
        {/* Arc */}
        <circle
          cx="12" cy="12" r={r}
          stroke="var(--color-icon-primary)" strokeWidth="2" fill="none"
          strokeDasharray={circ}
          strokeDashoffset={dashoffset}
          strokeLinecap="round"
          transform="rotate(-90 12 12)"
          className={indeterminate ? 'animate-progress-spin origin-center' : 'transition-[stroke-dashoffset] duration-200'}
        />
      </svg>
      {stoppable && (
        <button
          type="button"
          onClick={onStop}
          aria-label="Stop"
          className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 size-1.5 bg-icon-primary rounded-[1px] cursor-pointer p-0 border-0"
        />
      )}
    </div>
  );
};
```

Required Tailwind tokens + keyframes (in `tailwind.config.js`):

```js
theme: {
  extend: {
    colors: {
      'surface-disabled':         '#E1E7ED',
      'surface-neutral-subdued':  '#C7CFD6',
      'success-full':             '#0D853D',
      'icon-primary':             '#16191C',
      'text-primary':             '#16191C',
    },
    keyframes: {
      'progress-spin': {
        '0%':   { transform: 'rotate(0deg)' },
        '100%': { transform: 'rotate(360deg)' },
      },
    },
    animation: {
      'progress-spin': 'progress-spin 1.4s linear infinite',
    },
  },
},
```

## Standalone HTML / CSS

```html
<style>
  :root {
    --color-surface-default:          #FFFFFF;
    --color-surface-disabled:         #E1E7ED;
    --color-surface-neutral-subdued:  #C7CFD6;
    --color-surface-success-full:     #0D853D;
    --color-icon-primary:             #16191C;
    --color-text-primary:             #16191C;

    --size-cornerradius-2xs:   1px;
    --size-cornerradius-round: 999px;
    --size-comp-height-s:      16px;
    --size-comp-height-2xs:    8px;
    --spacing-padding-s:       8px;
  }

  /* ─── Linear ─── */
  .progress-linear {
    display: flex;
    align-items: center;
    gap: var(--spacing-padding-s);
    height: var(--size-comp-height-s);
  }
  .progress-linear__track {
    flex: 1 1 0;
    min-width: 0;
    height: var(--size-comp-height-2xs);
    background: var(--color-surface-disabled);
    border-radius: var(--size-cornerradius-round);
    overflow: hidden;
  }
  .progress-linear__fill {
    height: 100%;
    background: var(--color-surface-success-full);
    border-radius: var(--size-cornerradius-round);
    transition: width 200ms;
  }
  .progress-linear__label {
    width: 44px;
    text-align: right;
    font-family: 'Inter', system-ui, sans-serif;
    font-size: 14px;
    line-height: 20px;
    letter-spacing: 0.25px;
    color: var(--color-text-primary);
    font-variant-numeric: tabular-nums;
    flex-shrink: 0;
    white-space: nowrap;
  }

  /* ─── Circular ─── */
  .progress-circular {
    position: relative;
    width: 24px;
    height: 24px;
    display: inline-block;
  }
  .progress-circular__svg { width: 24px; height: 24px; display: block; }
  .progress-circular__track {
    fill: none;
    stroke: var(--color-surface-neutral-subdued);
    stroke-width: 2;
  }
  .progress-circular__arc {
    fill: none;
    stroke: var(--color-icon-primary);
    stroke-width: 2;
    stroke-linecap: round;
    transform: rotate(-90deg);
    transform-origin: 50% 50%;
    transition: stroke-dashoffset 200ms;
  }
  .progress-circular--indeterminate .progress-circular__arc {
    animation: progress-spin 1.4s linear infinite;
    transform-origin: 50% 50%;
  }
  @keyframes progress-spin {
    0%   { transform: rotate(-90deg); }
    100% { transform: rotate(270deg); }
  }
  .progress-circular__stop {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 6px;
    height: 6px;
    transform: translate(-50%, -50%);
    background: var(--color-icon-primary);
    border-radius: var(--size-cornerradius-2xs);
    border: 0;
    padding: 0;
    cursor: pointer;
  }
</style>

<!-- LINEAR · determinate 65% -->
<div class="progress-linear" role="progressbar" aria-valuenow="65" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-linear__track">
    <div class="progress-linear__fill" style="width: 65%;"></div>
  </div>
  <span class="progress-linear__label">65 %</span>
</div>

<!-- CIRCULAR · determinate 75% with stop -->
<div class="progress-circular" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <svg class="progress-circular__svg" viewBox="0 0 24 24">
    <circle class="progress-circular__track" cx="12" cy="12" r="9"/>
    <circle class="progress-circular__arc" cx="12" cy="12" r="9"
            stroke-dasharray="56.55" stroke-dashoffset="14.14"/>
  </svg>
  <button class="progress-circular__stop" aria-label="Stop"></button>
</div>

<!-- CIRCULAR · indeterminate -->
<div class="progress-circular progress-circular--indeterminate" role="progressbar" aria-label="Loading">
  <svg class="progress-circular__svg" viewBox="0 0 24 24">
    <circle class="progress-circular__track" cx="12" cy="12" r="9"/>
    <circle class="progress-circular__arc" cx="12" cy="12" r="9"
            stroke-dasharray="56.55" stroke-dashoffset="42.41"/>
  </svg>
</div>
```

**Math note** — for a 20px ring (2px inset on each side of 24×24), r = 9, circumference = 2 · π · 9 ≈ 56.55. To show N%, set `stroke-dashoffset = 56.55 - (56.55 × N / 100)`. The `rotate(-90deg)` ensures the arc starts at 12 o'clock and grows clockwise.

## Don'ts

- **Don't use the linear bar for indeterminate progress.** If you don't know the total, use the circular indeterminate spinner — a linear bar that's animated but never fills is misleading. (The classic Material indeterminate linear bar is intentionally not included here.)
- **Don't recolour the circular arc to match the linear green.** The colour split is deliberate — linear's green reads as "value accumulating positively", circular's dark reads as "task in progress, neutral status." Recolouring them to match collapses the semantic distinction.
- **Don't add an `error` colour to the progress bar.** A bar that turns red mid-fill is a confusing way to communicate failure. If a task fails, dismiss the progress and show an [[callout]] with the failure reason. (The progress bar exists to show *value*, not status.)
- **Don't introduce semantic colour variants (blue / red).** The linear bar is always `surface/success/full` green. If you find yourself reaching for a different colour, the answer is almost always a different component — a [[callout]] for status, a [[badge]] for state. Keep this one bar one colour.
- **Don't show the progress label below 1%.** "0 %" reads as broken or empty. Hide the label when value < 1 (or render "starting…").
- **Don't fix the linear bar to 300px.** Figma renders it at 300px because Figma frames need a width — real implementations should let it fill its container. Set a sensible `max-width` only when the bar would otherwise stretch absurdly wide.
- **Don't draw the circular ring at any size other than 24px.** This is the only size Figma defines. If you need a bigger spinner (loading screens, hero loaders), that's a *different* component — bring it up before extending this one.
- **Don't make the stop button area smaller than 24×24 effective hit target.** Even though the visual mark is 6×6, the underlying `<button>` should occupy the full 24×24 ring (use absolute positioning + transparent padding) so it's tap-friendly on mobile. Per WCAG SC 2.5.5.
- **Don't use the indeterminate spinner for fast operations.** If the task completes in under ~400ms, the flash of the spinner is more disruptive than helpful. Defer rendering by 200–300ms; if the task finishes inside that window, don't render anything.
- **Don't use Roboto.** Figma's `body/small/font` reads Roboto — placeholder. Web ships Inter. Per [[feedback-figma-font-placeholders]].
