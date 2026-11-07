import 'package:flet/flet.dart';
import 'package:material_ui/material_ui.dart';

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
