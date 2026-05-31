# Dialog

> **When to use:** Modal interruption requiring confirmation, input, or critical info. Use **only when blocking is justified** — the user must respond before continuing with the surrounding task. For non-blocking messages, use [Callout](callout.md). For low-emphasis status, use [Badge](badge.md).
>
> **Figma:** [open in UI Kit](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=8705-1226)

> **Notes:**
>
> - **Only one variant is documented at this Figma node** — `default`. The legacy design.md YAML listed `alert / confirmation / fullscreen` as separate variants and `[md, lg, xl]` as a size axis; those were dropped to match Figma 1:1.
> - **Width is fixed at 676px** (overrides the legacy `dialog: 704px` spacing token — design.md updated to match). Height is content-driven; the Figma frame shows 601px as one example. Centered horizontally and offset vertically from the viewport top.
> - **Header has three positions** — a leading back-affordance (`chevron_left`), a centered title with an optional inline `content_copy` icon, and a trailing dismiss-affordance (`close`). All three icons are 24×24.
> - **⚠ Shadow divergence from design.md's elevation rule:** The Dialog uses Figma's **Elevation/3**, a directional two-layer drop shadow with vertical offsets. design.md § Elevation says *"shadows are subtle and ambient, never directional"* — Dialog is an explicit exception (per the user's "Figma wins" call on this divergence). The directional shadow gives the modal an extra sense of separation from the underlying scrim. **Only Dialog uses this shadow** — other elevated surfaces (cards, popovers, dropdowns) still follow the pure-vertical ambient rule.
> - **`color/surface/default/inverse`** is a Figma alias that maps to the same hex as design.md's `color/surface/default` (`#FFFFFF`). Reuse the existing `surface/default` token in code; the "inverse" suffix is Figma-side only.
>
> **Token names** below match the Figma variable names verbatim. Every token is documented in design.md unless noted as a Dialog-specific exception.

## Variants

| Variant | Usage |
|---|---|
| `default` | The only documented variant. A blocking modal with a 3-element header (back · centered title · close) and a flexible content slot below. |

## Sizes

No size axis — the Dialog is fixed at **676px wide**, with height driven by content. If a wider or taller layout is needed, that's a different pattern (consider full-page navigation rather than a modal).

## States

- **open** — Visible, blocking. Surface fully rendered with directional shadow. Background scrim covers the rest of the viewport.
- **closing** — Not drawn in Figma but documented as a real animation state. The dialog should fade and translate slightly down (`animate-fadeOut` reversed) as it dismisses; the scrim fades concurrently. Implementation detail — the visual baseline is identical to `open` during the transition.

## Anatomy

```
   ┌──────────────────────────────────────────────────────────────────────┐  width: 676px
   │                                                                      │  bg: color/surface/default (#FFFFFF)
   │  ┌────────────────────────────────────────────────────────────────┐  │  border: 1px color/border/secondary
   │  │  ‹            Title that has 2 lines       ⎘            ✕      │  │  radius: size/cornerRadius/xl (16px)
   │  │                of text                                         │  │  padding: spacing/padding/xl (24px) all sides
   │  └────────────────────────────────────────────────────────────────┘  │  shadow: Elevation/3 (directional — Dialog-specific exception)
   │     ↑              ↑                          ↑              ↑       │
   │     chevron_left   title (centered)           content_copy   close   │  header: flex row, items-center, justify-between
   │     24×24          heading/medium 20px/600    24×24          24×24   │  3 elements: left · (center title + inline copy) · right
   │     color/icon/    line-height 1.0            color/icon/    color/  │  All icons 24×24, color/icon/primary or /secondary
   │     primary        color/text/primary         secondary      icon/primary
   │                                                                      │
   │                          gap (header ↔ slot)                         │  gap: spacing/stack/l (16px)
   │                                                                      │
   │  ┌────────────────────────────────────────────────────────────────┐  │
   │  │                                                                │  │  content slot
   │  │                       Slot                                     │  │  flex: 1 (flexes to fill remaining height)
   │  │                       Replace with local slot component        │  │  padding: 8px, inner radius: 12px
   │  │                                                                │  │  content is consumer-provided
   │  │                                                                │  │
   │  └────────────────────────────────────────────────────────────────┘  │
   │                                                                      │
   └──────────────────────────────────────────────────────────────────────┘
```

## Tokens

| Property | Token | Value |
|---|---|---|
| Surface | `color/surface/default` (Figma alias: `color/surface/default/inverse`) | `#FFFFFF` |
| Border (1px solid) | `color/border/secondary` | `#C7CFD6` |
| Border radius | `size/cornerRadius/xl` | `16px` |
| Padding (all sides) | `spacing/padding/xl` | `24px` |
| Gap (header ↔ slot) | `spacing/stack/l` | `16px` |
| Title type | `heading/medium` | 20px / 600 / Inter / lineHeight 1.0 / letterSpacing 0 |
| Title colour | `color/text/primary` | `#16191C` |
| Header icons (chevron_left, close) | `color/icon/primary` | `#16191C` |
| Inline title icon (content_copy) | `color/icon/secondary` | `#6C7680` |
| Shadow (Dialog-specific) | Figma `Elevation/3` — directional 2-layer | `0 1px 3px 0 rgba(0,0,0,0.20), 0 4px 8px 3px rgba(0,0,0,0.15)` |
| Background scrim (overlay behind the dialog) | `color/background/overlay dark` per design.md § Background | `rgba(0,0,0,0.25)` or `0.40` |
| Width | `spacing/dialog` | `676px` |

## Header icon glyphs

All from the approved icon set, sized **24×24**, inheriting colour via `currentColor`:

- **Leading — back:** [`chevron_left`](../../assets/icons/chevron-left.svg) · `color/icon/primary`. Hides if the dialog has no back-navigation step.
- **Title-inline — copy:** [`content_copy`](../../assets/icons/content-copy.svg) · `color/icon/secondary`. Optional; only render when the title is something the user might want to copy to clipboard (license key, identifier, etc.).
- **Trailing — close:** [`close`](../../assets/icons/close.svg) · `color/icon/primary`. Dismisses the dialog. Always present unless the dialog is **non-dismissible** (rare — only for blocking errors where the user must take an action).

## Code

### In-repo (React + Tailwind, scandit-web mapping)

```tsx
import { ChevronLeftIcon, ContentCopyIcon, CloseIcon } from '@/icons';

type DialogProps = {
  open: boolean;
  onClose: () => void;
  onBack?: () => void;             // omits the chevron_left if not provided
  title: string;
  onCopyTitle?: () => void;        // omits the content_copy if not provided
  children: React.ReactNode;
};

export function Dialog({ open, onClose, onBack, title, onCopyTitle, children }: DialogProps) {
  if (!open) return null;
  return (
    <div
      role="dialog"
      aria-modal="true"
      aria-labelledby="dialog-title"
      className="fixed inset-0 z-50 flex items-start justify-center bg-overlay-dark"
      onMouseDown={(e) => { if (e.target === e.currentTarget) onClose(); }}
    >
      <div
        className={[
          'w-[676px] mt-[211px] bg-white rounded-2xl border border-configurator-gray-20',
          'p-6 flex flex-col items-center gap-4',
          // Dialog-specific shadow — directional, distinct from the rest of the elevation scale
          'shadow-[0_1px_3px_0_rgba(0,0,0,0.20),0_4px_8px_3px_rgba(0,0,0,0.15)]',
        ].join(' ')}
      >
        {/* Header — three positions: left · (center title + copy) · right */}
        <div className="flex w-full items-center justify-between">
          {onBack ? (
            <button type="button" onClick={onBack} aria-label="Back" className="text-ntypo-primary">
              <ChevronLeftIcon className="size-6" />
            </button>
          ) : (
            <span aria-hidden="true" className="size-6" />
          )}

          <div className="flex items-center gap-2">
            <h2
              id="dialog-title"
              className="text-xl font-semibold text-ntypo-primary text-center leading-none w-40"
            >
              {title}
            </h2>
            {onCopyTitle && (
              <button type="button" onClick={onCopyTitle} aria-label="Copy title" className="text-ntypo-secondary">
                <ContentCopyIcon className="size-6" />
              </button>
            )}
          </div>

          <button type="button" onClick={onClose} aria-label="Close" className="text-ntypo-primary">
            <CloseIcon className="size-6" />
          </button>
        </div>

        {/* Content slot — fills remaining vertical space */}
        <div className="flex-1 w-full">{children}</div>
      </div>
    </div>
  );
}
```

### Standalone artifact (prototype)

```html
<style>
  :root {
    --color-surface-default:       #FFFFFF;   /* Figma alias: color/surface/default/inverse */
    --color-border-secondary:      #C7CFD6;
    --color-text-primary:          #16191C;
    --color-icon-primary:          #16191C;
    --color-icon-secondary:        #6C7680;
    --color-background-overlay:    rgba(0, 0, 0, 0.40);   /* color/background/overlay dark */
    /* Dialog-specific directional shadow — exception to design.md's pure-vertical rule */
    --shadow-dialog: 0 1px 3px 0 rgba(0, 0, 0, 0.20), 0 4px 8px 3px rgba(0, 0, 0, 0.15);
  }

  .dialog-overlay {
    position: fixed; inset: 0;
    background: var(--color-background-overlay);
    display: flex; justify-content: center; align-items: flex-start;
    z-index: 50;
  }

  .dialog {
    width: 676px;                               /* spacing/dialog */
    margin-top: 211px;
    background: var(--color-surface-default);
    border: 1px solid var(--color-border-secondary);
    border-radius: 16px;                        /* size/cornerRadius/xl */
    padding: 24px;                              /* spacing/padding/xl */
    display: flex; flex-direction: column; align-items: center;
    gap: 16px;                                  /* spacing/stack/l */
    box-shadow: var(--shadow-dialog);
    font-family: Inter, system-ui, sans-serif;
    color: var(--color-text-primary);
  }

  .dialog__header {
    display: flex; align-items: center; justify-content: space-between;
    width: 100%;
  }
  .dialog__title-wrap { display: flex; align-items: center; gap: 8px; }
  .dialog__title {
    font-size: 20px; font-weight: 600; line-height: 1.0;   /* heading/medium */
    text-align: center;
    color: var(--color-text-primary);
    margin: 0;
    width: 160px;                                          /* per Figma — wraps to two lines if needed */
  }

  .dialog__icon-btn {
    width: 24px; height: 24px;
    display: inline-grid; place-items: center;
    background: transparent; border: 0; padding: 0;
    color: var(--color-icon-primary);
    cursor: pointer;
  }
  .dialog__icon-btn--secondary { color: var(--color-icon-secondary); }

  .dialog__slot {
    flex: 1; width: 100%;
  }
</style>

<div class="dialog-overlay" role="dialog" aria-modal="true" aria-labelledby="dlg-title">
  <div class="dialog">
    <div class="dialog__header">
      <!-- Leading: chevron_left from assets/icons/chevron-left.svg -->
      <button class="dialog__icon-btn" type="button" aria-label="Back">
        <svg viewBox="0 0 24 24" fill="currentColor" width="24" height="24" aria-hidden="true">
          <path d="M14 18 8 12l6-6 1.4 1.4L10.8 12l4.6 4.6L14 18Z"/>
        </svg>
      </button>

      <!-- Center: title + optional content_copy -->
      <div class="dialog__title-wrap">
        <h2 id="dlg-title" class="dialog__title">Title that has 2 lines of text</h2>
        <!-- assets/icons/content-copy.svg (optional — only when the title is copyable) -->
        <button class="dialog__icon-btn dialog__icon-btn--secondary" type="button" aria-label="Copy title">
          <svg viewBox="0 0 24 24" fill="currentColor" width="24" height="24" aria-hidden="true">
            <path d="M9 18q-.825 0-1.412-.587Q7 16.825 7 16V4q0-.825.588-1.412Q8.175 2 9 2h9q.825 0 1.413.588Q20 3.175 20 4v12q0 .825-.587 1.413Q18.825 18 18 18H9Zm0-2h9V4H9v12Zm-4 6q-.825 0-1.412-.587Q3 20.825 3 20V6h2v14h11v2H5Zm4-6V4v12Z"/>
          </svg>
        </button>
      </div>

      <!-- Trailing: close from assets/icons/close.svg -->
      <button class="dialog__icon-btn" type="button" aria-label="Close">
        <svg viewBox="0 0 24 24" fill="currentColor" width="24" height="24" aria-hidden="true">
          <path d="M12 13.4 7.1 18.3q-.275.275-.7.275-.425 0-.7-.275-.275-.275-.275-.7 0-.425.275-.7L10.6 12 5.7 7.1q-.275-.275-.275-.7 0-.425.275-.7.275-.275.7-.275.425 0 .7.275L12 10.6l4.9-4.9q.275-.275.7-.275.425 0 .7.275.275.275.275.7 0 .425-.275.7L13.4 12l4.9 4.9q.275.275.275.7 0 .425-.275.7-.275.275-.7.275-.425 0-.7-.275L12 13.4Z"/>
      </button>
    </div>

    <div class="dialog__slot">
      <!-- Consumer content goes here -->
    </div>
  </div>
</div>
```

> The SVG paths shown above are placeholders for the structure — when rendering for real, **read the exact path from the matching `assets/icons/<name>.svg` file** and inline it byte-for-byte. Don't paraphrase or compress the path data.

## Don'ts

- **Don't use a Dialog for non-blocking messages.** A Dialog blocks the rest of the UI until the user takes an action. For status/notification that the user can dismiss or ignore, use [Callout](callout.md) (in-page) or a toast (transient).
- **Don't omit the dismiss affordance unless absolutely necessary.** The `close` (×) button gives the user a clear exit. Removing it traps them — use only for blocking errors that genuinely require an explicit decision (e.g. "Pick a workspace before continuing").
- **Don't stack Dialogs.** Two modals at once make the user lose context — they can't tell which they're interacting with. Sequence them: dismiss one, then open the next.
- **Don't put long-form content inside a Dialog.** If the content exceeds ~2 viewport heights, it's not a Dialog — it's a page. Either trim or navigate.
- **Don't change the directional shadow** to design.md's pure-vertical `shadow-xl`. The Dialog is an explicit exception (Figma render is canonical). Pure-vertical shadows are for cards / popovers / dropdowns — the modal tier visually separates itself from the scrim with directional offset.
- **Don't widen the Dialog beyond 676px** without a discussion. Wider modals start to feel like pages — and at that point the right pattern is probably a route, not an overlay.
- **Don't put the title's `content_copy` icon next to a title that isn't copyable.** It's an action affordance — if there's nothing to copy, omit the icon entirely. Putting it next to a regular title misleads the user into thinking the title text is interactive.
- **Don't omit `role="dialog"` and `aria-modal="true"`** on the container, and **`aria-labelledby="<title-id>"`** so screen readers announce the dialog correctly. The focus also needs to trap inside the dialog while it's open and return to the trigger element on close.
- **Don't reuse the Dialog shadow on other surfaces.** It's directional — outside the modal context, that style breaks the system's "elevation is ambient" rule.
