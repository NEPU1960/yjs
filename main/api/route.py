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
from ..model import get_notice,get_jiangpai,get_Score_by_name,get_Score_by_school,get_Score_by_time,get_picture,get_news,get_text,update,get_notice_id,get_score,get_score_info,update_score
from ..common import falseReturn,trueReturn
from flask import jsonify,request
import json
import requests
import time
from ..common import trueReturn,falseReturn
import json
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
@api.route("/title")
def title():
    back_title=get_news()
    return jsonify(trueReturn(data=back_title))
@api.route("/title-text" ,methods=['POST'])
def title_text():
    get_json = request.get_json()
    print(get_json)
    Title = get_json['Title']
    back_text=get_text(title=Title)
    return jsonify(trueReturn(data=back_text))
@api.route("/updata-notice")
def up():
    """增加赛事预告"""
    group=[
        {"number":"一","ID":"3502","name":"杜雨","school":"齐医学院"}
    ]
    json_group=json.dumps(group)
    update(noticetime="16:00",name="男子甲组标枪及格赛",local="东北石油大学田径场",group=json_group,noticedate="2019年07月14日")
    return "sucess"
@api.route("/search")
def get_notice_by_id():
    '''根据ID查询赛事预告详情'''
    info=get_notice_id("2695")
    return jsonify(trueReturn(data=info))
@api.route("/all-score")
def score_list():
    '''赛事成绩列表'''
    back=get_score()
    print(back)
    return jsonify(trueReturn(data=back))
@api.route("/updata-score")
def upscore():
    """添加赛事成绩"""
    group=[
        # {"id":"101","name":"杜雨","group":"齐医学院","score":"00:34.06","total":"9",'text':"DSQ"},
        # {"id": "102", "name": "杜雨", "group": "齐医学院", "score": "00:34.06", "total": "7", 'text': ""},
        {"name":"东北石油大学","score":"4"},
        {"name":"黑龙江省八一农垦大学","score":"1"}
    ]
    text=["女子甲组：00.32.16","NJW：超女子甲组  EJW：平女子甲组"]
    json_group=json.dumps(group)
    update_score(name="（高中青少年组）足球1/4决赛",result=json.dumps(group),style="比分",scoretime="2019年07月14日",text=json.dumps(text))
    return "sucess"
@api.route("/get-score",methods=['POST'])
def get_score_id():
    '''通过id查成绩'''
    get_json=request.get_json()
    print(get_json)
    ID=get_json['ID']
    print(ID)
    back=get_score_info(ID)
    return jsonify(trueReturn(data=back))
