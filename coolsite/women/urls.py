from django.urls import path, re_path

# Импорт видов от приложения women
from women.views import *

# URL внутри приложения women
urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add_page/', add_page, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),
    # path('post/<int:post_id>/<str:is_published>/', show_post, name='post'),

    # path('categories/<int:catID>', categories, name='categories'),
    # re_path(r'^archive/(?P<year>[0-9]{4})', archive, name='archive'),
]

