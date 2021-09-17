# Импорт класса привилегий и безопасных методов HTTP запроса
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrStaffOrReadOnly(BasePermission):
    """
    Создаем класс для определения прав доступа к обьектам.
    """

    def has_object_permission(self, request, view, obj):
        """
        Определяем права доступа одному обьекту по его ID.

        Даем все права на все, только владельцу или
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
        """Определяем права доступа к ряду обьектов."""
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )
