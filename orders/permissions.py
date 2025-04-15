from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthenticatedForCreate(BasePermission):
    """
    Allows anyone to view (GET), but only authenticated users can create/update/delete.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        return request.user and request.user.is_authenticated
