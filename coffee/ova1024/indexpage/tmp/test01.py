# -*- encoding:utf-8 -*-
import unittest
from coffee.ova1024.indexpage.index import IndexPage

class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index_page = IndexPage()

    def test_index_talk(self):
        self.index_page.talk_send(11223)

    # def test_index_tiaozhuang_group(self):
    #     self.index_page.tiaozhuan_group()



if __name__ == '__main__':
    unittest.main()
