from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        # read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissions are allowed only to the author of the post
        return obj.author == request.user
