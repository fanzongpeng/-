
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from commont.getpathg import GetPath
from commont.readini import ReadIni


class SeleniumDemoo:

    driver:WebDriver


    def __init__(self):
        self.action=ActionChains(self.driver)
        pass
    def findElement(self, by:str,locator):
        by=by.lower()
        if by=="id":
            return self.driver.find_element_by_id(locator)
        elif by=="xpath":
            return self.driver.find_element_by_xpath(locator)
        elif by=="css":
            return self.driver.find_element_by_css_selector(locator)
        elif by=="link":
            return self.driver.find_element_by_link_text(locator)

    def find(self,locator):
        self.wait(locator)
        return self.driver.find_element(*locator)
    def wait(self, locator):
        try:
            ##查看元素是否已经出现在页面的dom结构中，出现但不一定可见
            return WebDriverWait(self.driver, 10, 0.5).until(ec.presence_of_element_located(*locator))
        except:
            self.logger.debug("此元素还没有出现")
            return None
            # title_is：判断当前页面的title是否等于预期
            # title_contains：判断当前页面的title是否包含预期字符串
            # presence_of_element_located：判断某个元素是否被加到了dom树里，并不代表该元素一定可见
            # visibility_of_element_located：判断某个元素是否可见.可见代表元素非隐藏，并且元素的宽和高都不等于0
            # visibility_of：跟上面的方法做一样的事情，只是上面的方法要传入locator，这个方法直接传定位到的element就好了
            # presence_of_all_elements_located：判断是否至少有1个元素存在于dom树中。举个例子，如果页面上有n个元素的class都是
            # 'column-md-3'，那么只要有1个元素存在，这个方法就返回True
            # text_to_be_present_in_element：判断某个元素中的text是否
            # 包含
            # 了预期的字符串
            # text_to_be_present_in_element_value：判断某个元素中的value属性是否包含了预期的字符串
            # frame_to_be_available_and_switch_to_it：判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False
            # invisibility_of_element_located：判断某个元素中是否不存在于dom树或不可见
            # element_to_be_clickable - it is Displayed and Enabled：判断某个元素中是否可见并且是enable的，这样的话才叫clickable
            # staleness_of：等某个元素从dom树中移除，注意，这个方法也是返回True或False
            # element_to_be_selected：判断某个元素是否被选中了, 一般用在下拉列表
            # element_located_to_be_selected
            # element_selection_state_to_be：判断某个元素的选中状态是否符合预期
            # element_located_selection_state_to_be：跟上面的方法作用一样，只是上面的方法传入定位到的element，而这个方法传入locator
            # alert_is_present：判断页面上是否

    def doubleclick(self, element):
        ##双击鼠标左键
        self.action.double_click(element).perform()
        return self

    def contextclick(self, element):
        ##点击鼠标右键
        self.action.context_click(element).perform()
        return self

    def hodle(self, element):
        ##鼠标悬停
        self.action.click_and_hold(element).perform()
        return self

    def switchwindow(self,handle1):
        ##切换窗口
        handles = self.driver.window_handles
        for handle in handles:
            if handle1 !=handle:
                self.driver.switch_to.window(handle)
                break
    def swithalert(self):
        ##切换到弹窗
        WebDriverWait(self.driver,10,0.5).until(ec.alert_is_present)
        alert=self.driver.switch_to.alert
        return alert
    def swithframe(self,element):
        ##切换到frame
        self.driver.switch_to.frame(element)
        return self
    def select_text(self,element,text):
        ##下拉框选项select查询通过文本
        Select(element).select_by_visible_text(text)
    def select_index(self,element,indext):
        ##通过下标
        Select(element).select_by_index(indext)
    def select_value(self,element,value):
        ##通过下标值
        Select(element).select_by_value(value)


