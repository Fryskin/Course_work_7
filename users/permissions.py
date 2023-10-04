from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_permission(self, request, view):

        return request.user == view.get_object().user


class IsAuthenticated(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

        return False
