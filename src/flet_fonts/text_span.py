from typing import Optional, Union

import flet as ft

from .font_data import FontFamily


@ft.control("TextSpan")
class TextSpan(ft.LayoutControl):
    """
    This class is used to create spans.

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
                    content=ff.FletFonts(
                        value="dari flet-fonts",
                        spans=[
                            ff.TextSpan(
                                value="ini text span",
                            )
                        ],
                    ),
                ),
            )
        ft.run(main)
        ```

    Note:
        after you use the `ff.TextSpan()` class,
        you must enter a font theme. It cannot be empty,
        and the default is `ADLaM Display`.
    """

    value: str = ""
    google_fonts: Union[FontFamily, str] = "ADLaM Display"
    """
    If you cannot find the font you want to use,
    you can copy and paste the font name you took from `https://fonts.google.com/`.
    """

    spans: Optional[list["TextSpan"]] = None
    style: Optional[ft.TextStyle] = None
    semantic_label: Optional[str] = None
