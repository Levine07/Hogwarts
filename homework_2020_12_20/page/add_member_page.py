from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from homework_2020_12_20.page.BasePage import BasePage


class AddMemberPage(BasePage):
    _location_username = (By.XPATH, "//*[@id='username']")
    _location_acctid = (By.XPATH, "//*[@id='memberAdd_acctid']")
    _location_phone_number = (By.XPATH, "//*[@id='memberAdd_phone']")
    _location_save = (By.CSS_SELECTOR, ".js_btn_save")
    _location_tips = (By.CSS_SELECTOR, ".ww_inputWithTips_tips")

    def add_member_success(self):
        """
        行为：添加用户
        结果：添加成功
        :return:
        """
        self.find(self._location_username).send_keys("赫敏")
        self.find(self._location_acctid).send_keys("020")
        self.find(self._location_phone_number).send_keys("13177778882")
        self.find(self._location_save).click()
        from homework_2020_12_20.page.contact_page import ContactPage
        return ContactPage(self.driver)

    def add_member_error(self) -> list:
        """
        行为：添加用户
        结果：添加失败
        :return: 失败信息列表
        """
        self.find(self._location_username).send_keys("赫敏1")
        self.find(self._location_acctid).send_keys("020")
        self.find(self._location_phone_number).send_keys("13177778882")
        self.find(self._location_save).click()
        errors = self.finds(self._location_tips)
        return [i.text for i in errors if i.text is not '']
