from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "title", "author", "daily_fee")


class BookDetailSerializer(BookSerializer):
    class Meta:
        model = Book
        fields = "__all__"
