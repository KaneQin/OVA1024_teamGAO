# -*- encoding:utf-8 -*-
import time
from coffee.drivers.webdriver import driver
# from coffee.utils.urls import HOME_PAGE_URL
from coffee.coffeepage import CoffeeDriver
from coffee.ova1024.loginpage.login import login
# from coffee.utils.tools import Tool

class IndexPage(CoffeeDriver):
    xpath = "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]"
    keyword = u"最新签到用户"

    def __init__(self):
        self.driver = driver
        login().Sign_in("2507040987@qq.com","2507040987Gxl")

    def index(self):
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div/a[1]')
        return element

    def talk_dingwei(self):
        element = self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div[2]/div[2]/div/div[1]/form/textarea")
        return element

    def talk_an_dingwei(self):
        element = self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div[2]/div[2]/div/div[1]/form/input[2]")
        return element

    def talk_send(self,talk):
        self.talk_dingwei().send_keys(talk)
        self.talk_an_dingwei().click()

    def tiaozhuan_group_dingwei(self):
        element = self.driver.find_element_by_xpath("/html/body/div[1]/div/a[2]")
        return element
    def tiaozhuan_group(self):
        self.index().click()
        self.tiaozhuan_group_dingwei().click()