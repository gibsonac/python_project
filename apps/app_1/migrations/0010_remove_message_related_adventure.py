# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-25 01:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0009_auto_20190725_0104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='related_adventure',
        ),
    ]
