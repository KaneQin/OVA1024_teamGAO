# -*- encoding:utf-8 -*-
from coffee.drivers.webdriver import driver
from coffee.utils.tools import Debug
from coffee.utils.urls import LOGIN_PAGE_URL
class CoffeeDriver():
    def __init__(self):
        self.driver = driver
        Debug("coffeepage -> driver %s" % self.driver)
        self.driver.get(LOGIN_PAGE_URL)

    def open_and_check(self):
        Debug("coffeepage -> open_and_check %s" % self.url)
        return self.check_if_page_open()

    def check_if_page_open(self,xpath,keyword):
        Debug("coffeepage -> check_if_page_open 获取xpath： %s   比对keyword：%s" % (xpath,keyword.encode("utf-8")))
        label=self.driver.find_element_by_xpath(xpath)
        Debug("coffeepage -> find keywords %s" % label.text.encode("utf-8"))
        if label.text == keyword:
            return True
        else:
            Debug("'%s'!='%s'" % (label.text.encode('utf8'), keyword.encode('utf8')))
            return False