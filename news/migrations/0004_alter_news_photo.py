# Generated by Django 3.2.4 on 2021-06-17 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_auto_20210617_1950'),
        ('news', '0003_auto_20210611_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ManyToManyField(blank=True, to='images.Images', verbose_name='Изображения'),
        ),
    ]
