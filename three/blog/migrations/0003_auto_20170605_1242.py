# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170602_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Author Name'),
        ),
    ]
