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
def trueReturn(msg='',data=''):
    return {
        "status": True,
        "data": data,
        "msg": msg
    }


def falseReturn(msg='',data=''):
    return {
        "status": False,
        "data": data,
        "msg": msg
    }
