from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.base_page import AdminBasePage


# 后台商品管理页面
class GoodPage(AdminBasePage):

    # 实例属性-管理操作步骤在该页面中所用到元素定位信息
    def __init__(self):
        super().__init__()
        # iframe标签
        self.frame = (By.ID, "workspace")
        # 添加商品的按钮
        self.add_goods_btn = (By.CSS_SELECTOR, "[title='添加商品']")
        # 商品名称输入框
        self.goods_name = (By.NAME, "goods_name")
        # 一级分类
        self.one_catgrey = (By.ID, "cat_id")
        # 二级分类
        self.two_catgrep = (By.ID, "cat_id_2")
        # 三级分类
        self.thr_catgrep = (By.ID, "cat_id_3")
        # 本店售价
        self.shop_price = (By.NAME, "shop_price")
        # 市场价
        self.market_price = (By.NAME, "market_price")
        # 是否包邮:是
        self.is_recive = (By.ID, "is_free_shipping_label_1")
        # 确认提交
        self.submit_btn = (By.ID, "submit")

    def add_goods(self, g_name, oc, tc, thc, s_price, m_price):
        """
        :param g_name:商品名称
        :param oc:一级分类
        :param tc:二级分类
        :param thc:三级分类
        :param s_price:本店售价
        :param m_price:市场价
        :return:
        """
        # frame切换
        self.switch_frame(self.find_el(self.frame))
        # 2、点击【添加商品】
        self.find_el(self.add_goods_btn).click()
        # 3、输入商品名称
        self.input_text(self.find_el(self.goods_name), g_name)
        # 4、选择商品分类
        Select(self.find_el(self.one_catgrey)).select_by_value(oc)
        Select(self.find_el(self.two_catgrep)).select_by_value(tc)
        Select(self.find_el(self.thr_catgrep)).select_by_value(thc)
        # 5、输入本店售价
        self.input_text(self.find_el(self.shop_price), s_price)
        # 6、输入市场价
        self.input_text(self.find_el(self.market_price), m_price)
        # 7、选择是否包邮
        self.find_el(self.is_recive).click()
        # 9、点击【确认提交】
        self.find_el(self.submit_btn).click()
