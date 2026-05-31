# Sidebar

> **When to use:** Primary left-rail navigation on `background/brand`. Fixed at `lg` and above.
>
> **Figma:** [open in UI Kit](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=2934-5545)


> **Notes:** Sits on `background/brand` (`#141F2E`). Sidebar item anatomy: `h-12 px-3 mx-3 rounded-lg gap-3`, icon `24×24`, text `16px` with `tracking-[0.25px]` (body/medium). Selected items use 600/semibold; all other states use 400/regular.


## Variants

| Variant | Usage |
|---|---|
| `default` | TODO |
| `collapsed` | TODO |

## Sizes

| Size | Height | Font size | Padding | Icon size |
|---|---|---|---|---|
| `default` | TODO | TODO | TODO | TODO |

## States

- **default** — TODO
- **scrolled** — TODO

## Tokens per variant × state

The load-bearing reference. For each variant + state, name the exact semantic token used on each property. Cross-namespace usage is a violation — keep `surface/*` in the surface column, `text/*` in text, etc.

| Variant | State | Surface | Text | Border | Icon | Notes |
|---|---|---|---|---|---|---|
| `default` | `default` | TODO | TODO | TODO | TODO | |
| `default` | `scrolled` | TODO | TODO | TODO | TODO | |
| `collapsed` | `default` | TODO | TODO | TODO | TODO | |
| `collapsed` | `scrolled` | TODO | TODO | TODO | TODO | |

## Code

### In-repo (React + Tailwind, scandit-web mapping)

```tsx
// TODO: import from src/components/ if a shared atom already exists.
// Otherwise, the markup below uses production Tailwind classes.
```

### Standalone artifact (prototype)

```html
<!-- TODO: same component using semantic CSS variables declared in :root.
     Use --surface-*, --text-*, --border-*, --icon-* variables so the
     prototype can port to any Scandit product without renaming. -->
```

## Don'ts

- TODO: anti-patterns specific to this component (e.g. for Button: never two primaries in one view; for Dialog: never use for non-blocking messages — use Callout).
