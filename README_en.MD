# FLET FONTS

![PyPI - Downloads](https://img.shields.io/pypi/dw/flet-fonts)
![PyPI - Version](https://img.shields.io/pypi/v/flet-fonts)

#### [id_translate](README.md)

## Introduction

**Flet Fonts** is a library that provides **Google Fonts for Flet applications**.

This project is a **port of Google Fonts (Flutter)**, designed to be used directly and easily within Flet without the need for manual font configuration.

The main goals of this library are:

* To use Google Fonts in Flet **without the hassle**
* To provide a **simple & Pythonic** API
* To maintain consistency with font behavior in Flutter

With **Flet Fonts**, you can instantly access hundreds of Google Fonts simply by specifying the `google_fonts` property.

---

## Features

- 🚀 Direct port from **Google Fonts (Flutter)**
- 🎨 Supports **hundreds of Google Fonts**
- ⚡ Easy to use, no manual setup required
- 🖥️ Multi-platform support:
  - Android 🟢
  - Linux 🟢
  - Windows (untested)
  - macOS (untested)
  - Web 🟢

---

## Requirements

* **Python** `3.12`
* **Flet** `0.80.0`

> [!WARNING]
> ⚠️ This library is **not compatible** with Python versions below `3.12` or Flet versions other than `0.80.0`.

---

## Installation

### Using UV

```bash
uv add flet-fonts
```

---

## How to Use

> [!NOTE]
> Make sure to **build your project first** before running it. Why? Because Flet needs to register the fonts into the Flutter dependencies beforehand.

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
                value="from flet-fonts",
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
    
ft.app(main)

```
