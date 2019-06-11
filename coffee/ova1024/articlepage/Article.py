# encoding:utf-8

from coffee.coffeepage import CoffeeDriver
from coffee.drivers.webdriver import driver
from coffee.utils.urls import ARTICLE_PAGE_URL
import time
class Article(CoffeeDriver):


  @classmethod
  def Publish(self):
      driver.get(ARTICLE_PAGE_URL)
      Page_2=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[11]/nav/ul/li[2]/a")
      Page_2.click()
      atv=driver.current_url
      return atv

      # Title=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/div/form/div[1]/div[2]/div/p")
      # Title.send_keys(self.value)
      # time.sleep(3)
      # huifu=driver.find_element_by_link_text("回复")
      # huifu.click()

      # outline = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/form/div[3]/textarea")
      # outline.send_keys(self.outlines)
      # time.sleep(3)
      # contents=driver.
      # contents.send_keys(self.conte)
      # time.sleep(3)
      #
      # Label=driver.find_element_by_name("tag")
      # Label.send_keys(self.labe)
      # time.sleep(3)
      # Articl=driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/form/button")
      # Articl.click()