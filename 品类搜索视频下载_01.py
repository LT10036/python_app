
# --------------------------------------------------------------
#
#  摘 出 分 享 链 接 ，去 第 三 方 解 析 无 水 印 地 址
#            “http://www.chematong.com/”
#
# -------------------------------------------------------------


import os
import json
import requests
import time


# 伪 装 请 求 头 及 代 理 池
headers={"User-Agent" : "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
  "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  "Accept-Language" : "en-us",
  "Connection" : "keep-alive",
  "Accept-Charset" : "GB2312,utf-8;q=0.7,*;q=0.7"}
# proxies = {'http': '116.196.81.58:3128',
#            'https': '115.159.31.195:8080'
#            }

# 组 装 地 址
list_all = os.listdir('D:\\LT\\pyproj\\python_app\\sousuo_text')
print(list_all)
source = "D:\\LT\\pyproj\\python_app\\搜索品类视频\\"

#  json  文  件 读  取  循  环
for i in list_all:
    hre = 'D:\\LT\\pyproj\\python_app\\sousuo_text\\' +i
    f = open(hre,'r',encoding='utf-8')
    l = f.read()
    text_json = json.loads(l)

    l = len(text_json['data'])
    print(l)
    for i in range(l):
        try:
            print(text_json['data'][i]['aweme_info']['share_url'])
            # print(text_json['data'][i]['aweme_info']['share_info'])
        except:
            print('失败')
            continue
