# from django.http import HttpResponse, HttpResponseNotFound, Http404
# from django.shortcuts import render, redirect

# Импорт класса ModelViewSet для наследования и создания API
from rest_framework.viewsets import ModelViewSet
from store.models import Book
from store.serializers import BooksSerializer

from rest_framework import generics, status

from rest_framework.response import Response

# Для системы фильтрации сортировке
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# Импортируем класс для Аутентификации пользователей
# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import permissions

from . import custom_permissions


class BookViewSet(ModelViewSet):
    """Все CRUD к модели Book"""
    queryset = Book.objects.all()
    serializer_class = BooksSerializer

    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filter_fields = ['name']
    # search_fields = ['type', 'status']
    # ordering_fields = ['type', 'status']

    # Для Аутентифицированных
    # permission_classes = {permissions.IsAuthenticated}

    # Для Админов
    # permission_classes = {permissions.IsAdminUser}

    # Для Аутентифицированных или только на чтение. То есть
    # только Авориз могут отправлять POST PUT PATCH все ост только Чтение
    permission_classes = {custom_permissions.IsOwnerOrStaffOrReadOnly}

    # Переопределение метода сериализатора, который сохраняет
    # создает запись на основе данных от пользователя, и сюда
    # добавляем владельца
    def perform_create(self, serializer):
        """
        Текущий пользователь в системе по дефолту
        становится владельцем сохраняемой записи.
        """
        # при создании новой записи в БД, мы в поле владельца
        # сохраняем текущего сделавшего этот запрос пользователя,
        # мы юзаем метод IsAuthenticatedOrReadOnly тоетсь либо
        # читаем данные либо все что угодно если аутентифицированы
        # и сохраняем в модель с владельцем в виде текущего пользователя.
        serializer.validated_data['owner'] = self.request.user
        # Метод для десериализации и сохранения модели в БД
        serializer.save()

        # print('='*180)
        # print(serializer)
        # print('='*50)
        # print(serializer.validated_data)
        # serializer.validated_data['owner'] = self.request.user
        # print('=' * 50)
        # print(serializer.validated_data)
        # print('='*180)














# ListAPIView - определяет поведение для
# GET получения списка всех экземпляров
# class BookList(generics.ListAPIView):
#     serializer_class = BooksSerializer
#     queryset = Book.objects.all()
    # print('='*180)
    # print('user : ', user)
    # print('='*50)
    # print('return Book.objects.filter(owner=user) : ',
    #      Book.objects.filter(owner=user))
    # print('='*180)
    # def get_queryset(self):
    #     user = self.request.user
    #     return Book.objects.filter(owner=user)


# class BookCreateView(generics.CreateAPIView):
#     """API POST создать новую запись"""
#     queryset = Book.objects.all()
#     serializer_class = BooksSerializer
#
#     def create(self, request, *args, **kwargs):
#         # print('='*400)
#         super(BookCreateView, self).create(request, args, kwargs)
#         response = {
#             "status_code": status.HTTP_200_OK,
#             "message": "Нет блять !",
#             "result": request.data
#         }
#         return Response(response)
