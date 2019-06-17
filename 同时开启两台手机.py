
# ----------------------------------------------------------------------------------
# 同 时 打 开 两 台 手 机 上 的  app
# ----------------------------------------------------------------------------------

from appium import webdriver

# app 参 数 ：系统，版本，包名，入口名，设备码，不重复安装appium settings
# 第 一 个 手 机
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['appPackage'] = 'com.ss.android.ugc.aweme'
desired_caps['appActivity'] = 'com.ss.android.ugc.aweme.main.MainActivity'
desired_caps['deviceName'] = '88MFDMG3AVLH'
# 一 定 添 加 这 个 ， 不然 会 无 法 打 开 某 一 个 手 机 ， 指 定 启 动的 设 备 码
desired_caps['udid'] = '88MFDMG3AVLH'
desired_caps['automationName'] = 'UiAutomator2'

# 第 二 个 手 机
desired_caps2 = {}
desired_caps2['platformName'] = 'Android'
desired_caps2['platformVersion'] = '5.1'
desired_caps2['appPackage'] = 'com.ss.android.ugc.aweme'
desired_caps2['appActivity'] = 'com.ss.android.ugc.aweme.main.MainActivity'
desired_caps2['deviceName'] = '88AKDMH22BEC'
# 一 定 添 加 这 个 ， 不 然 会 无 法 打 开 某 一 个 手 机 ， 指 定 启 动 的 设 备 码
desired_caps2['udid'] = '88AKDMH22BEC'
desired_caps2['automationName'] = 'UiAutomator2'


# 开 始 运 行
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver2 = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps2)

# 隐 式 等 待 10 秒
driver.implicitly_wait(10)
driver2.implicitly_wait(10)


# 屏 幕 滑 动 从（200,500）滑到（200,100）
driver.swipe(200,500,200,100)
driver2.swipe(200,500,200,100)
