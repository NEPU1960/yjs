#!/usr/bin/python
# -*- coding:utf-8 -*-:
'''
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: wechat_get.py
@time: 2019/7/8 22:50
@desc:
'''
from datetime import *
dat=date.today()
day = datetime.strptime('{} 23:45:35'.format(dat), '%Y-%m-%d %H:%M:%S')
print(dat)
print(day)
day1=str('{} 15:45:35'.format(dat))
if day<datetime.now():
    print('已经超时')
else:
    print('时间未到')