import 'package:flutter/material.dart';
class MyWidget extends StatelessWidget{
  final Color color;
  final double textsize;
  final String message;
  const MyWidget(this.color,this.textsize,this.message);
  @override
  Widget build(BuildContext context) {
    return Material(
        color: color,
        shape:
        RoundedRectangleBorder(borderRadius:BorderRadius.circular(50.0) ),
        child: Center(
            child: Text(
                message,
                textDirection: TextDirection.ltr,
                style: TextStyle(
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                  fontStyle: FontStyle.italic,
                  fontSize: textsize,
                ),
            )));
  }
}