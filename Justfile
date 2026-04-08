default:
    @just --list

# build app {apk, linux, web}
build platform="linux":
    sync
    @cd examples/flet_fonts_example && \
    uv run flet build {{ platform }}

# run result build app {apk, web} default is linux
run platform="":
    @cd examples/flet_fonts_example && \
    uv run flet run {{ platform }} -d -r

# serve web after build app to web
serve:
    @cd examples/flet_fonts_example && \
    uv run flet serve

sync:
    uv add flet-cli==0.80.0 && \
    uv add flet-desktop==0.80.0 && \
    uv add flet-web==0.80.0
