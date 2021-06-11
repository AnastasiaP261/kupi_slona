from django.db import models


class Images(models.Model):
    title = models.CharField(max_length=30, verbose_name='Имя')
    image = models.ImageField(verbose_name="Расположение")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = "Изображения"
        ordering = ['title', 'id']
