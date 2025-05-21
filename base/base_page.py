import logging
from selenium.webdriver.support.wait import WebDriverWait
from utils import DriverUtils


class BuyerBasePage:

    def __init__(self):
        self.driver = DriverUtils.get_buyer_driver()

    # 公用元素定位方法
    # 调用该定位时,使用显示等待的方式定位元素
    # 记录代码执行定位的日志
    def find_el(self, location):
        try:
            # 显示等待定位元素
            el = WebDriverWait(self.driver, 10, 1). \
                until(lambda x: x.find_element(*location))
            logging.info(f"excute find_el {location} success!")
        except Exception as e:
            logging.error(f"excute find_el {location} failed!")
            el = None
        # 返回元素对象
        return el

    # 输入文本
    def input_text(self, el, key_text):
        """
        :param el: 元素对象
        :param key_text: 输入的文本
        :return:
        """
        try:
            # 模拟清除
            el.clear()
            logging.info(f"excute clear {el}'s text success!")
            # 模拟输入
            el.send_keys(key_text)
            logging.info(f"excute input {el}'s {key_text} success!")
        except Exception as e:
            logging.error(f"excute input {el}'s {key_text} failed!")

    # 窗口切换
    def switch_window(self, n):
        """
        :param n: 切换到第几个窗口,整型
        :return: None
        """
        try:
            # 获取句柄
            handles = self.driver.window_handles
            # 切换窗口
            self.driver.switch_to.window(handles[n])
            # 打印日志
            logging.info(f"switch to {n} window success!")
        except Exception as e:
            logging.error(f"switch to {n} window failed!")

    # frame切换
    def switch_frame(self, el):
        """
        :param el: <iframe>标签的元素对象
        :return: None
        """
        try:
            # 切换指定iframe标签
            self.driver.switch_to.frame(el)
            # 打印日志
            logging.info(f"switch to {el} iframe success!")
        except Exception as e:
            # 打印日志
            logging.info(f"switch to {el} iframe failed!")


class AdminBasePage:

    def __init__(self):
        self.driver = DriverUtils.get_admin_driver()

    # 公用元素定位方法
    # 调用该定位时,使用显示等待的方式定位元素
    # 记录代码执行定位的日志
    def find_el(self, location):
        try:
            # 显示等待定位元素
            el = WebDriverWait(self.driver, 10, 1). \
                until(lambda x: x.find_element(*location))
            logging.info(f"excute find_el {location} success!")
        except Exception as e:
            logging.error(f"excute find_el {location} failed!")
            el = None
        # 返回元素对象
        return el

    # 输入文本
    # 1.记录输入的日志
    # 2.清空输入框
    # 3.执行输入
    def input_text(self, el, key_text):
        """
        :param el: 元素对象
        :param key_text: 输入的文本
        :return:
        """
        try:
            # 模拟清除
            el.clear()
            logging.info(f"excute clear {el}'s text success!")
            # 模拟输入
            el.send_keys(key_text)
            logging.info(f"excute input {el}'s {key_text} success!")
        except Exception as e:
            logging.error(f"excute input {el}'s {key_text} failed!")

    # 窗口切换
    def switch_window(self, n):
        """
        :param n: 切换到第几个窗口,整型
        :return: None
        """
        try:
            # 获取句柄
            handles = self.driver.window_handles
            # 切换窗口
            self.driver.switch_to.window(handles[n])
            # 打印日志
            logging.info(f"switch to {n} window success!")
        except Exception as e:
            logging.error(f"switch to {n} window failed!")

    # frame切换
    def switch_frame(self, el):
        """
        :param el: <iframe>标签的元素对象
        :return: None
        """
        try:
            # 切换指定iframe标签
            self.driver.switch_to.frame(el)
            # 打印日志
            logging.info(f"switch to {el} iframe success!")
        except Exception as e:
            # 打印日志
            logging.info(f"switch to {el} iframe failed!")


class AppBasePage:

    def __init__(self):
        self.driver = DriverUtils.get_app_driver()

    # 公用元素定位方法
    # 调用该定位时,使用显示等待的方式定位元素
    # 记录代码执行定位的日志
    def find_el(self, location):
        try:
            # 显示等待定位元素
            el = WebDriverWait(self.driver, 10, 1). \
                until(lambda x: x.find_element(*location))
            logging.info(f"excute find_el {location} success!")
        except Exception as e:
            logging.error(f"excute find_el {location} failed!")
            el = None
        # 返回元素对象
        return el

    # 输入文本
    # 1.记录输入的日志
    # 2.清空输入框
    # 3.执行输入
    def input_text(self, el, key_text):
        """
        :param el: 元素对象
        :param key_text: 输入的文本
        :return:
        """
        try:
            # 模拟清除
            el.clear()
            logging.info(f"excute clear {el}'s text success!")
            # 模拟输入
            el.send_keys(key_text)
            logging.info(f"excute input {el}'s {key_text} success!")
        except Exception as e:
            logging.error(f"excute input {el}'s {key_text} failed!")

    # 窗口切换
    def switch_window(self, n):
        """
        :param n: 切换到第几个窗口,整型
        :return: None
        """
        try:
            # 获取句柄
            handles = self.driver.window_handles
            # 切换窗口
            self.driver.switch_to.window(handles[n])
            # 打印日志
            logging.info(f"switch to {n} window success!")
        except Exception as e:
            logging.error(f"switch to {n} window failed!")

    # frame切换
    def switch_frame(self, el):
        """
        :param el: <iframe>标签的元素对象
        :return: None
        """
        try:
            # 切换指定iframe标签
            self.driver.switch_to.frame(el)
            # 打印日志
            logging.info(f"switch to {el} iframe success!")
        except Exception as e:
            # 打印日志
            logging.info(f"switch to {el} iframe failed!")
