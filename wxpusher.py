# -*- coding: utf-8 -*-
# @Time    : 2021/4/9 06:30
# @Author  : skywolf627
# @Email   : skywolf627@qq.com

import traceback
import os
import requests
import urllib
import json

# 发送主题消息
def sendSingleMessage(appToken, title, content, uid, msgUrl):
    try:
        data = {
            "appToken": appToken,
            "content": content,
            "summary": title,
            "contentType": 1,
            "uids":  uid,
            "url": msgUrl
        }
        url = 'http://wxpusher.zjiecode.com/api/send/message'
        headers = {'Content-Type': 'application/json'}
        body = json.dumps(data).encode(encoding='utf-8')
        resp = requests.post(url, data=body, headers=headers)
        result = json.loads(resp.text)
        if result['code'] == 1000:
           print('创建发送任务成功') 
        else:               
           print(result['msg']) 
    except Exception as e:
        print('wxpusher通知推送异常，原因为: ' + str(e))
        print(traceback.format_exc())


# 发送单个消息
def sendTopicMessage(appToken, title, content, topicId, msgUrl):
    try:
        data = {
            "appToken": appToken,
            "content": content,
            "summary": title,
            "contentType": 1,
            "topicIds":  topicId,
            "url": msgUrl
        }
        url = 'http://wxpusher.zjiecode.com/api/send/message'
        headers = {'Content-Type': 'application/json'}
        body = json.dumps(data).encode(encoding='utf-8')
        resp = requests.post(url, data=body, headers=headers)
        result = json.loads(resp.text)
        if result['code'] == 1000:
           print('创建发送任务成功') 
        else:               
           print(result['msg']) 
    except Exception as e:
        print('wxpusher通知推送异常，原因为: ' + str(e))
        print(traceback.format_exc())


# 发送push+通知
def sendPushplus(token,title,content):
    try:
        # 发送内容
        data = {
            "token": token,
            "title": title,
            "content": content
        }
        url = 'http://www.pushplus.plus/send'
        headers = {'Content-Type': 'application/json'}
        body = json.dumps(data).encode(encoding='utf-8')
        resp = requests.post(url, data=body, headers=headers)
        print(resp)
    except Exception as e:
        print('push+通知推送异常，原因为: ' + str(e))
        print(traceback.format_exc())