<script>

export default{
    props: {
    todo : Object
    },
    methods:{
        handleChecked : function(id) {
            this.$emit('put', id, this.todo.text, this.todo.checked);
        },
    },
    emits : ['remove', 'put']
}

</script>

<template>
    <li :class="{ 'alert alert-success': todo.checked }">
        <label>{{todo.text}}
            <input type="checkbox" v-model="todo.checked" @click="handleChecked(todo.id)">
            <button @click="$emit('remove')"> X </button>
        </label>
    </li>
</template>