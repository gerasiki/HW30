# Generated by Django 4.1 on 2022-09-07 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_selection'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='selection',
            options={'verbose_name': 'Подборка', 'verbose_name_plural': 'Подборки'},
        ),
    ]