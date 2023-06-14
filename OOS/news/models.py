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

class Contact(models.Model):
    last_name = models.CharField('Фамилия', max_length=50)
    first_name = models.CharField('Имя', max_length=50)
    middle_name = models.CharField('Отчёство', null=True, max_length=60, blank=True)
    email = models.EmailField('Адрес электронной почты')
    organization = models.CharField('Организация', null=True, max_length=120, blank=True)
    phone = models.CharField('Телефон', null=True, max_length=15, blank=True)
    text = models.TextField('Текст обращения')
    file = models.FileField('Прикрепить файл', null=True, upload_to='files/', blank=True)

    def __str__(self):
        return self.last_name
    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
