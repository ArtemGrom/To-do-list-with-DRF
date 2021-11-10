from django.contrib import admin
from django.conf.locale.ru import formats as ru_formats
from rest_framework.authtoken.admin import TokenAdmin
from .models import Note

ru_formats.DATETIME_FORMAT = "d.m.Y H:i:s"

TokenAdmin.raw_id_fields = ['user']


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    # Поля в списке
    list_display = ("title", "message", "date_add", "public", "important", "author")

    # группировка поля в режиме редактирования
    fields = ("date_add", ("title", "public", "important"), "message", "author")

    # поля для чтения в режиме редактирования
    readonly_fields = ("date_add",)

    # поиск по выбранным полям
    search_fields = ["title", "message"]

    # фильтры справа
    list_filter = ("public", "important", )

    def save_model(self, request, obj, form, change):
        # Добавляем текущего пользователя (если не выбран) при сохранении модели
        if not hasattr(obj, 'author') or not obj.author:
            obj.author = request.user
        super().save_model(request, obj, form, change)

