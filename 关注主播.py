




from appium import webdriver
import time

# app 参 数 ：系统，版本，包名，入口名，设备码，不重复安装appium settings
# 第 一 个 手 机
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '5.1'
# desired_caps['appPackage'] = 'com.ss.android.ugc.aweme'
# desired_caps['appActivity'] = 'com.ss.android.ugc.aweme.main.MainActivity'
# desired_caps['deviceName'] = '88AKDMH22BEC'
# # 一 定 添 加 这 个 ， 不然 会 无 法 打 开 某 一 个 手 机 ， 指 定 启 动的 设 备 码
# desired_caps['udid'] = '88AKDMH22BEC'
# desired_caps['automationName'] = 'UiAutomator2'
# # 'noReset': "True"
# desired_caps['noReset'] = 'True'
desired_caps = {
                'platformName':'Android',
                'deviceName': '88AKDMH22BEC',
                'platformVersion': '5.1',
                'appPackage':'com.ss.android.ugc.aweme',
                'appActivity':'com.ss.android.ugc.aweme.main.MainActivity',
                'noReset': 'True'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(5)
driver.swipe(300,1000,300,200)
time.sleep(3)


try:
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/d8o').click()
except:
    print("无通知")
time.sleep(3)
driver.swipe(300,600,300,100)

print("翻页")

time.sleep(3)
print("开始点击关注主播")
driver.find_element_by_id('com.ss.android.ugc.aweme:id/ae0').click()
print("已关注")