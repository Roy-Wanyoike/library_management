<template>
    <div>
        <h2>Edit Book</h2>
        <input v-model="bookId" placeholder="Book ID" />
        <input v-model="title" placeholder="New Title" />
        <input v-model="author" placeholder="New Author" />
        <input v-model="stock" type="number" placeholder="New Stock" />
        <button @click="editBook">Edit Book</button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            bookId: '',
            title: '',
            author: '',
            stock: 0
        };
    },
    methods: {
        editBook() {
            fetch(`http://localhost:8000/api/books/${this.bookId}/`, {
                method: 'PUT',
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
                    alert('Book updated successfully');
                });
        }
    }
};
</script>
