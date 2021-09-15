from django.conf import settings
from django.core.files import File
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Images
from .serializers import ImagesSerializer

from .tasks import add, img_style
from django.core.files.images import ImageFile

class ImagesViewSet(ModelViewSet):
    """Все CRUD к модели Images"""
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    permission_classes = {permissions.AllowAny}

    def create(self, request, *args, **kwargs):

        # result = add.delay(155, 5555)
        # print('=' * 30)
        # print('Общий запуск')
        # result = img_style.delay(
        #     '/var/www/API-TEST/NIPS-TEST/main/media/images/api_img/big/2.jpg',
        #     '/var/www/API-TEST/NIPS-TEST/main/media/images/api_img/big/photo_2021-05-19_11-57-33.jpg'
        # )

        new_img = Images()

        print('='*40)
        print('type = ', type(new_img.big_image))
        print('new_img.big_image = ', new_img.big_image)
        print('path = ', new_img.big_image.path)
        print('='*40)
        # new_img.name = '999'
        # new_img.type = '000'
        #
        # r = ImageFile.open('/var/www/API-TEST/NIPS-TEST/main/media/images/api_img/big/2.jpg')
        #
        #
        # print('='* 30)
        # print('r = ', r)
        # print(r)
        # print('='* 30)
        #
        # new_img.big_image.save('stylize_img.png', File(r))
        # new_img.save()
        #
        # print('='*30)
        # print('result = ', type(result))
        # print('result = ', result)
        # print('result.result = ', result.result)
        # print('='*30)

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

