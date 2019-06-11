# -*- encoding:utf-8 -*-
from selenium import webdriver
from coffee.config import DRIVER
from coffee.utils.abs import Singleton

@Singleton
class CoffeeWebdriver():
    driver=None
    def __init__(self):
        if self.driver==None:
            if DRIVER=='Chrome':
                self.driver=webdriver.Chrome()
            else:
                self.driver=webdriver.Firefox()

    def get_driver(self):
        return self.driver

driver=CoffeeWebdriver().get_driver()