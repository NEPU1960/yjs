#!/usr/bin/python
# -*- coding:utf-8 -*-:
'''
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: wechat_get.py
@time: 2019/7/5 22:51
@desc:比赛成绩数据库
'''
from . import db
class Score(db.Model):
    __tablename__="score"
    ID=db.Column(db.String(20),primary_key=True,unique=True,nullable=False,doc="项目编号")
    name=db.Column(db.String(20),nullable=True,doc="比赛名称")
    result=db.Column(db.String(20),nullable=True,doc='结果')
    style = db.Column(db.String(20), nullable=True, doc='成绩类型')
    time = db.Column(db.String(20), nullable=True, doc='比赛日期')
    text = db.Column(db.String(20), nullable=True, doc='备注')

    def __init__(self,ID,name,result,style,time,text):
        self.ID = ID
        self.name = name
        self.result = result
        self.style = style
        self.time = time
        self.text = text

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self
