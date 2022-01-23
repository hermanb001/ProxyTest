# -*- coding: utf-8 -*-
# @Time    : 2021/4/9 06:30
# @Author  : skywolf627
# @Email   : skywolf627@qq.com
import traceback
import os
import requests
import urllib
import json
import logging

# 初始化日志记录器


def initLog(_logFilePath):
    global logFilePath
    logFilePath = './'+_logFilePath
    # 日志基础配置
    # 创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 创建一个handler，用于写入日志文件
    # w 模式会记住上次日志记录的位置
    fh = logging.FileHandler(logFilePath, mode='a', encoding='utf-8')
    fh.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(fh)
    # 创建一个handler，输出到控制台
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter(
        "[%(asctime)s]:%(levelname)s:%(message)s"))
    logger.addHandler(ch)


# 清空日志记录


def clearLog():
    open(logFilePath, mode='w', encoding='utf-8')


# 获取日志记录


def getLogContent():
    content = ''
    with open(logFilePath, "r", encoding='utf-8') as f:
        for line in f.readlines():
            content += line + '<br>'
    return content


# 读取用户配置信息
# 错误原因有两种：格式错误、未读取到错误
def readJsonFile(jsonFilePath):
    try:
        with open('./'+jsonFilePath, 'r') as fp:
            config = json.load(fp)
            return config
    except Exception as e:
        print(traceback.format_exc())
        logging.error('账号信息获取失败错误，原因为: ' + str(e))
        logging.error('1.请检查是否在Secrets添加了账号信息，以及添加的位置是否正确。')
        logging.error('2.填写之前，是否在网站验证过Json格式的正确性。')
