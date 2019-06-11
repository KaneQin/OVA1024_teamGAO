# -*- encoding:utf-8 -*-
from coffee.drivers.webdriver import driver
from coffee.utils.tools import Debug
class CoffeeDriver():
    def __init__(self):
        self.driver = driver
        Debug("coffeepage -> driver %s" % self.driver)