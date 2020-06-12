from selenium import webdriver


class TestDemo():
    def test1(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                                  desired_capabilities={'platform': 'ANY', 'browserName': 'chrome', 'version': '',
                                                        'javascriptEnabled': True})
        self.driver.implicitly_wait(5)
        self.driver.get('http://www.baidu.com')