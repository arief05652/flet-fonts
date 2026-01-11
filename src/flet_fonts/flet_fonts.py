from typing import Optional, Union

import flet as ft

from .font_data import FontFamily
from .text_span import TextSpan


@ft.control("FletFonts")
class Text(ft.LayoutControl):
    """
    class FletFonts uses Google Fonts to set the font family,
    easy to use without downloading files and setting them manually.

    Example:
        ```python
        import flet as ft
        import flet_fonts as ff

        def main(page: ft.Page):
            page.theme_mode = ft.ThemeMode.DARK

            page.add(
                ft.Container(
                    padding=10,
                    bgcolor=ft.Colors.WHITE_30,
                    height=150,
                    width=300,
                    content=ff.Text(
                        value="dari flet-fonts",
                        google_fonts="Aboreto"
                    ),
                ),
            )
        ft.run(main)
        ```

    Note:
        after you use the `ff.Text()` class,
        you must enter a font theme. It cannot be empty,
        and the default is `ADLaM Display`.
    """

    value: str = ""
    google_fonts: Union[FontFamily, str] = "ADLaM Display"
    """
    If you cannot find the font you want to use,
    you can copy and paste the font name you took from `https://fonts.google.com/`.
    """

    spans: Optional[list[TextSpan]] = None
    text_align: ft.TextAlign = ft.TextAlign.START
    style: Optional[ft.TextStyle] = None
    max_lines: Optional[int] = None
    selectable: Optional[bool] = None
    no_wrap: Optional[bool] = None
    semantics_label: Optional[str] = None
    show_selection_cursor: bool = False
    enable_interactive_selection: bool = True
    selection_cursor_width: int = 2
    selection_cursor_height: Optional[int] = None
    selection_cursor_color: Optional[ft.ColorValue] = None
    # error
    error_content: Optional[ft.Control] = None
