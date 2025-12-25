# Flet Fonts
flet fonts menggunakan [GoogleFonts: 6.1.0](https://pub.dev/packages/google_fonts) dibelakang layarnya


## Installation

> [!NOTE]
> library ini hanya bisa dipakai dengan python minimal versi `3.12`

perintah build
```
uv run flet run {apk|linux|web|macos|windows} -v
```

jika kamu pakai pip
```
pip install flet-fonts
```

jika kamu pakai uv
```
uv add flet-fonts
```

## How to Use

> [!WARNING]
> sebelum kamu jalankan project flet kamu pastikan build project kamu terlebih dahulu karena untuk mendaftarkan ekstension ke dalam flutter nya.

```python
import flet as ft

from flet_fonts import FletFonts


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
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


![screenshot](asset/hint-font.jpeg)