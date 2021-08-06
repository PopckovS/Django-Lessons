from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    """
    Представление для обработки главной страницы.

    request - ссылка на класс HttpRequest с инфой о запросе, сессии,
     куки,, заголовки и тд..

    return - на выходе должен быть экземпляр класса HttpResponse
    """
    return HttpResponse("Привет мир !")


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
    """
    """
    return HttpResponse(f"<h1>Архив по годам {year}</h1>")







