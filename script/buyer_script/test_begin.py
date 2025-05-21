import pytest

from utils import DriverUtils


@pytest.mark.run(order=101)
class TestBegin:

    def test_begin(self):
        # 运行时,修改开关值为False
        DriverUtils.change_buyer_key(False)
