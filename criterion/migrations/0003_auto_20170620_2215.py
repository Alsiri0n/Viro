# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criterion', '0002_auto_20170620_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criterion',
            name='conclusion',
        ),
        migrations.RemoveField(
            model_name='criterion',
            name='qnt',
        ),
        migrations.RemoveField(
            model_name='criterion',
            name='qntExam',
        ),
        migrations.AlterField(
            model_name='criterion',
            name='year',
            field=models.CharField(default='2017', max_length=4, verbose_name='Год проведения'),
        ),
    ]