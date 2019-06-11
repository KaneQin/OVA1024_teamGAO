# -*- encoding:utf-8 -*-

from coffee.ova1024.loginpage import login
from  coffee.coffeepage import CoffeeDriver

class UserPage(CoffeeDriver):

    coffeepage = CoffeeDriver()

    def login(self,email,password):

        email = "352093042@qq.com"
        password = "zsefbji3069"

        login(email,password)
