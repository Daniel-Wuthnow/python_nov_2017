# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_auto_20171130_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(blank=True, upload_to='../static/first_app/images'),
        ),
    ]
