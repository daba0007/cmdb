# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-17 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30, verbose_name='')),
                ('username', models.CharField(default='', max_length=30, verbose_name='\u7528\u6237\u540d')),
                ('password', models.CharField(max_length=30, verbose_name='\u5bc6\u7801')),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u4fe1\u606f',
                'verbose_name_plural': '\u4e3b\u673a\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='System_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physical_cpu_num', models.IntegerField(verbose_name='\u7269\u7406CPU')),
                ('logic_cpu_num', models.IntegerField(verbose_name='\u903b\u8f91CPU')),
                ('cpu_mode', models.CharField(max_length=30, verbose_name='CPU\u7c7b\u578b')),
                ('mem_num', models.IntegerField(verbose_name='\u5185\u5b58')),
                ('disk_num', models.IntegerField(default='', verbose_name='\u78c1\u76d8')),
                ('ip', models.CharField(max_length=30, verbose_name='IP')),
                ('operator', models.CharField(default='', max_length=30, verbose_name='\u8d23\u4efb\u4eba')),
                ('type', models.CharField(max_length=30, verbose_name='\u4e3b\u673a\u7c7b\u578b')),
                ('uuid', models.CharField(max_length=30, verbose_name='UUID')),
                ('status', models.CharField(default='', max_length=30, verbose_name='\u72b6\u6001')),
                ('date', models.DateField(auto_now_add=True, verbose_name='\u540c\u6b65\u65e5\u671f')),
                ('version', models.CharField(max_length=30, verbose_name='\u7248\u672c')),
            ],
            options={
                'verbose_name': '\u7cfb\u7edf\u4fe1\u606f',
                'verbose_name_plural': '\u7cfb\u7edf\u4fe1\u606f',
            },
        ),
    ]
