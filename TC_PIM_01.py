from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from Test_locators import locators
from Test_Data import data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import pytest


class Test_Search_Textbox:
     @pytest.fixture
     def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(data.Test_data().url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        
     def test_Login(self,booting_function):
      try:

           self.driver.implicitly_wait(10)
           self.driver.find_element(by=By.NAME, value=locators.Test_locators().username_locator).send_keys(data.Test_data().username)
           self.driver.find_element(by=By.NAME, value=locators.Test_locators().password_locator).send_keys(data.Test_data().password)
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().login_button).click()
           print("Login Sucessfull!")
           self.driver.implicitly_wait(5)
           Menu_items = ['ADMIN','PIM','LEAVE','TIME','RECRUITMENT','MY INFO','PERFORMANCE','DASHBOARD','DIRECTORY','MAINTENANCE','BUZZ']
           for item in Menu_items:
                self.driver.find_element(by=By.XPATH, value=locators.Test_locators().search_inputbox).send_keys(item)
                self.driver.refresh()
                self.driver.implicitly_wait(2)
                print("menu name {a} present and validated".format(a=item))
                self.driver.find_element(by=By.XPATH, value=locators.Test_locators().search_inputbox).send_keys(item.lower())
                self.driver.refresh()
                self.driver.implicitly_wait(2)
                print("menu name {b} present and Validated ".format(b=item.lower()))
                assert self.driver.title == 'OrangeHRM'
      except NoSuchElementException:
        print("login Unsucessful")
        self.driver.quit()
        
        

