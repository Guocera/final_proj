# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 20:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_auto_20160219_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='planrecipe',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 2, 19, 20, 46, 18, 418413, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planrecipe',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 2, 19, 20, 46, 25, 602033, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
