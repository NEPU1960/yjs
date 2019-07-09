#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: picture.py
@time: 2019/7/9 0009 15:34
@desc:
"""
from . import db
class Picture(db.Model):
    __tablename__="Picture"
    ID=db.Column(db.String(20),primary_key=True,unique=True,nullable=False,doc="图片编号")
    url=db.Column(db.String(200), nullable=True, doc="比赛日期")

    def __init__(self,ID,url):
        self.ID = ID
        self.date = url


    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self
