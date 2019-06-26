




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
driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="搜索"]').click()
# 定 义 操 作 指 令


def s_anchor (driver):
    n_name = input('请输入想要关注的主播官方昵称：')
    time.sleep(2)
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/a97').click()
    time.sleep(2)
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/a97').send_keys(n_name)
    time.sleep(2)
    try:
        driver.find_element_by_id('com.ss.android.ugc.aweme:id/d9a').click()
    except:
        print("此账号主播未找到，请确认名字是否正确，已返回主菜单")



def s_target(driver):
    n_name = input('请输入想要寻找的品类：')
    time.sleep(2)
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/a97').click()
    time.sleep(2)
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/a97').send_keys(n_name)
    time.sleep(2)
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/d9a').click()
    for i in range(30):
        time.sleep(1)
        driver.swipe(300, 1000, 300, 100)
    print("已保存前30个商品视频链接")


def d_video(driver):
    n_name = input('请输入想要下载的主播官方昵称：')
    time.sleep(2)
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/a97').click()
    time.sleep(2)
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/a97').send_keys(n_name)
    time.sleep(2)
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/d9a').click()
    time.sleep(5)
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/dba').click()
    for i in range(20):
        time.sleep(1)
        driver.swipe(300, 1000, 300, 100)
    print("已保存前20页面视频链接")

while True:

    l=input("请输入    搜索主播请输入： 1   搜索品类商品请输入： 2   下载主播视频 ： 3     结束请输入 ：0")

    try:
        l = int(l)
    except:
        print("非法指令  请输入数字")
    if l == 1:
        s_anchor(driver)
        print("已关注，如想继续关注其他请安指令操作")
    elif l == 2:
        s_target(driver)
        print('如想搜索其他商品，请按指令操作')
    elif l == 3:
        d_video(driver)
        print('如想下载其他主播视频，请按指令操作')
    elif l == 0:
        driver.quit()
        break
    else:
        print("非法指令，不在服务范围内")

print("谢谢使用，下次见")




