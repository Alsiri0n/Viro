# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criterion', '0007_auto_20170625_1034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='criterionlist',
            options={'verbose_name': 'Список критериев'},
        ),
        migrations.AddField(
            model_name='criterionlist',
            name='name',
            field=models.CharField(default=None, max_length=50, verbose_name='Район пользователя'),
        ),
    ]