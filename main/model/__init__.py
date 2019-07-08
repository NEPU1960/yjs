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
from .News import News
from .jiangpai import Jiangpai
from .notice import Notice
from .Score import Score
from datetime import *
from ..common import trueReturn,falseReturn
def get_notice(date):
    '''获取比赛预告'''
    Noticeinfo=Notice.query.filter_by(date=date).all()
    back_list=[]
    for i in Noticeinfo:
        new_dict={}
        day = datetime.strptime('{0} {1}'.format(date,i.time), '%Y-%m-%d %H:%M')#超时不显示
        print(day)
        if day>datetime.now():
            new_dict={"ID":i.ID,"time":i.time, "name":i.name, "local":i.local, "group":i.group, "date":i.date}
            back_list.append(new_dict)
        else:
            pass
    return back_list
def get_jiangpai():
    '''获取奖牌'''
    info=Jiangpai.query.filter_by().all()
    print(info)

# def get_info(IDNumber,input_name):
#     '''获取数据库用户信息'''
#     Userinfo=User.query.filter_by(IDNumber=IDNumber).first()
#     if Userinfo==None:
#         return falseReturn(msg='身份证号输入错误，系统中不存在')
#     else:
#         Name=Userinfo.Name
#         if Name!=input_name:
#             return falseReturn(msg='姓名和身份证号不符，请检查后输入')
#         else:
#             return trueReturn(data=Userinfo)
# def change_info(IDNumber,status):
#     Userinfo=User.query.filter_by(IDNumber=IDNumber).first()
#     Userinfo.Status=status
#     Userinfo.update()
# def save_address(IDNumber,Status,Address,Addressee,Tel,Code,Diaodang,addressinfo):
#     Userinfo = User.query.filter_by(IDNumber=IDNumber).first()
#     Userinfo.Status=Status
#     Userinfo.Address=Address
#     Userinfo.Addressee=Addressee
#     Userinfo.Tel=Tel
#     Userinfo.Code=Code
#     Userinfo.Diaodang=Diaodang
#     Userinfo.addressinfo=addressinfo
#     Userinfo.update()
# def jinshuju_db(IDNumber,Status,Address,Addressee,Tel,Code,Diaodang,addressinfo):
#     Userinfo = User.query.filter_by(IDNumber=IDNumber).first()
#     if Userinfo == None:
#         Userinfo=User(IDnumber=IDNumber,Name=Addressee,Addressee=Addressee,Status=Status,Address=Address,Tel=Tel,Code=Code,Diaodang=Diaodang,adressinfo=addressinfo,Number="0",)
#         Userinfo.save()
#         print(IDNumber+"错误")
#     elif Userinfo.Status=="1" or Userinfo.Status=="2":
#         pass
#     else:
#         Userinfo.Status = Status
#         Userinfo.Address = Address
#         Userinfo.Addressee = Addressee
#         Userinfo.Tel = Tel
#         Userinfo.Code = Code
#         Userinfo.Diaodang = Diaodang
#         Userinfo.addressinfo = addressinfo
#         Userinfo.update()
# def get_ems_info(IDNumber,input_name):
#     '''获取数据库用户信息'''
#     Userinfo=EMS.query.filter_by(IDNumber=IDNumber).first()
#     if Userinfo==None:
#         return falseReturn(msg='该身份证号未存在于数据库，请仔细核验身份证是否正确')
#     else:
#         Name=Userinfo.Name
#         if Name!=input_name:
#             return falseReturn(msg='姓名和身份证号不符，请检查后输入')
#         else:
#             return trueReturn(data=Userinfo)