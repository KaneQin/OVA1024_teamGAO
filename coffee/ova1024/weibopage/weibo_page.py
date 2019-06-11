# -*- encoding:utf-8 -*-
from coffee.drivers.webdriver import driver
from coffee.utils.urls import TO_NAG_PAGE_URL

class TonagPage():

    def __init__(self):
        self.driver = driver

    @property
    def page_flag(self):
        element = self.driver.find_element_by_xpath("/html/body/div[1]/div/a[4]")
        return element

    def open_and_check(self):
        self.driver.get(TO_NAG_PAGE_URL)

        if self.page_flag.text=="唠叨":
            return True
        else:
            return False

