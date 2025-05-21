import time

import allure
import pytest

import config
from config import BASE_PATH
from page.buyer_page.goods_page import GoodsPage
from page.buyer_page.index_page import IndexPage
from utils import DriverUtils, get_el_text


# 定义测试类
@pytest.mark.run(order=103)
class TestGoods:

    def setup_class(self):
        # 1.打开浏览器
        self.driver = DriverUtils.get_buyer_driver()
        self.driver.get("http://hmshop-test.itheima.net/")

    def teardown_class(self):
        # 5.关闭浏览器
        DriverUtils.quit_buyer_driver()

    # 定义测试方法
    def test_add_cart(self):
        # 1.搜索商品
        IndexPage().query_goods(config.GOODS_NAME)
        # 2.点击商品标题进入详情页后再点击加入购物车
        GoodsPage().add_goods_cart()
        # 断言
        try:
            # 调用获取弹出框提示信息
            msg = get_el_text(self.driver, "//*[@class='conect-title']/span")
            assert "添加成功" in msg
        except Exception as e:
            # 将错误截图插入到测试报告中
            allure.attach(self.driver.get_screenshot_as_png(),
                          BASE_PATH + "/img/test_add_cart.png", allure.attachment_type.PNG)
            raise e
