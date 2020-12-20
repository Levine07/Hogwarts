from time import sleep

from homework_2020_12_20.page.main_page import MainPage
import pytest


class TestAddMember(object):
    def setup(self) -> None:
        self.main = MainPage()

    def test_add_member_success(self) -> None:
        """
        测试行为：登录-通讯录-添加成员
        测试结果：成功
        :return:
        """
        res = self.main.goto_contact_page().add_member().add_member_success().get_member()
        assert "赫敏" in res

    def test_add_member_error(self) -> None:
        """
        测试行为：登录-通讯录-添加成员
        测试结果：失败
        :return:
        """
        res = self.main.goto_contact_page().add_member().add_member_error()
        assert '此手机号已被"赫敏"占有' in res

    def test_add_contact(self) -> None:
        """
        测试行为：登录-导入通讯录
        测试结果：成功
        :return:
        """
        self.main.goto_import_contact_page().import_contact()

    def test_register(self) -> None:
        """
        测试行为：登录-登出-注册用户
        测试结果：成功
        :return:
        """
        self.main.goto_login_page().goto_register_page().register_user()

    def test_add_party(self) -> None:
        """
        测试行为：登录-通讯录-添加部门
        测试结果：成功
        :return:
        """
        self.main.goto_contact_page().add_department()
