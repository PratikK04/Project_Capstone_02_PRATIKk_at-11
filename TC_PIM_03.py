from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from Test_locators import locators
from Test_Data import data
import pytest

class Test_Creation_of_new_user:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(data.Test_data().url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_Login(self,booting_function):
        try:
           self.driver.implicitly_wait(5)
           self.driver.find_element(by=By.NAME, value=locators.Test_locators().username_locator).send_keys(data.Test_data().username)
           self.driver.find_element(by=By.NAME, value=locators.Test_locators().password_locator).send_keys(data.Test_data().password)
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().login_button).click()
           print("Login Sucessfull!")
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().PIM_locator).click()#pim selector
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().Add_employee).click()#new employee
           self.driver.find_element(by=By.XPATH,value=locators.Test_locators().ep_namebox).send_keys(data.Test_data().ep_name)#add employee data
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().ep_mdnamebox).send_keys(data.Test_data().ep_md_name)
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().ep_lstnamebox).send_keys(data.Test_data().ep_lst_name)
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().toggle_creat).is_selected()#toggle selector
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().toggle_creat).click()#enabled
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().new_user).send_keys(data.Test_data().user_new)
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().key_word).send_keys(data.Test_data().passkey)
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().cnf_password).send_keys(data.Test_data().passkey)
           self.driver.find_element(by=By.XPATH, value=locators.Test_locators().cof_button).click()
           print("new user created")
           assert self.driver.title == 'OrangeHRM'
           self.driver.close()
        except NoSuchElementException:
         print('Unable to creat new user!')
        
         