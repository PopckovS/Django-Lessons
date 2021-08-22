from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import Women, Product

from coolsite.settings import BASE_DIR
import os


def index(request):
    """Главная страница опросов"""
    posts = Women.objects.all()
    context = {
        'title': 'Women Главная страница',
        'posts': posts,
        'menu': ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    """О приложении"""
    context = {
        'title': 'Women о сайте',
        'menu': ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']
    }
    return render(request, 'women/about.html', context=context)


def categories(request, catID: int):
    """Отображает категорию"""
    if request.GET:
        print(request.GET)
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Статья категории {catID}</h1>")


def archive(request, year):
    if int(year) > 2021:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архив по годам {year}</h1>")


def pageNotFound(request, exception):
    """Отображение страницы ошибок"""
    return HttpResponseNotFound("<h1>Страница не найдена, ошибка 404</h1>")

