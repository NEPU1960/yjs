#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: route.py
@time: 2019/6/3 0003 14:29
@desc:
"""
from flask import request
from . import api
# from ..model import get_info,change_info,save_address,jinshuju_db
from ..model import get_notice,get_jiangpai,get_Score_by_name,get_Score_by_school,get_Score_by_time,get_picture
from ..common import falseReturn,trueReturn
from flask import jsonify
import json
import requests
import time
from ..common import trueReturn,falseReturn
def today():
    year = '年'
    month = '月'
    day = '日'
    cc = time.localtime(time.time())
    today = str(cc.tm_year) + year + str("0" + str(cc.tm_mon)) + month + str(cc.tm_mday) + day
    print(cc.tm_mon, today)
    return today
@api.route("/")
def notice():
    '''预告信息查询'''
    test=get_notice(today())
    print(test)
    test1=json.dumps(test)
    test2=json.loads(test1)
    return jsonify(test)
@api.route('/onLoad')
def onLoad():
    '''打开加载'''
    weather_url = "http://api.map.baidu.com/telematics/v3/weather?location=%E5%A4%A7%E5%BA%86&output=json&ak=ddL0enbuhbnOipacUloOh1Di"
    weather = requests.get(weather_url).json()
    weather_data = weather['results'][0]['weather_data'][0]
    index = weather['results'][0]['index']
    weatherlist = [{"title": "今日天气",
                    "text": weather_data['date'] + "  " + weather_data['weather'] + "  " + weather_data['wind'] + "  " +
                            weather_data['temperature'] + "  " + "PM2.5: " + weather['results'][0]['pm25']},
                   {'title': index[0]['tipt'], "text": index[0]['des']},
                   {'title': index[2]['tipt'], "text": index[2]['des']},
                   {'title': index[3]['tipt'], "text": index[3]['des']},
                   {'title': index[4]['tipt'], "text": index[4]['des']}, ]
    back_info = get_notice(today())
    back_noicelist=[]
    picture=get_picture()
    try:
        for i in range(10):
            back_noicelist.append(back_info[i])
    except:
        pass
    if back_info ==[]:
        print('今日已无比赛')
        return jsonify(falseReturn(msg="今日已无比赛",data={"weather":weatherlist,"notice":"今日无赛事","picture":picture}))
    else:
        return jsonify(trueReturn(data={"weather":weatherlist,"notice":back_noicelist,"picture":picture}))
@api.route("/jiangpai")
def jiangpai():
    back_info=get_jiangpai()
    return jsonify(back_info)
@api.route("/notice")
def yugao():
    back_info = get_notice(today())
    if back_info == []:
        print('今日已无比赛')
        return jsonify(falseReturn(data=''))
    else:
        return jsonify(trueReturn(data=back_info))