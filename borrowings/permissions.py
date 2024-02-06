from rest_framework import permissions


class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    """
    Users can only edit their own objects
    """

    def has_object_permission(self, request, view, obj):
        if (request.method in permissions.SAFE_METHODS) and request.user.is_staff:
            return True
        return obj.user == request.user
