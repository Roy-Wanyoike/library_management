<template>
    <div>
        <h2>Add New Member</h2>
        <input v-model="name" placeholder="Member Name" />
        <input v-model="email" placeholder="Member Email" />
        <button @click="addMember">Add Member</button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            name: '',
            email: ''
        };
    },
    methods: {
        addMember() {
            fetch('http://localhost:8000/api/members/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    name: this.name,
                    email: this.email
                })
            })
                .then(response => response.json())
                .then(data => {
                    alert('Member added successfully');
                    this.name = '';
                    this.email = '';
                });
        }
    }
};
</script>
