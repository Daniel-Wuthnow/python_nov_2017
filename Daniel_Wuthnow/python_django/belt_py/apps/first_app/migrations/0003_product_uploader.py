# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-23 21:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='uploader',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='uploads', to='first_app.User'),
            preserve_default=False,
        ),
    ]