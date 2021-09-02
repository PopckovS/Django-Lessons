from django.urls import path, re_path
from drf.views import *

# Импортируем виды для нашей API системы
from .api import views

urlpatterns = [
    path('', index, name='home'),

    # URL для API системы
    # path('lists', views.PostViewSet.as_view(), name=None),
    path('lists', views.PostViewSet.as_view, name=None),

    path('list', views.PostListView.as_view(), name=None),
    path('create', views.PostCreateView.as_view(), name=None),
    path('<int:pk>', views.PostDetailView.as_view(), name=None)
]


# path('about/', about, name='about'),
# path('category/<int:cat_id>/', show_category, name='category'),
# path('add_page/', add_page, name='add_page'),
# path('contact/', contact, name='contact'),
# path('login/', login, name='login'),
# path('post/<int:post_id>/', show_post, name='post'),


