from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from Test_locators import locators
from Test_Data import data
import pytest


class Test_Admin_user_management:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(data.Test_data().url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        
    def test_adminpage(self,booting_function):
      try:     
           self.wait.until(EC.element_to_be_clickable((By.NAME, locators.Test_locators().username_locator)))
           self.driver.find_element(by=By.NAME, value=locators.Test_locators().username_locator).send_keys(data.Test_data().username)  
           self.wait.until(EC.element_to_be_clickable((By.NAME, locators.Test_locators().password_locator)))
           self.driver.find_element(by=By.NAME, value=locators.Test_locators().password_locator).send_keys(data.Test_data().password)
          
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().login_button)))
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().login_button).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().admin)))
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().admin).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().user_management)))
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().user_management).click() 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().user)))
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().user).click()  
           self.driver.execute_script("window.stop();");                  
           self.driver.find_element(by=By.XPATH, value =locators.Test_locators().userrole).click()
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().admin_select).click()
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().Enable).click()
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().ESS_select).click()
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().disable).click()
           self.driver.find_element(by=By.XPATH, value =locators.Test_locators().userrole).click()
           assert self.driver.title == 'OrangeHRM'
           print("The user should be able to see all dropdown visible")
      except NoSuchElementException:
              print('Some elements are missing !')
        