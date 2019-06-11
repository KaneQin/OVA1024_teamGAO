import unittest
from coffee.ova1024.userpage.userpage import UserPage



class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user_page = UserPage()

    def test_user_page(self):
        email = "352093042@qq.com"
        password = "zsefbji3069"
        self.user_page.user_page(email,password)
        self.user_page.open_and_check()


if __name__ == '__main__':
    unittest.main()
