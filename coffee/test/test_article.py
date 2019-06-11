# encoding:utf-8

import unittest
from coffee.ova1024.articlepage.Article import Article
from coffee.ova1024.loginpage.login import login
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        login().Sign_in("615800841@qq.com","huxu0315")


    def test_something(self):

       ext=Article().Publish()

       #实际值
       art="http://47.92.220.226/bbs/index.php/article/index/page-2"


       self.assertEqual(art, ext)


if __name__ == '__main__':
    unittest.main()
