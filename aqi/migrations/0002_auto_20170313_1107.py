# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aqi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aqi',
            name='city',
            field=models.CharField(max_length=50, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aqi',
            name='city_code',
            field=models.CharField(max_length=20, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aqi',
            name='station_code',
            field=models.CharField(max_length=20, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aqi',
            name='station',
            field=models.CharField(max_length=50),
        ),
    ]
