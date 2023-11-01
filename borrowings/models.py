from datetime import date

from django.db import models

from books.models import Book
from users.models import User


class Borrow(models.Model):
    borrow_date = models.DateField()
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    @property
    def is_active(self):
        today = date.today()
        return self.actual_return_date is None or self.actual_return_date >= today

    def save(self, *args, **kwargs):
        super(Borrow, self).save(*args, **kwargs)
        if self.actual_return_date:
            self.book.inventory += 1
            self.book.save()
        else:
            self.book.inventory -= 1
            self.book.save()
