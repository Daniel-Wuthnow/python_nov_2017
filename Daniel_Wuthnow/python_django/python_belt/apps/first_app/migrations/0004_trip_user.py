# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_trip'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='User',
            field=models.ManyToManyField(related_name='Trip', to='first_app.User'),
        ),
    ]