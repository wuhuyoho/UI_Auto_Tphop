from selenium.webdriver.common.by import By

from base.base_page import BuyerBasePage


# 定义代表页面类
class IndexPage(BuyerBasePage):
    # 定义实例属性:管理本次用例在该页面操作元素定位信息
    def __init__(self):
        super().__init__()
        # 搜索输入框
        self.search_box = (By.ID, "q")
        # 搜索按钮
        self.search_btn = (By.CLASS_NAME, "ecsc-search-button")

    # 定义业务方法:组织测试用例在该页面所执行的操作步骤
    def query_goods(self, key_word):
        # 1、在首页输入搜索关键字
        self.input_text(self.find_el(self.search_box), key_word)
        # 2、点击【搜索】
        self.find_el(self.search_btn).click()
