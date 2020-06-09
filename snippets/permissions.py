from rest_framework import permissions
from rest_framework import status


class IsOwnerOrReadOnly(permissions.BasePermission):
    """

    Custom permission to only allow the owner of an objet to edit it.
    """
    
    def has_object_permission(self, request, view, obj):
        # Read perms are allowed to any request,
        # so we'll always allow GET, HEAD, or options requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write perms are only allowed to owner to the owner of the snippet.
        return obj.owner == request.user