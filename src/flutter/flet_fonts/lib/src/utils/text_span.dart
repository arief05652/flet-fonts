import 'package:material_ui/material_ui.dart';
import 'package:flet/flet.dart';

import './google_fonts.dart';

/// Parses a list of span controls into [TextSpan] widgets.
///
/// Spans without a `google_fonts` value inherit [parentStyle].
List<TextSpan> parseSpans(List<Control> spans, BuildContext context,
    {TextStyle? parentStyle}) {
  return spans
      .map((span) => parseText(span, context, parentStyle: parentStyle))
      .toList();
}

/// Parses a single span control into a [TextSpan].
///
/// Returns an error [TextSpan] with red background when the requested
/// Google Font is not found.
TextSpan parseText(Control span, BuildContext context,
    {TextStyle? parentStyle}) {
  final theme = Theme.of(context);
  final text = span.getString("text");
  final googleFontName = span.getString("google_fonts");
  final style = span.getTextStyle("style", theme);

  final TextStyle? font;
  if (googleFontName == null) {
    // No font on this span: inherit the parent's resolved font.
    font = parentStyle == null
        ? style
        : (style == null ? parentStyle : parentStyle.merge(style));
  } else {
    font = googleFonts(googleFontName, style: style ?? parentStyle);
    if (font == null) {
      return TextSpan(
        text: "\nThe $googleFontName font cannot be found.",
        style: TextStyle(color: Colors.white, backgroundColor: Colors.red),
      );
    }
  }

  return TextSpan(
    text: text,
    style: font,
    children: parseSpans(span.children("spans"), context, parentStyle: font),
    semanticsLabel: span.getString("semantic_label"),
    spellOut: span.getBool("spell_out"),
  );
}
