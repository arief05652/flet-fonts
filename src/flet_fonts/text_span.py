from typing import Optional

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
    """

    value: str = ""
    spans: Optional[list["TextSpan"]] = None
    google_fonts: Optional[FontFamily] = None
    style: Optional[ft.TextStyle] = None
    semantic_label: Optional[str] = None
