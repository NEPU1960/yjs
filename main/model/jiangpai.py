#!/usr/bin/python
# -*- coding:utf-8 -*-:
'''
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: wechat_get.py
@time: 2019/7/5 22:55
@desc:奖牌榜单数据库
'''
from . import db
class Jiangpai(db.Model):
    __tablename__="jiangpai"
    name=db.Column(db.String(20),primary_key=True,unique=True,nullable=False,doc="队名")
    jifen=db.Column(db.String(20),nullable=True,doc="积分")
    jin=db.Column(db.String(20),nullable=True,doc='金牌')
    yin = db.Column(db.String(20), nullable=True, doc='银牌')
    tong = db.Column(db.String(20), nullable=True, doc='铜牌')
    total = db.Column(db.String(20), nullable=True, doc='总数')

    def __init__(self,name,jifen,jin,yin,tong,total):
        self.name = name
        self.jifen = jifen
        self.jin = jin
        self.yin = yin
        self.tong = tong
        self.total = total

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self