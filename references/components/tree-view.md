# Tree View

> **TL;DR**
> - A **vertical list of nested rows** for hierarchical data — folders, scan-result groupings, org structures, settings categories.
> - Two kinds of rows: **expandable parents** (have a chevron, can be opened to reveal children) and **non-expandable leaves** (no chevron, occupy the chevron's 24px reserve so titles align across the tree).
> - **One variant only.** "Tree with icons" / "tree with actions" aren't in Figma — extend the component when product needs them.
> - **Three interactive states (Figma-aligned)**: `default`, `hover`, `selected`. `selected` only applies to leaves (parents are navigation, not selection). No `focused` (uses `:focus-visible` outline). `expanded` is a *data property*, not a state.
> - **`selected` is TEXT-ONLY** — font-weight 600 SemiBold + `text/info/default` `#1660D9` (info blue), no surface tint, no border highlight. This is **intentional and distinct from [[menu]] / [[dropdown]] / [[list]]** (which use `surface/selected` background). The text-only treatment keeps the selected leaf from out-weighting its parent expand affordances in the visual hierarchy.
> - **Indentation: 24px per level.** Effective title left-edge = `24px × (level + 1)`.
> - **Hover** tints the row to `surface/hover` `#F3F5F8` (same as [[menu]] / [[list]]).

Figma source:
- [Tree item variants (collapsed / hover / expanded / selected leaf)](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=6639-2359)
- [Tree View assembled (multiple nested levels)](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=6639-2703)

## When to use

| Use Tree View when… | Use something else when… |
|---|---|
| Data is **hierarchical** with 2+ levels and the user needs to drill into specific branches | Data is flat — use a [[list]] |
| The user **navigates between branches** (open a folder, reveal scan results inside a session) | The user picks **one of many siblings** — use a [[radio]] group or [[dropdown]] |
| Branches can be **expanded/collapsed** independently | Branches are always all-open — render as a [[list]] with sub-headings instead |
| The hierarchy is **stable** (folders are folders, sessions are sessions) | The hierarchy is dynamic (sort/filter changes the parent-child relationships) — use a flat list with grouping headers |

## Anatomy

```
┌────────────────────────────────────────────┐  ← Tree view container
│ ▶  Parent A                                │     row: 40px tall, fluid width
│ ▼  Parent B                                │     chevron at left for expandable rows
│    ├─ Leaf B1                              │     non-expandable rows reserve the 24px slot
│    ├─ Leaf B2  ← selected (bold + blue)    │     selected = text-only treatment
│    ├─ Leaf B3                              │
│    └─ ▼ Parent B4 (nested expandable)      │     nesting increases left padding
│         ├─ Leaf B4a                        │       by 24px per level
│         └─ Leaf B4b                        │
│ ▶  Parent C                                │
└────────────────────────────────────────────┘
```

### Row layout

```
[ level-spacer | chevron (if expandable) | title… ]
```

- **Level spacer** — width = `level × 24px`. Empty space that pushes the row content rightward per nesting depth.
- **Chevron** (expandable rows only) — 20×20 icon (`arrow_triangle_right` when collapsed, `arrow_triangle_down` when expanded) inside a 24×24 button (`cornerradius/s` 6px, 8px padding).
- **24px chevron reserve** — non-expandable rows get `padding-left: 24px` so the title starts at the same x-position as the title-after-chevron on sibling parent rows. Titles align cleanly down the tree.
- **Title** — `body/medium` (16/400/24/0.25), `text/primary` `#16191C`. Selected leaves switch to SemiBold + info-blue (see States).

## States

| State | Surface | Title typography | Title colour | Chevron | When |
|---|---|---|---|---|---|
| `default` | transparent | `body/medium` (16/400/24/0.25) | `text/primary` `#16191C` | `arrow_triangle_right` (if expandable) | resting |
| `hover` | `surface/hover` `#F3F5F8` | `body/medium` (unchanged) | `text/primary` | unchanged | pointer over row |
| `selected` (leaves only) | **transparent** — NO surface tint | `body/medium` size, **weight 600 SemiBold**, line-height normal, letter-spacing 0 | **`text/info/default` `#1660D9`** (info blue) | — (selected items are leaves with no chevron) | the current leaf in a master-detail tree |
| `expanded` *(data prop, not a state)* | unchanged | unchanged | unchanged | switches to `arrow_triangle_down` | the row's `expanded: true` data prop |

**Why selected has no surface tint:**
Tree views are deeply nested by definition — adding `surface/selected` `#EFF5FA` would create a blue rectangle inside a tree of plain rows, visually heavier than the parent expand-collapse affordances. The text-only treatment (bold + blue) keeps the selected leaf legible without out-weighting the structural chrome around it. Different from [[menu]] / [[dropdown]] / [[list]] selected on purpose.

## Indentation

Each `level` adds 24px to the row's effective left padding.

| Level | Title left-edge from row's left edge |
|---:|---:|
| 0 (root) | 24px |
| 1 | 48px |
| 2 | 72px |
| 3 | 96px |
| N | `24 × (N + 1)` px |

The chevron (if any) sits in the first 24px after the level spacer. Non-expandable leaves use `pl-24` to occupy that same slot so titles align with their sibling parent's titles.

## React + Tailwind

```tsx
import { type FC, type ReactNode, useState } from 'react';

interface TreeItemData {
  id: string;
  title: string;
  expandable: boolean;
  children?: TreeItemData[];   // only populated when expandable
}

interface TreeItemProps {
  item: TreeItemData;
  level: number;
  expanded: boolean;
  selected: boolean;
  onToggle: (id: string) => void;
  onSelect: (id: string) => void;
}

const TreeItem: FC<TreeItemProps> = ({ item, level, expanded, selected, onToggle, onSelect }) => {
  const handleClick = () => {
    if (item.expandable) onToggle(item.id);
    else onSelect(item.id);
  };

  return (
    <div
      role={item.expandable ? 'treeitem' : 'treeitem'}
      aria-expanded={item.expandable ? expanded : undefined}
      aria-selected={!item.expandable ? selected : undefined}
      tabIndex={0}
      onClick={handleClick}
      onKeyDown={e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); handleClick(); } }}
      className={`flex items-center h-10 pr-4 rounded-[4px] cursor-pointer transition-colors hover:bg-surface-hover ${item.expandable ? '' : 'pl-6'}`}
      style={{ paddingLeft: item.expandable ? level * 24 : level * 24 + 24 }}
    >
      {item.expandable && (
        <span className="shrink-0 size-6 p-1 flex items-center justify-center text-icon-primary">
          {/* arrow_triangle_right when !expanded, arrow_triangle_down when expanded */}
        </span>
      )}
      <span
        className={
          selected && !item.expandable
            ? 'flex-1 text-base text-info font-semibold leading-none tracking-normal whitespace-nowrap'
            : 'flex-1 text-base text-primary leading-6 tracking-[0.25px] whitespace-nowrap'
        }
      >
        {item.title}
      </span>
    </div>
  );
};

export const TreeView: FC<{ data: TreeItemData[] }> = ({ data }) => {
  const [expandedIds, setExpandedIds] = useState<Set<string>>(new Set());
  const [selectedId, setSelectedId] = useState<string | null>(null);

  const renderItems = (items: TreeItemData[], level: number): ReactNode => {
    return items.map(item => {
      const isExpanded = expandedIds.has(item.id);
      return (
        <div key={item.id}>
          <TreeItem
            item={item}
            level={level}
            expanded={isExpanded}
            selected={selectedId === item.id}
            onToggle={id => setExpandedIds(prev => {
              const next = new Set(prev);
              next.has(id) ? next.delete(id) : next.add(id);
              return next;
            })}
            onSelect={setSelectedId}
          />
          {item.expandable && isExpanded && item.children && renderItems(item.children, level + 1)}
        </div>
      );
    });
  };

  return (
    <div role="tree" className="flex flex-col w-full">
      {renderItems(data, 0)}
    </div>
  );
};
```

Required Tailwind tokens (in `tailwind.config.js`):

```js
colors: {
  'surface-hover': '#F3F5F8',
  'text-primary': '#16191C',
  'text-info':    '#1660D9',
  'icon-primary': '#16191C',
},
```

## Standalone HTML / CSS

```html
<style>
  :root {
    --color-surface-hover:        #F3F5F8;
    --color-text-primary:         #16191C;
    --color-text-info-default:    #1660D9;
    --color-icon-primary:         #16191C;
    --size-cornerradius-xs:       4px;
    --size-cornerradius-s:        6px;
    --comp-height-xl:             40px;
  }

  .tree-view {
    display: flex;
    flex-direction: column;
    font-family: 'Inter', system-ui, sans-serif;
    width: 100%;
  }

  .tree-item {
    display: flex;
    align-items: center;
    height: var(--comp-height-xl);
    padding-right: 16px;
    border-radius: var(--size-cornerradius-xs);
    cursor: pointer;
    background: transparent;
    transition: background-color 80ms;
    user-select: none;
    width: 100%;
    box-sizing: border-box;
    /* padding-left is set inline per level — see usage example */
  }

  .tree-item--leaf { padding-left: 24px; }     /* reserve the chevron slot */

  .tree-item:not(.tree-item--disabled):hover,
  .tree-item.is-hover {
    background: var(--color-surface-hover);
  }

  .tree-item__chevron {
    flex-shrink: 0;
    width: 24px; height: 24px;
    padding: 2px;
    display: flex; align-items: center; justify-content: center;
    color: var(--color-icon-primary);
    border-radius: var(--size-cornerradius-s);
  }
  .tree-item__chevron svg { width: 20px; height: 20px; display: block; }

  .tree-item__title {
    flex: 1 1 0;
    min-width: 0;
    font-size: 16px;
    font-weight: 400;
    line-height: 24px;
    letter-spacing: 0.25px;
    color: var(--color-text-primary);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  /* Selected = text-only (bold + info-blue), NO surface tint */
  .tree-item--selected .tree-item__title {
    font-weight: 600;
    color: var(--color-text-info-default);
    line-height: 1;
    letter-spacing: 0;
  }
</style>

<div class="tree-view" role="tree">
  <!-- expandable, collapsed, level 0 -->
  <div class="tree-item" role="treeitem" aria-expanded="false" style="padding-left: 0">
    <span class="tree-item__chevron"><svg viewBox="0 0 24 24"><use href="#i-arrow-triangle-right"/></svg></span>
    <span class="tree-item__title">Parent A</span>
  </div>

  <!-- expandable, expanded, level 0 -->
  <div class="tree-item" role="treeitem" aria-expanded="true" style="padding-left: 0">
    <span class="tree-item__chevron"><svg viewBox="0 0 24 24"><use href="#i-arrow-triangle-down"/></svg></span>
    <span class="tree-item__title">Parent B</span>
  </div>

  <!-- leaves, level 1 (pl = 24 (reserve) + 24 (level) = 48) -->
  <div class="tree-item tree-item--leaf" role="treeitem" style="padding-left: 48px">
    <span class="tree-item__title">Leaf B1</span>
  </div>

  <!-- selected leaf — text-only treatment -->
  <div class="tree-item tree-item--leaf tree-item--selected" role="treeitem" aria-selected="true" style="padding-left: 48px">
    <span class="tree-item__title">Leaf B2</span>
  </div>
</div>
```

## Don'ts

- **Don't add a `surface/selected` background to the selected leaf.** Tree views are visually dense with nested rows — a blue background rectangle inside would compete with the parent expand affordances. The text-only treatment (bold + info-blue) is intentional. Different from [[menu]] / [[dropdown]] / [[list]] on purpose.
- **Don't allow expandable parents to be `selected`.** Parents are navigation only — clicking them toggles `expanded`. Selection lives at the leaf. If your data has "selectable parents", you're modelling a different control (probably a [[list]] with `radio` leading element).
- **Don't draw connecting lines between parent and children.** The 24px indent + chevron direction provides enough hierarchy. Adding vertical guide lines reads as a primitive filesystem viewer and clutters the visual rhythm of the rows.
- **Don't omit the 24px reserve on non-expandable leaves.** Without it, leaf titles start where the chevron WOULD be on parents, breaking the title-column alignment down the tree. The reserve makes the tree feel "structured" instead of "ragged."
- **Don't render more than ~3–4 levels of nesting by default.** Beyond 4 levels, indentation eats half the row width and titles get truncated. If you genuinely have 5+ levels, consider showing only the current branch (collapse siblings to keep the focal path visible).
- **Don't use `arrow_right` / `arrow_left` for the chevron** — the catalogued tokens are `arrow_triangle_right` (collapsed) and `arrow_triangle_down` (expanded). Per [[icons]] catalog.
- **Don't add a `focused` state with its own background colour.** Keyboard focus follows the OS-native `:focus-visible` outline. Same call as every other component.
- **Don't use Roboto.** Figma's `body/medium/font` reads Roboto — placeholder. Web ships Inter. Per [[feedback-figma-font-placeholders]].
- **Don't hand-type the chevron SVG paths.** Copy verbatim from `assets/icons/arrow-triangle-right.svg` and `assets/icons/arrow-triangle-down.svg`. Per [[feedback-icon-paths-from-assets]].
