# Flet Fonts

[![PyPI version](https://img.shields.io/pypi/v/flet-fonts)](https://pypi.org/project/flet-fonts/)
[![PyPI downloads](https://img.shields.io/pypi/dm/flet-fonts)](https://pypi.org/project/flet-fonts/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/)
[![Flet](https://img.shields.io/badge/flet-1.1.2%2B-blue)](https://flet.dev/)

Use any of the **1926 Google Fonts families** in Flet without managing font
files yourself. Fonts are resolved at runtime by the
[`google_fonts`](https://pub.dev/packages/google_fonts) Flutter package.

## Features

- `ff.Text` — a text widget with a `google_fonts` property.
- `ff.TextSpan` — rich spans, each with its own font, style, and semantics.
- `ff.use_google_font()` — apply one font to every text in the app through
  the page theme.
- Typed font names through `ff.FontFamily` (autocomplete for all 1926 families).
- Selectable text, selection cursor styling, max lines, no-wrap, and
  accessibility labels.
- Graceful error handling when a font cannot be resolved.

## Requirements

| Requirement | Version |
| --- | --- |
| Python | 3.12+ |
| Flet | 1.1.2+ |
| Flutter (for builds) | 3.47+ |
| Dart (for builds) | 3.13+ |

## Installation

```bash
uv add flet-fonts
```

or

```bash
pip install flet-fonts
```

> [!IMPORTANT]
> Run `flet build` before shipping. The build registers the `flet_fonts`
> Flutter extension and the `google_fonts` dependency in the app bundle.
> Without it, `ff.Text` is not available on the client.

## Quick start

```python
import flet as ft
import flet_fonts as ff


def main(page: ft.Page):
    page.add(
        ff.Text(
            value="Hello from flet-fonts!",
            google_fonts="Aboreto",
            style=ft.TextStyle(size=32),
        )
    )


ft.run(main)
```

## Usage

### Text widget

`ff.Text` wraps Flutter's `Text` / `SelectableText` and resolves the font
named in `google_fonts`.

```python
ff.Text(
    value="Hello world",
    google_fonts="Roboto",
    style=ft.TextStyle(size=24, color=ft.Colors.AMBER),
    text_align=ft.TextAlign.CENTER,
    max_lines=2,
)
```

If `google_fonts` is omitted, the widget falls back to `"ADLaM Display"`.

### Global font (text theme)

Apply one Google Font to the whole app instead of using `ff.Text` for every
control:

```python
import flet as ft
import flet_fonts as ff


def main(page: ft.Page):
    ff.use_google_font(page, "Aboreto")
    page.add(ft.Text("Every text uses Aboreto"))


ft.run(main)
```

`use_google_font()`:

1. resolves the font file URL from the Google Fonts API,
2. registers it in `page.fonts`,
3. sets `font_family` on both `page.theme` and `page.dark_theme`.

Call it before `page.add()`. A network connection is required at startup.
Because the font is applied at the page level, dialogs and overlays use it
too.

> [!NOTE]
> `page.fonts` accepts one file per family, so only the regular weight is
> loaded and bold text is synthesized by Flutter. Use `ff.Text` with
> `google_fonts` when you need true per-weight files.

### Rich spans

Each span can use a different font, style, or semantics:

```python
ff.Text(
    value="Hello ",
    google_fonts="ADLaM Display",
    max_lines=1,
    style=ft.TextStyle(size=20),
    spans=[
        ff.TextSpan(
            text="world",
            google_fonts="Aboreto",
            style=ft.TextStyle(color=ft.Colors.AMBER),
        ),
    ],
)
```

Spans without `google_fonts` inherit the parent's font and style. Spans can be
nested:

```python
ff.Text(
    value="a",
    google_fonts="Roboto",
    spans=[
        ff.TextSpan(
            text="b",
            google_fonts="Aboreto",
            spans=[ff.TextSpan(text="c")],
        ),
    ],
)
```

### Selectable text

```python
ff.Text(
    value="You can select and copy this text.",
    google_fonts="Roboto",
    selectable=True,
    show_selection_cursor=True,
    selection_cursor_color=ft.Colors.AMBER,
    selection_cursor_width=3,
    selection_cursor_height=24,
)
```

### Accessibility

```python
ff.Text(
    value="Password: 1234",
    google_fonts="Roboto",
    semantics_label="Password field",
    spans=[ff.TextSpan(text="1234", spell_out=True)],
)
```

`spell_out=True` makes screen readers announce text character by character.

### Error handling

When a font cannot be resolved, `ff.Text` shows an inline error message. You
can replace it with your own control:

```python
ff.Text(
    value="Hello",
    google_fonts="Font That Does Not Exist",
    error_content=ft.Text("Font unavailable", color=ft.Colors.RED),
)
```

Spans that reference a missing font render as red error text inside the line.

## API reference

### `ff.Text`

A `ft.LayoutControl` that renders text with a Google Font.

| Property | Type | Default | Description |
| --- | --- | --- | --- |
| `value` | `str` | `""` | Text content. |
| `google_fonts` | `FontFamily \| None` | `None` | Google Font family name. Falls back to `"ADLaM Display"`. |
| `spans` | `list[TextSpan] \| None` | `None` | Inline rich-text spans. |
| `text_align` | `ft.TextAlign` | `START` | Alignment inside the bounding box. |
| `style` | `ft.TextStyle \| None` | `None` | Text style applied to the whole text. |
| `max_lines` | `int \| None` | `None` | Maximum lines before overflow. |
| `no_wrap` | `bool \| None` | `None` | Disable wrapping. Ignored when `selectable=True`. |
| `semantics_label` | `str \| None` | `None` | Accessibility label. |
| `selectable` | `bool \| None` | `None` | Allow selecting and copying. |
| `show_selection_cursor` | `bool` | `False` | Show a visible selection cursor. |
| `enable_interactive_selection` | `bool` | `True` | Allow long-press or drag selection. |
| `selection_cursor_width` | `int` | `2` | Cursor width in logical pixels. |
| `selection_cursor_height` | `int \| None` | `None` | Cursor height. Defaults to text height. |
| `selection_cursor_color` | `ft.ColorValue \| None` | `None` | Cursor color. Defaults to the theme. |
| `error_content` | `ft.Control \| None` | `None` | Fallback widget when the font is missing. |

### `ff.TextSpan`

A styled fragment inside `ff.Text`.

| Property | Type | Default | Description |
| --- | --- | --- | --- |
| `text` | `str` | `""` | Span text. |
| `google_fonts` | `FontFamily \| None` | `None` | Font for this span. Inherits from the parent when omitted. |
| `spans` | `list[TextSpan] \| None` | `None` | Nested child spans. |
| `style` | `ft.TextStyle \| None` | `None` | Span style. Inherits from the parent when omitted. |
| `semantic_label` | `str \| None` | `None` | Accessibility label. |
| `spell_out` | `bool \| None` | `None` | Announce character by character. Inherited by child spans. |

### `ff.use_google_font(page, font)`

Apply a Google Font to the whole app through the page theme.

| Argument | Type | Description |
| --- | --- | --- |
| `page` | `ft.Page` | Target page. |
| `font` | `FontFamily` | Google Font family name. |

Raises `ValueError` when the family does not exist.

### `ff.FontFamily`

A `Literal` type with all 1926 supported family names. Use it for type hints
and editor autocomplete:

```python
from flet_fonts import FontFamily, Text


def heading(font: FontFamily) -> Text:
    return Text(value="Title", google_fonts=font)
```

## Fonts

All families from <https://fonts.google.com/> that are supported by
`google_fonts` 9.0.0 are available (1926 families). Font names are
case-sensitive and must match the Google Fonts family name exactly.

Browse the catalog at <https://fonts.google.com/>.

## Platform support

| Platform | Status |
| --- | --- |
| Android | Supported |
| Linux | Supported |
| Windows | Supported |
| macOS | Supported |
| Web | Not supported |

Fonts are downloaded at runtime and cached on the device.

## Development

```bash
git clone https://github.com/arief05652/flet-fonts
cd flet-fonts

just run          # run the example app
just build linux  # build the example app, including the Flutter extension
```

`flet run` reuses the client produced by `flet build` when
`examples/flet_fonts_example/build/<platform>/` exists. Rebuild after changing
Dart code or upgrading Flet, otherwise the app keeps using the old client.

Project layout:

```
src/flet_fonts/           Python package
  flet_fonts.py           ff.Text control
  text_span.py            ff.TextSpan control
  font_data.py            FontFamily literal (1926 fonts)
  theme.py                use_google_font()
src/flutter/flet_fonts/   Flutter extension (Dart)
examples/                 example app
```

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

[MIT](LICENSE)
