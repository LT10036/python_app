
# -------------------------------------------------------------------------
#  本操作手机为 OPPO R9m  如换手机请更改模拟点击的 tap 像素
#  按 1 进入 搜索主播，并关注
#  按 2 进入 搜索品类
#  按 3 进入 主播视频下载
#  按 4 进入 主播视频点赞并评论，评论已写死，可改文本读取
#  按 5 进入 批量添加某个主播的粉丝
#  按 6 进入 批量添加某个主播关注的人为关注
#  按 7 进入 私信主播
#  按 0 退出
#  使 用 前 注 意 修 改 搜 索 框 send_keys 的 id ，经 常 会 变
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
for i in range(2):
    time.sleep(2)
    driver.swipe(300,800,300,100)
# 点 击 搜 索   id 及 xpath 不 好 使 ，不 如 直 接 点 击
driver.tap([(987,132)],100)
# 定 义 操 作 指 令


def s_anchor (driver):
    n_name = input('请输入想要关注的主播官方昵称：')
    time.sleep(2)
    driver.tap([(400,120)],100)
    time.sleep(1)
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/a8d').send_keys(n_name)
    time.sleep(2)
    driver.tap([(984,130)],100)
    try:
        driver.tap([(900,600)],100)
        print("已关注主播%d"%n_name)
    except:
        print("此账号主播未找到，请确认名字是否正确，已返回主菜单")



def s_target(driver):
    n_name = input('请输入想要寻找的品类：')

    time.sleep(2)
    driver.tap([(400,120)],100)
    time.sleep(1)
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/a8d').send_keys(n_name)
    time.sleep(2)
    # 点击搜索
    driver.tap([(984,130)],100)
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
    driver.tap([(400,120)],100)
    time.sleep(1)
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/a8d').send_keys(n_name)
    time.sleep(2)
    # 点击搜索
    driver.tap([(984,130)],100)
    time.sleep(5)
    # 进入主页
    driver.tap([(387,530)],100)
    num = input("请输入想要保存多少页的视频，按回车键结束")
    try:
        num = int(num)
        for i in range(num):
            time.sleep(1)
            driver.swipe(300, 1200, 300, 300)
        print("已保存前%d页面视频链接，讲会返回主菜单，请按提示操作" % num)
        driver.tap([(80,130),100])
        driver.tap([(987,132)],100)
    except:
        print("请输入正确数字，本次操作无效，即将返回主菜单，请按提示操作")
def G_up(drover):
    n_name = input('请输入想要点赞和评论视频的主播官方昵称：')
    time.sleep(3)
    driver.tap([(400,120)],100)
    time.sleep(1)
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/a8d').send_keys(n_name)
    time.sleep(2)
    # 点击搜索
    driver.tap([(984,130)],100)
    time.sleep(2)
    # 进入主页
    driver.tap([(387,530)],100)

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
    except:
        print("请输入合法数字，本次操作无效，即将返回主菜单，请按照操作提示")

def foll_Fans(driver):
    # 寻找某个主播的粉丝
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
    driver.tap([(800,1310)],100)
    time.sleep(2)
    num = input("请输入想要关注前几页的粉丝:")
    num = int(num)
    driver.swipe(600,656,600,410)
    for r in range(num):
        c=328
        n = 328
        for i in range(7):
            driver.tap([(900,n)],100)
            n = n + 228
            time.sleep(1)
        n = c
        driver.swipe(600,1810,600,210)
    driver.tap([(80,130)],100)
    time.sleep(2)
    driver.tap([(80,130)],100)
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
def P_letter(driver):
    # 输 入 要 私 信 的 主 播 完 整 名 字
    n_name = input("请先输入要私信的主播名字：")
    con = input("请输入要发送的私信内容：")
    driver.tap([(987,132)],100)
    time.sleep(3)
    driver.tap([(400,120)],100)
    time.sleep(2)
    driver.find_element_by_id('com.ss.android.ugc.aweme:id/a9d').send_keys(n_name)
    time.sleep(2)
    # 点击搜索
    driver.tap([(984,130)],100)
    time.sleep(5)
    # 进入主页
    try:
        driver.tap([(387,530)],100)
        time.sleep(4)
        # 点 击 发 送 私 信
        driver.tap([(840,470)],100)
        time.sleep(3)
        driver.tap([(300,1820)],100)
        driver.find_element_by_id('com.ss.android.ugc.aweme:id/bio').send_keys(con)
        time.sleep(2)
        # 点 击 发 送 按 钮
        driver.tap([(1000, 1010)], 100)
        # 连 点 三 次 回 到 主 页 面
        driver.tap([(80, 130)], 100)
        time.sleep(1)
        driver.tap([(80, 130)], 100)
        time.sleep(1)
        driver.tap([(80, 130)], 100)
    except:
        print("只能给已关注的主播发送私信,即将返回主菜单，请按操作提示进行操作")
while True:
    print("请 按 需 求 输 入 对 应 数 字")
    print('想 要 添 加 某 主 播 未 关 注 请 输 入 ： 1 ')
    print('搜 索 品 类 商 品 请 输 入 ： 2 ')
    print('下 载 主 播 视 频 ： 3  ')
    print('评 论 主 播 视 频 及 点 赞 请 输 入： 4 ')
    print('批 量 添 加 某 个 主 播 的 粉 丝 为 关 注 请 输 入  ： 5 ')
    print('添 加 某 个 主 播 的 关 注 对 选 哪 个 为 关 注 请 输 入 ： 6 ')
    print('私 信 主 播 请 输 入 ： 7')
    print('退 出 请 按 ： 0 ')

    l=input()
    try:
        l = int(l)
    except:
        print("非法指令  请输入数字")
    if l == 1:
        s_anchor(driver)
        print("已关注，如想继续关注其他请安指令操作")
        time.sleep(5)
    elif l == 2:
        s_target(driver)
        print('浏览的视频链接已保存，如想搜索其他商品，请按指令操作')
        time.sleep(5)
    elif l == 3:
        d_video(driver)
        print('主播视频链接已保存，如想下载其他主播视频，请按指令操作')
        time.sleep(5)
    elif l == 4:
        G_up(driver)
        print('如想继续评论其他主播视频，请按指令操作')
        time.sleep(5)
    elif l == 5:
        foll_Fans(driver)
        print('添加粉丝为关注已完成，请按指令操作')
        time.sleep(5)
    elif l == 6:
        foll_anchor(driver)
        print('添加主播关注对象为关注已完成，请按指令操作')
        time.sleep(5)
    elif l == 7:
        P_letter(driver)
        print('私信该主播已完成，请按指令操作')
        time.sleep(5)

    elif l == 0:
        driver.quit()
        break
    else:
        print("非法指令，不在服务范围内")

print("谢谢使用，下次见")




