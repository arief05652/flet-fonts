import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

// get google font
TextStyle googleFonts(String fontFamily, {TextStyle? style}) {
  return GoogleFonts.getFont(fontFamily, textStyle: style);
}
