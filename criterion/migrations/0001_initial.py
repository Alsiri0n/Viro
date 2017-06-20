# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Criterion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=5, verbose_name='Номер')),
                ('description', models.CharField(max_length=300, verbose_name='Описание')),
                ('year', models.CharField(max_length=4, verbose_name='Год')),
            ],
        ),
    ]
