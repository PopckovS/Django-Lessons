from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    """
    Представление для обработки главной страницы.

    request - ссылка на класс HttpRequest с инфой о запросе, сессии,
     куки,, заголовки и тд..

    return - на выходе должен быть экземпляр класса HttpResponse
    """
    return HttpResponse("Women главная страница")


def categories(request, catID: int):
    """
    Отображает категорию

    catID - номер категории, параметр URL строки
    """
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
    return HttpResponseNotFound("<h1>Страница не найдена, ошибка 404</h1>")




