from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=100)
    intro_anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    photo = models.ImageField('Изображение', null=True, blank=True, upload_to='images/')
    date = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
