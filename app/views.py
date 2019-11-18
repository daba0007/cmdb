# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
import json
from core import Session, Client
from models import System_info, Host


def getInfo(request):
    infoList = []
    host = Host.objects.all()
    for h in host:
        info = System_info.objects.get(ip=h.ip)
        infoList.append({"ip": info.ip, "physical_cpu_num": info.physical_cpu_num, "logic_cpu_num": info.logic_cpu_num,
                         "cpu_mode": info.cpu_mode, "mem_num": info.mem_num, "type": info.type, "uuid": info.uuid,
                         "version": info.version})
    return HttpResponse(json.dumps(infoList))


def getHost(request):
    """
    get info from db
    :param request:
    :return:
    """
    hostList = []
    host = Host.objects.all()
    for h in host:
        hostList.append({"ip": h.ip})
    return HttpResponse(json.dumps(hostList))


def postHost(request):
    ip = request.POST.get('ip', '')
    uname = request.POST.get('username', '')
    pwd = request.POST.get('password', '')
    Client(ip=ip, uname=uname, pwd=pwd)
    session= Session(ip=ip)
    session.setHost()
    return HttpResponse(json.dumps({"info": "success"}))
