import allure
from selenium.webdriver import ActionChains

from page.basepage import BasePage
from page.mainpage import MainPage

@allure.feature("登录页面封装方法")
class LoginPage(BasePage):
    @allure.story("登录")
    def loggin(self, uid, pwd):

        with allure.step("输入账号"):
            self.driver.find_element_by_id("uid").send_keys(uid)
        with allure.step("输入密码"):
             self.driver.find_element_by_id("pwd").send_keys(pwd)
        with allure.step("双击机构代码"):
            self.comcode = self.driver.find_element_by_id("comcode")
            ActionChains(self.driver).double_click(self.comcode).perform()##执行链中的所有操作
        with allure.step("点击登录"):
            self.driver.find_element_by_id("btn").click()
        return MainPage(self.driver)
