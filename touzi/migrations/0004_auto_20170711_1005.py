# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touzi', '0003_auto_20170711_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klineltcday',
            name='time',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='klineltcmonth',
            name='time',
            field=models.CharField(max_length=6, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='klineltcweek',
            name='time',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
    ]