from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: only owners of an expense can edit/delete it.
    Others can only read.
    """
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = GET, HEAD, OPTIONS (read-only requests)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only allow owners to edit/delete
        return obj.owner == request.user
