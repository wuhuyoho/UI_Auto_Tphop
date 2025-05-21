import logging

from selenium.webdriver.common.by import By

from base.base_page import AppBasePage


# 定义页面对象
class AppIndexPage(AppBasePage):
    # 定义实例属性:所操作的元素的定位信息
    def __init__(self):
        super().__init__()
        # 频道区域
        self.area_el = (By.ID, "com.tencent.news:id/rl_list_container")
        # 频道
        self.chl_name = (By.XPATH, "//*[contains(@text,'{}')]")

    # 定义业务方法:
    def select_channecl(self, ch_name):
        # 获取区域元素位置
        lt = self.find_el(self.area_el).location  # {x: ,y:}
        # 获取区域元素大小
        sz = self.find_el(self.area_el).size  # {width: , height:}
        # 按住的起始坐标
        s_x = lt["x"] + sz["width"] * 0.8
        # 按住的结束坐标
        s_y = lt["y"] + sz["height"] * 0.5
        # 结束的横坐标
        e_x = lt["x"] + sz["width"] * 0.2
        # 结束的纵坐标
        e_y = s_y

        # 循环
        while True:
            # 尝试在打开的页面上找指定频道
            try:
                # 如果能找到则直接点击
                self.driver.find_element(self.chl_name[0], self.chl_name[1].format(ch_name)).click()
                # 跳出循环
                break
            # 如找不到
            except Exception as e:
                # 滑动之前获取当前页面的所有元素
                old_page = self.driver.page_source
                # 则滑动一次屏幕
                self.driver.swipe(start_x=s_x, start_y=s_y, end_x=e_x, end_y=e_y, duration=3000)
                # 滑动之后获取当前页面的所有元素
                new_page = self.driver.page_source

            # 如滑动之前和滑动之后页面元素一模一样,则代表滑动到最底部，不再循环,打印找不到指定的频道
            if old_page == new_page:
                logging.error(f"页面已经滑动到最后,但是没有找到{ch_name}的频道")
                break
