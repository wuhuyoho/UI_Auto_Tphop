from selenium.webdriver.common.by import By
from base.base_page import AdminBasePage


# admin-登录页面
class AdminLoginPage(AdminBasePage):
    # 实例属性-管理操作步骤在该页面中所用到元素定位信息
    def __init__(self):
        super().__init__()
        # 用户名输入框
        self.username = (By.NAME, "username")
        # 密码输入框
        self.password = (By.NAME, "password")
        # 验证码输入框
        self.code = (By.ID, "vertify")
        # 登录按钮
        self.login_btn = (By.NAME, "submit")

    # 实例方法（业务操作层）-封装测试用例在该页面的操作步骤
    def admin_login(self, usr, pwd, cod):
        # 1、输入用户名
        self.input_text(el=self.find_el(self.username), key_text=usr)
        # 2、输入密码
        self.input_text(el=self.find_el(self.password), key_text=pwd)
        # 3、输入验证码
        self.input_text(el=self.find_el(self.code), key_text=cod)
        # 4、点击登陆按钮
        self.find_el(self.login_btn).click()
