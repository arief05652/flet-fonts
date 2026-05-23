from typing import Optional, Union

import flet as ft

from .font_data import FontFamily
from .text_span import TextSpan


@ft.control("FletFonts")
class Text(ft.LayoutControl):
    """Renders text using Google Fonts without manual font file management.

    This widget wraps Flutter's `Text` / `SelectableText` with automatic
    Google Font resolution. Simply pass a font name from
    `https://fonts.google.com/` — the font is resolved at runtime in the
    Flutter layer.

    Example:
        ```python
        import flet as ft
        import flet_fonts as ff

        def main(page: ft.Page):
            page.add(
                ff.Text(
                    value="Hello from flet-fonts!",
                    google_fonts="Aboreto",
                ),
            )

        ft.app(main)
        ```

    Note:
        A `google_fonts` value is required. Falls back to `"ADLaM Display"`
        when not specified.
    """

    # ── Content ──────────────────────────────────────────────────────────

    value: str = ""
    """The text content to display."""

    google_fonts: Union[FontFamily, str, None] = None
    """The Google Font family name.

    You can use any font from `https://fonts.google.com/`. Falls back to
    `"ADLaM Display"` when not specified.
    """

    spans: Optional[list[TextSpan]] = None
    """Inline rich-text spans within the same text line.

    Each span can use a different Google Font, style, or semantic label.

    Example:
        ```python
        ff.Text(
            value="hello",
            google_fonts="Ancizar Serif",
            spans=[
                ff.TextSpan(value="world", google_fonts="Aboreto"),
            ],
        )
        ```
    """

    # ── Layout & Style ──────────────────────────────────────────────────

    text_align: ft.TextAlign = ft.TextAlign.START
    """Alignment of the text within its bounding box."""

    style: Optional[ft.TextStyle] = None
    """A `ft.TextStyle` to customise the appearance of the text."""

    max_lines: Optional[int] = None
    """Maximum number of lines before the text overflows."""

    no_wrap: Optional[bool] = None
    """Prevents text from wrapping to the next line on overflow."""

    semantics_label: Optional[str] = None
    """Alternative label used by assistive technologies.

    When set, screen readers will announce this value instead of the
    actual text content.
    """

    # ── Selection ───────────────────────────────────────────────────────

    selectable: Optional[bool] = None
    """When `True`, users can select and copy the text."""

    show_selection_cursor: bool = False
    """Whether to show a visible cursor when the text is selected."""

    enable_interactive_selection: bool = True
    """Whether the user can interactively select text via long-press or drag."""

    selection_cursor_width: int = 2
    """Width of the selection cursor in device-independent pixels."""

    selection_cursor_height: Optional[int] = None
    """Height of the selection cursor. When `None`, matches the text height."""

    selection_cursor_color: Optional[ft.ColorValue] = None
    """Colour of the selection cursor. Falls back to the theme's default."""

    # ── Error Handling ──────────────────────────────────────────────────

    error_content: Optional[ft.Control] = None
    """A fallback widget shown when the requested font cannot be resolved.

    When `None`, an inline error message is displayed instead.
    """
