# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-25 01:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0008_remove_adventure_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='related_adventure',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='adventure_ratings', to='app_1.Adventure'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='rating',
            field=models.PositiveIntegerField(),
        ),
    ]
