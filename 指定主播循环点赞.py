
# -------------------------------------------------------------------------------
# 关 注 主 播 下 的 单个  视 频
#
#
# -------------------------------------------------------------------------------


from appium import webdriver
import time

# app 参 数 ：系统，版本，包名，入口名，设备码，不重复安装appium settings
# 第 一 个 手 机
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['appPackage'] = 'com.ss.android.ugc.aweme'
desired_caps['appActivity'] = 'com.ss.android.ugc.aweme.main.MainActivity'
desired_caps['deviceName'] = '88AKDMH22BEC'
# 一 定 添 加 这 个 ， 不然 会 无 法 打 开 某 一 个 手 机 ， 指 定 启 动的 设 备 码
desired_caps['udid'] = '88AKDMH22BEC'
desired_caps['automationName'] = 'UiAutomator2'
# 'noReset': "True"  启 用 app 登 录 信 息
desired_caps['noReset'] = 'True'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 上 滑 一 下
time.sleep(2)
driver.swipe(300,800,300,100)
while True:
    l = input("循环开始：  开始点赞请输入  1    退出请输入  2")
    l = int(l)
    if l == 2:
        break
    elif l == 1:
        # 主 播 昵 称
        n_name = input("请输入主播名字：")
        driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="搜索"]').click()
        time.sleep(2)
        driver.find_element_by_id('com.ss.android.ugc.aweme:id/a97').click()
        time.sleep(1)
        driver.find_element_by_id('com.ss.android.ugc.aweme:id/a97').send_keys(n_name)
        time.sleep(2)
        driver.find_element_by_id('com.ss.android.ugc.aweme:id/d9a').click()
        time.sleep(5)
        driver.find_element_by_id('com.ss.android.ugc.aweme:id/dba').click()

        #  按 坐 标 点 击 第一  个 置 顶 视 频
        time.sleep(5)
        driver.tap([(100,1100)],100)


        # 点 击 红 心 关 注
        time.sleep(5)
        driver.tap([(610,610)],100)
        print("已点赞")

        # 循 环 点 赞
        for i in range(20):
            driver.swipe(300,800,300,100)
            time.sleep(5)
            driver.tap([(610, 610)], 100)
            time.sleep(2)
    else:
        print("请 输 入 正 确 指 定 范 围")




