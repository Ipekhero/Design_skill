# Search

> **TL;DR**
> - A single **searchbar** — pill-shaped (`cornerradius/round` 999px), 48px tall (`comp-height/2xl`), fluid width, gray surface (`surface/formcomp/default` `#F3F5F8`).
> - **One variant only.** "Search with suggestions" is a Combobox/Autocomplete pattern (search wrapped in a [[menu]] — handled by composition, not a separate variant). "Search with filters" is a composition with adjacent [[chip]]s or [[button]]s. Neither lives in this component.
> - **Five states** — `default`, `hover`, `selected`, `filled`, `disabled`. State naming follows Figma verbatim (Figma calls the focused-with-caret state `Selected` — kept as-is so future Figma changes flow through cleanly; this is the same state most other libraries call `focused`).
> - **The border colour for `selected` is near-black** (`border/interactive` `#16191C`), NOT brand blue. `border/interactive` is catalogued as dark in the web design system — distinct from `surface/interactive` which IS brand blue. Same call as [[dropdown]]'s open state.
> - **Trailing clear button** (close_small icon button) appears only when `filled` or `selected` — when there's something to clear OR the input is being actively used.
> - **Hover** is a translucent overlay (`surface/formcomp/hover` `rgba(0,0,0,0.05)`), not a surface swap.
> - **Disabled is not in Figma** but every product search input needs it (e.g. search field grayed out when no dataset is loaded or while a long search is in flight). Documented here using the same disabled treatment as other form controls.

Figma source:
- [Searchbar (4 state variants)](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=7343-20283)

## When to use

| Use Search when… | Use something else when… |
|---|---|
| The user needs to **filter a list by typing a free-text query** (search a dataset, filter records, find a doc) | The choice is from a **small finite set of options** → use a [[dropdown]] |
| The query targets a **single field** with no autocomplete, just text-match | The query needs **autocomplete with suggestions appearing as you type** → wrap the search in a [[menu]] (Combobox pattern) — outside this component |
| The search input is the **primary affordance** of the page or panel | The search is **one of several adjacent fields** in a form → use the standard [[text-field]] (when documented) |
| You need a quick **client-side filter** of an already-loaded list | The search needs **scoping chips** ("All", "Unread", "Archive") next to it → compose with [[chip]]s separately; the search itself is still this component |

## Anatomy

```
┌────────────────────────────────────────────────────────────┐  ← 48px pill, gray surface
│                                                            │     border: 1px secondary
│   [🔍]   Search                                            │     padding: 0 12px, gap: 8px
│                                                            │     leading icon · placeholder
└────────────────────────────────────────────────────────────┘

  Default (no value, no focus)

┌════════════════════════════════════════════════════════════┐  ← 2px border-interactive
│                                                            │     dark near-black ring
│   [🔍]   Search                                      [✕]   │     blinking caret + clear button
│           |                                                │     visible
└════════════════════════════════════════════════════════════┘

  Selected (Figma's "focused")

┌────────────────────────────────────────────────────────────┐
│                                                            │
│   [🔍]   Acme Corp                                   [✕]   │     filled — primary text colour
│                                                            │     clear button visible
└────────────────────────────────────────────────────────────┘

  Filled (has a value, not focused)
```

- **Container** — 48px tall, fluid width (Figma frames it at 329px but real implementations fill their container). Pill (`cornerradius/round`), `surface/formcomp/default` background. 1px border.
- **Leading icon** — `search` from `icons.md`, 20×20, `icon/primary` (`#16191C`).
- **Input** — `body/medium` (16/400/24/0.25) text. Placeholder colour `text/secondary` (`#525A61`); filled value `text/primary` (`#16191C`).
- **Trailing clear button** — `close_small` icon (20×20 inside a 24×24 icon-button wrapper with 8px padding and `cornerradius/s` 6px). Only rendered when `selected` or `filled`. Clicking it clears the input and returns the bar to `default`.

## States

