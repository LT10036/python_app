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
list_all = os.listdir('D:\\LT\\pyproj\\l1')
print(list_all)
source = "D:\\LT\\pyproj\\l1\\"

#  json  文  件 读  取  循  环
for i in list_all:
    hre = source +i
    f = open(hre,'r',encoding='utf-8')
    l = f.read()
    text_json = json.loads(l)

    # 一 般 情 况 是 每 个 json 有 5 个 视 频  地  址 ，后 期 完 善 re 获 取 全 部 网 址
    for i in range(5):
        try:
            titm_t = int(time.time())
            title = str(titm_t)+ ".mp4"
            hre = text_json['aweme_list'][i]['video']['play_addr']['url_list'][0]
            print(hre)
            f = open(title,'ab')
            cont = requests.get(hre,headers=headers)
            f.write(cont.content)
            f.close()
            time.sleep(10)
            print("本 次 下 载 完 毕 ，开 始 下 一 个 ")
        except:

            print("这 个 视 频 下 载 出 错")
            continue


    print("------------------------------视 频 全 部 下 载  完 毕--------------------------------")













