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
import datetime
import time
from datetime import datetime
year='年'
month='月'
day='日'
cc=time.localtime(time.time())
today=str(cc.tm_year)+year+str("0"+str(cc.tm_mon))+month+str(cc.tm_mday)+day
print(today)
print()
print(datetime.today())
# day = datetime.strptime('{0} {1}'.format(date,i.time), '%Y-%m-%d %H:%M')
time=datetime.today()
day = datetime.strptime(str(time), '%Y-%m-%d %H:%M')