import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, default_driver: WebDriver = None):
        if default_driver is None:
            self.driver = webdriver.Chrome()  # 初始化驱动
            self.driver.implicitly_wait(5)  # 隐式等待
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")  # 跳转至login登录界面
            self.__cookies_login()
        else:
            self.driver = default_driver

    def __cookies_login(self):
        # 读取cookies
        with open("../cookdes/data.yaml", "r", encoding="UTF-8")as f:
            cookies = yaml.safe_load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")  # 跳转至主页

    def teardown(self):
        self.driver.quit()

    def find(self, type_id: str or tuple, value: str = None):
        """
        寻找元素函数，传入tuple时，value为None
        :param type_id: 寻找方式
        :param value: 匹配词条
        :return:
        """
        if value is None:
            return self.driver.find_element(*type_id)
        return self.driver.find_element(by=type_id, value=value)

    def finds(self, type_id: str or tuple, value: str = None):
        """
        寻找元素函数集，传入tuple时，value为None
        :param type_id: 寻找方式
        :param value: 匹配词条
        :return:
        """
        if value is None:
            return self.driver.find_elements(*type_id)
        return self.driver.find_elements(by=type_id, value=value)

    def wait_click(self, locator):
        return WebDriverWait(self.driver, 9).until(expected_conditions.element_to_be_clickable(locator))

    def quit(self):
        """
        退出二次封装
        :return:
        """
        self.driver.quit()
