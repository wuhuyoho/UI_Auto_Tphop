import time

from selenium.webdriver.common.by import By
import config
from base.base_page import BuyerBasePage


# 包含:搜索结果页+商品详情页
class GoodsPage(BuyerBasePage):

    def __init__(self):
        super().__init__()
        # 商品名称
        self.goods_name = (By.XPATH, "//*[contains(text(),'{}')]")
        # 加入购物车
        self.add_cart_btn = (By.ID, "join_cart")
        # iframe标签
        self.frame = (By.CSS_SELECTOR, "[id*='layui-layer-iframe']")

    # 加入购物车
    def add_goods_cart(self):
        # 点击商品名称
        # self.find_el(self.goods_name).click()
        time.sleep(2)
        self.driver.find_elements(self.goods_name[0], self.goods_name[1].format(config.GOODS_NAME))[1].click()
        # 点击加入购物车
        self.find_el(self.add_cart_btn).click()
        # frame切换。调用父类切换frame的方法
        self.switch_frame(self.find_el(self.frame))
