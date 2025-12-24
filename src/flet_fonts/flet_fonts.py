from typing import Optional

from flet.core.constrained_control import ConstrainedControl
from flet.core.control import OptionalNumber
from flet.core.types import ColorEnums, ColorValue

from .font_data import FontFamily, FontWeight, TextAlign, TextOverflow


class FletFonts(ConstrainedControl):
    """
    FletFonts Control description.
    """

    def __init__(
        self,
        #
        # FletFonts specific
        #
        value: str,
        *,
        font_family: Optional[FontFamily] = None,
        font_size: OptionalNumber = None,
        selectable: bool = False,
        bgcolor: Optional[ColorValue] = None,
        color: Optional[ColorValue] = None,
        italic: bool = False,
        font_weight: Optional[FontWeight] = "normal",
        max_line: Optional[int] = None,
        overflow: Optional[TextOverflow] = None,
        rtl: Optional[bool] = None,
        semantic_label: Optional[str] = None,
        text_align: Optional[TextAlign] = None,
        wrap: Optional[bool] = True,
        #
        # Control
        #
        opacity: OptionalNumber = None,
    ):
        ConstrainedControl.__init__(self, rtl=rtl, opacity=opacity)
        self.value = value
        self.font_family = font_family
        self.font_size = font_size
        self.selectable = selectable
        self.bgcolor = bgcolor
        self.color = color
        self.italic = italic
        self.font_weight = font_weight
        self.max_line = max_line
        self.overflow = overflow
        self.semantic_label = semantic_label
        self.text_align = text_align
        self.wrap = wrap

        # kondisi selectable
        if selectable and wrap:
            raise ValueError(
                """Selectable tidak bisa dipakai berbarengan dengan wrap,
                wrap harus di set ke false atau tidak perlu dipakai"""
            )

        if selectable and overflow:
            raise ValueError(
                """Selectable tidak bisa dipakai berbarengan dengan overflow,
                overflow harus di set ke false atau tidak perlu dipakai"""
            )

    def _get_control_name(self):
        return "flet_fonts"

    # value
    @property
    def value(self):
        """
        Value property description.
        """
        return self._get_attr("value")

    @value.setter
    def value(self, value):
        self._set_attr("value", value)

    # font_family
    @property
    def font_family(self):
        """
        font_family property description.
        """
        return self._get_attr("font_family")

    @font_family.setter
    def font_family(self, value):
        self._set_attr("font_family", value)

    # font_size
    @property
    def font_size(self):
        """
        font_size property description.
        """
        return self._get_attr("font_size")

    @font_size.setter
    def font_size(self, value):
        self._set_attr("font_size", value)

    # selectable
    @property
    def selectable(self):
        """
        selectable property description.
        """
        return self._get_attr("selectable")

    @selectable.setter
    def selectable(self, value):
        self._set_attr("selectable", value)

    # bgcolor
    @property
    def bgcolor(self) -> Optional[ColorValue]:
        """
        bgcolor property description.
        """
        return self._get_attr("bgcolor")

    @bgcolor.setter
    def bgcolor(self, value: Optional[ColorValue]):
        self._set_enum_attr("bgcolor", value, ColorEnums)

    # color
    @property
    def color(self) -> Optional[ColorValue]:
        """
        color property description.
        """
        return self._get_attr("color")

    @color.setter
    def color(self, value: Optional[ColorValue]):
        self._set_enum_attr("color", value, ColorEnums)

    # italic
    @property
    def italic(self):
        """
        italic property description.
        """
        return self._get_attr("italic")

    @italic.setter
    def italic(self, value):
        self._set_attr("italic", value)

    # font_weight
    @property
    def font_weight(self):
        """
        font_weight property description.
        """
        return self._get_attr("font_weight")

    @font_weight.setter
    def font_weight(self, value):
        self._set_attr("font_weight", value)

    # max_line
    @property
    def max_line(self):
        """
        max_line property description.
        """
        return self._get_attr("max_line")

    @max_line.setter
    def max_line(self, value):
        self._set_attr("max_line", value)

    # overflow
    @property
    def overflow(self):
        """
        overflow property description.
        """
        return self._get_attr("overflow")

    @overflow.setter
    def overflow(self, value):
        self._set_attr("overflow", value)

    # semantic_label
    @property
    def semantic_label(self):
        """
        semantic_label property description.
        """
        return self._get_attr("semantic_label")

    @semantic_label.setter
    def semantic_label(self, value):
        self._set_attr("semantic_label", value)

    # text_align
    @property
    def text_align(self):
        """
        text_align property description.
        """
        return self._get_attr("text_align")

    @text_align.setter
    def text_align(self, value):
        self._set_attr("text_align", value)

    # wrap
    @property
    def wrap(self):
        """
        wrap property description.
        """
        return self._get_attr("wrap")

    @wrap.setter
    def wrap(self, value):
        self._set_attr("wrap", value)
