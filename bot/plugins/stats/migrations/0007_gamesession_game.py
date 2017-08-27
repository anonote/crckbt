# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 22:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_populate_games'),
        ('stats', '0006_auto_20161006_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamesession',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='games.Game'),
        ),
    ]
