# -*- encoding:utf-8 -*-

from coffee.ova1024.loginpage import login
from  coffee.coffeepage import CoffeeDriver
from coffee.drivers.webdriver import driver

class SearchPage(CoffeeDriver):


    xpath = "/html/body/div[3]/div/div[2]/div/div/div[3]"
    keyword = u"标题模糊搜索"

    def search_page(self,email,password):

        login.login.Sign_in(email,password)

        search_xpath = "/html/body/div[1]/div/a[6]"
        search_page = driver.find_element_by_xpath(search_xpath)
        search_page.click()

class Page(CoffeeDriver):
    xpath='/html/body/div[3]/div/div/div[2]'
    keyword=u'获得约 2 条结果'