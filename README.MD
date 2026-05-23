# Flet Fonts

![PyPI - Downloads](https://img.shields.io/pypi/dm/flet-fonts)
![PyPI - Version](https://img.shields.io/pypi/v/flet-fonts)

**Google Fonts, instantly in Flet** — no downloads, no manual font setup.

---

## Installation

```bash
uv add flet-fonts
```

> **Python 3.12+** and **Flet ≥ 0.85** required.

---

## Platforms

![Android](https://img.shields.io/badge/Android-✓-brightgreen)
![Linux](https://img.shields.io/badge/Linux-✓-brightgreen)
![Windows](https://img.shields.io/badge/Windows-✓-brightgreen)
![macOS](https://img.shields.io/badge/macOS-✓-brightgreen)
![Web](https://img.shields.io/badge/Web-x-red)

---

## Usage

> [!IMPORTANT]
> **Build your project first** so Flet registers the fonts into the Flutter dependencies:
> ```bash
> flet build
> ```

### Basic

```python
import flet as ft
import flet_fonts as ff

def main(page: ft.Page):
    page.add(ff.Text(value="Hello!", google_fonts="Aboreto"))

ft.app(main)
```

### Rich spans

```python
ff.Text(
    value="hello",
    google_fonts="ADLaM Display",
    max_lines=1,
    style=ft.TextStyle(size=20),
    spans=[
        ff.TextSpan(text=" world", google_fonts="Aboreto"),
    ],
)
```

### Selectable text

```python
ff.Text(
    value="You can copy this text.",
    google_fonts="Roboto",
    selectable=True,
)
```

---

<p align="center" style="font-style: italic;">Semoga library ini membantu! 🌴</p>
