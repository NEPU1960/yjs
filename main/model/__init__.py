#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: __init__.py.py
@time: 2019/6/3 0003 14:17
@desc:
"""
from flask_sqlalchemy import SQLAlchemy
from ..common import trueReturn,falseReturn
db=SQLAlchemy()
from .User import User
def get_info(IDNumber,input_name):
    '''获取数据库用户信息'''
    Userinfo=User.query.filter_by(IDNumber=IDNumber).first()
    if Userinfo==None:
        return falseReturn(msg='身份证号输入错误，系统中不存在')
    else:
        Name=Userinfo.Name
        if Name!=input_name:
            return falseReturn(msg='姓名和身份证号不符，请检查后输入')
        else:
            return trueReturn(data=Userinfo)
def change_info(IDNumber,status):
    Userinfo=User.query.filter_by(IDNumber=IDNumber).first()
    Userinfo.Status=status
    Userinfo.update()
def save_address(IDNumber,Status,Address,Addressee,Tel,Code,Diaodang):
    Userinfo = User.query.filter_by(IDNumber=IDNumber).first()
    Userinfo.Status=Status
    Userinfo.Address=Address
    Userinfo.Addressee=Addressee
    Userinfo.Tel=Tel
    Userinfo.Code=Code
    Userinfo.Diaodang=Diaodang
    Userinfo.update()