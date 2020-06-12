import pymysql
import pytest
from selenium import webdriver

# @pytest.fixture(scope='session', autouse=True)
# def sql():
#     ##连接数据库
#     connect = pymysql.connect(host="10.7.129.247",
#                                    user="mysql",
#                                    password="YGBXygbx123!",
#                                    database="ipsdb_dev")
#     yield connect
#     connect.close()
from commont.getdata import GetData
from commont.getpathg import GetPath


@pytest.fixture(scope="session")
def driver():
    filepath = GetPath().filepath("data", "hub.yaml")
    data = GetData().yaml_data(filepath, "hub")
    host = data["host"]
    browsername = data["brows"][0]
    driver = webdriver.Remote(command_executor=host + '/wd/hub',
                              desired_capabilities={'platform': 'ANY', 'browserName': browsername, 'version': '',
                                                    'javascriptEnabled': True})
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()
