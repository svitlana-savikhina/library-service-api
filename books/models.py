from django.core.exceptions import ValidationError
from django.db import models


class Book(models.Model):
    HARD = "HARD"
    SOFT = "SOFT"

    COVER_CHOICES = [
        (HARD, "Hardcover"),
        (SOFT, "Softcover"),
    ]
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover = models.CharField(max_length=4, choices=COVER_CHOICES)
    inventory = models.PositiveIntegerField()
    daily_fee = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.title}"

    def clean(self):
        super().clean()
        if self.inventory == 0:
            raise ValidationError("Inventory cannot be 0.")

    def save(self, *args, **kwargs):
        self.clean()
        super(Book, self).save(*args, **kwargs)
