from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import Women,  drop_category, category

menu = [
        {'title': 'О сайте',         'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь',  'url_name': 'contact'},
        {'title': 'Войти',           'url_name': 'login'},
    ]


def index(request):
    """Главная страница"""
    posts = Women.objects.all()
    context = {
        'title': 'Главная страница Women',
        'posts': posts,
        'menu': menu
    }
    drop_category()
    # women_1 = Women.objects.get(pk=1)
    # women_1.cat = None
    # women_1.save()

    return render(request, 'women/index.html', context=context)


def about(request):
    """О приложении"""
    context = {
        'title': 'Women о сайте',
        'menu': menu
    }
    return render(request, 'women/about.html', context=context)


def contact(request):
    """Контакты"""
    return HttpResponse('contact')


def login(request):
    """Логин"""
    return HttpResponse('login')


def add_page(request):
    return HttpResponse('add_page')


def show_post(request, post_id):
    return HttpResponse(f'show_post post_id = {post_id}')


def pageNotFound(request, exception):
    """Отображение страницы ошибок"""
    return HttpResponseNotFound("<h1>Страница не найдена, ошибка 404</h1>")

