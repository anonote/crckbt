# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-08 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_member_last_seen'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_bot',
            field=models.BooleanField(default=False),
        ),
    ]
