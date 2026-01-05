# FLET FONTS

![PyPI - Downloads](https://img.shields.io/pypi/dw/flet-fonts)
![PyPI - Version](https://img.shields.io/pypi/v/flet-fonts)

#### [en_translate](README_en.MD)

## Introduction

**Flet Fonts** adalah library yang menyediakan **Google Fonts untuk aplikasi Flet**.  
Project ini merupakan **porting dari Google Fonts (Flutter)** agar bisa digunakan secara langsung dan mudah di Flet tanpa konfigurasi font manual.

Tujuan utama library ini adalah:
- Menggunakan Google Fonts di Flet **tanpa ribet**
- API yang **simple & Pythonic**
- Konsisten dengan behavior font di Flutter

Dengan **Flet Fonts**, kamu bisa langsung memakai ratusan font dari Google Fonts hanya dengan menentukan `google_fonts`.

---

## Features

- 🚀 Porting langsung dari **Google Fonts (Flutter)**
- 🎨 Mendukung **ratusan font Google Fonts**
- ⚡ Mudah digunakan, tanpa setup font manual
- 🖥️ Support multi-platform:
  - Android
  - Linux
  - Windows (belum di test)
  - macOS (belum di test)
  - Web (belum di test)

---

## Requirements

- **Python** `3.12` 
- **Flet** `0.80.0`

> [!WARNING]
> ⚠️ Library ini **tidak kompatibel** dengan Python versi di bawah `3.12` atau Flet versi selain `0.80.0`.

---

## Installation

### Using PIP

```bash
pip install flet-fonts
```

### Using UV

```bash
uv add flet-fonts
```

## How to Use

> [!NOTE]
> sebelum dijalankan pastikan kamu build terlebih dahulu, kenapa? karna flet harus mendaftarkan terlebih dahulu ke depedensi flutter nya

```python
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
            content=ff.Text(
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
```
