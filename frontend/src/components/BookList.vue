<template>
  <div>
    <h1>Books</h1>
    <ul>
      <li v-for="book in books" :key="book.id">
        {{ book.title }} by {{ book.author }} - Stock: {{ book.stock }}
        <button @click="issueBook(book.id)">Issue</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      books: []
    }
  },
  created() {
    this.fetchBooks();
  },
  methods: {
    fetchBooks() {
      fetch('http://localhost:8000/api/books/')
        .then(response => response.json())
        .then(data => this.books = data);
    },
    issueBook(bookId) {
      fetch(`http://localhost:8000/api/issue/${bookId}/1/`, { method: 'POST' }) // Assuming member_id = 1
        .then(() => this.fetchBooks());
    }
  }
}
</script>
