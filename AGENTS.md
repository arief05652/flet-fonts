# AGENTS.md

Flet extension that exposes Google Fonts as Python controls. Two halves must stay
in sync: Python (`src/flet_fonts/`) and Dart (`src/flutter/flet_fonts/lib/`).

## Commands

```bash
just run                 # run example app (desktop, watch mode)
just build linux         # build example app, includes the Flutter extension
just serve               # serve the example app
cd src/flutter/flet_fonts && dart analyze   # only static check for Dart
uv run python -c "import flet_fonts"        # Python import smoke test
```

No test suite, no CI, no lint config. Verification is `dart analyze`, Python
import, and running the example app.

## Critical gotchas

- `flet run` reuses `examples/flet_fonts_example/build/<platform>/` when it
  exists. After any Dart or Flet version change run `just build linux` first,
  otherwise the app runs an old client. The standard/light client does not
  contain this extension, so `ff.Text` shows as an unknown control.
- `just build` runs `sync` first, which executes `uv add flet-cli/desktop/web==1.1.2`
  at the repo root and mutates `pyproject.toml`/`uv.lock`.
- `src/flet_fonts/font_data.py` is generated from `GoogleFonts.asMap()` of the
  installed `google_fonts` Dart package as a `FontFamily` enum. Do not hand-edit.
  Regenerate by extracting keys between `asMap() => const {` and
  `_asMapOfTextThemes() => const {` in
  `~/.pub-cache/hosted/pub.dev/google_fonts-<version>/lib/src/google_fonts_all_parts.dart`.
- Flet 1.x moved Material out of the Flutter SDK. Import
  `package:material_ui/material_ui.dart`, never `package:flutter/material.dart`;
  its `ThemeData` is a different type and breaks `getTextStyle()`.
- `google_fonts` 9.0.0 requires Flutter >= 3.47 / Dart >= 3.13. Flet 1.1.2 pins
  Flutter 3.47.9. Check that pin before bumping `google_fonts` or `flet`.
- `pubspec.lock` is gitignored on purpose (Dart library convention).
- Root readme is `README.MD` (uppercase), referenced by `pyproject.toml`.

## Control wiring

Adding a property to a control means editing both sides:

1. Python dataclass field in `src/flet_fonts/flet_fonts.py` or `text_span.py`.
2. Dart read in `lib/src/flet_fonts.dart` (`control.getString/getBool/getInt/...`)
   or `lib/src/utils/text_span.dart`.

`@ft.control("FletFonts")` must match `case "FletFonts"` in `extension.dart`.
`TextSpan` is not registered as a Flutter widget; it is parsed manually by
`parseSpans()` from the `spans` child list.

Python side is Flet 1.x API: `ft.run()` (not `ft.app()`), `ft.LayoutControl`,
`@ft.control(...)`.

## Theme helper

`use_google_font(page, font)` resolves a TTF URL from the Google Fonts CSS API,
registers it in `page.fonts`, and sets `font_family` on `page.theme` and
`page.dark_theme`. `page.fonts` accepts one file per family, so only regular
weight is loaded and bold is synthesized. Needs network at startup.

## Releases

`pyproject.toml` and `src/flutter/flet_fonts/pubspec.yaml` versions must match.
Add a `CHANGELOG.md` entry for every release. Current version: 1.0.0.

Generated/untracked: `build/`, `graphify-out/`, `*.egg-info`, `pubspec.lock`,
`.venv/`, `.ruff_cache/`.
