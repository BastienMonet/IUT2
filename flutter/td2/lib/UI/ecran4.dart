import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../modele/task.dart';
import '../viewmodel/taskviewmodel.dart';

class Ecran4 extends StatelessWidget{

  final _formKey = GlobalKey<FormState>();
  var taskName = '';
  Task? task = null;

  Ecran4({super.key, this.task = null});


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Add Task'),
      ),
      body: Column(
        children: [
          ElevatedButton(
            style: ElevatedButton.styleFrom(
              foregroundColor: Colors.redAccent,
              backgroundColor: Colors.lightBlue,
            ),
            onPressed: () {
              String errorMessage = '';
              if (_formKey.currentState!.validate()) {
                if (task != null) {
                  context.read<TaskViewModel>().modifyTask(task!.id, taskName);
                } else {
                  List<Task> tasks = context.read<TaskViewModel>().liste;
                  if (tasks.where((task) => task.title == taskName).isNotEmpty){
                    errorMessage = 'une tache existe déjà avec ce même nom';
                  } else {
                    context.read<TaskViewModel>().addTask(Task.newTask(name: taskName));
                  }

                }
                if (errorMessage != ''){
                  var mySnackBar = SnackBar(
                    content: Text(errorMessage ,style: TextStyle(fontSize: 20)),
                    duration: Duration(milliseconds: 1500),
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
                Navigator.pop(context);
              }
            },
            child: const Text("Add Task"),
          ),
         Form(
          key: _formKey,
          child:  Column(
            children: [
              TextFormField(
                initialValue: task?.title ?? '',
                // The validator receives the text that the user has entered.
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter some text';
                  } else {
                    taskName = value;
                  }
                  return null;
                },
              ),

            ],
            ),
         )]
      ),
    ) ;
  }
}