from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=1024, verbose_name='Название')
    image = models.ImageField(upload_to='main/static/main/img/images/')
    text = models.TextField(max_length=300, verbose_name='Текст', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
