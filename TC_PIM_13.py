from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from Test_locators import locators
from Test_Data import data
import pytest


class Test_Tax_details:
 @pytest.fixture
 def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(data.Test_data().url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
 def test_tax_details (self,booting_function):
        try:
           self.wait.until(EC.element_to_be_clickable((By.NAME, locators.Test_locators().username_locator)))
           self.driver.find_element(by=By.NAME, value=locators.Test_locators().username_locator).send_keys(data.Test_data().username) 
           
           self.wait.until(EC.element_to_be_clickable((By.NAME, locators.Test_locators().password_locator)))
           self.driver.find_element(by=By.NAME, value=locators.Test_locators().password_locator).send_keys(data.Test_data().password)
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().login_button)))
           self .driver.find_element(by=By.XPATH, value=locators.Test_locators().login_button).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().PIM_locator).click()))

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().ep_namebox)))
           self .driver.find_element(by=By.XPATH, value=locators.Test_locators().ep_namebox).send_keys(data.Test_data().employeename)
           sleep(3)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().search_inputbox)))
           self .driver.find_element(by=By.XPATH, value=locators.Test_locators().search_inputbox).click()     
           sleep(2)           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().edit_button)))
           self .driver.find_element(by=By.XPATH, value=locators.Test_locators().edit_button).click() 
           
           self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, locators.Test_locators().Tax)))
           self .driver.find_element(by=By.LINK_TEXT, value=locators.Test_locators().Tax).click() 
           sleep(2)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().federal_status)))
           status=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().federal_status)
           status.click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().drop_down)))
           drop_downvalue14=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().drop_down).text
           print(drop_downvalue14)
           if drop_downvalue14.__contains__("Married"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Married'",status) 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().Exemptions)))
           self .driver.find_element(by=By.XPATH, value=locators.Test_locators().Exemptions).send_keys(data.Test_data().value_Exemptions)
                
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().state_2)))
           state=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().state_2)
           state.click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().drop_down)))
           drop_downvalue15=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().drop_down).text
           print(drop_downvalue15)
           if drop_downvalue15.__contains__("Indiana"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Indiana'",state)
                
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().status_data)))
           tax=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().status_data)
           tax.click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().drop_down)))
           drop_downvalue16=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().drop_down).text
           print(drop_downvalue16)
           if drop_downvalue16.__contains__("Single"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Single'",tax)
                
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().tax_Exemptions)))
           self .driver.find_element(by=By.XPATH, value=locators.Test_locators().tax_Exemptions).send_keys(data.Test_data().per_Exemptions)
                     
                
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().unemployee_state)))
           unemployee=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().unemployee_state)
           unemployee.click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().drop_down)))
           drop_downvalue17=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().drop_down).text
           print(drop_downvalue17)
           if drop_downvalue17.__contains__("American Samoa"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='American Samoa'",unemployee)
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().work_state)))
           work=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().work_state)
           work.click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().drop_down)))
           drop_downvalue18=self.driver.find_element(by=By.XPATH, value=locators.Test_locators().drop_down).text
           print(drop_downvalue18)
           if drop_downvalue18.__contains__("American Samoa"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='American Samoa'",work) 
                       
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Test_locators().complete)))
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().complete).click()           
           assert self.driver.title == 'OrangeHRM'        
           print("The user should be able to see all the filled details present in Tax Exemptions details page")
        except NoSuchElementException:
            print("not defiend")   


















































# class Employee_list_Page:
#     driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#     wait = WebDriverWait(driver, 10)
#     driver.maximize_window()
#     def __init__(self):
#         self.driver.get(data.Test_data().url)

#     def Login(self):
#         sleep(5)
#         self.driver.find_element(by=By.NAME, value=locators.Test_locators().username_locator).send_keys(data.Test_data().username)
#         self.driver.find_element(by=By.NAME, value=locators.Test_locators().password_locator).send_keys(data.Test_data().password)
#         self.driver.find_element(by=By.XPATH, value=locators.Test_locators().login_button).click()
#         self.driver.implicitly_wait(4) 
#         self.driver.find_element(by=By.XPATH, value=locators.Test_locators().PIM_locator).click()
#         self.driver.find_element(by=By.XPATH, value=locators.Test_locators().Add_employee).click()
#         self.driver.implicitly_wait(5)
#         self.driver.find_element(by=By.XPATH, value=locators.Test_locators().Name_inputbox).send_keys(data.Test_data().ep_name)
#         self.driver.find_element(by=By.XPATH, value=locators.Test_locators().lstname_inputbox).send_keys(data.Test_data().ep_lst_name)
#         self.driver.find_element(by=By.XPATH, value=locators.Test_locators().save_button).click()
#         self.driver.find_element(by=By.XPATH, value=locators.Test_locators().Contact_info).click()

# Employee_list_Page().Login()

#         # sleep(2)
#         # # self.driver.find_element(by=By.XPATH, value=locators.Test_locators().ep_mdnamebox).send_keys(data.Test_data().ep_md_name)
#         # self.driver.find_element(by=By.XPATH, value=locators.Test_locators().nick_name).send_keys(data.Test_data().Nk_name)
#         # self.driver.find_element(by=By.XPATH, value=locators.Test_locators().dr_lic_loc).send_keys(data.Test_data().licence_number)
#         # self.driver.find_element(by=By.XPATH, value=locators.Test_locators().expiry_date).send_keys(data.Test_data().date_lc)
#         # sleep(2)
#         # # select=Select(self.driver.find_element(by=By.XPATH, value=locators.Test_locators().nationality).click())
#         # # select.select_by_value('India')
#         # # select=Select(self.driver.find_element(by=By.XPATH, value=locators.Test_locators().marital_status).click())
#         # # select.select_by_value('Single')
#         # # sleep(2)
#         # self.driver.find_element(by=By.XPATH, value=locators.Test_locators().Miltery).send_keys(data.Test_data().Military_st)
#         # self.driver.find_element(by=By.XPATH, value=locators.Test_locators().save_btn1).click()
#         # select=Select(self.driver.find_element(by=By.XPATH, value=locators.Test_locators().Blood_group).click())
#         # # select.deselect_by_visible_text('A+')
#         # self.driver.find_element(by=By.XPATH, value=locators.Test_locators().save_btn2).click()
        
#         # sleep(2)






