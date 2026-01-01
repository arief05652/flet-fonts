import flet as ft
import flet_fonts as ff


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
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
                        value="inside flet-fonts",
                        google_fonts="Aboreto",
                        style=ft.TextStyle(size=15, overflow=ft.TextOverflow.ELLIPSIS),
                        spans=[
                            ff.TextSpan(
                                value="nested span",
                                google_fonts="Agdasima",
                                style=ft.TextStyle(
                                    size=15, overflow=ft.TextOverflow.ELLIPSIS
                                ),
                            )
                        ],
                    )
                ],
                max_lines=1,
                style=ft.TextStyle(size=15),
            ),
        ),
    )


ft.run(main)
