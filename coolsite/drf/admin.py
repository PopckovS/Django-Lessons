from django.contrib import admin

from .models import Post

# Модель Post используется для API
admin.site.register(Post)

