from selenium.webdriver.common.by import By

from base.base_page import AdminBasePage


# 后台系统主页
class HomePage(AdminBasePage):

    # 实例属性-管理操作步骤在该页面中所用到元素定位信息
    def __init__(self):
        super().__init__()
        # 一级菜单:商城
        self.goods_shop_link = (By.XPATH, "//*[text()='商城']")
        # 二级菜单:商品列表
        self.goods_list = (By.CSS_SELECTOR, "[data-param='goodsList|Goods']")

    # 跳转商品管理页面
    def to_goods_page(self):
        # 点击一级菜单:商城
        self.find_el(self.goods_shop_link).click()
        # 点击二级菜单:商品列表
        self.find_el(self.goods_list).click()
