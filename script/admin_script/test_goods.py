import time

import allure
import pytest

import config
from config import BASE_PATH
from page.admin_page.goods_page import GoodPage
from page.admin_page.home_page import HomePage
from page.admin_page.login_page import AdminLoginPage
from utils import DriverUtils, el_is_exist_by_text


# 1.定义测试类
@pytest.mark.run(order=3)
class TestAddGoods:

    # 类级别的初始化方法
    def setup_class(self):
        # 打开浏览器
        self.driver = DriverUtils.get_admin_driver()
        # 打开测试网址
        self.driver.get("http://hmshop-test.itheima.net/admin")

    # 类级别的销毁的方法
    def teardown_class(self):
        # 关闭浏览器
        DriverUtils.quit_admin_driver()

    # 2.定义测试方法
    def test_add_goods(self):
        # 执行登录操作步骤
        # AdminLoginPage().admin_login("admin", "123456", "8888")
        # 执行跳转新增商品页面
        HomePage().to_goods_page()
        # 商品名称
        config.GOODS_NAME = f"goods_{time.strftime('%Y%m%d%H%M%S')}"
        # 执行新增商品
        GoodPage().add_goods(config.GOODS_NAME, "5", "39", "320", "210", "220")
        # 断言
        try:
            # 调用根据文本判断元素是否存在的函数
            assert el_is_exist_by_text(self.driver, False, config.GOODS_NAME)
        except Exception as e:
            # 如断言失败,则截图结果界面
            # self.driver.get_screenshot_as_file(BASE_PATH + "/img/test_add_goods.png")
            # 将错误截图插入到测试报告中
            allure.attach(self.driver.get_screenshot_as_png(),
                          BASE_PATH + "/img/test_add_goods.png", allure.attachment_type.PNG)
            raise e
