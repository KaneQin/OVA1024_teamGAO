# -*- encoding:utf-8 -*-
import unittest
from coffee.ova1024.userpage.userpage import UserPage
import time



class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user_page = UserPage()

    def test_user_page(self):
        email = "352093042@qq.com"
        password = "zsefbji3069"
        self.user_page.user_page(email,password)
        time.sleep(5)
        self.user_page.open_and_check()


if __name__ == '__main__':
    unittest.main()
