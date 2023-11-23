from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated


from borrowings.models import Borrow
from borrowings.permissions import IsOwnerOrAdminOrReadOnly
from borrowings.serializers import (
    BorrowSerializer,
    BorrowDetailSerializer,
    BorrowListSerializer,
)
from borrowings.tasks import send_borrowing_notification


class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.all().select_related("book", "user")
    serializer_class = BorrowSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdminOrReadOnly]

    def get_serializer_class(self):
        if self.action == "list":
            return BorrowListSerializer

        if self.action == "retrieve":
            return BorrowDetailSerializer
        return BorrowSerializer

    def perform_create(self, serializer: BorrowSerializer) -> None:
        borrowing = serializer.save(user=self.request.user)
        text = f"New borrowing created: book- {borrowing.book.title}, user-{borrowing.user.email}"
        send_borrowing_notification.apply_async(args=[text])
