"""coolsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


from coolsite import settings

from women.views import *

# yasg Для описания API в swagger
from .yasg import urlpatterns as doc_urls

#
from rest_framework.routers import SimpleRouter
from store.views import BookViewSet


router = SimpleRouter()

router.register(r'book', BookViewSet)

urlpatterns = [
    # Админ панель сайта
    path('admin/', admin.site.urls),

    # Приложение women
    # path('women/', include('women.urls')),
    path('', include('women.urls')),

    # path('store/', include('store.urls')),

    # приложение для DRF
    path('drf/', include('drf.urls')),

    # Приложение pools
    # path('polls/', include('polls.urls')),

    # Приложение python
    # path('python/', include('python.urls')),

    # Путь к html-редактору что подключен к админке
    path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

# Для Swagger
urlpatterns += doc_urls

# Для book
urlpatterns += router.urls

# Установка директорий для скачивания статических файлов дял dev/prod
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )


# faulthandler = pageNotFound
handler404 = pageNotFound
