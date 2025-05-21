import pytest

from utils import DriverUtils


@pytest.mark.run(order=199)
class TestEnd:

    def test_end(self):
        # 运行时,修改开关值为True
        DriverUtils.change_buyer_key(True)
        # 主动关闭浏览器
        DriverUtils.quit_buyer_driver()
