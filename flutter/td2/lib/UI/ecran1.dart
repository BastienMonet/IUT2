import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:td2/UI/ecran4.dart';

import '../modele/task.dart';
import '../viewmodel/taskviewmodel.dart';

class Ecran1 extends StatelessWidget{
  late List<Task> tasks;
  //= Task.generateTask(50);
  String tags='';
  @override
  Widget build(BuildContext context) {
    tasks = context.watch<TaskViewModel>().liste;
    return Scaffold(
        body : ListView.builder(
            itemCount: tasks.length,
            itemBuilder: (context, index) {
              return Row(
                children: [
                  Text(tasks[index].title),
                  ElevatedButton(
                      onPressed: () {
                        context.read<TaskViewModel>().deleteTask(tasks[index].id);
                        const mySnackBar = SnackBar(
                          content: Text("tache supprimer",style: TextStyle(fontSize: 20)),
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
                      },
                      child: Text("supprimer")),
                  ElevatedButton(
                      onPressed: () {
                        Navigator.push(context, MaterialPageRoute(
                          builder: (context) => Ecran4(task : tasks[index]),
                        ));
                      },
                      child: Text("Modifier")
                  )],
              );

            }),
        floatingActionButton: FloatingActionButton(
          onPressed: (){
            Navigator.push(context, MaterialPageRoute(
              builder: (context) => Ecran4(),
            )
            );
          },
          child: const Icon(Icons.add),
        )
    );
  }
}