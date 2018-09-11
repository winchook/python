#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/9/10

#udp客户端实现并发发送消息
from socket import *

ip_port=('127.0.0.1',8080)
buffer_size=1024

udp_client=socket(AF_INET,SOCK_DGRAM) #数据报

while True:
    msg=input('>>: ').strip()
    udp_client.sendto(msg.encode('utf-8'),ip_port)

    data,addr=udp_client.recvfrom(buffer_size)
    # print(data.decode('utf-8'))
    print(data)