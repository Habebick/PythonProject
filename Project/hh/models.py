from django.db import models
import functools




class Articles(models.Model):
    name = models.CharField('Название', max_length=250)
    description = models.TextField('Описание')
    skills = models.TextField('Навыки')
    company = models.CharField('Компания', max_length=250)
    salary = models.CharField('Зарплата', max_length=80)
    region = models.TextField('Регион')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'






