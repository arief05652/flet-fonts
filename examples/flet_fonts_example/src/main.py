import flet as ft

from flet_fonts import FletFonts


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.always_on_top
    page.theme_mode = ft.ThemeMode.DARK

    page.add(
        ft.Container(
            height=150,
            width=300,
            padding=10,
            bgcolor=ft.Colors.WHITE24,
            border_radius=15,
            content=FletFonts(
                "Hello, World uqwjndkjansdkjanskjdnasjkdnkasmkasdaskdaksdmalsd kasmdasklmdaksmdaskldmalsdmaslkdmalskdm",
                font_family="ADLaM Display"
            ),
        ),
        ft.Text(),
    )


ft.app(main)
