from tkinter import Image
from django.db import models
from PIL import Image


class New(models.Model):
    title = models.CharField('Название', max_length=50)
    news = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='news_images/', null=True, blank=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            max_size = (250, 250)  # Максимальный размер для изображения
            if img.height > max_size[0] or img.width > max_size[1]:
                img.thumbnail(max_size)
                img.save(self.image.path)

