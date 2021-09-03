# from django.http import HttpResponse, HttpResponseNotFound, Http404
# from django.shortcuts import render, redirect

# Импорт класса ModelViewSet для наследования и создания API
from rest_framework.viewsets import ModelViewSet

from store.models import Book

from store.serializers import BooksSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer

