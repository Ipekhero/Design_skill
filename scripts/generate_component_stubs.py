#!/usr/bin/env python3
"""
Generate per-component reference stubs for the Scandit design skill.

Reads the variant/size/state enums from references/design.md's YAML frontmatter
(components: block) and writes one stub file per component to references/components/.
Each stub follows the same template so Claude can find token-state bindings, sizes,
and code examples in a predictable place.

Re-run safely — files are overwritten only if --force is passed.
"""

from __future__ import annotations
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "references" / "components"
FIGMA_BASE = "https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit"

# Each entry: (yaml-key, Title, "when to use" blurb, figma node-id, variants, sizes, states, extra_notes)
# Variant blurbs are short; user will refine.
COMPONENTS = [
    ("accordion", "Accordion",
     "Disclose sections of content one at a time to reduce vertical density.",
     "2934-5760",
     ["default"],
     ["md"],
     ["collapsed", "expanded", "hover", "focused", "disabled"],
     None),

    ("badge", "Badge",
     'Tag a status or count next to a label (e.g. "New", "3 issues").',
     "4832-11808",
     ["neutral", "info", "success", "warning", "danger", "brand", "new"],
     ["sm", "md"],
     ["default"],
     None),

    # branding intentionally not modelled as a component — the Scandit logo
    # is a static SVG asset at assets/scandit-logo.svg. See design.md § Brand assets.

    ("button", "Button",
     "The primary affordance for an action. One primary button per view; ghost for secondary navigation.",
     "2803-4942",
     ["primary", "secondary", "ghost", "destructive"],
     ["sm", "md", "lg"],
     ["default", "hover", "focused", "pressed", "disabled", "loading"],
     "**Hierarchy rule:** one **primary** button per view. Reach for **ghost** for low-emphasis or icon-only actions, **destructive** only when the action is irreversible (delete, remove)."),

    ("breadcrumbs", "Breadcrumbs",
     "Show the user's location in a multi-level page hierarchy.",
     "2934-6290",
     ["default"],
     ["md"],
     ["default", "hover", "current", "truncated"],
     None),

    ("callout", "Callout",
     "Inline status message tied to a section (info, success, warning, danger).",
     "7031-931",
     ["info", "success", "warning", "danger", "neutral"],
     ["md"],
     ["default", "dismissible"],
     "Surface uses the `*/soft` step of the matching ramp; border uses `border/notification/*`; icon uses `icon/{info|positive|warning|danger}`."),

    ("card", "Card",
     "Group related content into a contained surface — the dashboard's main composition unit.",
     "2803-4467",
     ["default", "interactive", "elevated", "bordered"],
     ["sm", "md", "lg"],
     ["default", "hover", "pressed", "selected", "disabled"],
     "Default radius `rounded-2xl` (16px). Padding `24px` keeps dense tables breathable. `interactive` variant gets hover/pressed treatment; `elevated` adds `shadow-md`."),

    ("checkbox", "Checkbox",
     "Multi-select binary input. Use in forms, filters, and table-row selection.",
     "4788-86",
     ["default"],
     ["sm", "md"],
     ["unchecked", "checked", "indeterminate", "hover", "focused", "disabled", "error"],
     None),

    ("chip", "Chip",
     "Compact tag for features, filters, or selectable options on cards.",
     "4397-3636",
     ["neutral", "filter", "choice", "action"],
     ["sm", "md"],
     ["default", "hover", "focused", "selected", "disabled", "removable"],
     "Always `rounded-full` (pill shape)."),

    ("dialog", "Dialog",
     "Modal interruption requiring confirmation, input, or critical info. Use only when blocking is justified.",
     "2934-5695",
     ["default", "alert", "confirmation", "fullscreen"],
     ["md", "lg", "xl"],
     ["open", "closing"],
     "Standard width: `w-dialog` (704px). Large: `w-dialogXl` (749px). Scrim uses `background/overlay dark` or `background/overlay darker`. `alert` variant uses a danger border or icon to signal severity."),

    ("dropdown", "Dropdown",
     "Single- or multi-select picker for a finite, pre-defined option list.",
     "2934-5921",
     ["single-select", "multi-select", "with-search"],
     ["sm", "md", "lg"],
     ["default", "hover", "focused", "open", "filled", "disabled", "error"],
     "Trailing chevron uses `icon/secondary`. Open menu sits on `surface/default` with `shadow-lg`."),

    ("link", "Link",
     "Inline navigation to another page or external resource. Distinct from buttons.",
     "2934-5429",
     ["default", "inline", "standalone", "external"],
     ["sm", "md", "lg"],
     ["default", "hover", "focused", "pressed", "visited", "disabled"],
     "Use `text/info/*` for color (link != button)."),

    ("list", "List",
     "Ordered enumeration of items with optional leading / trailing affordances.",
     "3152-150",
     ["default", "with-actions", "with-icons", "interactive"],
     ["sm", "md", "lg"],
     ["default", "hover", "focused", "selected", "disabled"],
     None),

    ("menu", "Menu",
     'Floating action list triggered by a control (kebab, "more", contextual right-click).',
     "5992-5045",
     ["default", "with-icons", "with-shortcuts", "contextual"],
     ["md"],
     ["default", "hover", "focused", "selected", "disabled"],
     "Sits on `surface/default` with `shadow-lg`. `with-shortcuts` aligns shortcut hints right with `text/secondary`."),

    ("progress", "Progress",
     "Communicate loading, completion percentage, or a long-running task.",
     "4995-7653",
     ["linear", "circular"],
     ["sm", "md", "lg"],
     ["indeterminate", "determinate", "complete", "error"],
     None),

    ("radio", "Radio",
     "Single-select from 2–5 mutually exclusive options. Prefer Dropdown beyond that.",
     "4788-85",
     ["default"],
     ["sm", "md"],
     ["unchecked", "checked", "hover", "focused", "disabled", "error"],
     None),

    ("search", "Search",
     "Input field for querying a dataset. Pair with suggestions or filters where relevant.",
     "4052-3806",
     ["default", "with-suggestions", "with-filters"],
     ["sm", "md", "lg"],
     ["default", "hover", "focused", "filled", "disabled"],
     "Leading `search` icon uses `icon/secondary`."),

    ("sidebar", "Sidebar",
     "Primary left-rail navigation on `background/brand`. Fixed at `lg` and above.",
     "2934-5545",
     ["default", "collapsed"],
     ["default"],
     ["default", "scrolled"],
     "Sits on `background/brand` (`#141F2E`). Sidebar item anatomy: `h-12 px-3 mx-3 rounded-lg gap-3`, icon `24×24`, text `16px` with `tracking-[0.25px]` (body/medium). Selected items use 600/semibold; all other states use 400/regular."),

    ("text-field", "Text Field",
     "Free-text input for forms. Default to single-line; use textarea variant for multi-line.",
     "5294-1106",
     ["default", "with-label", "with-helper", "with-icon", "textarea"],
     ["sm", "md", "lg"],
     ["default", "hover", "focused", "filled", "error", "disabled", "read-only"],
     "Radius `rounded` (4px). Focused border uses `surface/interactive`; error border uses `border/danger` with helper text in `text/danger`."),

    ("toggle", "Toggle",
     "Immediate on/off binary control. Use when the change takes effect instantly, not for forms.",
     "2934-5542",
     ["default"],
     ["sm", "md"],
     ["off", "on", "hover", "focused", "disabled"],
     "Use **Toggle** when the change applies immediately. Use **Checkbox** inside forms where the change applies on submit."),

    ("tree-view", "Tree view",
     "Hierarchical navigation through nested data (folders, org structures, scan-result trees).",
     "6639-1940",
     ["default", "with-icons", "with-actions"],
     ["md"],
     ["default", "hover", "focused", "selected", "expanded", "collapsed", "disabled"],
     None),
]


