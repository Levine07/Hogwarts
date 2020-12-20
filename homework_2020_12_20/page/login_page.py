from selenium.webdriver.common.by import By

from homework_2020_12_20.page.BasePage import BasePage


class LoginPage(BasePage):
    _location_register = (By.CSS_SELECTOR, 'a[class="login_registerBar_link"]')

    def goto_register_page(self):
        """
        进入这册用户界面
        :return:
        """
        self.find(self._location_register).click()
        from homework_2020_12_20.page.register_page import RegisterPage
        return RegisterPage(self.driver)
