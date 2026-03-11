<script>
import TodoItem from './components/TodoItem.vue';

let data = {
  todos: [{ text: 'Faire les courses', checked: true }, { text: 'Apprendre REST', checked: false }],
  title: 'Mes tâches',
  newItem: '',
  newTitle: '',
  maxId: 0,
  message: ''
};

export default {

  data() {
    return data;
  },
  async mounted() {
        this.updateData();
      },
  methods: {
      updateData : async function() {
        this.todos = [];
        const fetched_todo = await this.fetchTodo();
        this.maxId = fetched_todo.length;
        fetched_todo.forEach(element => {
          this.todos.push({
            text: element.title,
            checked: element.completed,
            id: element.id
          });
        })
        this.message = "data updated";
      },
      addItem: function () {
        let text = this.newItem.trim();
        if (text) {
          try {
            this.postTodo(text);
            this.todos.push({ text: text, checked: false, id: this.maxId + 1 });
            this.maxId++;
            console.log('Données envoyées :', text);
          } catch (error) {
            console.error('Erreur lors de l\'envoi des données :', error);
          }
          this.newItem = '';
        }
      },
      remove: function(id) {
        
        try {
          this.deleteTodo(id);
          this.todos = this.todos.filter(todo => String(todo.id) !== String(id));
          console.log('Données supprimées :', id);
        } catch(error) {
          console.error('Erreur lors de la suppression des données :', error);
        }
      },
      changeTitle: function() {
        this.title = this.newTitle;
      },
      fetchTodo : async function() {
          try {
              const response = await fetch('http://localhost:3000/task');
              const data = await response.json();
              console.log('Données récupérées :', data);
              return data;
          } catch (error) {
              console.error('Erreur lors de la récupération des données :', error);
          }
      },
      postTodo : async function(text) {
          try {
              const response = await fetch('http://localhost:3000/task', {
                  method: 'POST',
                  headers: {
                      'Content-Type': 'application/json'
                  },
                  body: JSON.stringify({
                      id : this.maxId + 1,
                      userId : this.maxId + 1,
                      title: text,
                      completed: false
                  })
              });
              this.maxId += 1;
              const data = await response.json();
              console.log('Données envoyées :', data);
          } catch (error) {
              console.error('Erreur lors de l\'envoi des données :', error);
          }
      },
      deleteTodo : async function(id) {
          try {
              const response = await fetch(`http://localhost:3000/task/${id}`, {
                  method: 'DELETE'
              });
              const data = await response.json();
              console.log('Données supprimées :', data);
          } catch (error) {
              console.error('Erreur lors de la suppression des données :', error);
          }
      },
      putTodo : async function(id, text, checked) {
            try {
            const response = await fetch(`http://localhost:3000/task/${id}`, {
                  method: 'PUT',
                  headers: {
                      'Content-Type': 'application/json',
                  },
                  body: JSON.stringify({
                      id : id,
                      userId : id,
                      title: text,
                      completed: !checked
                  })
              });
            const data = await response.json();
            console.log('Données mises à jour :', data);
            return data;
            } catch (error) {
                console.error('Erreur lors de la mise à jour des données :', error);
            }
     }
    },
  components: {
    TodoItem
  }


}
</script>


<template>
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
 <div  class="container">
<h2>{{ title }}</h2>
<input type="text" v-model="newTitle" @keyup.enter="changeTitle">
  <ol>
    <TodoItem v-for="todo in todos" :todo="todo" @remove="remove(todo.id)" @put="putTodo"/>
  </ol>
  <div class="input-g">
    <input v-model="newItem" 
     @keyup.enter="addItem" 
     placeholder="Ajouter une tache à la liste" 
    type="text"
    class="form-control">
    <span class="input-group-btn">
      <button @click="addItem" 
      class="btn btn-primary" 
      type="button">Ajouter</button>
    </span>
  </div>
</div>

</template>

