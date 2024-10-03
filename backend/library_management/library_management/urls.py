from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.list_books, name="list_books"),
    path("issue/<int:book_id>/<int:member_id>/", views.issue_book, name="issue_book"),
    path("return/<int:transaction_id>/", views.return_book, name="return_book"),
]
