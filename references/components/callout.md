# Callout

> **When to use:** Inline status message tied to a section of the page. Loads with the page (not triggered by an action), placed contextually next to the thing it describes, and **cannot be dismissed**. Use for important information the user needs at the moment they read it — not for transient feedback (use a toast/notification system) or interaction prompts (use a Dialog).
>
> **Figma:** [open in UI Kit](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=7031-931)

> **Notes:**
>
> - Scandit web design system is web-only — there is no Mobile variant to document.
> - **Each variant has its own icon** from the approved set: Info → [`lightbulb`](../../assets/icons/lightbulb.svg), Warning → [`warning_triangle`](../../assets/icons/warning-triangle.svg), Success → [`check_circle_outside`](../../assets/icons/check-circle-outside.svg), Error → [`error_circle`](../../assets/icons/error-circle.svg). Icons are sized 24×24 and inherit colour from a namespace-matched `color/icon/*` token.
> - Layout uses `items: start` — the icon aligns with the **top** of the text, not the centre. This matters when the message wraps to multiple lines (icon stays at the first line, doesn't drift to the middle).
> - **Callouts are not dismissible.** No close button at any state. If the user needs to be able to dismiss the message, the right primitive is a different component (toast / notification banner) — not a Callout.
>
> **Token names** below match the Figma variable names verbatim. Every token is documented in [`../design.md`](../design.md) at the same hex / spec — the catalog and this file are in sync.

## Variants

| Variant | Figma label | When to use | Icon |
|---|---|---|---|
| `info` | Info | Informational note that adds context the user might miss otherwise. No action implied. | [`lightbulb`](../../assets/icons/lightbulb.svg) |
| `success` | Success | Confirms a state the user can rely on (e.g. "All licenses are active", "Sync completed"). | `check_circle_outside` |
| `warning` | Warning | Soft caution — something the user should know but isn't blocked by (e.g. "License expires in 7 days"). | `warning_triangle` |
| `danger` | Error | Failure or critical state requiring attention (e.g. "Failed to load data", "Quota exceeded"). | `error_circle` |

## Sizes

| Size | Padding | Gap (icon ↔ text) | Icon size | Text style | Container corner radius | Border |
|---|---|---|---|---|---|---|
| `md` (Web — only documented at this Figma node) | `spacing/padding/l` (16px) all sides | `spacing/padding/s` (8px) | 24×24 | `body/medium` — 16px Regular, 24px line-height, 0.25px letter-spacing, Inter | `size/cornerRadius/m` (8px) | 1px solid in the variant's `color/border/notification/*` token |

## States

- **default** — The only documented state. Callouts are not interactive and not dismissible; there are no hover, pressed, focused, or disabled states.

## Tokens per variant × state

For each row, the surface fill, border, icon, and text tokens used. All values match design.md verbatim — the catalog and this file are in sync.

| Variant | State | Surface (background) | Border (1px solid) | Icon glyph | Icon colour | Text colour |
|---|---|---|---|---|---|---|
| `info` | `default` | `color/surface/info/soft` (`#D9E7FF`) | `color/border/notification/info` (`#B2D0FF`) | `lightbulb` (24×24) | `color/icon/info` (`#1660D9`) | `color/text/on-color/blue` (`#1047A1`) |
| `warning` | `default` | `color/surface/warning/soft` (`#FFF1CC`) | `color/border/notification/warning` (`#FFE7A6`) | `warning_triangle` (24×24) | `color/icon/warning` (`#F0BD30`) | `color/text/on-color/yellow` (`#4D3800`) |
| `success` | `default` | `color/surface/success/soft` (`#CEF2DC`) | `color/border/notification/success` (`#A1E5BC`) | `check_circle_outside` (24×24) | `color/icon/positive` (`#0D853D`) | `color/text/on-color/green` (`#05612A`) |
| `danger` | `default` | `color/surface/danger/soft` (`#FFD9D9`) | `color/border/notification/error` (`#FFB8B8`) | `error_circle` (24×24) | `color/icon/danger` (`#D92121`) | `color/text/on-color/red` (`#AD1111`) |

## Anatomy

```
┌──────────────────────────────────────────────────────────────────┐  ← container
│ ┌────┐                                                           │     border: 1px color/border/notification/<variant>
│ │ ●  │  This is an in-place notification.                        │     radius: size/cornerRadius/m (8px)
│ └────┘                                                           │     background: color/surface/<variant>/soft
└──────────────────────────────────────────────────────────────────┘     padding: spacing/padding/l (16px) all sides
   ↑     ↑
  24×24  body/medium · color/text/on-color/<hue>
  icon   16/24/0.25 · Inter Regular
  ↑      ↑
  color/icon/<variant>
  ↑
  gap: spacing/padding/s (8px)
  alignment: items-start (icon aligns to top of text, not centre)
```

## Code

### In-repo (React + Tailwind, scandit-web mapping)

```tsx
type CalloutVariant = 'info' | 'warning' | 'success' | 'danger';

import {
  LightbulbIcon, WarningTriangleIcon,
  CheckCircleOutsideIcon, ErrorCircleIcon,
} from '@/icons';

const CALLOUT: Record<CalloutVariant, {
  icon: React.ComponentType<{ className?: string }>;
  surface: string; border: string; iconColor: string; text: string;
}> = {
  info: {
    icon: LightbulbIcon,
    surface: 'bg-surface-soft-info',
    border:  'border-[#B2D0FF]',                  // color/border/notification/info
    iconColor: 'text-surface-full-info',          // color/icon/info — #1660D9
    text:    'text-[#1047A1]',                    // color/text/on-color/blue
  },
  warning: {
    icon: WarningTriangleIcon,
    surface: 'bg-surface-soft-warning',
    border:  'border-[#FFE7A6]',
    iconColor: 'text-surface-full-warning',
    text:    'text-[#4D3800]',
  },
  success: {
    icon: CheckCircleOutsideIcon,
    surface: 'bg-surface-soft-positive',
    border:  'border-[#A1E5BC]',
    iconColor: 'text-surface-full-positive',
    text:    'text-[#05612A]',
  },
  danger: {
    icon: ErrorCircleIcon,
    surface: 'bg-surface-soft-error',
    border:  'border-[#FFB8B8]',
    iconColor: 'text-ntypo-danger',
    text:    'text-[#AD1111]',
  },
};

type CalloutProps = { variant?: CalloutVariant; children: React.ReactNode };

export function Callout({ variant = 'info', children }: CalloutProps) {
  const c = CALLOUT[variant];
  const Icon = c.icon;
  return (
    <div
      role="status"
      className={[
        'flex items-start gap-2 p-4 rounded-lg border',
        'text-base leading-6 tracking-[0.25px]',     // body/medium
        c.surface, c.border, c.text,
      ].join(' ')}
    >
      <Icon className={['size-6 shrink-0', c.iconColor].join(' ')} aria-hidden="true" />
      <p className="flex-1 m-0">{children}</p>
    </div>
  );
}
```

### Standalone artifact (prototype)

```html
<style>
  :root {
    /* Surface — soft pastel fill per variant */
    --color-surface-info-soft:    #D9E7FF;
    --color-surface-warning-soft: #FFF1CC;
    --color-surface-success-soft: #CEF2DC;
    --color-surface-danger-soft:  #FFD9D9;

    /* Border — notification ramp (a tone lighter than the icon colour) */
    --color-border-notification-info:    #B2D0FF;
    --color-border-notification-warning: #FFE7A6;
    --color-border-notification-success: #A1E5BC;
    --color-border-notification-error:   #FFB8B8;

    /* Icon — variant-coloured glyph */
    --color-icon-info:     #1660D9;
    --color-icon-warning:  #F0BD30;
    --color-icon-positive: #0D853D;
    --color-icon-danger:   #D92121;

    /* Text — on-color tokens for legibility on the soft surfaces */
    --color-text-on-color-blue:   #1047A1;
    --color-text-on-color-yellow: #4D3800;
    --color-text-on-color-green:  #05612A;
    --color-text-on-color-red:    #AD1111;
  }

  .callout {
    display: flex; align-items: flex-start; gap: 8px;            /* items-start + spacing/padding/s */
    padding: 16px;                                               /* spacing/padding/l */
    border: 1px solid;
    border-radius: 8px;                                          /* size/cornerRadius/m */
    font-family: Inter, system-ui, sans-serif;
    font-size: 16px; line-height: 24px;                          /* body/medium */
    letter-spacing: 0.25px;
  }
  .callout__icon  { width: 24px; height: 24px; flex-shrink: 0; }
  .callout__text  { flex: 1; margin: 0; }

  .callout--info     { background: var(--color-surface-info-soft);    border-color: var(--color-border-notification-info);    color: var(--color-text-on-color-blue); }
  .callout--info    .callout__icon { color: var(--color-icon-info); }
  .callout--warning  { background: var(--color-surface-warning-soft); border-color: var(--color-border-notification-warning); color: var(--color-text-on-color-yellow); }
  .callout--warning .callout__icon { color: var(--color-icon-warning); }
  .callout--success  { background: var(--color-surface-success-soft); border-color: var(--color-border-notification-success); color: var(--color-text-on-color-green); }
  .callout--success .callout__icon { color: var(--color-icon-positive); }
  .callout--danger   { background: var(--color-surface-danger-soft);  border-color: var(--color-border-notification-error);   color: var(--color-text-on-color-red); }
  .callout--danger  .callout__icon { color: var(--color-icon-danger); }
</style>

<!-- Info — assets/icons/lightbulb.svg -->
<div class="callout callout--info" role="status">
  <span class="callout__icon" aria-hidden="true">
    <svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M10 18C9.45 18 8.97917 17.8042 8.5875 17.4125C8.19583 17.0208 8 16.55 8 16V14.75C7.05 14.1 6.3125 13.2667 5.7875 12.25C5.2625 11.2333 5 10.15 5 9C5 7.05 5.67917 5.39583 7.0375 4.0375C8.39583 2.67917 10.05 2 12 2C13.95 2 15.6042 2.67917 16.9625 4.0375C18.3208 5.39583 19 7.05 19 9C19 10.15 18.7375 11.2292 18.2125 12.2375C17.6875 13.2458 16.95 14.0833 16 14.75V16C16 16.55 15.8042 17.0208 15.4125 17.4125C15.0208 17.8042 14.55 18 14 18H10ZM10 16H14V13.7L14.85 13.1C15.5333 12.6333 16.0625 12.0375 16.4375 11.3125C16.8125 10.5875 17 9.81667 17 9C17 7.61667 16.5125 6.4375 15.5375 5.4625C14.5625 4.4875 13.3833 4 12 4C10.6167 4 9.4375 4.4875 8.4625 5.4625C7.4875 6.4375 7 7.61667 7 9C7 9.81667 7.1875 10.5875 7.5625 11.3125C7.9375 12.0375 8.46667 12.6333 9.15 13.1L10 13.7V16ZM10 22C9.71667 22 9.47917 21.9042 9.2875 21.7125C9.09583 21.5208 9 21.2833 9 21V20H15V21C15 21.2833 14.9042 21.5208 14.7125 21.7125C14.5208 21.9042 14.2833 22 14 22H10Z"/>
    </svg>
  </span>
  <p class="callout__text">This is an in-place notification.</p>
</div>

<!-- Warning — assets/icons/warning-triangle.svg -->
<div class="callout callout--warning" role="status">
  <span class="callout__icon" aria-hidden="true">
    <svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M2.725 21C2.54167 21 2.375 20.9542 2.225 20.8625C2.075 20.7708 1.95833 20.65 1.875 20.5C1.79167 20.35 1.74583 20.1875 1.7375 20.0125C1.72917 19.8375 1.775 19.6667 1.875 19.5L11.125 3.5C11.225 3.33333 11.3542 3.20833 11.5125 3.125C11.6708 3.04167 11.8333 3 12 3C12.1667 3 12.3292 3.04167 12.4875 3.125C12.6458 3.20833 12.775 3.33333 12.875 3.5L22.125 19.5C22.225 19.6667 22.2708 19.8375 22.2625 20.0125C22.2542 20.1875 22.2083 20.35 22.125 20.5C22.0417 20.65 21.925 20.7708 21.775 20.8625C21.625 20.9542 21.4583 21 21.275 21H2.725ZM4.45 19H19.55L12 6L4.45 19ZM12 18C12.2833 18 12.5208 17.9042 12.7125 17.7125C12.9042 17.5208 13 17.2833 13 17C13 16.7167 12.9042 16.4792 12.7125 16.2875C12.5208 16.0958 12.2833 16 12 16C11.7167 16 11.4792 16.0958 11.2875 16.2875C11.0958 16.4792 11 16.7167 11 17C11 17.2833 11.0958 17.5208 11.2875 17.7125C11.4792 17.9042 11.7167 18 12 18ZM12 15C12.2833 15 12.5208 14.9042 12.7125 14.7125C12.9042 14.5208 13 14.2833 13 14V11C13 10.7167 12.9042 10.4792 12.7125 10.2875C12.5208 10.0958 12.2833 10 12 10C11.7167 10 11.4792 10.0958 11.2875 10.2875C11.0958 10.4792 11 10.7167 11 11V14C11 14.2833 11.0958 14.5208 11.2875 14.7125C11.4792 14.9042 11.7167 15 12 15Z"/>
    </svg>
  </span>
  <p class="callout__text">License expires in 7 days. Renew before it lapses.</p>
</div>

<!-- Success — assets/icons/check-circle-outside.svg (Figma's Success callout uses the "outside" variant, distinct from check_circle) -->
<div class="callout callout--success" role="status">
  <span class="callout__icon" aria-hidden="true">
    <svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 22C10.6167 22 9.31667 21.7375 8.1 21.2125C6.88333 20.6875 5.825 19.975 4.925 19.075C4.025 18.175 3.3125 17.1167 2.7875 15.9C2.2625 14.6833 2 13.3833 2 12C2 10.6167 2.2625 9.31667 2.7875 8.1C3.3125 6.88333 4.025 5.825 4.925 4.925C5.825 4.025 6.88333 3.3125 8.1 2.7875C9.31667 2.2625 10.6167 2 12 2C12.8 2 13.5792 2.09167 14.3375 2.275C15.0958 2.45833 15.825 2.725 16.525 3.075C16.775 3.20833 16.9375 3.40833 17.0125 3.675C17.0875 3.94167 17.0417 4.19167 16.875 4.425C16.7083 4.65833 16.4875 4.80833 16.2125 4.875C15.9375 4.94167 15.6667 4.90833 15.4 4.775C14.8667 4.525 14.3125 4.33333 13.7375 4.2C13.1625 4.06667 12.5833 4 12 4C9.78333 4 7.89583 4.77917 6.3375 6.3375C4.77917 7.89583 4 9.78333 4 12C4 14.2167 4.77917 16.1042 6.3375 17.6625C7.89583 19.2208 9.78333 20 12 20C14.2167 20 16.1042 19.2208 17.6625 17.6625C19.2208 16.1042 20 14.2167 20 12C20 11.8667 19.9958 11.7375 19.9875 11.6125C19.9792 11.4875 19.9667 11.3583 19.95 11.225C19.9167 10.9417 19.9708 10.6708 20.1125 10.4125C20.2542 10.1542 20.4667 9.98333 20.75 9.9C21.0167 9.81667 21.2667 9.84167 21.5 9.975C21.7333 10.1083 21.8667 10.3083 21.9 10.575C21.9333 10.8083 21.9583 11.0417 21.975 11.275C21.9917 11.5083 22 11.75 22 12C22 13.3833 21.7375 14.6833 21.2125 15.9C20.6875 17.1167 19.975 18.175 19.075 19.075C18.175 19.975 17.1167 20.6875 15.9 21.2125C14.6833 21.7375 13.3833 22 12 22ZM10.6 13.8L19.9 4.475C20.0833 4.29167 20.3125 4.19583 20.5875 4.1875C20.8625 4.17917 21.1 4.275 21.3 4.475C21.4833 4.65833 21.575 4.89167 21.575 5.175C21.575 5.45833 21.4833 5.69167 21.3 5.875L11.3 15.9C11.1 16.1 10.8667 16.2 10.6 16.2C10.3333 16.2 10.1 16.1 9.9 15.9L7.05 13.05C6.86667 12.8667 6.775 12.6333 6.775 12.35C6.775 12.0667 6.86667 11.8333 7.05 11.65C7.23333 11.4667 7.46667 11.375 7.75 11.375C8.03333 11.375 8.26667 11.4667 8.45 11.65L10.6 13.8Z"/>
    </svg>
  </span>
  <p class="callout__text">Sync completed. 1,248 records updated.</p>
</div>

<!-- Danger — assets/icons/error-circle.svg -->
<div class="callout callout--danger" role="status">
  <span class="callout__icon" aria-hidden="true">
    <svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 17C12.2833 17 12.5208 16.9042 12.7125 16.7125C12.9042 16.5208 13 16.2833 13 16C13 15.7167 12.9042 15.4792 12.7125 15.2875C12.5208 15.0958 12.2833 15 12 15C11.7167 15 11.4792 15.0958 11.2875 15.2875C11.0958 15.4792 11 15.7167 11 16C11 16.2833 11.0958 16.5208 11.2875 16.7125C11.4792 16.9042 11.7167 17 12 17ZM12 13C12.2833 13 12.5208 12.9042 12.7125 12.7125C12.9042 12.5208 13 12.2833 13 12V8C13 7.71667 12.9042 7.47917 12.7125 7.2875C12.5208 7.09583 12.2833 7 12 7C11.7167 7 11.4792 7.09583 11.2875 7.2875C11.0958 7.47917 11 7.71667 11 8V12C11 12.2833 11.0958 12.5208 11.2875 12.7125C11.4792 12.9042 11.7167 13 12 13ZM12 22C10.6167 22 9.31667 21.7375 8.1 21.2125C6.88333 20.6875 5.825 19.975 4.925 19.075C4.025 18.175 3.3125 17.1167 2.7875 15.9C2.2625 14.6833 2 13.3833 2 12C2 10.6167 2.2625 9.31667 2.7875 8.1C3.3125 6.88333 4.025 5.825 4.925 4.925C5.825 4.025 6.88333 3.3125 8.1 2.7875C9.31667 2.2625 10.6167 2 12 2C13.3833 2 14.6833 2.2625 15.9 2.7875C17.1167 3.3125 18.175 4.025 19.075 4.925C19.975 5.825 20.6875 6.88333 21.2125 8.1C21.7375 9.31667 22 10.6167 22 12C22 13.3833 21.7375 14.6833 21.2125 15.9C20.6875 17.1167 19.975 18.175 19.075 19.075C18.175 19.975 17.1167 20.6875 15.9 21.2125C14.6833 21.7375 13.3833 22 12 22ZM12 20C14.2333 20 16.125 19.225 17.675 17.675C19.225 16.125 20 14.2333 20 12C20 9.76667 19.225 7.875 17.675 6.325C16.125 4.775 14.2333 4 12 4C9.76667 4 7.875 4.775 6.325 6.325C4.775 7.875 4 9.76667 4 12C4 14.2333 4.775 16.125 6.325 17.675C7.875 19.225 9.76667 20 12 20Z"/>
    </svg>
  </span>
  <p class="callout__text">Quota exceeded. Some scans were not recorded.</p>
</div>
```

## Don'ts

- **Don't add a dismiss (X) button.** Callouts are intentionally persistent — they're tied to the section and shouldn't disappear on click. If the message needs to be dismissible, reach for a different component (toast, notification banner).
- **Don't centre-align the icon.** Use `items-start` so the icon sits at the top of the text. When the message wraps to multiple lines, `items-center` makes the icon drift to the middle and breaks the visual scan.
- **Don't reach across namespaces.** A success callout uses `color/surface/success/soft` + `color/icon/positive` + `color/text/on-color/green`. Don't try to use `color/text/positive` (used for inline body text) on a green surface — the contrast is wrong.
- **Don't substitute a different icon** for each variant. The icon glyphs are documented per variant (`lightbulb` for info, `warning_triangle` for warning, `check_circle_outside` for success, `error_circle` for danger). Mixing them up breaks the system's "you can recognise the type at a glance" contract.
- **Don't use a Callout for an action prompt** ("Click here to fix"). Callouts are read-only status. If the user needs to act, place a Button or Link **inside** the callout — or use a different component (Dialog, Banner) if the action is the point.
- **Don't render Callouts in dense data tables.** They're a section-level affordance, not a row-level one. For row-level status, use a Badge in a Status column.
- **Don't shrink the icon under 24×24.** The callout is a section-level affordance — scaling the icon down makes it look like an inline pill and breaks the hierarchy. If you need a tighter status indicator, use a Badge instead.
