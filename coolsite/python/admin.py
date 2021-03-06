from django.contrib import admin

from .models import python_section, python_lesson


class python_section_admin(admin.ModelAdmin):
    """Управление разделами Python уроков в админке"""
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title', 'time_create')
    search_fields = ('id', 'title')


class python_lesson_admin(admin.ModelAdmin):
    """Управление уроками для Python в админке"""
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title', 'time_create')
    search_fields = ('id', 'title')


# Register your models here.
admin.site.register(python_section, python_section_admin)
admin.site.register(python_lesson, python_lesson_admin)

