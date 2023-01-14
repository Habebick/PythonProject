from django.contrib import admin
from .models import Mainskills
# Register your models here.
admin.site.register(Mainskills)


class Meta:
    verbose_name = 'Навыки'
    verbose_name_plural = 'Навыки'
