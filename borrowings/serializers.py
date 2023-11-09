from rest_framework import serializers

from books.serializers import BookSerializer
from borrowings.models import Borrow
from users.serializers import UserSerializer


class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = (
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book",
            "user",
            "is_active",
        )


class BorrowDetailSerializer(BorrowSerializer):
    book = BookSerializer(many=False, read_only=True)
    user = UserSerializer(many=False, read_only=True)


class BorrowListSerializer(BorrowSerializer):
    book = serializers.SlugRelatedField(many=False, read_only=True, slug_field="title")
    user = serializers.SlugRelatedField(many=False, read_only=True, slug_field="email")
