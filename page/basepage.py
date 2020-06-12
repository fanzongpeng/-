from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from commont.logger import Logger


class BasePage():
    def __init__(self, driver: WebDriver):

        self.driver = driver
        self.logger = Logger().logger()
    def openbrowser(self,url):
        self.driver.get(url)
    def quite(self):
        self.driver.quit()





