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
from flask import Flask
from .config import shuju
from .model import db

def create_app():
    app=Flask(__name__)
    app.config.from_object(shuju)
    shuju.init_app(app)
    db.init_app(app)
    from .api import api
    app.register_blueprint(api, url_prefix='/api')
    return app