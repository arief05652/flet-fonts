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
    """Enter the text you want to display"""

    google_fonts: Union[FontFamily, str, None] = None
    """
    If you cannot find the font you want to use,
    you can copy and paste the font name you took from `https://fonts.google.com/`.
    """

    spans: Optional[list[TextSpan]] = None
    """
    In a single line of text, you can use different Google fonts

    Example:
        ```
        ff.Text(
            value="hello",
            google_fonts="Ancizar Serif",
            spans=[
                ff.TextSpan(
                    value="hello",
                    google_fonts="Aboreto",
                )
            ]
        )
        ```
    """

    text_align: ft.TextAlign = ft.TextAlign.START
    """text layout"""

    style: Optional[ft.TextStyle] = None
    """You can design text widgets however you like using `flet.TextStyle`"""

    max_lines: Optional[int] = None
    """You can set the number of lines that can be filled with text"""

    selectable: Optional[bool] = None
    """Users can select text and copy it"""

    no_wrap: Optional[bool] = None
    """Use this if you want to prevent text overflow"""

    semantics_label: Optional[str] = None

    show_selection_cursor: bool = False
    """You can highlight the text that is currently selected"""

    enable_interactive_selection: bool = True

    selection_cursor_width: int = 2

    selection_cursor_height: Optional[int] = None

    selection_cursor_color: Optional[ft.ColorValue] = None

    # error
    error_content: Optional[ft.Control] = None
