from rest_framework.serializers import ModelSerializer

from .models import Images


class ImagesSerializer(ModelSerializer):
    """Сериализатор CRUD операций к модели Images"""
    class Meta:
        model = Images
        fields = ['id', 'type', 'big_image', 'min_image']