| State | Surface | Border | Leading icon | Placeholder | Caret | Clear button | Notes |
|---|---|---|---|---|---|---|---|
| `default` | `surface/formcomp/default` (`#F3F5F8`) | **1px** `border/secondary` (`#C7CFD6`) | `icon/primary` | `text/secondary` "Search" | — | hidden | Resting state. |
| `hover` | `surface/formcomp/default` + overlay `surface/formcomp/hover` (`rgba(0,0,0,0.05)`) | **1px** `border/secondary` (unchanged) | `icon/primary` | `text/secondary` "Search" | — | hidden | Hover is an overlay tint, NOT a surface swap. The 1px gray border stays. |
| `selected` | `surface/formcomp/default` (unchanged) | **2px** `border/interactive` (`#16191C` — near-black, NOT brand blue) | `icon/primary` | `text/secondary` "Search" | blinking, `text/primary` | visible | Figma name — input has keyboard focus + caret. Border thickens to 2px and darkens to near-black. Clear button appears even before the user types (so they can quickly bail). |
| `filled` | `surface/formcomp/default` (unchanged) | **1px** `border/secondary` (unchanged) | `icon/primary` | — (replaced by value) | — (only when focused) | visible | Has a value but no focus. Value text in `text/primary`. Clear button stays visible until the value is cleared. |
| `disabled` | `surface/disabled` (`#E1E7ED`) | none (or 1px `border/secondary` if you want a visible edge — match your form's disabled-input convention) | `icon/disabled` (`#ACB6BF`) | `text/disabled` (`#ACB6BF`) "Search" | — | hidden | Not in Figma — added for product use. Mirrors the disabled treatment from other form controls. Cursor `not-allowed`. |

## React + Tailwind

```tsx
import { type FC, useState } from 'react';

interface SearchProps {
  value?: string;
  defaultValue?: string;
  placeholder?: string;
  disabled?: boolean;
  onChange?: (value: string) => void;
  onClear?: () => void;
  ariaLabel?: string;
  className?: string;
}

export const Search: FC<SearchProps> = ({
  value: controlledValue,
  defaultValue = '',
  placeholder = 'Search',
  disabled = false,
  onChange,
  onClear,
  ariaLabel = 'Search',
  className,
}) => {
  const [internal, setInternal] = useState(defaultValue);
  const isControlled = controlledValue !== undefined;
  const value = isControlled ? controlledValue : internal;

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (!isControlled) setInternal(e.target.value);
    onChange?.(e.target.value);
  };

  const handleClear = () => {
    if (!isControlled) setInternal('');
    onClear?.();
    onChange?.('');
  };

  const hasValue = value.length > 0;

  return (
    <div
      className={`flex items-center gap-2 h-12 px-3 rounded-full transition-colors
        ${disabled
          ? 'bg-surface-disabled cursor-not-allowed border border-transparent'
          : 'bg-surface-formcomp border border-border-secondary hover:bg-surface-formcomp-hover focus-within:bg-surface-formcomp focus-within:border-2 focus-within:border-border-interactive focus-within:px-[11px]'}
        ${className ?? ''}`}
    >
      <SearchIcon className={`size-5 shrink-0 ${disabled ? 'text-icon-disabled' : 'text-icon-primary'}`} />
      <input
        type="search"
        value={value}
        onChange={handleChange}
        disabled={disabled}
        placeholder={placeholder}
        aria-label={ariaLabel}
        className="flex-1 min-w-0 bg-transparent border-0 outline-none text-base leading-6 tracking-[0.25px] text-primary placeholder:text-secondary disabled:placeholder:text-disabled disabled:cursor-not-allowed"
      />
      {hasValue && !disabled && (
        <button
          type="button"
          onClick={handleClear}
          aria-label="Clear search"
          className="shrink-0 size-6 p-1 rounded-md hover:bg-surface-hover text-icon-primary cursor-pointer"
        >
          <CloseSmallIcon className="size-5" />
        </button>
      )}
    </div>
  );
};
```

Required Tailwind tokens (in `tailwind.config.js`):

```js
colors: {
  'surface-formcomp':        '#F3F5F8',
  'surface-formcomp-hover':  'rgba(0, 0, 0, 0.05)',   /* overlay tint */
  'surface-disabled':        '#E1E7ED',
  'surface-hover':           '#F3F5F8',
  'border-secondary':        '#C7CFD6',
  'border-interactive':      '#16191C',
  'text-primary':            '#16191C',
  'text-secondary':          '#525A61',
  'text-disabled':           '#ACB6BF',
  'icon-primary':            '#16191C',
  'icon-disabled':           '#ACB6BF',
},
```

> **Note on the focused `px-[11px]` trick** — when the border grows from 1px to 2px in the focused state, the inner content jumps 1px. Compensating padding (12px → 11px) keeps the children visually still. Test that this lines up at your zoom level; if not, use `outline` with negative offset instead of `border` width changes.

## Standalone HTML / CSS

```html
<style>
  :root {
    --color-surface-formcomp-default:  #F3F5F8;
    --color-surface-formcomp-hover:    rgba(0, 0, 0, 0.05);
    --color-surface-hover:             #F3F5F8;
    --color-surface-disabled:          #E1E7ED;
    --color-border-secondary:          #C7CFD6;
    --color-border-interactive:        #16191C;
    --color-text-primary:              #16191C;
    --color-text-secondary:            #525A61;
    --color-text-disabled:             #ACB6BF;
    --color-icon-primary:              #16191C;
    --color-icon-disabled:             #ACB6BF;

    --size-comp-height-2xl:    48px;
    --size-cornerradius-round: 999px;
    --size-cornerradius-s:     6px;
    --spacing-padding-s:       8px;
    --spacing-padding-m:       12px;
  }

  .search {
    position: relative;
    display: flex;
    align-items: center;
    gap: var(--spacing-padding-s);
    height: var(--size-comp-height-2xl);
    padding: 0 var(--spacing-padding-m);
    background: var(--color-surface-formcomp-default);
    border: 1px solid var(--color-border-secondary);
    border-radius: var(--size-cornerradius-round);
    transition: background-color 80ms, border-color 80ms, padding 80ms;
    box-sizing: border-box;
    font-family: 'Inter', system-ui, sans-serif;
  }

  /* hover overlay — translucent black on top of the default surface */
  .search:not(.search--selected):not(.search--disabled):hover,
  .search.is-hover {
    background-image: linear-gradient(var(--color-surface-formcomp-hover), var(--color-surface-formcomp-hover));
  }

  /* selected (Figma name for "focused with caret") — 2px near-black border */
  .search:focus-within:not(.search--disabled),
  .search.is-selected {
    border: 2px solid var(--color-border-interactive);
    padding: 0 11px;                              /* compensate the +1px border so children stay still */
  }

  /* disabled */
  .search--disabled {
    background: var(--color-surface-disabled);
    border-color: transparent;
    cursor: not-allowed;
  }

  .search__icon {
    flex-shrink: 0;
    width: 20px; height: 20px;
    color: var(--color-icon-primary);
  }
  .search--disabled .search__icon { color: var(--color-icon-disabled); }

  .search__input {
    flex: 1 1 0;
    min-width: 0;
    background: transparent;
    border: 0; outline: 0;
    font-size: 16px;
    font-weight: 400;
    line-height: 24px;
    letter-spacing: 0.25px;
    color: var(--color-text-primary);
    font-family: inherit;
  }
  .search__input::placeholder { color: var(--color-text-secondary); }
  .search--disabled .search__input { cursor: not-allowed; }
  .search--disabled .search__input::placeholder { color: var(--color-text-disabled); }

  /* Suppress the browser's NATIVE clear button on type="search" — Safari/Chrome render their own
     "×" by default, which collides with our close-small button. Firefox doesn't render one. */
  .search__input::-webkit-search-cancel-button,
  .search__input::-webkit-search-decoration {
    -webkit-appearance: none;
    appearance: none;
    display: none;
  }

  .search__clear {
    flex-shrink: 0;
    width: 24px; height: 24px;
    padding: 2px;
    background: transparent;
    border: 0;
    border-radius: var(--size-cornerradius-s);
    color: var(--color-icon-primary);
    cursor: pointer;
    display: flex; align-items: center; justify-content: center;
  }
  .search__clear:hover { background: var(--color-surface-hover); }
  .search__clear svg { width: 20px; height: 20px; display: block; }
</style>

<!-- Default -->
<div class="search">
  <svg class="search__icon" viewBox="0 0 24 24"><use href="#i-search"/></svg>
  <input type="search" class="search__input" placeholder="Search">
</div>

<!-- Filled (with clear button) -->
<div class="search">
  <svg class="search__icon" viewBox="0 0 24 24"><use href="#i-search"/></svg>
  <input type="search" class="search__input" value="Acme Corp">
  <button type="button" class="search__clear" aria-label="Clear">
    <svg viewBox="0 0 24 24"><use href="#i-close-small"/></svg>
  </button>
</div>
```

## Composition with other components

- **Search + suggestions (Combobox)** — wrap the search in a [[menu]] that opens below as the user types. The menu items mirror typed input against the dataset. Live filtering is implemented in product code, not in this component.
- **Search + filter chips** — render a row of [[chip]]s (selectable variant) above or beside the search to narrow scope. The search and the chips are *independent* controls that the page combines into a query.
- **Search inside a [[card]]** — a common dashboard pattern. The search fills the card's content area, chips below scope the filter, list below shows results.

## Don'ts

- **Don't use Figma's `surface/interactive` as the focused border colour.** The catalog's `border/interactive` is intentionally near-black `#16191C` (matches [[dropdown]]). `surface/interactive` (which IS brand blue) is for filled action surfaces, not for input borders. Don't conflate them.
- **Don't hide the clear button when the input is focused but empty.** Figma's `Selected` state shows the clear button even with no value — it's a quick-bail affordance. The button just doesn't do anything when there's nothing to clear (or it dismisses focus).
- **Don't recolour the search-icon to `icon/secondary` for "muted" feel.** The catalog uses `icon/primary` (#16191C). The dim look comes from the input being unfocused and the placeholder being `text/secondary` — the leading icon stays at full primary contrast.
- **Don't put the search inside a form group with its own label.** The placeholder + leading icon already say "this is for searching." If you need a label *above* the input (e.g. in a sidebar filter panel), use a small `label/medium` heading separately — don't wrap with a `<label>` that obscures the input's affordance.
- **Don't trigger the search on every keystroke without debouncing.** This is a product-code rule, not a component rule, but ship-blocking — undebounced searches spam the backend. Debounce to ~250ms typing-idle.
- **Don't use the search to launch actions.** If the user types "Open settings" and hits enter, that's a command palette, not a search. Build a different component (a `command` palette) for actionable autocomplete.
- **Don't hand-type the search/close-small SVG paths.** Copy verbatim from `assets/icons/search.svg` and `assets/icons/close-small.svg`. Per [[feedback-icon-paths-from-assets]].
- **Don't forget to suppress the browser's native search clear button.** When you use `<input type="search">`, Safari and Chrome render their own little "×" inside the field that collides with our custom `close-small` button — two clears in a row. Hide it with `input::-webkit-search-cancel-button { -webkit-appearance: none; display: none; }`. Tailwind users can add this in their global stylesheet. If you skip `type="search"` and use `type="text"` instead, you lose the semantic role for screen readers — suppressing the native button is the right fix.
- **Don't use Roboto.** Figma's `body/medium/font` reads Roboto — placeholder. Web ships Inter. Per [[feedback-figma-font-placeholders]].
