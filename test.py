import requests
import json
import time
import re
import logging
import traceback
import os
import random
import datetime
import utils
# import base64


def main(event, context):
    # 初始化日志文件
    utils.initLog('log.txt')
    utils.clearLog()
    savePoint(
        'https://free886.herokuapp.com/clash/proxies', 'free886-00')

    savePoint(
        'https://free.jingfu.cf/clash/proxies?nc=CN&speed=20', 'guest997-50')
      
    savePoint(
        'http://guobang.herokuapp.com/clash/proxies?nc=CN&speed=30', 'guobang-30')


# 获取文章地址


def savePoint(url, name):
    resp = requests.get(url)
    dirs = './subscribe'
    day = time.strftime('%Y.%m.%d', time.localtime(time.time()))
    if 'proxies' in resp.text:
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        with open(dirs + '/' + name, 'w', encoding='utf-8') as f:
            f.write(resp.text.replace('"name":"','"name":"'+ day+'_'))
            print(name+'生成成功')


# 主函数入口
if __name__ == '__main__':
    main("", "")
