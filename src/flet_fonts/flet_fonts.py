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
                    google_fonts=ff.FontFamily.ABORETO,
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

    google_fonts: FontFamily | str | None = None
    """The Google Font family name.

    Use a `FontFamily` member for autocomplete, e.g.
    `ff.FontFamily.ABORETO`. Plain family names are accepted too. Falls
    back to `"ADLaM Display"` when not specified.
    """

    spans: list[TextSpan] | None = None
    """Inline rich-text spans within the same text line.

    Each span can use a different Google Font, style, or semantic label.

    Example:
        ```python
        ff.Text(
            value="hello",
            google_fonts=ff.FontFamily.ANCIZAR_SERIF,
            spans=[
                ff.TextSpan(text="world", google_fonts=ff.FontFamily.ABORETO),
            ],
        )
        ```
    """

    # ── Layout & Style ──────────────────────────────────────────────────

    text_align: ft.TextAlign = ft.TextAlign.START
    """Alignment of the text within its bounding box."""

    style: ft.TextStyle | None = None
    """A `ft.TextStyle` to customise the appearance of the text."""

    max_lines: int | None = None
    """Maximum number of lines before the text overflows."""

    no_wrap: bool | None = None
    """Prevents text from wrapping to the next line on overflow."""

    semantics_label: str | None = None
    """Alternative label used by assistive technologies.

    When set, screen readers will announce this value instead of the
    actual text content.
    """

    # ── Selection ───────────────────────────────────────────────────────

    selectable: bool | None = None
    """When `True`, users can select and copy the text."""

    show_selection_cursor: bool = False
    """Whether to show a visible cursor when the text is selected."""

    enable_interactive_selection: bool = True
    """Whether the user can interactively select text via long-press or drag."""

    selection_cursor_width: int = 2
    """Width of the selection cursor in device-independent pixels."""

    selection_cursor_height: int | None = None
    """Height of the selection cursor. When `None`, matches the text height."""

    selection_cursor_color: ft.ColorValue | None = None
    """Colour of the selection cursor. Falls back to the theme's default."""

    # ── Error Handling ──────────────────────────────────────────────────

    error_content: ft.Control | None = None
    """A fallback widget shown when the requested font cannot be resolved.

    When `None`, an inline error message is displayed instead.
    """
