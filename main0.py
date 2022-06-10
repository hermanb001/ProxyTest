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
        'https://eu-proxypool.herokuapp.com/clash/proxies?nc=CN&speed=30', 'eu-proxypool')

    savePoint(
        'https://free886.herokuapp.com/clash/proxies', 'free886')
      
    savePoint(
        'http://guobang.herokuapp.com/clash/proxies?nc=CN&speed=30', 'guobang')

    savePoint(
        'https://hellopool.herokuapp.com/clash/proxies?nc=CN&speed=50', 'hellopool')
    
    savePoint(
        'https://free.jingfu.cf/clash/proxies?nc=CN&speed=20', 'jingfu')
    
    savePoint(
        'https://fq.lonxin.net/clash/proxies?nc+CN&type=trojan', 'lonxin')
    
    savePoint(
        'https://origamiboy.herokuapp.com/clash/proxies?nc=CN&speed=10', 'origamiboy')
    
    savePoint(
        'https://sspool.herokuapp.com/clash/proxies?nc=CN&speed=50', 'sspool')
    
#    savePoint(
#        'http://clash.3wking.com:12580/clash/proxies?nc=CN', '3wking')
    
#    savePoint(
#        'https://proxy.cloudkingzst.xyz/clash/proxies?c=US&type=ss', 'cloudkingzst')
    
#    savePoint(
#        'https://ednovas.design/clash/proxies?nc=CN&speed=40', 'ednovas')
    

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
