# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='virouser',
            name='region',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='customuser.Region', verbose_name='Район'),
        ),
    ]