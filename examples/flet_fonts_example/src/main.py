import flet as ft

import flet_fonts as ff


def main(page: ft.Page):
    ff.use_google_font(page, "Acme")
    page.add(ft.Text("Everything uses Acme"))

ft.run(main)
