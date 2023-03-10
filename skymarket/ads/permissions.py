from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = 'You are not an owner.'

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
