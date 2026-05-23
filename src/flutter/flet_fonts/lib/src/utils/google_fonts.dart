import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

/// Resolves a Google Font by [fontFamily], returning `null` when the font
/// is not found instead of throwing.
TextStyle? googleFonts(String fontFamily, {TextStyle? style}) {
  try {
    return GoogleFonts.getFont(fontFamily, textStyle: style);
  } catch (_) {
    return null;
  }
}
