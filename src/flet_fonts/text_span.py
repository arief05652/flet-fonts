from typing import Optional, Union

import flet as ft

from .font_data import FontFamily


@ft.control("TextSpan")
class TextSpan(ft.Control):
    """
    This class is used to create spans.

    Example:
        ```python
        import flet as ft
        import flet_fonts as ff

        def main(page: ft.Page):
            page.theme_mode = ft.ThemeMode.DARK

            page.add(
                ft.Container(
                    padding=10,
                    bgcolor=ft.Colors.WHITE_30,
                    height=150,
                    width=300,
                    content=ff.FletFonts(
                        value="dari flet-fonts",
                        spans=[
                            ff.TextSpan(
                                value="ini text span",
                            )
                        ],
                    ),
                ),
            )
        ft.run(main)
        ```

    Note:
        after you use the `ff.TextSpan()` class,
        you must enter a font theme. It cannot be empty,
        and the default is `ADLaM Display`.
    """

    text: str = ""
    google_fonts: Union[FontFamily, str, None] = None
    """
    If you cannot find the font you want to use,
    you can copy and paste the font name you took from `https://fonts.google.com/`.
    """

    spans: Optional[list["TextSpan"]] = None
    """
    Additional spans to include as children.

    Note:
        If both `spans` and [`text`][(c).] are defined,
        the `text` takes precedence.
    """

    style: Optional[ft.TextStyle] = None
    """
    Defines the style of this text span.
    """

    semantic_label: Optional[str] = None
    """
    An alternative semantics label for this text.

    If present, the semantics of this control will contain this value instead of the
    actual text.

    Raises:
        ValueError: If [`semantics_label`][(c).] is set when [`text`][(c).] is `None`.
    """

    spell_out: Optional[bool] = None
    """"
    Whether the assistive technologies should spell out this text
    character by character.

    If the text is 'hello world', setting this to true causes the assistive
    technologies, such as VoiceOver or TalkBack, to pronounce
    'h-e-l-l-o-space-w-o-r-l-d' instead of complete words.
    This is useful for texts, such as passwords or verification codes.

    If this span contains other text span children, they also inherit the property from
    this span unless explicitly set.

    If the property is not set, this text span inherits the spell out setting
    from its parent. If this text span does not have a parent or the parent does
    not have a spell out setting, this text span does not spell out the text by default.
    """
