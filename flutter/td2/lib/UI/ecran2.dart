import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:td2/api/api.dart';

import '../modele/task.dart';

class Ecran2 extends StatelessWidget {
  Ecran2({super.key});

  final _api = new MyAPI();

  @override
  Widget build(BuildContext context) {
    return Center(
      child : FutureBuilder(
          future: _api.getTasks(),
          builder: (context, snapshot) {
            if (snapshot.hasData) {
              List<Task>? tasks = snapshot.data;
              if (tasks != null){
                return ListView.builder(
                  itemCount: tasks.length,
                  itemBuilder: (BuildContext context, int index) {
                    return ListTile(
                        title: Text(tasks[index].title)
                    );
                  },

                );
              }
              }
            else if (snapshot.hasError) {
              return Text("error :${snapshot.error}");
            }
            return CircularProgressIndicator();
          }
      )
    );
  }

}