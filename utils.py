import json
import logging
import os

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import selenium.webdriver
import appium.webdriver


# 驱动工具类
from config import BASE_PATH


class DriverUtils:
    # 门户网站驱动对象存储的私有属性
    __buyer_driver = None
    # 后台管理系统网站驱动对象存储的私有属性
    __admin_driver = None
    # APP驱动对象存储的私有属性
    __app_driver = None

    # 获取门户网站的驱动对象
    @classmethod
    def get_buyer_driver(cls):
        if cls.__buyer_driver is None:
            cls.__buyer_driver = selenium.webdriver.Chrome()
            cls.__buyer_driver.maximize_window()
            cls.__buyer_driver.implicitly_wait(30)
        return cls.__buyer_driver

    # 关闭门户浏览器驱动对象的开关
    __buyer_key = True

    # 修改关闭驱动对象开关值的方法
    @classmethod
    def change_buyer_key(cls, key):
        cls.__buyer_key = key

    # 关闭门户网站的驱动对象
    @classmethod
    def quit_buyer_driver(cls):
        if cls.__buyer_driver is not None and cls.__buyer_key:
            cls.__buyer_driver.quit()
            cls.__buyer_driver = None

    # 获取后台网站的驱动对象
    @classmethod
    def get_admin_driver(cls):
        if cls.__admin_driver is None:
            cls.__admin_driver = selenium.webdriver.Chrome()
            cls.__admin_driver.maximize_window()
            cls.__admin_driver.implicitly_wait(30)
        return cls.__admin_driver

    # 关闭浏览器驱动对象的开关
    __admin_key = True

    # 修改关闭驱动对象开关值的方法
    @classmethod
    def change_admin_key(cls,key):
        cls.__admin_key = key

    # 关闭后台网站的驱动对象
    @classmethod
    def quit_admin_driver(cls):
        if cls.__admin_driver is not None and cls.__admin_key:
            cls.__admin_driver.quit()
            cls.__admin_driver = None

    # 获取APP网站的驱动对象
    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            # ② 配置启动参数
            desied_caps = {}
            desied_caps["platformName"] = "Android"  # IOS
            desied_caps["platformVersion"] = "6"
            desied_caps["deviceName"] = "adassd"  # 可以随便写但是不能不写
            desied_caps["appPackage"] = "com.tencent.news"  # 包名
            desied_caps["appActivity"] = "com.tencent.news.activity.SplashActivity"  # 界面名
            desied_caps["unicodeKeyboard"] = True  # 使用自带输入法，输入中文时填True
            desied_caps["resetKeyboard"] = True  # 执行完程序恢复原来输入法
            desied_caps["noReset"] = True
            # ③ 创建APP驱动对象
            cls.__app_driver = appium.webdriver.Remote('http://127.0.0.1:4723/wd/hub', desied_caps)
            cls.__app_driver.implicitly_wait(30)
        return cls.__app_driver

    # 关闭APP网站的驱动对象
    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver is not None:
            cls.__app_driver.quit()
            cls.__app_driver = None


# 读取json数据的公用函数
def build_data(file_name):
    # 文件路径
    filepath = BASE_PATH + f"/data/{file_name}.json"
    # 最终测试数据容器
    case_data = []
    # 打开数据文件
    with open(file=filepath, encoding="utf8") as f:
        # 读取数据并转换成python字典
        all_data = json.load(f)
    # 遍历字典数据
    for i in all_data.values():
        # 获取每次遍历的数据键值,需要强转成列表,并且存储到一个最终数据的容器中
        case_data.append(list(i.values()))
    # 返回测试数据
    return case_data


# 函数:公用的获取任意元素文本
def get_el_text(driver, xpath_str):
    # 获取元素文本
    # msg = DriverUtils.get_driver().find_element(By.XPATH, xpath_str).text
    try:
        msg = WebDriverWait(driver, 10, 1). \
            until(lambda x: x.find_element(By.XPATH, xpath_str)).text
        print(msg)
    except Exception as e:
        logging.error(f"没有获取到{xpath_str}的元素对象文本!")
        msg = None
    # 返回获取的文本
    return msg


# 函数:根据文本判断当前页面是否有对应的元素对象
def el_is_exist_by_text(driver, is_app, key_text):
    """
    :param driver: 驱动对象
    :param is_app: 是否是app的标识
    :param key_text: 关键字文本
    :return:
    """
    if is_app:
        xpath_str = f"//*[@text='{key_text}']"
    else:
        xpath_str = f"//*[text()='{key_text}']"
    # 根据本次新增的联系人信息的文本,到界面上找元素，如能找到则代表新增成功找不到则失败截图
    try:
        # 如找到元素对象则把元素对象赋值给is_suc
        is_suc = WebDriverWait(driver, 10, 1). \
            until(lambda x: x.find_element(By.XPATH, xpath_str))
    except Exception as e:
        # 找不到则给is_suc赋值为False
        is_suc = False
        # 截图
        # driver.get_screenshot_as_file(f"{key_text}未找到.png")
        logging.error(f"未找到文本为{key_text}的元素对象!")
    # 返回是否找到结果
    return is_suc
