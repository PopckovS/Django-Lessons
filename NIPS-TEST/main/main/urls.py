from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from app.views import ImagesViewSet

router = SimpleRouter()
router.register(r'api/v1/images', ImagesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
