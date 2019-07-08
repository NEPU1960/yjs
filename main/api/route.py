#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: route.py
@time: 2019/6/3 0003 14:29
@desc:
"""
from flask import request
from . import api
# from ..model import get_info,change_info,save_address,jinshuju_db
from ..model import get_notice,get_jiangpai
from ..common import falseReturn,trueReturn
from flask import jsonify
import json

@api.route("/")
def notice():
    '''预告信息查询'''
    test=get_notice('2019-07-18')
    print(test)
    test1=json.dumps(test)
    test2=json.loads(test1)
    return jsonify(test)