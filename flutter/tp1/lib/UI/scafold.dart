import 'package:flutter/material.dart';
import '../modele/Question.dart';
import 'myButton.dart';
import 'myInputButton.dart';
class IndexChanged extends Notification{
  final int val;
  IndexChanged(this.val);
}

class MyWidget2 extends StatefulWidget{
  final Color color;
  final double textsize;
  final String message;
  const MyWidget2(this.color,this.textsize,this.message);

  @override
  State<MyWidget2> createState() => _MyWidget2State();
}

class _MyWidget2State extends State<MyWidget2> {

  int score = 0;
  int _currentQuestion = 0;
  final List _questions = [Question.name("The question number 1 is a very long question and her answer is true.", true, "flag.png"),
    Question.name("The question number 2 is true again.", true,
        "img.png"),
    Question.name("The question number 3 is false.", false, "img.png"),
    Question.name("The question number 4 is false again.", false,
        "flag.png"),
    Question.name("The question number 5 is true.", true, "flag.png")];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text("Quizz App"),
          centerTitle: true,
          backgroundColor: Colors.lightBlue,
        ),
        backgroundColor: widget.color,
        body: NotificationListener<IndexChanged>(
          child: Center (
            child : Column(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [Text(
                    _questions[_currentQuestion].questionText,
                    textDirection: TextDirection.ltr,
                    style: TextStyle(
                      color: Colors.white,
                      fontWeight: FontWeight.bold,
                      fontStyle: FontStyle.italic,
                      fontSize: widget.textsize,
                    )
                ),
                  Image.asset("images/${_questions[_currentQuestion].image}",
                  width: 250, height: 180,),
                  Row(
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                      children: [
                        MyIconButton(myIcon: Icons.arrow_back, value: -1),
                        MyTextButton(
                            myText: "TRUE", myValue: true, returnValue: _handleValue),
                        MyTextButton(
                            myText: "FALSE", myValue: false, returnValue: _handleValue),
                        MyIconButton(myIcon: Icons.arrow_forward, value: 1),
                      ])
                ])),
            onNotification: (n){
              _changeQuestion(n.val);
              return true;
            },
        ));
  }

  _nextQuestion() {
    setState(() {
      if (_currentQuestion+1 != _questions.length){
        _currentQuestion = (_currentQuestion+1);
      }

    });
  }

  void _handleValue(bool value) {
    debugPrint(value.toString());
    if (value == _questions[_currentQuestion].isCorrect) {
      debugPrint("good");
      const mySnackBar = SnackBar(
        content: Text("GOOD ANSWER!!!",style: TextStyle(fontSize: 20)),
        duration: Duration(milliseconds: 500),
        backgroundColor: Colors.lightGreen,
        width: 180.0, // Width of the SnackBar.
        padding: EdgeInsets.symmetric(
          horizontal: 8.0, // Inner padding for SnackBar content.
        ),
        behavior: SnackBarBehavior.floating,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.all(Radius.circular(20)),
        ),);
      ScaffoldMessenger.of(context).showSnackBar(mySnackBar);
    } else {
      debugPrint("bad");
      const mySnackBar = SnackBar(
        content: Text("BAD ANSWER!!!",style: TextStyle(fontSize: 20),),
        duration: Duration(milliseconds: 500),
        backgroundColor: Colors.red,
        width: 180.0, // Width of the SnackBar.
        padding: EdgeInsets.symmetric(
          horizontal: 8.0, // Inner padding for SnackBar content.
        ),
        behavior: SnackBarBehavior.floating,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.all(Radius.circular(20)),
        ),);
      ScaffoldMessenger.of(context).showSnackBar(mySnackBar);
    }
    _nextQuestion();
  }

  _changeQuestion(int n){
    setState(() {
      if (_currentQuestion + n >= 0 && _currentQuestion + n < _questions.length){
        _currentQuestion = (_currentQuestion + n) %_questions.length;
      }

    });
  }
}