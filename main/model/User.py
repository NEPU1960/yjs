#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: User.py
@time: 2019/6/3 0003 15:45
@desc:
"""
from . import db
class User(db.Model):
    __tablename__="User"
    IDNumber=db.Column(db.String(20),primary_key=True,unique=True,nullable=False,doc="身份证号")
    Name=db.Column(db.String(20),nullable=True,doc="姓名")
    Number=db.Column(db.String(20),nullable=True,doc='序号')
    Status=db.Column(db.String(20),nullable=True,doc="状态")
    Address=db.Column(db.String(20),nullable=True,doc="地址")
    Addressee=db.Column(db.String(20),nullable=True,doc="收件人")
    Tel=db.Column(db.String(20),nullable=True,doc="手机号")
    Code=db.Column(db.String(20),nullable=True,doc="邮编")
    Diaodang=db.Column(db.String(20),nullable=True,doc="是否需要调档函")
    addressinfo = db.Column(db.String(20), nullable=True, doc="详细地址")
    def __init__(self,IDnumber,Name,Number,Status,Address,Addressee,Tel,Code,Diaodang,adressinfo):
        self.IDNumber=IDnumber
        self.Name=Name
        self.Number=Number
        self.Status=Status
        self.Address=Address
        self.Addressee=Addressee
        self.Tel=Tel
        self.Code=Code
        self.Diaodang=Diaodang
        self.addressinfo=adressinfo

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self
