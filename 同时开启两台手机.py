
# ----------------------------------------------------------------------------------
# 本操作手机为  魅蓝 2
# 同 时 打 开 两 台 手 机 上 的  app
# ----------------------------------------------------------------------------------
import threading
from appium import webdriver
import time



def P_S(driver):
    print("我开始跑了哦。。。。。。。。。。。。。。。。。。。")
    for i in range(10):
        driver.swipe(200,1700,200,300)
        time.sleep(3)
    print("我跑完了，等你哦")
    driver.quit()












# app 参 数 ：系统，版本，包名，入口名，设备码，不重复安装appium settings
# 第 一 个 手 机
l=['JJUC7L8T99999999','88AKDMH22BEC']

desired_caps = {}
desired_caps['deviceName']='JJUC7L8T99999999'
desired_caps['udid']='JJUC7L8T99999999'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['appPackage'] = 'com.ss.android.ugc.aweme'
desired_caps['appActivity'] = 'com.ss.android.ugc.aweme.main.MainActivity'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['noReset'] = 'True'

desired_caps1 = {}
desired_caps1['deviceName']='SGSWD6CQH66SBEFI'
desired_caps1['udid']='SGSWD6CQH66SBEFI'
desired_caps1['platformName'] = 'Android'
desired_caps1['platformVersion'] = '5.1'
desired_caps1['appPackage'] = 'com.ss.android.ugc.aweme'
desired_caps1['appActivity'] = 'com.ss.android.ugc.aweme.main.MainActivity'
desired_caps1['automationName'] = 'UiAutomator2'
desired_caps1['noReset'] = 'True'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver2 = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps1)

t = threading.Thread(target=P_S,args=(driver,))
t.start()
t2 = threading.Thread(target=P_S,args=(driver2,))
t2.start()
print("。。。。。。。。都开始跑了。。。。。。。")
while True:
    l = threading.active_count()
    if  l==1:
        break
    else:
        time.sleep(3)
print("...............都跑完了..................")