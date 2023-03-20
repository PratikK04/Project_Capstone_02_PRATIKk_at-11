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

class Test_Employee_Dependents_details:
   @pytest.fixture   
   def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(data.Test_data().url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

   def test_dependents_details(self,booting_function):
        try:
           self.wait.until(EC.element_to_be_clickable((By.NAME, locators.Test_locators().username_locator)))
           self.driver.find_element(by=By.NAME, value=locators.Test_locators().username_locator).send_keys(data.Test_data().username) 
           
           self.wait.until(EC.element_to_be_clickable((By.NAME, locators.Test_locators().password_locator)))
           self.driver.find_element(by=By.NAME, value=locators.Test_locators().password_locator).send_keys(data.Test_data().password)
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().login_button)))
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().login_button).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().PIM_locator)))
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().PIM_locator).click()

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().ep_namebox)))
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().ep_namebox).send_keys(data.Test_data().employeename)
           sleep(2)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().search_inputbox)))
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().search_inputbox).click()    
           sleep(2)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().edit_button)))
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().edit_button).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().Dependent)))
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().Dependent).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().Dependents_add)))
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().Dependents_add).click()  
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().Dependents_name)))
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().Dependents_name).send_keys(data.Test_data().Relation_name)
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().relationship_member)))
           relative = self.driver.find_element(by=By.XPATH, value=locators.Test_locators().relationship_member)
           relative.click()
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().drop_down)))
           dropdown3=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().drop_down).text
           print(dropdown3)
           if dropdown3.__contains__("Child"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Child'",relative)
                   
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().date_of_year)))
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().date_of_year).send_keys(data.Test_data().Relation_dob)
           sleep(3)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().ok_button)))
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().ok_button).click()     
           assert self.driver.title == "OrangeHRM"
           print("The user should be able to see all the filled details present in dependent details page")
        except NoSuchElementException:
            print("not defiend")   
        print("cannot update employee dependent details")