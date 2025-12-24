import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

TextStyle get_google_font(
    {String? fontFamily,
    double? fontSize,
    Color? bgColor,
    Color? color,
    FontStyle? italic,
    String? font_weight}) {
  // jika `fontFamily` null pakai "Lato"
  final getFont =
      (fontFamily == null || fontFamily.isEmpty) ? "Lato" : fontFamily;

  // passing font weight
  final Map<String, FontWeight> getStyle = {
    "bold": FontWeight.bold,
    "normal": FontWeight.normal,
    "w100": FontWeight.w100,
    "w200": FontWeight.w200,
    "w300": FontWeight.w300,
    "w400": FontWeight.w400,
    "w500": FontWeight.w500,
    "w600": FontWeight.w600,
    "w700": FontWeight.w700,
    "w800": FontWeight.w800,
    "w900": FontWeight.w900,
  };

  // pakai dynamic get font untuk mencari font ada
  return GoogleFonts.getFont(
    getFont,
    fontSize: fontSize,
    backgroundColor: bgColor,
    color: color,
    fontStyle: italic,
    fontWeight: getStyle[font_weight],
  );
}
