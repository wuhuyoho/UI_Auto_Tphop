import pytest

from config import BASE_PATH
from page.admin_page.login_page import AdminLoginPage
from utils import DriverUtils, el_is_exist_by_text


# 1.定义测试类
@pytest.mark.run(order=2)
class TestLogin:

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
    def test_login(self):
        # 执行登录操作步骤
        AdminLoginPage().admin_login("admin", "123456", "8888")
        # 断言
        try:
            # 调用根据文本判断元素是否存在的函数
            assert el_is_exist_by_text(self.driver, False, "admin")
        except Exception as e:
            # 如断言失败,则截图结果界面
            self.driver.get_screenshot_as_file(BASE_PATH + "/img/test_login.png")
            raise e
