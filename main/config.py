#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: config.py
@time: 2019/6/3 0003 14:18
@desc:
"""
class shuju():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://yzb:945999685@182.254.226.202:3306/yzb'

    @staticmethod
    def init_app(app):
        pass