import 'package:flutter/material.dart';
import 'package:tp1/UI/home.dart';
import 'package:tp1/UI/scafold.dart';
void main() {
  runApp(MaterialApp(
      theme: ThemeData(
          elevatedButtonTheme: ElevatedButtonThemeData(
              style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.blueGrey.shade900,
                  padding: const EdgeInsets.symmetric(horizontal: 20),
                  shape: const RoundedRectangleBorder(
                    borderRadius: BorderRadius.all(Radius.circular(20)),
                  ))
          )),
      debugShowCheckedModeBanner: false,
      title: "Application Quizz",
      home: const
      MyWidget2(Colors.teal,40.0,"Message super super super super super long du widget")
  ));
}