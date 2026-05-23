from typing import Optional, Union

import flet as ft

from .font_data import FontFamily


@ft.control("TextSpan")
class TextSpan(ft.Control):
    """A styled fragment of text within a parent `ff.Text` widget.

    Use spans to apply different fonts, styles, or semantic properties to
    portions of a single text line.

    Example:
        ```python
        import flet_fonts as ff

        ff.Text(
            value="Hello ",
            spans=[
                ff.TextSpan(
                    text="world",
                    google_fonts="Aboreto",
                    style=ft.TextStyle(size=24),
                ),
            ],
        )
        ```

    Note:
        When `google_fonts` is not specified, this span inherits the font
        from its parent `ff.Text`. Falls back to `"ADLaM Display"` if the
        parent also has no font set.
    """

    # ── Content ─────────────────────────────────────────────────────────

    text: str = ""
    """The text content of this span.

    When both `text` and parent `value` are defined, the parent's `value`
    acts as a prefix and the span's `text` replaces it at the span position.
    """

    google_fonts: Union[FontFamily, str, None] = None
    """The Google Font family name for this span.

    You can use any font from `https://fonts.google.com/`. When not set,
    the span inherits the font from its parent `ff.Text` control.
    """

    spans: Optional[list["TextSpan"]] = None
    """Nested child spans within this span.

    Child spans inherit properties (e.g. `spell_out`) from this span
    unless explicitly overridden.
    """

    style: Optional[ft.TextStyle] = None
    """A `ft.TextStyle` to customise the appearance of this span.

    When not set, the span inherits the style from its parent.
    """

    # ── Semantics ───────────────────────────────────────────────────────

    semantic_label: Optional[str] = None
    """Alternative label used by assistive technologies.

    When set, screen readers will announce this value instead of the
    span's actual text content.
    """

    spell_out: Optional[bool] = None
    """Whether assistive technologies should spell the text character by
    character.

    When `True`, "hello" is pronounced "h-e-l-l-o" instead of the whole
    word. This is useful for passwords, verification codes, etc.

    Child spans inherit this value unless explicitly overridden.
    Defaults to `False` when neither this span nor its parent set a value.
    """