TEMPLATE = """# {title}

> **When to use:** {when_to_use}
>
> **Figma:** [open in UI Kit]({figma_url})

{extra_notes_block}
> **Token naming convention:** All token references below use the **exact Figma variable names** (e.g. `color/border/secondary`, `size/cornerRadius/m`, `heading/large`, `spacing/padding/s`). Every token referenced here is documented in [`../design.md`](../design.md). Where Figma and design.md spell things differently, the Figma name is canonical.

## Variants

| Variant | Usage |
|---|---|
{variants_rows}

## Sizes

| Size | Height | Title type (`heading/*` or `body/*`) | Padding (`spacing/padding/*`) | Icon size | Container radius (`size/cornerRadius/*`) |
|---|---|---|---|---|---|
{sizes_rows}

## States

{states_list}

## Tokens per variant × state

The load-bearing reference. For each variant + state, name the exact **Figma variable** used on each property (e.g. `color/surface/interactive`, `color/text/on-color/blue`). Cross-namespace usage is a violation — keep `color/surface/*` in the surface column, `color/text/*` in text, etc.

| Variant | State | Surface (`color/surface/*` or `color/background/*`) | Text (`color/text/*`) | Border (`color/border/*`) | Icon (`color/icon/*`) | Notes |
|---|---|---|---|---|---|---|
{token_matrix_rows}

## Code

### In-repo (React + Tailwind, scandit-web mapping)

```tsx
// TODO: import from src/components/ if a shared atom already exists.
// Otherwise, the markup below uses production Tailwind classes that map
// to the Figma tokens above (see references/design.md for the Tailwind
// equivalents of each token).
```

### Standalone artifact (prototype)

```html
<!-- TODO: same component using semantic CSS variables declared in :root.
     Name the variables after the Figma tokens (--color-surface-default,
     --color-text-primary, etc.) so the prototype can port to any
     Scandit product without renaming. -->
```

## Don'ts

- TODO: anti-patterns specific to this component (e.g. for Button: never two primaries in one view; for Dialog: never use for non-blocking messages — use Callout).
"""


