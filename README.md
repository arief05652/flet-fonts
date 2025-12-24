# Flet Fonts
flet fonts menggunakan [GoogleFonts: 6.1.0](https://pub.dev/packages/google_fonts) dibelakang layarnya


## Installation

> [!NOTE]
> library ini hanya bisa dipakai dengan python minimal versi `3.12`

```

```




## How to Use

```python
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
                "Hello, World",
                font_size=20,
                font_family="ADLaM Display"
            ),
        ),
        ft.Text(),
    )


ft.app(main)
```

> [!NOTE]
> default dari class `FletFonts` memakai properti `wrap=True`, ketika anda ingin memakai selectable harap ubah `wrap=False` terlebih dahulu. begitupun dengan `overflow`, properti ini tidak bisa bekerja dengan selectable yang true.


![screen shot](asset/hint-font.jpeg)





<!-- Add dependency to `pyproject.toml` of your Flet app:

* **Git dependency**

Link to git repository:

```
dependencies = [
  "flet-fonts @ git+https://github.com/MyGithubAccount/flet-fonts",
  "flet>=0.28.3",
]
```

* **PyPi dependency**  

If the package is published on pypi.org:

```
dependencies = [
  "flet-fonts",
  "flet>=0.28.3",
]
```

Build your app:
```
flet build macos -v
``` -->
