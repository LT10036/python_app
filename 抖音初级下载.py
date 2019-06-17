
# ------------------------------------------------------------------------------------
# 简 单 功 能 ： 打 开 抖 音 ， 然 后 保 存 视 频 到 本 地
# 需 要 提 前 开 启 appium 服 务 ，打 开 appium 程 序 即 可
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

# 隐 式 等 待 10 秒
driver.implicitly_wait(10)

# 屏 幕 滑 动 从（200,500）滑到（200,100）
driver.swipe(200,500,200,100)

# 点 击“分享按钮”
driver.find_element_by_id('com.ss.android.ugc.aweme:id/cgz').click()
time.sleep(2)

# 点 击“保存到本地”
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ImageView').click()

# 等 待 下 载 完 毕
time.sleep(60)

# 退 出 app
driver.quit()