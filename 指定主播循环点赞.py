
# -------------------------------------------------------------------------------
# 本 操 作 手 机 为 oppo R9m  如 果 更 换 手 机 请 修 改 tap 参 数
#
# 指 定 主 播 下 的 视 频 循 环 点 赞 评 论
# -------------------------------------------------------------------------------


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

l = input("循环开始：  开始点赞并评论请输入：  1    退出请输入：  2")
n_name = input("请输入主播名字：")


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 上 滑 一 下
for i in range(2):
    time.sleep(5)
    driver.swipe(300,1200,300,300)
try:
    while True:
            # l = input("循环开始：  开始点赞并评论请输入：  1    退出请输入：  2")
            l = int(l)
            if l == 2:
                break
            elif l == 1:
                # 主 播 昵 称
                # n_name = input("请输入主播名字：")
                driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="搜索"]').click()
                time.sleep(3)
                driver.find_element_by_id('com.ss.android.ugc.aweme:id/a8d').click()
                time.sleep(1)
                driver.find_element_by_id('com.ss.android.ugc.aweme:id/a8d').send_keys(n_name)
                time.sleep(2)
                # 点击搜索
                driver.find_element_by_id('com.ss.android.ugc.aweme:id/d6m').click()
                time.sleep(5)
                # 进入主页
                driver.find_element_by_id('com.ss.android.ugc.aweme:id/d9j').click()

                #  按 坐 标 点 击 第一  个 置 顶 视 频
                time.sleep(2)
                driver.tap([(100,1600)],100)
                for i in range(20):
                    time.sleep(2)
                    driver.tap([(960, 900)], 100)
                    time.sleep(2)
                    # 开 始 评 论
                    driver.find_element_by_id('com.ss.android.ugc.aweme:id/ta').click()
                    time.sleep(2)
                    driver.find_element_by_id('com.ss.android.ugc.aweme:id/ta').send_keys("人间套路深")
                    time.sleep(1)
                    driver.find_element_by_id('com.ss.android.ugc.aweme:id/tq').click()
                    time.sleep(2)
                    driver.swipe(300,1200,300,200)
                    print("完成一次，继续中")
            else:
                print("请 输 入 正 确 指 定 范 围")

except:
    driver.quit()


