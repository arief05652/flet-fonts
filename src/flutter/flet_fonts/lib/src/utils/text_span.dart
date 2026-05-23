import 'package:flutter/material.dart';
import 'package:flet/flet.dart';

import './google_fonts.dart';

/// Parses a list of span controls into [TextSpan] widgets.
List<TextSpan> parseSpans(List<Control> spans, BuildContext context) {
  return spans.map((span) => parseText(span, context)).toList();
}

/// Parses a single span control into a [TextSpan].
///
/// Returns an error [TextSpan] with red background when the requested
/// Google Font is not found.
TextSpan parseText(Control span, BuildContext context) {
  final theme = Theme.of(context);
  final text = span.getString("text");
  final googleFontName = span.getString("google_fonts", "ADLaM Display")!;
  final style = span.getTextStyle("style", theme);

  final font = googleFonts(googleFontName, style: style);
  if (font == null) {
    return TextSpan(
      text: "\nThe $googleFontName font cannot be found.",
      style: TextStyle(color: Colors.white, backgroundColor: Colors.red),
    );
  }

  return TextSpan(
    text: text,
    style: font,
    children: parseSpans(span.children("spans"), context),
    semanticsLabel: span.getString("semantic_label"),
    spellOut: span.getBool("spell_out"),
  );
}
