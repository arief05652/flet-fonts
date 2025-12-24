default:
    just --list

sync-lib:
    uv sync

sync-flutter:
    cd src/flutter/flet_fonts/
    flutter pub get

sync-example:
    cd examples/flet_fonts_example/
    uv sync
