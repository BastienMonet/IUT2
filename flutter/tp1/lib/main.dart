import 'package:flutter/material.dart';
void main() {
  runApp(MaterialApp(
      debugShowCheckedModeBanner: false,
      title: "Application Quizz",
      home: Material( //Widget générique
          color: Colors.teal,
          shape:
          RoundedRectangleBorder(borderRadius:BorderRadius.circular(50.0) ),
          child: const Column (
                children : [
                  Text(
                    "Hello world !!",
                    textDirection: TextDirection.ltr,
                    style: TextStyle(
                      color: Colors.white,
                      fontWeight: FontWeight.bold,
                      fontStyle: FontStyle.italic,
                      fontSize: 35.0,
                    )),
                  Text("je suis noir")
                ]
              ),
              )));
}