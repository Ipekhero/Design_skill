# Text Field

> **When to use:** Free-text input for forms. Default to single-line; use textarea variant for multi-line.
>
> **Figma:** [open in UI Kit](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=5294-1106)


> **Notes:** Radius `rounded` (4px). Focused border uses `surface/interactive`; error border uses `border/danger` with helper text in `text/danger`.


## Variants

| Variant | Usage |
|---|---|
| `default` | TODO |
| `with-label` | TODO |
| `with-helper` | TODO |
| `with-icon` | TODO |
| `textarea` | TODO |

## Sizes

| Size | Height | Font size | Padding | Icon size |
|---|---|---|---|---|
| `sm` | TODO | TODO | TODO | TODO |
| `md` | TODO | TODO | TODO | TODO |
| `lg` | TODO | TODO | TODO | TODO |

## States

- **default** — TODO
- **hover** — TODO
- **focused** — TODO
- **filled** — TODO
- **error** — TODO
- **disabled** — TODO
- **read-only** — TODO

## Tokens per variant × state

The load-bearing reference. For each variant + state, name the exact semantic token used on each property. Cross-namespace usage is a violation — keep `surface/*` in the surface column, `text/*` in text, etc.

| Variant | State | Surface | Text | Border | Icon | Notes |
|---|---|---|---|---|---|---|
| `default` | `default` | TODO | TODO | TODO | TODO | |
| `default` | `hover` | TODO | TODO | TODO | TODO | |
| `default` | `focused` | TODO | TODO | TODO | TODO | |
| `default` | `filled` | TODO | TODO | TODO | TODO | |
| `default` | `error` | TODO | TODO | TODO | TODO | |
| `default` | `disabled` | TODO | TODO | TODO | TODO | |
| `default` | `read-only` | TODO | TODO | TODO | TODO | |
| `with-label` | `default` | TODO | TODO | TODO | TODO | |
| `with-label` | `hover` | TODO | TODO | TODO | TODO | |
| `with-label` | `focused` | TODO | TODO | TODO | TODO | |
| `with-label` | `filled` | TODO | TODO | TODO | TODO | |
| `with-label` | `error` | TODO | TODO | TODO | TODO | |
| `with-label` | `disabled` | TODO | TODO | TODO | TODO | |
| `with-label` | `read-only` | TODO | TODO | TODO | TODO | |
| `with-helper` | `default` | TODO | TODO | TODO | TODO | |
| `with-helper` | `hover` | TODO | TODO | TODO | TODO | |
| `with-helper` | `focused` | TODO | TODO | TODO | TODO | |
| `with-helper` | `filled` | TODO | TODO | TODO | TODO | |
| `with-helper` | `error` | TODO | TODO | TODO | TODO | |
| `with-helper` | `disabled` | TODO | TODO | TODO | TODO | |
| `with-helper` | `read-only` | TODO | TODO | TODO | TODO | |
| `with-icon` | `default` | TODO | TODO | TODO | TODO | |
| `with-icon` | `hover` | TODO | TODO | TODO | TODO | |
| `with-icon` | `focused` | TODO | TODO | TODO | TODO | |
| `with-icon` | `filled` | TODO | TODO | TODO | TODO | |
| `with-icon` | `error` | TODO | TODO | TODO | TODO | |
| `with-icon` | `disabled` | TODO | TODO | TODO | TODO | |
| `with-icon` | `read-only` | TODO | TODO | TODO | TODO | |
| `textarea` | `default` | TODO | TODO | TODO | TODO | |
| `textarea` | `hover` | TODO | TODO | TODO | TODO | |
| `textarea` | `focused` | TODO | TODO | TODO | TODO | |
| `textarea` | `filled` | TODO | TODO | TODO | TODO | |
| `textarea` | `error` | TODO | TODO | TODO | TODO | |
| `textarea` | `disabled` | TODO | TODO | TODO | TODO | |
| `textarea` | `read-only` | TODO | TODO | TODO | TODO | |

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
