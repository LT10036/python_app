

from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['appPackage'] = 'com.ss.android.ugc.aweme'
desired_caps['appActivity'] = 'com.ss.android.ugc.aweme.main.MainActivity'
desired_caps['deviceName'] = 'SGSWD6CQH66SBEFI'
# 一 定 添 加 这 个 ， 不然 会 无 法 打 开 某 一 个 手 机 ， 指 定 启 动的 设 备 码
desired_caps['udid'] = 'SGSWD6CQH66SBEFI'
desired_caps['automationName'] = 'UiAutomator2'
# 'noReset': "True"  启 用 app 登 录 信 息
desired_caps['noReset'] = 'True'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
for i in range(2):
    time.sleep(1)
    driver.swipe(300,1200,300,300)
def foll_anchor(driver):
    # 寻找某个主播的关注
    n_name = input("请先输入要找的主播名字:")
    driver.tap([(987,132)],100)
    time.sleep(3)
    driver.tap([(400,120)],100)
    time.sleep(1)
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/a8d').send_keys(n_name)
    time.sleep(2)
    # 点击搜索
    driver.tap([(984,130)],100)
    time.sleep(5)
    # 进入主页
    driver.tap([(387,530)],100)
    time.sleep(4)
    # 进入粉丝列表页面
    driver.tap([(500,1318)],100)
    time.sleep(2)
    num = input("请输入想要关注前几页的该主播:")
    num = int(num)
    for r in range(num):
        c=328
        n_n = 328
        for i in range(7):
            driver.tap([(900,n)],100)
            n = n + 228
            time.sleep(1)
        n_n = c
        driver.swipe(600,1810,600,210)
    driver.tap([(80,130)],100)
    time.sleep(2)
    driver.tap([(80,130)],100)
    print("已关注完成，即将返回首页，请按提示操作")