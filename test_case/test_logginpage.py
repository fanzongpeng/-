from page.loginpage import LoginPage


class TestLoginPage():
    def test_loggin(self, driver):
        LoginPage(driver).loggin("00000000", "0000")
