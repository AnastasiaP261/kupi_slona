from django.db import models
from django.utils.html import mark_safe


class Images(models.Model):
    title = models.CharField(max_length=30, verbose_name='Имя')
    image = models.ImageField(verbose_name="Расположение")

    def __str__(self):
        return self.title

    def thumbnail(self):
        _str = f'<img scr="images/{self.image}" />'
        print(_str)
        return mark_safe(_str)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = "Изображения"
        ordering = ['title', 'id']

