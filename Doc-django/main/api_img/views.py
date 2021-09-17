from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from config.settings.base import BIG_IMG_PATH
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from image_transform.img_stylize import stylize_images
from .models import Images
from .serializers import ImagesSerializer

from django.conf import settings
from .tasks import img_style


class ImagesViewSet(ModelViewSet):
    """Все CRUD к модели Images"""
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    # filter_backends = [DjangoFilterBackend, OrderingFilter]
    # filter_fields = ['id', 'type']
    # ordering_fields = ['id', 'type']
    permission_classes = {permissions.AllowAny}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.custom_data = {}

    def create(self, request, *args, **kwargs):
        """
        Переопределенный метод сохранения записи, или
        создание комбинированной картинки на основе JSON

        1) Создать запись: POST host/api/v1/images/
        2) пример JSON для создания изображения.
        { "bind_images": {"photo_id": 3, "filter_id": 8} }
        """
        if self.validate_request(request.data) and self.validate_objects(request.data):

            # Создаем заись для хранения нового стилизованного изображения
            new_image = Images(type='result')
            new_image.save()

            # Генерация нового изображения
            img_style.delay(
                photo_image_path=self.custom_data['photo'].big_image.path,
                filter_image_path=self.custom_data['filter'].big_image.path,
                img_id=new_image.id
            )

            # Отдаем ответ, о создании нового стилизованного изображения
            response = {
                "message": "Successfully created",
                "id": new_image.id,
            }
            return Response(response, status=status.HTTP_201_CREATED)

        # POST стандартный процесс на создание записи
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response = {
            "status": status.HTTP_201_CREATED,
            "message": "Successfully created",
            "id": serializer.instance.id,
        }
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)

    def validate_request(self, data):
        """Проверка, есть ли в JSON нужные параметры."""
        if "bind_images" in data \
            and "photo_id" in data["bind_images"] \
            and "filter_id" in data["bind_images"] \
            and isinstance(data["bind_images"]["photo_id"], int) and \
            isinstance(data["bind_images"]["filter_id"], int):
            return True

    def validate_objects(self, data):
        """Проверка обьектов на существование."""
        try:
            photo = Images.objects.get(pk=data["bind_images"]["photo_id"])
            filter = Images.objects.get(pk=data["bind_images"]["filter_id"])
            if photo.type != "photo" and filter.type != "filter":
                raise Exception
        except Exception:
            return False

        self.custom_data['photo'] = photo
        self.custom_data['filter'] = filter
        return True

    def perform_create(self, serializer):
        """Метод сохранения модели в БД"""
        serializer.save()

    def perform_update(self, serializer):
        """Метод обновления модели в БД"""
        serializer.save()

    def list(self, request, *args, **kwargs):
        """Получение всех записей из Модели по GET запросу"""
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
