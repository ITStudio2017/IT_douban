# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-07 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180406_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
