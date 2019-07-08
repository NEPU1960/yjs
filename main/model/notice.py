#!/usr/bin/python
# -*- coding:utf-8 -*-:
'''
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: wechat_get.py
@time: 2019/7/5 22:58
@desc:预告数据库
'''
from . import db
class Notice(db.Model):
    __tablename__="notice"
    ID=db.Column(db.String(20),primary_key=True,unique=True,nullable=False,doc="项目编号")
    date=db.Column(db.String(20), nullable=True, doc="比赛日期")
    time = db.Column(db.String(20), nullable=True, doc="比赛名称")
    name=db.Column(db.String(20),nullable=True,doc="比赛名称")
    local=db.Column(db.String(20),nullable=True,doc='地点')
    group = db.Column(db.String(20), nullable=True, doc='比赛队伍')

    def __init__(self,ID,time,name,local,group,date):
        self.ID = ID
        self.date = date
        self.time = time
        self.name = name
        self.local = local
        self.group = group

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self
