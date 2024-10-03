<template>
    <div>
        <h2>Search Book</h2>
        <input v-model="searchQuery" placeholder="Search by name or author" />
        <button @click="searchBook">Search</button>

        <div v-if="books.length">
            <h3>Results</h3>
            <ul>
                <li v-for="book in books" :key="book.id">
                    {{ book.title }} by {{ book.author }} - Stock: {{ book.stock }}
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            searchQuery: '',
            books: []
        };
    },
    methods: {
        searchBook() {
            fetch(`http://localhost:8000/api/books/?search=${this.searchQuery}`)
                .then(response => response.json())
                .then(data => this.books = data);
        }
    }
};
</script>
