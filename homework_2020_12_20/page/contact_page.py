from time import sleep

from selenium.webdriver.common.by import By

from homework_2020_12_20.page.BasePage import BasePage


class ContactPage(BasePage):
    _location_tr_elements = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _location_goto_add_member = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    _location_goto_create_party = (By.CSS_SELECTOR, ".js_create_party")
    _location_create_dropdown = (By.CSS_SELECTOR, ".js_create_dropdown")
    _location_party_dropdown_arrow = (By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[3]/a/span[1]')
    _location_party_name = (By.XPATH, '//*[@name="name"]')
    _location_selector_party = (By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[3]/div/div/ul/li/a')
    _location_create_party_submit = (By.XPATH, '//*[@d_ck="submit"]')

    def add_member(self):
        """
        添加成员
        :return:
        """
        self.find(self._location_goto_add_member).click()
        from homework_2020_12_20.page.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)

    def add_department(self):
        """
        添加部门
        :return:
        """
        self.find(self._location_create_dropdown).click()
        sleep(1)
        self.find(self._location_goto_create_party).click()
        sleep(1)
        self.find(self._location_party_dropdown_arrow).click()
        self.find(self._location_party_name).send_keys("测试组")
        sleep(1)
        self.find(self._location_selector_party).click()
        self.find(self._location_create_party_submit).click()
        return ContactPage(self.driver)

    def get_member(self) -> list:
        """
        获取通讯录用户
        :return: 通讯录用户列表
        """
        eles = self.finds(self._location_tr_elements)
        member_list = [i.text for i in eles]
        return member_list
