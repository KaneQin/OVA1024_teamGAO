# -*- encoding:utf-8 -*-
from coffee.drivers.webdriver import driver
from coffee.utils.tools import Tool
from coffee.utils.urls import LOGIN_PAGE_URL
class CoffeeDriver(Tool):


    xpath = None
    keyword = None

    def __init__(self):
        self.driver = driver
        self.Debug("coffeepage -> driver %s" % self.driver)
        self.driver.get(LOGIN_PAGE_URL)

    def open_and_check(self):

        return self.check_if_page_open()

    def check_if_page_open(self):

        label=self.driver.find_element_by_xpath(self.xpath)

        if label.text == self.keyword:
            return True
        else:

            return False