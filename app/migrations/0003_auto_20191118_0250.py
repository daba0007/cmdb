# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-18 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191118_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system_info',
            name='uuid',
            field=models.IntegerField(verbose_name='UUID'),
        ),
    ]
