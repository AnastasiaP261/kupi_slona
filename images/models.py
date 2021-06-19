from django.db import models
from django.utils.html import mark_safe, format_html
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


class Images(models.Model):
    title = models.CharField(max_length=30, verbose_name='Имя')
    # image = ProcessedImageField(verbose_name="Расположение")
    image = ProcessedImageField(processors=[ResizeToFit(
                                                            width=1300,
                                                            height=750,
                                                            mat_color='white',
                                                            upscale=False,
                                                        )],
                                verbose_name="Расположение")

    def __str__(self):
        return self.title

    def get_thumbnail(self):
        _str = f""" <img src="/images/{self.image}" class="img-thumbnail" alt="..."> """
        print(_str)
        return format_html('<img src="/images/{}" class="img-thumbnail" alt="...">', self.image,)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = "Изображения"
        ordering = ['title', 'id']

