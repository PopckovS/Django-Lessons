from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrStaffOrReadOnly(BasePermission):

    # Отрабатывает на те L которые обращаются к конкретному id записи
    #
    def has_object_permission(self, request, view, obj):
        """
        Переопределяем права доступа.

        Даем все права на запись, только владельцу или
        администратору, на чтение даем право всем.
        Возвращаем `True` если есть разрешение, `False` если нет.
        """

        # print('Тут ! ')
        # print('='*100)
        # print(obj)
        # print('=' * 50)
        # print(obj.owner)
        # print('='*100)
        if request.user.is_superuser:
            print('is_superuser')
        if request.user.is_staff:
            print('is_staff')

        return bool(
            request.method in SAFE_METHODS
            or
            request.user and request.user.is_authenticated
            and
            (obj.owner == request.user or request.user.is_superuser)
        )

    # return bool(
    #     request.method in SAFE_METHODS or
    #     request.user and
    #     request.user.is_authenticated and
    #     (obj.owner == request.user or request.user.is_staff)
    # )

    # Проверяет те методы views которые работают с списками обьектов
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )
