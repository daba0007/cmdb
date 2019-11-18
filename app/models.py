# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class System_info(models.Model):
    physical_cpu_num = models.IntegerField(verbose_name=u'物理CPU')
    logic_cpu_num = models.IntegerField(verbose_name=u'逻辑CPU')
    cpu_mode = models.CharField(max_length=30, verbose_name=u'CPU类型')
    mem_num = models.IntegerField(verbose_name=u'内存')
    disk_num = models.IntegerField(verbose_name=u'磁盘', default="")
    ip = models.CharField(max_length=30, verbose_name=u'IP')
    operator = models.CharField(max_length=30, verbose_name=u'责任人', default="")
    type = models.CharField(max_length=30, verbose_name=u'主机类型')
    uuid = models.CharField(max_length=30, verbose_name=u'UUID')
    status = models.CharField(max_length=30, verbose_name=u'状态', default="")
    date = models.DateField(auto_now_add=True, verbose_name=u'同步日期')
    version = models.CharField(max_length=30, verbose_name=u'版本')

    class Meta:
        verbose_name = u'系统信息'
        verbose_name_plural = verbose_name


class Host(models.Model):
    ip = models.CharField(max_length=30, verbose_name=u'')
    username = models.CharField(max_length=30, verbose_name=u'用户名', default="")
    password = models.CharField(max_length=30, verbose_name=u'密码')

    class Meta:
        verbose_name = u'主机信息'
        verbose_name_plural = verbose_name
