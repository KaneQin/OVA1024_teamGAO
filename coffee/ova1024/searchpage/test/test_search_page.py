# -*- encoding:utf-8 -*-
import unittest
from coffee.ova1024.searchpage.serchpage import SearchPage,Page
import time
from coffee.drivers.webdriver import driver



class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.search_page = SearchPage()

    def test_search_page(self):
        self.driver=driver
        email = "kujipi@qq.com"
        password = "kjp19920630"
        self.search_page.search_page(email,password)
        time.sleep(5)
        self.search_page.open_and_check()
        key=self.driver.find_element_by_name("kw")
        key.send_keys(u"你")
        key2 = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div[2]/form/div/div/button")
        key2.click()
        page=Page()
        page.open_and_check()


if __name__ == '__main__':
    unittest.main()