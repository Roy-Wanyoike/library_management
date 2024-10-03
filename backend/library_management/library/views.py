from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Member, Transaction


def list_books(request):
    books = Book.objects.all()
    return render(request, "library/books.html", {"books": books})


def issue_book(request, book_id, member_id):
    book = get_object_or_404(Book, id=book_id)
    member = get_object_or_404(Member, id=member_id)

    if book.stock > 0:
        book.stock -= 1
        book.save()
        Transaction.objects.create(
            member=member, book=book, rent_fee=100
        )  # Example rent fee
    return redirect("list_books")


def return_book(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    transaction.return_date = timezone.now()

    # Calculate fees
    if transaction.rent_fee > 0:
        transaction.member.outstanding_debt += transaction.rent_fee
        transaction.member.save()

    # Update stock
    transaction.book.stock += 1
    transaction.book.save()
    transaction.save()
    return redirect("list_books")
