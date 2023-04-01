from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        if request.user.is_superuser and request.user.is_staff:
            return True
        return request.user == obj.creator
