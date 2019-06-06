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
from ..model import get_info,change_info,save_address
from ..common import falseReturn,trueReturn
from flask import jsonify

def search():
    """查询用户信息"""
    te=get_info("230622199407032050","戚开元")
    print(te)
    if te['status']==False:
        return te["msg"]
    else:
        print(te['data'])
        info=te['data']
        return trueReturn(data=info)
@api.route("/lq",methods=['GET'])
def lq():
    '''现场领取校验'''
    back_info=search()
    if back_info['status']==False:
        return back_info
    else:
        info=back_info['data']
        status=info.Status
        if status=="1": #已经选择了邮寄
            return jsonify(falseReturn(msg="已选择邮寄",data=info.Address))
        elif status=="0":#已经领取
            print("已经领取")
            return jsonify(falseReturn(msg="已经领取",data=info.Number))
        else:
            change_info("230622199407032050","0")
            print("sucess")
            return jsonify(trueReturn(msg=info.Number))
@api.route("/yj",methods=['GET'])
def yj():
    """邮寄校验"""
    back_info=search()
    if back_info['status'] == False:
        return back_info
    else:
        info = back_info['data']
        status = info.Status
        if status == "1":  # 已经填写邮寄地址
            return jsonify(falseReturn(msg="已经填写邮寄地址", data=info.Address))
        elif status == "0":  # 已经领取
            print("已经领取")
            return jsonify(falseReturn(msg="已经领取", data=info.Number))
        else:
            # change_info("230622199407032050", "1")#没有填写
            # print("sucess")
            return jsonify(trueReturn(msg=info.Number))
@api.route("/upinfo",methods=['GET'])
def upinfo():
    '''填写信息'''
    save_address(IDNumber="230622199407032050",Status="1",Address="黑龙江省大庆市肇源县茂兴镇",Addressee="戚开元",Tel="13359500305",
                 Code="166514",Diaodang="0")
    return "success"