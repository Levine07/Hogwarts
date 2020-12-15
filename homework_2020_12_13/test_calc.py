import pytest
from homework_2020_12_09.pythoncode import calculator

c = calculator.Calculator()


class TestCal(object):
    @classmethod
    def setup_class(cls):
        print("开始测试\n")

    @classmethod
    def teardown_class(cls):
        print("\n结束测试")

    @pytest.mark.parametrize("a, b, expect", [
        (3, 5, 8), (-1, -2, -3), (100, 300, 400), (3.2, 3.3, 6.5)], ids=["int", "minus", "large number", "point"])
    def test_add(self, a, b, expect):
        assert c.add(a, b) == expect

    @pytest.mark.parametrize("a, b, expect", [
        (8, 5, 3), (-3, -2, -1), (400, 300, 100), (3.3, 3.2, 0.1)], ids=["int", "minus", "large number", "point"])
    def test_sub(self, a, b, expect):
        assert c.sub(a, b) == expect

    @pytest.mark.parametrize("a, b, expect", [
        (3, 5, 15), (-3, -2, 6), (100, 300, 30000), (3, 3.2, 9.6)], ids=["int", "minus", "large number", "point"])
    def test_mul(self, a, b, expect):
        assert c.mul(a, b) == expect

    @pytest.mark.parametrize("a, b, expect", [
        (15, 5, 3), (6, -2, -3), (100, 4, 25), (9.6, 3, 3.2)], ids=["int", "minus", "large number", "point"])
    def test_div(self, a, b, expect):
        assert c.div(a, b) == expect
