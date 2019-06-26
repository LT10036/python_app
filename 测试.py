
# 提取首页列表
# import json
#
# f = open('D:\\LT\\pyproj\\python_app\\liulan_text\\123.json','r',encoding='utf-8')
#
# text = f.read()
# text_n = json.loads(text)
# for i in range(0,5):
#     max_link = text_n['aweme_list'][i]['video']['play_addr']['url_list'][0]
#     print(max_link)



import json


f = open('D:\\LT\pyproj\\python_app\\sousuo_text\\111.json','r',encoding='utf-8')
text = f.read()
text_n = json.loads(text)

print(text_n)


print(text_n['data'][0]['aweme_info']['video']['bit_rate'][1]['play_addr']['url_list'][0])


