import flet as ft

import flet_fonts as ff


def main(page: ft.Page):
    ff.use_google_font(page, ff.FontFamily.TINY5)
    page.add(ft.Text("Everything uses Tiny5", size=50))

ft.run(main)
