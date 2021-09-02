from django.contrib import admin

from .models import Women
from .models import category


class WomenAdmin(admin.ModelAdmin):
    # Поля которые показывать при просмотре всех записей
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    # Поля которые будут служить ссылками на запись
    list_display_links = ('id', 'title')
    # Поля по которым можно вести поиск записей
    search_fields = ('title', 'content')
    # Списки полей которые можно редактировать не переходя к самой записи
    list_editable = ('is_published', 'photo')
    # Добавление сайдбара с возможностью фильтрации
    list_filter = ('time_create', 'is_published')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Women, WomenAdmin)
admin.site.register(category, CategoryAdmin)
