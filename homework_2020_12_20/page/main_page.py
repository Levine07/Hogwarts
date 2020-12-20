from selenium.webdriver.common.by import By

from homework_2020_12_20.page.BasePage import BasePage


class MainPage(BasePage):
    def goto_add_member_page(self):
        """
        跳转至添加成员界面
        :return: 添加成员界面
        """
        self.driver.find_element(By.CSS_SELECTOR, "a[node-type='addmember']").click()
        from homework_2020_12_20.page.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)

    def goto_contact_page(self):
        """
        跳转至通讯录界面
        :return:
        """
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        from homework_2020_12_20.page.contact_page import ContactPage
        return ContactPage(self.driver)

    def goto_import_contact_page(self):
        """
        跳转至导入通讯录界面
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, "a[node-type='import']").click()
        from homework_2020_12_20.page.import_contact_page import ImportContactPage
        return ImportContactPage(self.driver)

    def goto_login_page(self):
        """
        跳转至登录界面
        :return:
        """
        self.driver.find_element(By.ID, "logout").click()
        from homework_2020_12_20.page.login_page import LoginPage
        return LoginPage(self.driver)
