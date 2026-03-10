import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../viewmodel/settingViewModel.dart';
import 'mytheme.dart';
import 'package:settings_ui/settings_ui.dart';


class Ecran3 extends StatefulWidget {
  const Ecran3({super.key});

  @override
  State<Ecran3> createState() => _Ecran3State();
}

class _Ecran3State extends State<Ecran3> {
  bool _dark =true;
  @override
  Widget build(BuildContext context) {
    return Center(
      child: SettingsList(
        darkTheme: SettingsThemeData(
            settingsListBackground: MyTheme.dark().scaffoldBackgroundColor,
            settingsSectionBackground:
            MyTheme.dark().scaffoldBackgroundColor
        ),
        lightTheme: SettingsThemeData(
            settingsListBackground: MyTheme.light().scaffoldBackgroundColor,
            settingsSectionBackground:
            MyTheme.light().scaffoldBackgroundColor
        ),
        sections: [
          SettingsSection(
              title: const Text('Theme'),
              tiles: [
                SettingsTile.switchTile(
                  initialValue: context.watch<SettingViewModel>().isDark,
                  onToggle: (bool value) {
                    context.read<SettingViewModel>().isDark = value;
                  },
                  title: const Text('Dark mode'),
                  leading: const Icon(Icons.invert_colors),)
              ])
        ],
      ),
    );
  }
}