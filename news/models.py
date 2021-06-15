from django.db import models
from django.urls import reverse
from images.models import Images


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последней редакции")
    photo = models.ManyToManyField(Images, verbose_name="Изображения")
    is_published = models.BooleanField(default=True, verbose_name="Статус")
    author = models.CharField(max_length=30, verbose_name="Автор")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-updated_at']

    def get_absolute_url(self):
        return reverse('article', kwargs={'article_id': self.pk})
