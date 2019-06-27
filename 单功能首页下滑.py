
# ------------------------------------------------------------------------------------
# 本操作手机为 魅蓝 2
# 简 单 功 能 ： 打 开 抖 音 ， 然 后 保 存 视 频 到 本 地
# 需 要 提 前 开 启 appium 服 务 ，打 开 appium 程 序 即 可
# 可 以 保 存 到 本 地 （已 注 释 掉，因 为 有 水 印 ）
# 打 开 fiddler  ,设 置 手 机 上 网 代 理 通 过 fiddler 联 网
# fiddler 设 置 好 保 存 json 文 件 ，方 便 02 使 用，注 意 修 改 fiddler 中 的 地 址
# 主 要 是 fiddler 中 的 json 来 源 网 址 修 改
#-------------------------------------------------------------------------------------


from appium import webdriver
import time

# app 参 数 ：系统，版本，包名，入口名，设备码，不重复安装appium settings
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['appPackage'] = 'com.ss.android.ugc.aweme'
desired_caps['appActivity'] = 'com.ss.android.ugc.aweme.main.MainActivity'
desired_caps['deviceName'] = '88AKDMH22BEC'
desired_caps['automationName'] = 'UiAutomator2'

# 开 始 运 行
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(10)
# 隐 式 等 待 10 秒
driver.implicitly_wait(10)

for i in range(10):
    # 隐 式 等 待 10 秒

    # 屏 幕 滑 动 从（200,500）滑到（200,100）
    driver.swipe(200,1000,200,300)
    # 强 制 休 息 5 秒
    time.sleep(5)

driver.quit()