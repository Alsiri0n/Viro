# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 09:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('criterion', '0006_criterionlist'),
        ('customuser', '0004_auto_20170620_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='virouser',
            name='criterion',
        ),
        migrations.AddField(
            model_name='virouser',
            name='criterionList',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='criterion.CriterionList', verbose_name='Список критериев'),
        ),
        migrations.AlterField(
            model_name='virouser',
            name='region',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='customuser.Region', verbose_name='Район'),
        ),
    ]