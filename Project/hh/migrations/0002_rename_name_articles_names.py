# Generated by Django 4.1.5 on 2023-01-13 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hh', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='name',
            new_name='names',
        ),
    ]
