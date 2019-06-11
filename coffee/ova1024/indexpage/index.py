# -*- encoding:utf-8 -*-
import time
from coffee.drivers.webdriver import driver
from coffee.utils.urls import HOME_PAGE_URL
from coffee.coffeepage import CoffeeDriver
from coffee.ova1024.loginpage.login import login
from coffee.utils.tools import Tool

class IndexPage(CoffeeDriver):

    def __init__(self):
        self.driver = driver
        login().Sign_in("2507040987@qq.com","2507040987Gxl")
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div/a[1]')
        element.click()

    def talktalk(self):
        element = self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div[2]/div[2]/div/div[1]/form/textarea")
        return element

    def an(self):
        element = self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div[2]/div[2]/div/div[1]/form/input[2]")
        return element

    def send(self,talk):
        self.talktalk().send_keys(talk)
        self.an().click()