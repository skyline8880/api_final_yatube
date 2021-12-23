from rest_framework import permissions


class AuthOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class AuthOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class DisableChangeAlienContent(permissions.BasePermission, Exception):
    pass


class DisableDeleteAlienContent(permissions.BasePermission, Exception):
    pass
