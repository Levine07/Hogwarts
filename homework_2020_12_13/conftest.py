import pytest


@pytest.fixture(scope="module")
def module_run():
    print("开始测试\n")
    yield
    print("\n结束测试")


def pytest_collection_modifyitems(session, config, items) -> None:
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")
