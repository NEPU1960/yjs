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
from .picture import Picture
from .News import News
from datetime import *
from ..common import trueReturn,falseReturn
import time
import random
import json
year='年'
month='月'
day='日'
cc=time.localtime(time.time())
today=str(cc.tm_year)+year+str(cc.tm_mon)+month+str(cc.tm_mday)+day
print(today)
def make_id():
    number=random.randint(0,3000)
    return number
def get_picture():
    back_info=Picture.query.filter_by().order_by(Picture.ID).all()
    back_list=[]
    for i in back_info:
        back_list.append({"ID":i.ID,"url":i.url,"type": 'image'})
    return back_list
def get_notice(date):
    '''获取当日比赛预告'''
    Noticeinfo=Notice.query.filter_by(date=date).order_by(Notice.time).all()
    back_list=[]
    for i in Noticeinfo:
        print(i)
        new_dict={}
        # day = datetime.strptime('{0} {1}'.format(date,i.time), '%Y-%m-%d %H:%M')#超时不显示
        # print(day)
        # if day>datetime.now():
        new_dict={"ID":i.ID,"time":i.time, "name":i.name, "local":i.local, "group":json.loads(i.group), "date":i.date}
        back_list.append(new_dict)
        # else:
        #     pass
    return back_list
def get_jiangpai():
    '''获取奖牌'''
    info=Jiangpai.query.filter_by().order_by(Jiangpai.total.desc()).all()
    print(info)
    back_list=[]
    for i in info:
        print(i)
        new_dict = {"name": i.name, "jin": i.jin, "yin": i.yin, "tong": i.tong, "total": i.total, "jifen": i.jifen}
        back_list.append(new_dict)
    return back_list
def get_Score_by_name(name):
    Noticeinfo = Score.query.filter_by().order_by(Notice.time).all()
    back_list=[]
    for i in Noticeinfo:
        if name in i.group:
            new_dict = {"ID": i.ID, "name": i.name, "result": i.result, "style": i.style}
            back_list.append(new_dict)
    return back_list
def get_score():
    '''获取成绩列表'''
    Scoreinfo = Score.query.filter_by().order_by(Score.time).all()
    back_lict=[]
    for i in Scoreinfo:
        back_lict.append({"ID":i.ID,"name":i.name,"style":i.style,"time":i.time})
    return back_lict
def get_score_info(ID):
    '''根据项目id获得信息'''
    Scoreinfo = Score.query.filter_by(ID=ID).first()
    back=json.loads(Scoreinfo.result)
    return back
def get_Score_by_time(time):
    Noticeinfo = Score.query.filter_by(time=time).order_by(Notice.time).all()
    back_list = []
    for i in Noticeinfo:
        new_dict={"ID":i.ID,"name":i.name,"result":i.result,"style":i.style}
        back_list.append(new_dict)
    return back_list
def get_Score_by_school(school):
    Noticeinfo = Score.query.filter_by().order_by(Notice.time).all()
    back_list=[]
    for i in Noticeinfo:
        if school in i.group:
            new_dict = {"ID": i.ID, "name": i.name, "result": i.result, "style": i.style}
            back_list.append(new_dict)
    return back_list
def get_news():
    Newsinfo = News.query.filter_by().order_by(News.time).all()
    back_list=[]
    for i in Newsinfo:
        back_list.append({"title":i.title,"time":i.time})
    return back_list
def get_text(title):
    News_text=News.query.filter_by(title=title).first()
    back_list={"title":News_text.title,"time":News_text.time,"text":News_text.text,"author":News_text.author}
    return back_list
def check_id(info,noticetime,name,local,group,noticedate):
    if info != None:
        update(noticetime,name,local,group,noticedate)
    else:
        pass
def update(noticetime,name,local,group,noticedate):
    ID=make_id()
    print(ID)
    info=Notice.query.filter_by(ID=ID).first()
    print(info)
    check_id(info,noticetime,name,local,group,noticedate)
    notice_data=Notice(ID=ID, time=noticetime, name=name, local=local, group=group, date=noticedate)
    notice_data.save()
def update_score(name,result,style,scoretime,text):
    ID=make_id()
    print(ID)
    info=Score.query.filter_by(ID=ID).first()
    print(info)
    check_id(info,name,result,style,scoretime,text)
    notice_data=Score(ID=ID, name=name,result=result, style=style, time=scoretime, text=text)
    notice_data.save()
def get_notice_id(ID):
    Noticeinfo = Notice.query.filter_by(ID=ID).first()
    new_dict = json.loads(Noticeinfo.group)
    return new_dict
        # else:
        #     pass
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