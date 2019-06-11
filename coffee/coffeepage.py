# -*- encoding:utf-8 -*-
from coffee.drivers.webdriver import driver
from coffee.utils.tools import Tool
from coffee.utils.urls import LOGIN_PAGE_URL
class CoffeeDriver(Tool):

    def __init__(self):
        self.driver = driver
        self.Debug("coffeepage -> driver %s" % self.driver)
        self.driver.get(LOGIN_PAGE_URL)

    def open_and_check(self):
        self.Debug("coffeepage -> open_and_check %s" % self.url)
        return self.check_if_page_open()

    def check_if_page_open(self,xpath,keyword):
        self.Debug("coffeepage -> check_if_page_open 获取xpath： %s   比对keyword：%s" % (xpath,keyword.encode("utf-8")))
        label=self.driver.find_element_by_xpath(xpath)
        self.Debug("coffeepage -> find keywords %s" % label.text.encode("utf-8"))
        if label.text == keyword:
            return True
        else:
            self.Debug("'%s'!='%s'" % (label.text.encode('utf8'), keyword.encode('utf8')))
            return False