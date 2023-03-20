from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from Test_locators import locators
from Test_Data import data
import pytest

class Test_Employee_list:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(data.Test_data().url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
    def test_Login(self,booting_function):
        try:
            self.driver.find_element(by=By.NAME, value=locators.Test_locators().username_locator).send_keys(data.Test_data().username)
            self.driver.find_element(by=By.NAME, value=locators.Test_locators().password_locator).send_keys(data.Test_data().password)
            self.driver.find_element(by=By.XPATH, value=locators.Test_locators().login_button).click()
            self.driver.implicitly_wait(4) 
            print("login Failed")
            self.driver.find_element(by=By.XPATH, value=locators.Test_locators().PIM_locator).click()
            self.driver.find_element(by=By.XPATH, value=locators.Test_locators().Add_employee).click()
            self.driver.implicitly_wait(5)
            self.driver.find_element(by=By.XPATH, value=locators.Test_locators().Name_inputbox).send_keys(data.Test_data().first_name)
            self.driver.find_element(by=By.XPATH, value=locators.Test_locators().lstname_inputbox).send_keys(data.Test_data().last_name)
            self.driver.find_element(by=By.XPATH, value=locators.Test_locators().save_button).click()
            Menu_items = ['Personal Details','Contact Details','Emergency Contact','Dependents','Immigration','Job','Salary','Tax Exemptions','Report-to','Qualifications','Memberships']
            for item in Menu_items:
             try:
                self.driver.find_element(by=By.XPATH, value=locators.Test_locators().personal_details).click()
                print("Mene option {a} present and Validated ".format(a=item))
             except:
                print('element {item} not found')
                assert self.driver.title == 'OrangeHRM'        
            
        except:
            print("missing fields")


