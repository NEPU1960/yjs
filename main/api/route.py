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

def search(idnumber,name):
    """查询用户信息"""
    te=get_info(idnumber,name)
    print(te)
    if te['status']==False:
        return falseReturn(msg=te['msg'])
    else:
        print(te['data'])
        info=te['data']
        return trueReturn(data=info)
@api.route("/lq",methods=['POST'])
def lq():
    '''现场领取校验'''
    idnumber=request.get_json()
    name=idnumber['studentid']
    idcard=idnumber['passwd']
    print(idcard,name)
    back_info=search(idcard,name)
    if back_info['status']==False:
        return jsonify(back_info)
    else:
        info=back_info['data']
        status=info.Status
        if status=="1": #已经选择了邮寄
            return jsonify(falseReturn(msg="已选择邮寄:{}".format(info.Address),data=info.Address))
        elif status=="0":#已经领取
            print("已经领取")
            return jsonify(falseReturn(msg="已经领取,领取序号为:{}".format(info.Number),data=info.Number))
        else:
            change_info("230622199407032050","0")
            print("sucess")
            return jsonify(trueReturn(data=info.Number))
@api.route("/yj",methods=['POST'])
def yj():
    """邮寄校验"""
    idnumber = request.get_json()
    name = idnumber['studentid']
    idcard = idnumber['passwd']
    back_info = search(idcard, name)
    if back_info['status'] == False:
        return jsonify(back_info)
    else:
        info = back_info['data']
        status = info.Status
        if status == "1":  # 已经填写邮寄地址
            return jsonify(falseReturn(msg="已选择邮寄:{}".format(info.Address), data=info.Address))
        elif status == "0":  # 已经领取
            return jsonify(falseReturn(msg="已经领取,领取序号为:{}".format(info.Number), data=info.Number))
        else:
            # change_info("230622199407032050", "1")#没有填写
            # print("sucess")
            return jsonify(trueReturn(msg=info.Number))
@api.route("/upinfo",methods=['POST'])
def upinfo():
    '''填写信息'''
    try:
        save_address(IDNumber="230622199407032050",Status="1",Address="黑龙江省大庆市肇源县茂兴镇",Addressee="戚开元",Tel="13359500305",
                 Code="166514",Diaodang="0")
        return jsonify(trueReturn(msg="sucess"))
    except:
        return jsonify(falseReturn())