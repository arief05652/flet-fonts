import re
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import replace

import flet as ft

from .font_data import FontFamily

_TTF_URL = re.compile(r"src: url\((https://[^)]+\.ttf)\)")


def use_google_font(page: ft.Page, font: FontFamily) -> None:
    """Use a Google Font for all text in the app through the page theme.

    Loads the font with `page.fonts` and sets it as the default font family
    of both `page.theme` and `page.dark_theme`.

    Call it before adding controls so the first frame already uses the font.

    Example:
        ```python
        import flet as ft
        import flet_fonts as ff

        def main(page: ft.Page):
            ff.use_google_font(page, "Aboreto")
            page.add(ft.Text("Everything uses Aboreto"))

        ft.run(main)
        ```
    """
    page.fonts = {**(page.fonts or {}), font: _ttf_url(font)}
    page.theme = _with_font(page.theme, font)
    page.dark_theme = _with_font(page.dark_theme, font)


def _with_font(theme: ft.Theme | None, font: str) -> ft.Theme:
    return ft.Theme(font_family=font) if theme is None else replace(theme, font_family=font)


def _ttf_url(font: str) -> str:
    query = urllib.parse.urlencode({"family": font})
    try:
        with urllib.request.urlopen(
            f"https://fonts.googleapis.com/css2?{query}", timeout=10
        ) as response:
            css = response.read().decode()
    except urllib.error.HTTPError as error:
        raise ValueError(f"Google Font '{font}' not found") from error

    match = _TTF_URL.search(css)
    if not match:
        raise ValueError(f"Google Font '{font}' has no TrueType file")
    return match.group(1)
