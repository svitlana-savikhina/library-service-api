from rest_framework import viewsets, permissions

from books.models import Book
from books.serializers import BookSerializer, BookDetailSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action == "list":
            return [permissions.AllowAny()]
        elif self.action in [
            "create",
            "update",
            "partial_update",
            "destroy",
            "retrieve",
        ]:
            return [permissions.IsAdminUser()]

        return [permissions.IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == "list":
            return BookSerializer
        return BookDetailSerializer
