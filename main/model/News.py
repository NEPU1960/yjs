#!/usr/bin/python
# -*- coding:utf-8 -*-:
'''
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: wechat_get.py
@time: 2019/6/27 22:24
@desc:新闻通知数据库
'''
from . import db
class News(db.Model):
    __tablename__="news"
    title=db.Column(db.String(20),primary_key=True,unique=True,nullable=False,doc="标题")
    text=db.Column(db.String(20),nullable=True,doc="内容")
    time=db.Column(db.String(20),nullable=True,doc='时间')
    author = db.Column(db.String(20), nullable=True, doc='发布人')

    def __init__(self,title,text,time,author):
        self.title=title
        self.text=text
        self.time=time
        self.author=author

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self
