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
from time import sleep

class Test_Activate_employee:
   @pytest.fixture   
   def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(data.Test_data().url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
   def test_activate_employee(self,booting_function):
       try:
        self.driver.find_element(by=By.NAME, value=locators.Test_locators().username_locator).send_keys(data.Test_data().username)
        self.driver.find_element(by=By.NAME, value=locators.Test_locators().password_locator).send_keys(data.Test_data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Test_locators().login_button).click()
        self.driver.find_element(by=By.XPATH, value=locators.Test_locators().PIM_locator).click() 
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().ep_namebox)))
        self .driver.find_element(by=By.XPATH, value=locators.Test_locators().ep_namebox).send_keys(data.Test_data().ep_name)
        sleep(3)
        self.driver.find_element(by=By.XPATH, value=locators.Test_locators().search_button).click()     
        sleep(2)           
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().edit_button)))
        self.driver.find_element(by=By.XPATH, value=locators.Test_locators().edit_button).click()  
        sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().job)))
        self.driver.find_element(by=By.XPATH, value=locators.Test_locators().job).click()       
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().activate)))  
        assert self.driver.title == 'OrangeHRM'
        print("The user should be able to see activation on job  Details page")
       except NoSuchElementException:  
            print('no') 
        