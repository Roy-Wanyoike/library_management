<template>
  <div id="app" class="container">
    <header class="header">
      <h1>Library Management System</h1>
    </header>

    <section class="section">
      <div class="grid-container">
        <div class="grid-item">
          <BookSearch />
        </div>
        <div class="grid-item">
          <AddBook />
        </div>
        <div class="grid-item">
          <AddMember />
        </div>
        <div class="grid-item">
          <EditBook />
        </div>
        <div class="grid-item">
          <IssueInvoice />
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import BookSearch from './components/BookSearch.vue';
import AddBook from './components/AddBook.vue';
import AddMember from './components/AddMember.vue';
import EditBook from './components/EditBook.vue';
import IssueInvoice from './components/IssueInvoice.vue';

export default {
  components: {
    BookSearch,
    AddBook,
    AddMember,
    EditBook,
    IssueInvoice
  }
};
</script>

<style scoped>
/* General page styling */
.container {
  font-family: Arial, sans-serif;
  margin: 20px;
  padding: 20px;
  background-color: #f7f7f7;
  border-radius: 8px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

.header {
  text-align: center;
  margin-bottom: 40px;
}

.header h1 {
  color: #4a90e2;
  font-size: 2.5rem;
  margin: 0;
}

/* Grid for components */
.grid-container {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 20px;
}

.grid-item {
  padding: 20px;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.1);
}

/* Inputs and buttons */
input {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border-radius: 4px;
  border: 1px solid #ccc;
}

button {
  width: 100%;
  padding: 12px;
  background-color: #4a90e2;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
}

button:hover {
  background-color: #357abd;
}

h2 {
  font-size: 1.5rem;
  color: #333;
  margin-bottom: 15px;
}

/* Styling for sections */
.section {
  margin-bottom: 40px;
}

.section h3 {
  font-size: 1.3rem;
  color: #555;
}

ul {
  padding: 0;
  list-style-type: none;
}

li {
  padding: 10px;
  border-bottom: 1px solid #eee;
}

li:last-child {
  border-bottom: none;
}
</style>
