from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from Test_locators import locators
from Test_Data import data
import pytest

from time import sleep
class Test_Employee_emergancy_contact_info:
   @pytest.fixture   
   def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(data.Test_data().url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
   def test_emg_contact_info (self,booting_function):
       try:
        self.driver.find_element(by=By.NAME, value=locators.Test_locators().username_locator).send_keys(data.Test_data().username)
        self.driver.find_element(by=By.NAME, value=locators.Test_locators().password_locator).send_keys(data.Test_data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Test_locators().login_button).click()
        self.driver.find_element(by=By.XPATH, value=locators.Test_locators().PIM_locator).click()
        self.driver.find_element(by=By.XPATH, value=locators.Test_locators().Add_employee).click()
        self.driver.find_element(by=By.XPATH, value=locators.Test_locators().Name_inputbox).send_keys(data.Test_data().ep_name)
        self.driver.find_element(by=By.XPATH, value=locators.Test_locators().lstname_inputbox).send_keys(data.Test_data().ep_lst_name)
        self.driver.find_element(by=By.XPATH, value=locators.Test_locators().Contact_info).click()
        self.driver.find_element(by=By.XPATH, value=locators.Test_locators().street_name01).send_keys(data.Test_data().street_name1)
        self.driver.find_element(by=By.XPATH, value=locators.Test_locators().street_name02).send_keys(data.Test_data().street_name2)
        self.driver.find_element(by=By.XPATH, value=locators.Test_locators().city_loc).send_keys(data.Test_data().city)
        self.driver.find_element(by=By.XPATH, value=locators.Test_locators().state_loc).send_keys(data.Test_data().state)
        self.driver.find_element(by=By.XPATH, value=locators.Test_locators().post_code).send_keys(data.Test_data().code)
        self.driver.find_element(by=By.XPATH, value=locators.Test_locators().country_loc).send_keys(data.Test_data().country)
        self.driver.find_element(by=By.XPATH, value=locators.Test_locators().home).send_keys(data.Test_data().home_nm)
        self.driver.find_element(by=By.XPATH, value=locators.Test_locators().moblie).send_keys(data.Test_data().Mobile_nm)
        self.driver.find_element(by=By.XPATH, value=locators.Test_locators().work).send_keys(data.Test_data().work_nm)
        self.driver.find_element(by=By.XPATH, value=locators.Test_locators().work_mail).send_keys(data.Test_data().work_mail_d)
        self.driver.find_element(by=By.XPATH, value=locators.Test_locators().other_mail).send_keys(data.Test_data().other_mail_d)
        self.driver.find_element(by=By.XPATH, value=locators.Test_locators().save_button2).send_keys(data.Test_data().city)
        assert self.driver.title == 'OrangeHRM'
        print("Your detailes updated sucessfully! ")
        
       except:
        print("cannot update employee contact details")