from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from Test_locators import locators
from Test_Data import data
from time import sleep
import pytest

class Test_Employee_Job_details:
   @pytest.fixture   
   def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(data.Test_data().url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
  
   def test_job_detail(self,booting_function):
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
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().ep_namebox).send_keys(data.Test_data().ep_name)
           sleep(2)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().search_inputbox)))
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().search_inputbox).click()    
           sleep(2)
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().job)))
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().job).click()
           sleep(2)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().joined)))
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators()).send_keys(data.Test_data().start_date) 
           sleep(2)
                
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().job_title)))
           job_name=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().job_title)
           job_name.click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().drop_down)))
           dropdown_value4=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().drop_down).text
           if dropdown_value4.__contains__("Software Engineer"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Software Engineer'",job_name)

           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().job_category)))
           job_role=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().job_category)
           job_role.click()
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().drop_down)))
           dropdown_value5=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().drop_down).text
           if dropdown_value5.__contains__("Technicians"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Technicians'",job_role)
                   
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().sub_unit)))
           sub_name=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().sub_unit)
           sub_name.click()
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().drop_down)))
           dropdown_value6=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().drop_down).text
           if dropdown_value6.__contains__("Engineering"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Engineering'",sub_name)    
               
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().location)))
           area=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().location)
           area.click()
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().drop_down)))
           dropdown_value7=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().drop_down).text
           if dropdown_value7.__contains__("New York Sales Office"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='New York Sales Office'",area)    
               
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().employee_status)))
           employee_position=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().employee_status)
           employee_position.click()
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().drop_down)))
           dropdown_value8=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().drop_down).text
           if dropdown_value8.__contains__("Full-Time Contract"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Full-Time Contract'",employee_position)  
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().Yes_button)))
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().Yes_button).click()
           assert self.driver.title == 'OrangeHRM'
           print("The user should be able to see all the filled details present in job details page")
         except NoSuchElementException:  
            print('no')  
     
