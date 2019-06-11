# -*- encoding:utf-8 -*-
from coffee.coffeepage import CoffeeDriver
from coffee.ova1024.loginpage.login import login
from coffee.drivers.webdriver import driver

class CreateGroup(CoffeeDriver):
    def __init__(self):
        self.driver=driver
        login().Sign_in("1690344964@qq.com", "6149762364")
        element=self.driver.find_element_by_xpath("/html/body/div[1]/div/a[2]")
        element.click()

    def label_create_group(self):
        element=self.driver.find_element_by_xpath("/html/body/div[3]/nav/a")
        return element
    @property
    def groupname(self):
        element=self.driver.find_element_by_name("groupname")
        return element
    @property
    def groupdesc(self):
        element=self.driver.find_element_by_name("groupdesc")
        return element
    @property
    def photo(self):
        element=self.driver.find_element_by_name("photo")
        return element
    @property
    def grouptag(self):
        element=self.driver.find_element_by_name("tag")
        return element
    def label_creategroup(self):
        element=self.driver.find_element_by_xpath("//*[@type='submit']")
        return element
    def create(self,groupname,groupdesc,grouptag):
        self.label_create_group().click()
        self.Debug("向小组名称控件中输入名称：%s" % groupname)
        self.groupname.send_keys(groupname)
        self.Debug("向小组介绍控件中输入描述：%s" % groupdesc)
        self.groupdesc.send_keys(groupdesc)
        self.Debug("向小组标签控件中输入标签：%s" % grouptag)
        self.grouptag.send_keys(grouptag)
        self.label_creategroup().click()
