from coffee.drivers.webdriver import driver
import time
from coffee.utils.urls import LOGIN_PAGE_URL
class login():

    @classmethod
    def Sign_in(cls,email,password):
        __driver = driver
        __driver.get(LOGIN_PAGE_URL)
        user= __driver.find_element_by_name("email")
        user.send_keys(email)
        passwords=__driver.find_element_by_name("pwd")
        passwords.send_keys(password)
        denglv=__driver.find_element_by_id("comm-submit")
        denglv.click()
        time.sleep(1)



