<template>
    <div>
        <h2>Add New Book</h2>
        <input v-model="title" placeholder="Book Title" />
        <input v-model="author" placeholder="Author" />
        <input v-model="stock" type="number" placeholder="Stock" />
        <button @click="addBook">Add Book</button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            title: '',
            author: '',
            stock: 0
        };
    },
    methods: {
        addBook() {
            fetch('http://localhost:8000/api/books/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    title: this.title,
                    author: this.author,
                    stock: this.stock
                })
            })
                .then(response => response.json())
                .then(data => {
                    alert('Book added successfully');
                    this.title = '';
                    this.author = '';
                    this.stock = 0;
                });
        }
    }
};
</script>
