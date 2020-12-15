import pytest
import yaml
from .pythoncode.calculator import *
import os

c = Calculator()
datas = yaml.safe_load(open("./datas.yml"))  # 执行效率角度，封装效率较低。采用全局变量


@pytest.mark.usefixtures("module_run")
class TestCal(object):
    # @classmethod
    # def setup_class(cls):
    #     print("开始测试\n")
    #
    # @classmethod
    # def teardown_class(cls):
    #     print("\n结束测试")

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a, b, expect", datas["add"], ids=datas["tag_name"])
    def test_add(self, a, b, expect):
        assert c.add(a, b) == expect

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a, b, expect", datas["sub"], ids=datas["tag_name"])
    def test_sub(self, a, b, expect):
        assert c.sub(a, b) == expect

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a, b, expect", datas["mul"], ids=datas["tag_name"])
    def test_mul(self, a, b, expect):
        assert c.mul(a, b) == expect

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a, b, expect", datas["div"], ids=datas["tag_name"])
    def test_div(self, a, b, expect):
        assert c.div(a, b) == expect
