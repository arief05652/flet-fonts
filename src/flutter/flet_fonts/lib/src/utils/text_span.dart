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
  var text = span.getString("value");
  var google_fonts = span.getString("google_fonts", "ADLaM Display")!;
  var style = span.getTextStyle("style", theme);

  /** handle error jika font tidak ada
  gapakai return dari `ErrorControl` karna harus mengembalikan `TextSpan`
  */
  var fonts = googleFonts(google_fonts, style: style);
  if (fonts == null) {
    return TextSpan(
        text: "\nThe ${google_fonts} font cannot be found.",
        style: TextStyle(color: Colors.white, backgroundColor: Colors.red));
  }

  return TextSpan(
      text: text,
      children: parseSpans(span.children("spans"), context),
      style: googleFonts(google_fonts, style: style),
      semanticsLabel: span.getString("semantic_label"));
}
