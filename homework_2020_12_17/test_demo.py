import json
from time import sleep

import pytest
import yaml
from selenium import webdriver


class TestWework(object):
    def setup(self):
        self.cookie = None

    @pytest.mark.run(order=1)
    def test_demo(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        driver.find_element_by_id("menu_contacts").click()
        self.cookie = driver.get_cookies()
        with open("page_object/data.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(self.cookie, f)
        with open("data.json", "w", encoding="UTF-8") as f:
            json.dump(self.cookie, f)

    @pytest.mark.run(order=2)
    def test_cookie(self):
        user_list = []
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        with open("page_object/data.yaml", "r", encoding="UTF-8") as f:
            cookies = yaml.safe_load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        driver.find_element_by_id("menu_contacts").click()
        driver.find_element_by_link_text("添加成员").click()
        driver.find_element_by_id("username").send_keys("测试用户2")
        driver.find_element_by_id("memberAdd_english_name").send_keys("testUser1")
        driver.find_element_by_id("memberAdd_acctid").send_keys("testUser1")
        driver.find_element_by_id("memberAdd_phone").send_keys("13533333333")
        driver.find_element_by_link_text("保存").click()

        sleep(2)
        driver.find_element_by_id("menu_contacts").click()
        table = driver.find_element_by_id("member_list")
        row = table.find_elements_by_tag_name("tr")
        for i in row:
            ele = i.find_elements_by_tag_name("td")
            user_list.append(ele[1].text)

        assert "测试用户2" in user_list
        sleep(3)
        driver.quit()
