import 'scafold.dart';
import 'package:flutter/material.dart';
class MyIconButton extends StatelessWidget{
  IconData myIcon;
  int value;
  MyIconButton({required this.myIcon,required this.value});
  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: () => IndexChanged(value).dispatch(context),
      child: Icon(
        myIcon,
        color: Colors.white,
      ),
    );
  }
}