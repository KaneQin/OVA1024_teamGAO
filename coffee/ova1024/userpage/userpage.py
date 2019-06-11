# -*- encoding:utf-8 -*-

from coffee.ova1024.loginpage import login
from  coffee.coffeepage import CoffeeDriver
from coffee.drivers.webdriver import driver

class UserPage(CoffeeDriver):


    exp_xpath = "/html/body/div[3]/div/div[2]/dl/dd/ul/li[1]/p/a"
    exp_key_word = u"武汉彭于晏"

    def user_page(self,email,password):

        login.login.Sign_in(email,password)

        user_xpath = "/html/body/div[1]/div/a[5]"
        user_page = driver.find_element_by_xpath(user_xpath)
        user_page.click()