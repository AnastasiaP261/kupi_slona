from django.db import models


class Images(models.Model):
    title = models.CharField(max_length=30, verbose_name='Имя')
    image = models.ImageField(verbose_name="Расположение")

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = "Изображения"
