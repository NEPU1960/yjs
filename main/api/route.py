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
    te=get_info(IDNumber=idnumber,input_name=name)
    print(te)
    if te['status']==False:
        print("false")
        return falseReturn(msg=te['msg'])
    else:
        info=te['data']
        print(info)
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
    print(idnumber)
    if back_info['status'] == False:
        return jsonify(back_info)
    else:
        info = back_info['data']
        print(info.Address)
        status = info.Status

        if status == "1":  # 已经填写邮寄地址
            print("test")
            print(info.Address)
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
    info=request.get_json()
    print(info)
    print("1")
    tel=info['tel']
    Addressee=info['name']
    diaodang=info['diaodang']
    areaInfo=info['areaInfo']
    address = info['address']
    code = info['code']
    IdNumber=info['IDnumber']
    try:
        save_address(IDNumber=IdNumber,Status="1",Address=areaInfo,Addressee=Addressee,Tel=tel,
                 Code=code,Diaodang=diaodang,addressinfo=address)
        return jsonify(trueReturn(msg="sucess"))
    except:
        return jsonify(falseReturn())