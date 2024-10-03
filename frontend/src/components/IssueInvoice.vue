<template>
    <div>
        <h2>Issue Invoice</h2>
        <input v-model="memberId" placeholder="Member ID" />
        <input v-model="bookId" placeholder="Book ID" />
        <button @click="issueInvoice">Issue Invoice</button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            memberId: '',
            bookId: ''
        };
    },
    methods: {
        issueInvoice() {
            fetch('http://localhost:8000/api/transactions/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    member: this.memberId,
                    book: this.bookId,
                    rent_fee: 100 // Example fee
                })
            })
                .then(response => response.json())
                .then(data => {
                    alert('Invoice issued successfully');
                });
        }
    }
};
</script>
