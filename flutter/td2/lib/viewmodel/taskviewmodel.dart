import 'package:flutter/cupertino.dart';

import '../modele/task.dart';

class TaskViewModel extends ChangeNotifier{
  late List<Task> liste;

  TaskViewModel(){
    liste=[];
  }
  void addTask(Task task){
    liste.add(task);
    notifyListeners();
  }
  void modifyTask(int id, String newTitle){
    for (Task task in liste) {
      if (task.id == id && task.title != newTitle) {
        task.title = newTitle;
      }
    }
    notifyListeners();
  }


  void deleteTask(id){
    for (Task task in liste) {
      if (task.id == id) {
        liste.remove(task);
        return;
      }
    }
    notifyListeners();
  }
  void generateTasks(){
    liste = Task.generateTask(50);
    notifyListeners();
  }
}