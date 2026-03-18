class Task {
  int id;
  String title;
  List<String> tags;
  int nbhours;
  int difficuty;
  String description;
  static int nb = 0;

  Task({required this.id,required this.title,required this.tags,required
  this.nbhours,required this.difficuty,required this.description});
  static List<Task> generateTask(int i){
    List<Task> tasks=[];
    for(int n=0;n<i;n++){
      nb++;
      tasks.add(Task(id: n, title: "title $n", tags: ['tag $n','task${n+1}'], nbhours: n, difficuty: n, description: '$n'));
          }
          return tasks;
      }


  static Task fromJson(Map<String, dynamic> element) {
    final tags = <String>[];

    if (element['tags']!=null){
      element['tags'].forEach((t){
        tags.add(t);
      });
    }
    return Task(id : element['id'], title : element['title'], tags : tags, nbhours :element['nbhours'], difficuty : element['difficulty'], description : element['description']);
  }

  factory Task.newTask({String name = ''}){
    nb++; //attribut static de la classe.
    if (name == ''){
      name = nb.toString();
    }
    return Task(id: nb, title: '$name', tags: ['tags $nb'], nbhours: nb, difficuty: nb%5, description: 'description $nb');
  }
}