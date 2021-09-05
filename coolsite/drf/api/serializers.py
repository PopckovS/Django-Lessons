from ..models import Post
from rest_framework import serializers

# https://www.youtube.com/watch?v=vRRlKPiRoqA&list=PLF-NY6ldwAWqSxUpnTBObEP21cFQxNJ7C&index=14
# pip3 install drf-yasg


class PostSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Post"""
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'is_featured', 'image')
















# class PostSerializer(serializers.ModelSerializer):
#     """Сериалайзер для модели Post"""

    # class Meta:
        # model - Указываем модель для сериализации
        # model = Post

        # fields - Указываем какие поля сериализовать, если
        # не обьявить, то будут сериализованы все поля.
        # fields = ('title', 'content', 'is_featured')
        # fields = ('id', 'title', 'content', 'is_featured', 'image')


