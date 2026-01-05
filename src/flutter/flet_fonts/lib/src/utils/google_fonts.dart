import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

// get google font
dynamic googleFonts(String fontFamily, {TextStyle? style}) {
  try {
    return GoogleFonts.getFont(fontFamily, textStyle: style);
  } catch (_) {
    return null;
  }
}
