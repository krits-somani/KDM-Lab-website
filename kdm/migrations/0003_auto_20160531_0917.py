# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 09:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('kdm', '0002_blog_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blog',
            name='publish',
            field=models.DateField(default=datetime.datetime(2016, 5, 31, 9, 17, 42, 904025, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
