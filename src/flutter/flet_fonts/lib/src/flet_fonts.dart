import 'package:flet/flet.dart';
import 'package:flutter/material.dart';

import 'utils/text_span.dart';
import 'utils/google_fonts.dart';

class FletFontsControl extends StatelessWidget {
  final Control control;

  const FletFontsControl({super.key, required this.control});

  @override
  Widget build(BuildContext context) {
    control.notifyParent = true;

    // theme context
    final theme = Theme.of(context);

    // attr from py
    var value = control.getString("value", "");
    var spans = control.children("spans");
    var google_fonts = control.getString("google_fonts");
    var text_align = control.getTextAlign("text_align");
    var style = control.getTextStyle("style", theme);
    var max_lines = control.getInt("max_lines");
    var selectable = control.getBool("selectable", false)!;
    var no_wrap = control.getBool("no_wrap", false)!;
    var semantics_label = control.getString("semantics_label");
    var show_selection_cursor =
        control.getBool("show_selection_cursor", false)!;
    var enable_interactive_selection =
        control.getBool("enable_interactive_selection", true)!;
    var selection_cursor_width =
        control.getDouble("selection_cursor_width", 2.0)!;
    var selection_cursor_height = control.getDouble("selection_cursor_height");
    var selection_cursor_color =
        control.getColor("selection_cursor_color", context);

    Widget widget = SizedBox.shrink();

    // jika selectable
    if (selectable) {
      // cek spans jika ada
      if (spans.isNotEmpty) {
        widget = SelectableText.rich(
          TextSpan(
              text: value,
              style: (google_fonts != null)
                  ? googleFonts(google_fonts, style: style)
                  : style,
              semanticsLabel: semantics_label,
              children: parseSpans(spans, context)),
          maxLines: max_lines,
          textAlign: text_align,
          showCursor: show_selection_cursor,
          enableInteractiveSelection: enable_interactive_selection,
          cursorWidth: selection_cursor_width,
          cursorHeight: selection_cursor_height,
          cursorColor: selection_cursor_color,
        );
        // ga ada spans tapi selectable
      } else {
        widget = SelectableText(
          value!,
          style: (google_fonts != null)
              ? googleFonts(google_fonts, style: style)
              : style,
          maxLines: max_lines,
          textAlign: text_align,
          showCursor: show_selection_cursor,
          enableInteractiveSelection: enable_interactive_selection,
          cursorWidth: selection_cursor_width,
          cursorHeight: selection_cursor_height,
          cursorColor: selection_cursor_color,
        );
      }
      // tidak selectable tapi spans
    } else {
      if (spans.isNotEmpty) {
        widget = Text.rich(
          TextSpan(
              text: value,
              style: (google_fonts != null)
                  ? googleFonts(google_fonts, style: style)
                  : style,
              semanticsLabel: semantics_label,
              children: parseSpans(spans, context)),
          style: (google_fonts != null)
              ? googleFonts(google_fonts, style: style)
              : style,
          maxLines: max_lines,
          textAlign: text_align,
          semanticsLabel: semantics_label,
          softWrap: !no_wrap,
        );
        // tidak selectable dan tidak spans
      } else {
        widget = Text(
          value!,
          style: (google_fonts != null)
              ? googleFonts(google_fonts, style: style)
              : style,
          maxLines: max_lines,
          textAlign: text_align,
          semanticsLabel: semantics_label,
          softWrap: !no_wrap,
        );
      }
    }

    return LayoutControl(
      control: control,
      child: widget,
    );
  }
}
