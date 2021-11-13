from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


STATUS_CHOICES = [
    ('активно', 'активно'),
    ('отложено', 'отложено'),
    ('выполнено', 'выполнено'),
]


def one_day_from_today():
    return timezone.now() + timedelta(days=1)


class Note(models.Model):
    """Основная запись в приложении"""
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    message = models.TextField(default='', verbose_name='Текст')
    date_add = models.DateTimeField(default=one_day_from_today, verbose_name='Время изменения')
    public = models.BooleanField(default=False, verbose_name='Опубликовать')
    important = models.BooleanField(default=False, verbose_name='Важность')
    author = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=False, verbose_name='Автор')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="активно", verbose_name='Статус')

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.title
