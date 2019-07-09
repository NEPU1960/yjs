#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: common.py
@time: 2019/6/3 0003 16:16
@desc:
"""
def trueReturn(msg='',data='',type=''):
    return {
        "status": True,
        "data": data,
        "msg": msg,
        "type":type
    }


def falseReturn(msg='',data='',type=''):
    return {
        "status": False,
        "data": data,
        "msg": msg,
        "type":type
    }
