
#  --------------------------------------------
#    五 分  钟  误  操  作   会   退 出  app
#
# ---------------------------------------------


from appium import webdriver
import time
import random

desired_caps1 = {}
desired_caps1['deviceName']='SGSWD6CQH66SBEFI'
desired_caps1['udid']='SGSWD6CQH66SBEFI'
desired_caps1['platformName'] = 'Android'
desired_caps1['platformVersion'] = '5.1'
desired_caps1['appPackage'] = 'com.ss.android.ugc.aweme'
desired_caps1['appActivity'] = 'com.ss.android.ugc.aweme.main.MainActivity'
desired_caps1['automationName'] = 'UiAutomator2'
desired_caps1['noReset'] = 'True'
# appium默认60秒内无指令会退出app，下边修改成了300秒
desired_caps1['newCommandTimeout']='300'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps1)
# 点击搜索
driver.tap([(990, 130)], 100)
time.sleep(2)
driver.tap([(500, 120)], 100)
time.sleep(2)

# 输入内容点击搜索
driver.find_element_by_id('com.ss.android.ugc.aweme:id/a9h').send_keys("美食")
time.sleep(1)
driver.tap([(980, 130)], 100)
# 寻找用户
time.sleep(5)
driver.tap([(450, 270)], 100)
time.sleep(2)
# 大循环，要刷多少个用户，暂时一直刷新，后期将 while Ture 改成   for in range()
t11 = random.randint(10,20)
while True:
    # 翻看多少个视频
    t5 = random.randint(10,12)
    print("本次共需要观看%d个视频"%t5)
    t6 = t5-1
    t000 = 0
    # 要给多少个视频点赞
    t00 = random.randint(1,2)
    # 分别给第几个视频点赞
    t0 = []
    while True:
        if len(t0) == t00:
            break
        else:
            t4 = random.randint(20,30)
            if t4 not in t0:
                t0.append(t4)
            else:
                continue
    # 开始点击列表顶端的用户（暂定第一个的位置，进去主播主页）
    print("这次点赞的视频分别是",t0)
    driver.tap([(500,470)],100)
    # 开始点击第一个视频,等待3秒缓冲，防止视频刷不出来
    time.sleep(10)
    driver.tap([(180,1700)],100)
    for t7 in range(t6):
        # 每个视频观看20-30秒之间
        t3 = random.randint(5,7)
        time.sleep(t3)
        print("本次观看了%d秒,然后开始判断其是否需要点赞"%t3)
        # 判断是否点赞的节点
        if t000 not in t0:
            driver.swipe(600,1700,600,200)
            t000 = t000+1
            print("本次不在，不点赞，所以直接翻过去了")
        else:
            # 点赞，并评论
            driver.tap([(990,900)],100)
            time.sleep(3)
            print("已点赞，开始评论了")
            driver.find_element_by_id('com.ss.android.ugc.aweme:id/tu').click()
            driver.find_element_by_id('com.ss.android.ugc.aweme:id/tu').send_keys("你开心就好")
            driver.find_element_by_id('com.ss.android.ugc.aweme:id/u_').click()
            time.sleep(2)
            t000 = t000 + 1
            print("评论完了，开始下一个视频")
            driver.swipe(600, 1700, 600, 200)
    driver.tap([(80, 150)], 100)
    time.sleep(2)
    try:
        text_g = driver.find_element_by_id('com.ss.android.ugc.aweme:id/aah').text
        if text_g=="关注":
            driver.tap([(800, 130)], 100)
            t12 = random.randint(5, 10)
            print("点赞后-------休息5-10秒")
            time.sleep(t12)
            #     点两次回到用户列表
            driver.tap([(80, 130)], 100)
            time.sleep(3)
            #     开始向上划去一段距离 228 一个模块
            t8 = random.randint(2, 5)
            t9 = t8 * 228
            t10 = 1700 - t9
            driver.swipe(300, 1700, 300, t10)
        else:
            t12 = random.randint(5, 10)
            print("不点赞--------------休息5-10秒")
            time.sleep(t12)
            driver.tap([(80, 130)], 100)
            time.sleep(3)
            #     开始向上划去一段距离 228 一个模块
            t8 = random.randint(2, 5)
            t9 = t8 * 228
            t10 = 1700 - t9
            driver.swipe(300, 1700, 300, t10)
    except:

    #     休息5-10分钟 300--600 秒
        t12 = random.randint(5,10)
        print("报错后---------------休息5-10秒")
        time.sleep(t12)
    #     点两次回到用户列表
        driver.tap([(80, 130)], 100)
        time.sleep(3)
    #     开始向上划去一段距离 228 一个模块
        t8 = random.randint(2,5)
        t9 = t8*228
        t10 = 1700-t9
        driver.swipe(300,1700,300,t10)



























