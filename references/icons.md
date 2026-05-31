# Icons

### Library
We use the **Scandit UI Kit** icon set (outline style by default, filled for active/selected states).
SVG assets live in [`../assets/icons/`](../assets/icons/).
Figma source: [UI Kit – Icons](https://www.figma.com/design/wzrIzPpikfyF9K6Y3UHUf8/UI-Kit?node-id=136-70)

### New icons → Material Symbols
If a needed icon is **not** in the approved set below, source it from **Material Symbols** with the following styling — no exceptions:

| Setting | Value |
|---|---|
| Style | **Rounded** |
| Weight | **400** |
| Size | **24dp** |
| Fill | 0 (outline) by default, 1 (filled) for active/selected states |
| Grade | 0 |
| Optical size | 24 |

Browse and copy at [fonts.google.com/icons](https://fonts.google.com/icons). Download the SVG, add it to `assets/icons/` using kebab-case (e.g. `notifications-active.svg`), and add a row to the approved set below.

### Usage Rules
- Default size: 24px (use 16px for dense UIs, 20px for inline)
- Color: always use a semantic `icon/*` token — never hardcode hex values or rely on `currentColor`
- Style: outline for actions, filled for active/selected states
- Pair outline + filled variants for toggleable states (e.g. `book` / `book_filled`)

#### Semantic icon colors
Use the role that matches the icon's meaning — not the visual color.

| Token | Use for |
|---|---|
| `icon/primary` | Default icon color (high-emphasis actions, body-level UI) |
| `icon/secondary` | De-emphasized icons (metadata, helper rows) |
| `icon/disabled` | Disabled controls |
| `icon/on-color` | Icons on filled semantic surfaces — pair with `text/on-color/*` |
| `icon/brand` | Brand-led moments only (logo lockups, brand CTAs) |
| `icon/brand dark` | Brand on dark surfaces |
| `icon/info` | Informational status |
| `icon/positive` | Success status |
| `icon/warning` | Warning status |
| `icon/danger` | Error / destructive status |
| `icon/highlight` | Featured callouts only — use sparingly |

### Approved Icon Set

#### Navigation & arrows
| Name | Icon key | Asset | Usage |
|---|---|---|---|
| Chevron down | `chevron_down` | [chevron-down.svg](../assets/icons/chevron-down.svg) | Expand, dropdown trigger |
| Chevron up | `chevron_up` | [chevron-up.svg](../assets/icons/chevron-up.svg) | Collapse |
| Chevron left | `chevron_left` | [chevron-left.svg](../assets/icons/chevron-left.svg) | Back, previous |
| Chevron right | `chevron_right` | [chevron-right.svg](../assets/icons/chevron-right.svg) | Forward, drill-in |
| Arrow right | `arrow_right` | [arrow-right.svg](../assets/icons/arrow-right.svg) | CTAs, navigation |
| Arrow left | `arrow_left` | [arrow-left.svg](../assets/icons/arrow-left.svg) | Back navigation |
| Arrow triangle down | `arrow_triangle_down` | [arrow-triangle-down.svg](../assets/icons/arrow-triangle-down.svg) | Dropdown trigger (closed) — chunky filled triangle. Used in Dropdown's trailing arrow. |
| Arrow triangle up | `arrow_triangle_up` | [arrow-triangle-up.svg](../assets/icons/arrow-triangle-up.svg) | Dropdown trigger (open) — pairs with `arrow_triangle_down`. |
| Arrow triangle left | `arrow_triangle_left` | [arrow-triangle-left.svg](../assets/icons/arrow-triangle-left.svg) | Compact "back" / collapse affordance. Differs from `chevron_left` — solid filled triangle. |
| Arrow triangle right | `arrow_triangle_right` | [arrow-triangle-right.svg](../assets/icons/arrow-triangle-right.svg) | Compact "next" / expand affordance. Differs from `chevron_right` — solid filled triangle. |
| Open in new | `open_in_new` | [open-in-new.svg](../assets/icons/open-in-new.svg) | External links |
| Exit | `exit` | [exit.svg](../assets/icons/exit.svg) | Leave flow, sign out |

#### Actions
| Name | Icon key | Asset | Usage |
|---|---|---|---|
| Search | `search` | [search.svg](../assets/icons/search.svg) | Search inputs |
| Close | `close` | [close.svg](../assets/icons/close.svg) | Dismiss modals, clear |
| Close small | `close_small` | [close-small.svg](../assets/icons/close-small.svg) | Remove chips, tags |
| Plus | `plus` | [plus.svg](../assets/icons/plus.svg) | Add primary action |
| Add circle | `add_circle` | [outline](../assets/icons/add-circle.svg) · [filled](../assets/icons/add-circle-filled.svg) | Add item (active state filled) |
| Minus | `minus` | [minus.svg](../assets/icons/minus.svg) | Decrement, remove |
| Delete | `delete` | [delete.svg](../assets/icons/delete.svg) | Destructive remove |
| Pen | `pen` | [outline](../assets/icons/pen.svg) · [filled](../assets/icons/pen-filled.svg) | Edit (active state filled) |
| Filter | `filter` | [filter.svg](../assets/icons/filter.svg) | Filter lists |
| Refresh | `refresh` | [refresh.svg](../assets/icons/refresh.svg) | Reload data |
| Download | `download` | [download.svg](../assets/icons/download.svg) | Download file |
| Upload | `upload` | [upload.svg](../assets/icons/upload.svg) | Upload file |
| Share | `share` | [share.svg](../assets/icons/share.svg) | Share content |
| Content copy | `content_copy` | [content-copy.svg](../assets/icons/content-copy.svg) | Copy to clipboard |
| Settings | `settings` | [outline](../assets/icons/settings.svg) · [filled](../assets/icons/settings-filled.svg) | Settings entry (active state filled) |

#### Menus & layout
| Name | Icon key | Asset | Usage |
|---|---|---|---|
| Menu hamburger | `menu_hamburger` | [menu-hamburger.svg](../assets/icons/menu-hamburger.svg) | Mobile nav |
| Menu dots vertical | `menu_dots_vertical` | [menu-dots-vertical.svg](../assets/icons/menu-dots-vertical.svg) | Row actions, overflow |
| Drag handle | `drag_handle` | [drag-handle.svg](../assets/icons/drag-handle.svg) | Reorder rows |
| Grid view | `grid_view` | [grid-view.svg](../assets/icons/grid-view.svg) | Switch to grid layout |
| List | `list` | [list.svg](../assets/icons/list.svg) | Switch to list layout |
| Dashboard | `dashboard` | [dashboard.svg](../assets/icons/dashboard.svg) | Dashboard nav entry |

#### Status & feedback
| Name | Icon key | Asset | Usage |
|---|---|---|---|
| Check | `check` | [check.svg](../assets/icons/check.svg) | Confirm, success inline |
| Check circle | `check_circle` | [outline](../assets/icons/check-circle.svg) · [filled](../assets/icons/check-circle-filled.svg) | Success state — check stays **inside** the circle |
| Check circle outside | `check_circle_outside` | [check-circle-outside.svg](../assets/icons/check-circle-outside.svg) | "Done / completed" emphasis — check extends **outside** the circle. Used in the Success Callout. |
| Cross circle | `cross_circle` | [outline](../assets/icons/cross-circle.svg) · [filled](../assets/icons/cross-circle-filled.svg) | Error state |
| Warning triangle | `warning_triangle` | [outline](../assets/icons/warning-triangle.svg) · [filled](../assets/icons/warning-triangle-filled.svg) | Warnings |
| Error circle | `error_circle` | [outline](../assets/icons/error-circle.svg) · [filled](../assets/icons/error-circle-filled.svg) | Critical errors |
| Info circle | `info_circle` | [outline](../assets/icons/info-circle.svg) · [filled](../assets/icons/info-circle-filled.svg) | Informational hints |
| Lightbulb | `lightbulb` | [lightbulb.svg](../assets/icons/lightbulb.svg) | Tips, suggestions, in-place hints. Used in the Info Callout. |
| Question mark | `question_mark` | [question-mark.svg](../assets/icons/question-mark.svg) | Help, tooltips |

#### Visibility & view
| Name | Icon key | Asset | Usage |
|---|---|---|---|
| Visibility | `visibility` | [outline](../assets/icons/visibility.svg) · [filled](../assets/icons/visibility-filled.svg) | Show password / preview |
| Visibility off | `visibility_off` | [outline](../assets/icons/visibility-off.svg) · [filled](../assets/icons/visibility-off-filled.svg) | Hide password / preview |
| Zoom in | `zoom_in` | [zoom-in.svg](../assets/icons/zoom-in.svg) | Zoom in |
| Zoom out | `zoom_out` | [zoom-out.svg](../assets/icons/zoom-out.svg) | Zoom out |

#### Domain (scanning & capture)
| Name | Icon key | Asset | Usage |
|---|---|---|---|
| Scan | `scan` | [scan.svg](../assets/icons/scan.svg) | Trigger scan |
| Barcode | `Barcode` | [barcode.svg](../assets/icons/barcode.svg) | Barcode references |
| Barcode scanner | `barcode_scanner` | [barcode-scanner.svg](../assets/icons/barcode-scanner.svg) | Scanner entry point |
| QR code | `qr_code` | [qr-code.svg](../assets/icons/qr-code.svg) | QR-specific flows |
| Photo camera | `photo_camera` | [outline](../assets/icons/photo-camera.svg) · [filled](../assets/icons/photo-camera-filled.svg) | Camera capture |
| Flip camera | `flip_camera` | [outline](../assets/icons/flip-camera.svg) · [filled](../assets/icons/flip-camera-filled.svg) | Switch front/back camera |
| Flash on | `flash_on` | [flash-on.svg](../assets/icons/flash-on.svg) | Torch on |
| Flash off | `flash_off` | [flash-off.svg](../assets/icons/flash-off.svg) | Torch off |
| View in AR | `view_in_ar` | [view-in-ar.svg](../assets/icons/view-in-ar.svg) | AR view |

> **Full Figma catalog:** 144 icons live in the UI Kit. Only icons listed above are approved for product use. To add a new icon: source from Material Symbols (Rounded / 400 / 24dp), drop the SVG into `assets/icons/`, and add a row above.
