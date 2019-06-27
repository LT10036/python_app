
# -------------------------------------------------------------------------
#  本操作手机为 OPPO R9m  如换手机请更改模拟点击的 tap 像素
#  按 1 进入 搜索主播，并关注
#  按 2 进入 搜索品类
#  按 3 进入 主播视频下载
#  按 4 进入 主播视频点赞并评论，评论已写死，可改文本读取
#  按 0 退出
# -------------------------------------------------------------------------

from appium import webdriver
import time

# app 参 数 ：系统，版本，包名，入口名，设备码，不重复安装appium settings
# 第 一 个 手 机
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

# 上 滑 一 下
time.sleep(2)
driver.swipe(300,800,300,100)
driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="搜索"]').click()
# 定 义 操 作 指 令


def s_anchor (driver):
    n_name = input('请输入想要关注的主播官方昵称：')
    time.sleep(2)
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/a8d').click()
    time.sleep(1)
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/a8d').send_keys(n_name)
    time.sleep(2)
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/d6m').click()
    try:
        driver.find_element_by_id('com.ss.android.ugc.aweme:id/n2').click()
        print("已关注主播%d"%n_name)
    except:
        print("此账号主播未找到，请确认名字是否正确，已返回主菜单")



def s_target(driver):
    n_name = input('请输入想要寻找的品类：')

    time.sleep(2)
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/a8d').click()
    time.sleep(1)
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/a8d').send_keys(n_name)
    time.sleep(2)
    # 点击搜索
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/d6m').click()
    num = input("请输入要浏览多少个视频")
    try:
        num = int(num)
        for i in range(num):
            time.sleep(1)
            driver.swipe(300, 1200, 300, 300)
        print("已保存前30个商品视频链接,将要返回主菜单，请按提示操作")
    except:
        print("请输入合法数字，本次操作无效，即将返回主菜单，请按提示操作")


def d_video(driver):
    n_name = input('请输入想要下载的主播官方昵称：')
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
    num = input("请输入想要保存多少页的视频，按回车键结束")
    try:
        num = int(num)
        for i in range(num):
            time.sleep(1)
            driver.swipe(300, 1200, 300, 300)
        print("已保存前%d页面视频链接，讲会返回主菜单，请按提示操作" % num)
        driver.tap([(80,130),100])
    except:
        print("请输入正确数字，本次操作无效，即将返回主菜单，请按提示操作")
def G_up(drover):
    n_name = input('请输入想要下载的主播官方昵称：')
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
    driver.tap([(100, 1600)], 100)

    # 循 环 点 赞  前 20 个 时 视 频
    num = input("请输入想要点赞的视频数量，从主页第一个视频开始")
    try:
        num = int(num)
        for i in range(num):
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
            driver.swipe(300, 1200, 300, 200)
            print("完成一次点赞和评论，继续中")
        print("点赞评论结束，即将返回主菜单，请按操作提示")
    except:
        print("请输入合法数字，本次操作无效，即将返回主菜单，请按照操作提示")



while True:

    l=input("请输入    搜索主播请输入： 1   搜索品类商品请输入： 2   下载主播视频 ： 3       评论主播视频及点赞请输入： 4       结束请输入 ：0")

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
    elif l == 4:
        d_video(driver)
        print('如想点赞评论其他主播视频，请按指令操作')
    elif l == 0:
        driver.quit()
        break
    else:
        print("非法指令，不在服务范围内")

print("谢谢使用，下次见")




