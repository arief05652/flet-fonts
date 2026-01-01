import 'package:flet/flet.dart';
import 'package:flutter/material.dart';

import 'flet_fonts.dart';

class Extension extends FletExtension {
  @override
  Widget? createWidget(Key? key, Control control) {
    switch (control.type) {
      case "FletFonts":
        return FletFontsControl(control: control);
      default:
        return null;
    }
  }
}