def make_variants_rows(variants: list[str]) -> str:
    return "\n".join(f"| `{v}` | TODO |" for v in variants)


def make_sizes_rows(sizes: list[str]) -> str:
    return "\n".join(f"| `{s}` | TODO | TODO | TODO | TODO |" for s in sizes)


def make_states_list(states: list[str]) -> str:
    return "\n".join(f"- **{s}** — TODO" for s in states)


def make_token_matrix_rows(variants: list[str], states: list[str]) -> str:
    # Reduce noise: emit one row per (variant, state) for the most-likely
    # interactive states. The user can drop or extend rows as needed.
    rows = []
    for v in variants:
        for s in states:
            rows.append(f"| `{v}` | `{s}` | TODO | TODO | TODO | TODO | |")
    return "\n".join(rows)


def render(comp) -> str:
    key, title, when_to_use, node_id, variants, sizes, states, extra = comp
    figma_url = f"{FIGMA_BASE}?node-id={node_id}"
    extra_block = f"\n> **Notes:** {extra}\n\n" if extra else "\n"
    return TEMPLATE.format(
        title=title,
        when_to_use=when_to_use,
        figma_url=figma_url,
        extra_notes_block=extra_block,
        variants_rows=make_variants_rows(variants),
        sizes_rows=make_sizes_rows(sizes),
        states_list=make_states_list(states),
        token_matrix_rows=make_token_matrix_rows(variants, states),
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true",
                    help="Overwrite existing files (otherwise skip).")
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    written, skipped = 0, 0
    for comp in COMPONENTS:
        key = comp[0]
        path = OUT_DIR / f"{key}.md"
        if path.exists() and not args.force:
            skipped += 1
            print(f"skip   {path.relative_to(ROOT)} (exists)")
            continue
        path.write_text(render(comp))
        written += 1
        print(f"write  {path.relative_to(ROOT)}")
    print(f"\nDone. {written} written, {skipped} skipped.")


if __name__ == "__main__":
    main()
