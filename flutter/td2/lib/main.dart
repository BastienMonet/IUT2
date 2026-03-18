import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:td2/UI/ecran4.dart';
import 'package:td2/viewmodel/settingViewModel.dart';
import 'package:td2/viewmodel/taskviewmodel.dart';
import 'UI/mytheme.dart';
import 'UI/ecran1.dart';
import 'UI/ecran2.dart';
import 'UI/ecran3.dart';


void main() {
  runApp(WidgetIdk());
}

class WidgetIdk extends StatelessWidget {
  WidgetIdk({super.key});


  @override
  Widget build(BuildContext context) {
    return MultiProvider(
        providers: [
          ChangeNotifierProvider(create: (_) {
            SettingViewModel settingviewmodel = SettingViewModel();
            return settingviewmodel;
          }),
          ChangeNotifierProvider(
              create:(_){
                TaskViewModel taskViewModel = TaskViewModel();
                taskViewModel.generateTasks();
                return taskViewModel;
              } )
        ],
        child: Consumer<SettingViewModel>(
            builder: (context, SettingViewModel notifier, child) {
              return MaterialApp(
                  theme: notifier.isDark ? MyTheme.dark() : MyTheme.light(),
                  home: MyHomePage(title: "hello")
              );
            }
        ));
  }
}


class MyHomePage extends StatefulWidget {

  final String title;

  const MyHomePage({super.key,required this.title});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _selectedIndex = 0;
  final List<Widget> _pages = [
    new Ecran1(), new Ecran2(), new Ecran3(), new Ecran4()
  ];

  void _toogleIndex(int idx) {
    setState(() {
      _selectedIndex = idx;
    });
  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
          appBar : AppBar(
              title: Text("TD 2", style : Theme.of(context).appBarTheme.titleTextStyle)
          ),
          body : Center(
              child: _pages[_selectedIndex]
          ),
          bottomNavigationBar: BottomNavigationBar(
              items: <BottomNavigationBarItem> [
                BottomNavigationBarItem(icon: Icon(Icons.fireplace),label: '1'),
                BottomNavigationBarItem(icon: Icon(Icons.transgender),label : '2'),
                BottomNavigationBarItem(icon: Icon(Icons.sanitizer), label : '3'),
              ],
              onTap: _toogleIndex
          )
      );
    }
  }



