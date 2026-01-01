import 'package:flutter/material.dart';

// get font
final Map<String, FontWeight> getWeight = {
  "BOLD": FontWeight.bold,
  "NORMAL": FontWeight.normal,
  "W_100": FontWeight.w100,
  "W_200": FontWeight.w200,
  "W_300": FontWeight.w300,
  "W_400": FontWeight.w400,
  "W_500": FontWeight.w500,
  "W_600": FontWeight.w600,
  "W_700": FontWeight.w700,
  "W_800": FontWeight.w800,
  "W_900": FontWeight.w900,
};

FontWeight? font_weight([String? weight]) {
  if (weight == null) {
    return null;
  }

  return getWeight[weight];
}
