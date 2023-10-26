from django.db import models

from books.models import Book
from users.models import User


class Borrow(models.Model):
    borrow_date = models.DateField(auto_now_add=True)
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"Book {self.book.title} must be returned on {self.expected_return_date} by user {self.user.username}"
