# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-18 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system_info',
            name='mem_num',
            field=models.CharField(max_length=30, verbose_name='\u5185\u5b58'),
        ),
    ]
