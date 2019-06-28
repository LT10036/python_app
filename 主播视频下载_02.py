
# -------------------------------------------------------------------------------------------------------
#
#  1.  主 播 视 频 下 载 因 为 主 播 请 求 的 都 是 一 个 地 址 ， 所 以 存 储 在 了 一 个 json 文 件 中
#      了 ， 需 要 提 取 出 来 链 接
#  2.   json.loads 不 好 使 ，直 接 正 则 提 取，然 后 requests.get 获 取 后 转 成 二 进 制
#  3.  打 开 一 个 二 进 制 的 MP4 文 件，以 二 进 制 格 式 写 入 数 据
#                                 注 意 ：是 二 进 制 数 据 写 入
#
# ------------------------------------------------------------------------------------------------------

import requests
import re
import time
import os

root_ntext = 'D:\\LT\\pyproj\\python_app\\zhubo_text\\'
root = 'D:\\LT\pyproj\\python_app\\主播视频\\'
list_j = os.listdir('D:\\LT\\pyproj\\python_app\\zhubo_text')
# 伪 装 请 求 头 及 代 理 池
headers={"User-Agent" : "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
  "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  "Accept-Language" : "en-us",
  "Connection" : "keep-alive",
  "Accept-Charset" : "GB2312,utf-8;q=0.7,*;q=0.7"}

# 开 始 读 取 json 文 件
for m in list_j:
    text_l = root_ntext + m
    f = open(text_l,'r',encoding='utf-8')
    text_m = f.read()

    # 提 取 视 频 大 地 址 范 围
    l = re.findall('"video":{"play_addr":{"uri":.*?]',text_m)

    #  获 取 小 地 址
    for i in l:
        hre = re.findall('"http://.*?"',i)
        try:
            hre_n = hre[0][1:-1]
            print(hre_n)
            # 文件 名 字 以 时 间 戳 命 名
            r = time.time()
            r = str(int(r))
            page = requests.get(hre_n)
            # 组 装 视 频 保 存 地 址
            root_t = root+r+'.mp4'
            w = open(root_t,'wb')
            w.write(page.content)
            w.close()
            time.sleep(10)
            print("完成一次")
        except:
            continue







