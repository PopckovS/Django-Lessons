from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrStaffOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        """
        Переопределяем права доступа.

        Даем все права на запись, только владельцу или
        администратору, на чтение даем право всем.
        Возвращаем `True` если есть разрешение, `False` если нет.
        """
        return bool(
            request.method in SAFE_METHODS
            or
            request.user and request.user.is_authenticated
            and
            (obj.owner == request.user or request.user.is_superuser)
        )

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )
