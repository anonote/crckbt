# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-15 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_notifications', '0003_gamenotification_last_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamenotification',
            name='muted',
            field=models.BooleanField(default=False),
        ),
    ]
