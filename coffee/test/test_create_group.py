# -*-encoding:utf-8-*-
import unittest
from coffee.ova1024.gruoppage.group import CreateGroup
from coffee.ova1024.loginpage.login import login

class TestCreateGroup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.creategroup=CreateGroup()
        login.Sign_in("1690344964@qq.com","6149762364")
        cls.creategroup.label_group.click()
    def test_creat_group(self):
        self.creategroup.create("uasdwfsdfq","dsuj","dsasa")
        result=self.creategroup.open_and_check()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
