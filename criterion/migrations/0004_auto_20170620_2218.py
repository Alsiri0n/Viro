# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criterion', '0003_auto_20170620_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criterion',
            name='deadline',
            field=models.CharField(blank=True, max_length=100, verbose_name='Срок проведения'),
        ),
    ]
