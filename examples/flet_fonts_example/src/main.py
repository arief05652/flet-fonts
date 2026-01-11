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
            alignment=ft.Alignment.CENTER,
            content=ff.Text(
                value="Hello world",
                google_fonts="Zen Dots",
            ),
        ),
    )


ft.run(main)
