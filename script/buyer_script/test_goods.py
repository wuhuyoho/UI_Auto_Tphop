import allure
import pytest

import config
from config import BASE_PATH
from page.buyer_page.index_page import IndexPage
from utils import DriverUtils, el_is_exist_by_text


# 定义测试类
@pytest.mark.run(order=102)
class TestGoods:

    def setup_class(self):
        # 1.打开浏览器
        self.driver = DriverUtils.get_buyer_driver()
        self.driver.get("http://hmshop-test.itheima.net/")

    def teardown_class(self):
        # 5.关闭浏览器
        DriverUtils.quit_buyer_driver()

    # 定义测试方法
    def test_query_goods(self):
        # 2.在首页输入搜索关键字
        # 3.点击【搜索】
        IndexPage().query_goods(config.GOODS_NAME)
        # 4.断言
        try:
            # 调用根据文本判断元素是否存在的函数
            assert el_is_exist_by_text(self.driver, False, config.GOODS_NAME)
        except Exception as e:
            # 将错误截图插入到测试报告中
            allure.attach(self.driver.get_screenshot_as_png(),
                          BASE_PATH + "/img/query_goods.png", allure.attachment_type.PNG)
            raise e
