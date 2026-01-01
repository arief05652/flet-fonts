import 'package:flutter/material.dart';
import 'package:flet/flet.dart';

import './google_fonts.dart';

// convert list span to map/dict
List<TextSpan> parseSpans(List<Control> spans, BuildContext context) {
  return spans.map((span) => parseText(span, context)).toList();
}

// parsing per each span
TextSpan parseText(Control span, BuildContext context) {
  final theme = Theme.of(context);
  var google_fonts = span.getString("google_fonts");
  var style = span.getTextStyle("style", theme);

  return TextSpan(
      text: span.getString("value"),
      children: parseSpans(span.children("spans"), context),
      style: (google_fonts != null)
          ? googleFonts(google_fonts, style: style)
          : style,
      semanticsLabel: span.getString("semantic_label"));
}
