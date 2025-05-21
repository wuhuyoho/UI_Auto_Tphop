import time

import allure

from config import BASE_PATH
from page.app_page.app_index_page import AppIndexPage
from utils import DriverUtils, get_el_text


# 定义测试类
class TestQueryNews:

    def setup_class(self):
        # 1.打开浏览器
        self.driver = DriverUtils.get_app_driver()

    def teardown_class(self):
        # 5.关闭浏览器
        DriverUtils.quit_app_driver()

    # 定义测试方法
    def test_query_news(self):
        # 调用app首页根据频道搜索文章的方法
        AppIndexPage().select_channecl("足球")
        # 断言
        try:
            # 调用获取弹出框提示信息
            msg = get_el_text(self.driver, "//*[@id='com.tencent.news:id/title_text']")
            assert msg
        except Exception as e:
            # 将错误截图插入到测试报告中
            allure.attach(self.driver.get_screenshot_as_png(),
                          BASE_PATH + "/img/test_query_news.png", allure.attachment_type.PNG)
            raise e

