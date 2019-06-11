# -*- encoding:utf-8 -*-
import unittest
from coffee.ova1024.loginpage.login import login
from  coffee.coffeepage import CoffeeDriver

class TestUserUtils(unittest.TestCase):

    def test_userlogin(self):
        email = '1010528925@qq.com'
        pwd = '123456'
        login.Sign_in(email,pwd)

if __name__ == '__main__':
    unittest.main()

