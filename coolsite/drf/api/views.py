from ..models import Post
from . import serializers

from rest_framework import generics, status
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


# Эксперимент по фильтрации
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['title']
    search_fields = ['title']


class PostListView(generics.ListAPIView):
    """API GET лучение всех данных"""
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostCreateView(generics.CreateAPIView):
    """API POST создать новую запись"""
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def create(self, request, *args, **kwargs):
        super(PostCreateView, self).create(request, args, kwargs)
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Successfully created",
            "result": request.data
        }

        # print('='*100)
        # print(response)
        # print('='*100)

        return Response(response)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def retrieve(self, request, *args, **kwargs):
        """Получить обьект"""
        super(PostDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        """Обновление"""
        super(PostDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "result": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        """Удаление ресурса"""
        super(PostDetailView, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully deleted"}
        return Response(response)













# generics.ListAPIView   - Для получения
# generics.CreateAPIView - Для создания

# Делаем запрос к ORM модели, эти поля и будут сериализованы
# queryset = Post.objects.all()
#
# Указываем класс который будет указывать как надо будет сериализовать
# serializer_class = serializers.PostSerializer






