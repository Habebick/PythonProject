from django.db import models

# Create your models here.
class Mainskills(models.Model):
    year = models.CharField('Год', max_length=4)
    name = models.CharField('Навык', max_length=200)
    count = models.CharField('Количество упоминаний', max_length=50)

