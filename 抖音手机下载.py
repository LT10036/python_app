import os
import json
import requests
import time

list_all = os.listdir('F:\\l1')
print(list_all)
source = "F:\\l1\\"
for i in list_all:
    hre = source +i
    f = open(hre,'r',encoding='utf-8')
    l = f.read()
    text_json = json.loads(l)
    for i in range(5):
        try:
            titm_t = int(time.time())
            title = str(titm_t)+ ".mp4"
            hre = text_json['aweme_list'][0]['video']['play_addr']['url_list'][0]
            f = open(title,'ab')
            cont = requests.get(hre)
            f.write(cont.content)
            f.close()
        except:
            continue




    # print(text_json['aweme_list']['video']['play_addr']['url_list'][0])
    # video = text_json['aweme_list']['video']
    # print(video)
    print("--------------------------------------------------------------")













