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

class Test_Salary_component:
 @pytest.fixture
 def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(data.Test_data().url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        
 def test_salary_details (self,booting_function):
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
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().ep_namebox)))
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().ep_namebox).send_keys(data.Test_data().ep_name)                
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().userrole)))
           userrole1=self .driver.find_element(by=By.XPATH, value=locators.Test_locators().userrole)
           userrole1.click()
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().drop_down)))
           drop_downvalue19=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().drop_down).text
           if drop_downvalue19.__contains__("Admin"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Admin'",userrole1)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().status)))
           status1=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().status)
           status1.click()
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().drop_down1)))
           drop_downvalue20=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().drop_down1).text
           if drop_downvalue20.__contains__("Enabled"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Enabled'",status1)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().admin)))
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().admin).click()
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().user_management)))
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().user_management).click() 
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().user)))
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().user).click()   
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().ep_namebox)))
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().ep_namebox).send_keys(data.Test_data().ep_name)                
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().userrole)))
           userrole2=self .driver.find_element(by=By.XPATH, value=locators.Test_locators().userrole)
           userrole2.click()
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().drop_down)))
           drop_downvalue21=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().drop_down).text
           if drop_downvalue21.__contains__("ESS"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='ESS'",userrole2)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().status_3)))
           status2=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().status_3)
           status2.click()
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().drop_down1)))
           drop_downvalue22=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().drop_down1).text
           if drop_downvalue22.__contains__("Disabled"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Disabled'",status2)
           assert self.driver.title == 'OrangeHRM'
           print("The user should be able to see all dropdown visible")
        except NoSuchElementException:
              print('Some elements are missing !')
              

