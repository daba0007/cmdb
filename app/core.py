#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import paramiko
import threading
from models import System_info, Host
from enum import Enum, unique


class paramikoThreading(threading.Thread):
    def __init__(self, command, host, username, password, port=22):
        self.command = command
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        super(paramikoThreading, self).__init__()

    def run(self):
        ssh = paramiko.SSHClient()
        # 创建一个ssh的白名单
        know_host = paramiko.AutoAddPolicy()
        # 加载创建的白名单
        ssh.set_missing_host_key_policy(know_host)
        # 连接服务器
        ssh.connect(hostname=self.host, port=self.port, username=self.username, password=self.password)
        stdin, stdout, stderr = ssh.exec_command(self.command)
        ssh.close()
        return stdout


@unique
class Command(Enum):
    """
    Command
    """
    hostname = "hostname"
    ip = "ifconfig"
    version = "cat /etc/redhat-release"
    cpu = "cat /proc/cpuinfo"
    mem = "cat /proc/meminfo"
    type = "dmidecode -s system-product-name"
    uuid = "dmidecode -s system-uuid"


class Client():
    """
    host
    """

    def __init__(self, ip, uname, pwd):
        self.ip = ip
        self.uname = uname
        self.pwd = pwd
        if Host.objects.filter(ip=self.ip):
            host = Host.objects.get(ip=self.ip)
            host.username = self.uname
            host.password = self.pwd
            host.save()
        else:
            Host.objects.create(ip=self.ip, username=self.uname, password=self.pwd)

    def testHost(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session = ssh.connect(self.ip, username=self.uname, password=self.pwd)
        try:
            session.exec_command(Command.date.value)
        except Exception:
            print("Session error")


class Session():
    """
    session
    """

    def __init__(self, ip):
        self.ip = ip
        self.host = Host.objects.get(ip=self.ip)
        self.uname = self.host.username
        self.pwd = self.host.password
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.ip, port=22, username=self.uname, password=self.pwd)
        self.session = ssh

    def getHostname(self):
        stdin, stdout, stderr = self.session.exec_command(Command.hostname.value)
        hostname = stdout.read().rstrip("\n")
        return hostname

    def getIfconfig(self):
        stdin, stdout, stderr = self.session.exec_command(Command.ip.value)
        data = stdout.read()
        ret = re.compile(
            '(?:19[0-9]\.)((?:1[0-9][0-9]\.)|(?:25[0-5]\.)|(?:2[0-4][0-9]\.)|(?:[1-9][0-9]\.)|(?:[0-9]\.)){2}((1[0-9][0-9])|(2[0-4][0-9])|(25[0-5])|([1-9][0-9])|([0-9]))')
        ip = ret.search(data).group()
        return ip

    def getVersion(self):
        stdin, stdout, stderr = self.session.exec_command(Command.version.value)
        version = stdout.read().rstrip("\n")
        return version

    def getCpu(self):
        cpunum = 0
        processor = 0
        cpumode = 0
        stdin, stdout, stderr = self.session.exec_command(Command.cpu.value)
        cpuinfo = stdout.readlines()
        for i in cpuinfo:
            if i.startswith('physical id'):
                cpunum = i.split(":")[1]
            if i.startswith('processor'):
                processor = processor + 1
            if i.startswith('model name'):
                cpumode = i.split(":")[1].rstrip("\n")
        return int(cpunum) + 1, processor, cpumode

    def getMem(self):
        stdin, stdout, stderr = self.session.exec_command(Command.mem.value)
        meminfo = stdout.readlines()
        memory = 0
        for i in meminfo:
            if i.startswith('MemTotal'):
                memory = int(i.split()[1].strip())
                memory = '%.f' % (memory / 1024.0) + 'MB'
            else:
                pass
        return memory

    def getType(self):
        stdin, stdout, stderr = self.session.exec_command(Command.type.value)
        type = stdout.read().rstrip("\n")
        return type

    def getUuid(self):
        stdin, stdout, stderr = self.session.exec_command(Command.type.value)
        uuid = stdout.read().rstrip("\n")
        return uuid

    def getAll(self):
        info = {}
        info['hostname'] = self.getHostname()
        info['ip'] = self.getIfconfig()
        info['version'] = self.getVersion()
        info['cpu'] = self.getCpu()
        info['mem'] = self.getMem()
        info['type'] = self.getType()
        info['uuid'] = self.getUuid()
        return info

    def setHost(self):
        System_info.objects.create(ip=self.ip, physical_cpu_num=self.getCpu()[1], logic_cpu_num=self.getCpu()[0],
                                   cpu_mode=self.getCpu()[2], mem_num=self.getMem(), type=self.getType(),
                                   uuid=self.getUuid(), version=self.getVersion())
        return
