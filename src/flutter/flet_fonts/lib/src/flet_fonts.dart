import 'package:flet/flet.dart';
import 'package:flutter/material.dart';

import 'get_font.dart';

class FletFontsControl extends StatelessWidget {
  final Control? parent;
  final Control control;

  const FletFontsControl({
    super.key,
    required this.parent,
    required this.control,
  });

  @override
  Widget build(BuildContext context) {
    // ambil argumen
    final text = control.attrString("value", "")!;
    final String? fontFamily = control.attrString('font_family');
    final fontSize = control.attrDouble('font_size');
    final selectableText = control.attrBool("selectable", false);
    final bgColor = control.attrColor('bgcolor', context);
    final color = control.attrColor('color', context);
    final italic = control.attrBool('italic', false);
    final String? font_weight = control.attrString('font_weight')!;
    final int? max_line = control.attrInt('max_line');
    final String? overflow = control.attrString('overflow');
    final String? text_align = control.attrString("text_align");
    final String? semantic_label = control.attrString("semantic_label");
    final bool? wrap = control.attrBool("wrap", true);

    // text widget
    Widget textWidget;

    // kondisi untuk italic style
    final getItalic = (italic == false) ? FontStyle.normal : FontStyle.italic;

    // passing text overflow
    final Map<String, TextOverflow>? getOverFlow = {
      "fade": TextOverflow.fade,
      "elipsis": TextOverflow.ellipsis,
      "clip": TextOverflow.clip,
      "visible": TextOverflow.visible,
    };

    // passing text text align
    final Map<String, TextAlign>? getTextAlign = {
      "start": TextAlign.start,
      "center": TextAlign.center,
      "end": TextAlign.end,
      "justify": TextAlign.justify,
      "left": TextAlign.left,
      "right": TextAlign.right,
    };

    // kondisi untuk selectable text
    if (selectableText == true) {
      textWidget = SelectableText(
        text,
        maxLines: max_line,
        textAlign: (text_align != null) ? getTextAlign![text_align] : null,
        semanticsLabel: semantic_label,
        style: get_google_font(
            fontFamily: fontFamily,
            fontSize: fontSize,
            bgColor: bgColor,
            color: color,
            italic: getItalic,
            font_weight: font_weight),
      );
    } else {
      textWidget = Text(
        text,
        maxLines: max_line,
        softWrap: wrap,
        textAlign: (text_align != null) ? getTextAlign![text_align] : null,
        overflow: (overflow != null) ? getOverFlow![overflow] : null,
        semanticsLabel: semantic_label,
        style: get_google_font(
            fontFamily: fontFamily,
            fontSize: fontSize,
            bgColor: bgColor,
            color: color,
            italic: getItalic,
            font_weight: font_weight),
      );
    }

    return constrainedControl(context, textWidget, parent, control);
  }
}
