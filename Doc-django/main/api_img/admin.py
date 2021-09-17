from django.contrib import admin
from .models import Images


class ImagesAdmin(admin.ModelAdmin):
    """Настройка отображения модели Images в админ панели"""
    list_display = ('id', 'type', 'big_image', 'min_image')
    list_display_links = ('id', 'type', 'big_image', 'min_image')
    search_fields = ('id', 'type')


admin.site.register(Images, ImagesAdmin)
