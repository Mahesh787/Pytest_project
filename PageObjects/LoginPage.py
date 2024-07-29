# Create a Login Page Details for NpoCommerce website
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    text_box_UserName_id = 'Email'
    text_box_Password_id = 'Password'
    button_login_xpath = "//button[@class='button-1 login-button']"
    link_logout_linktext = 'Logout'

    def __init__(self,driver):
        self.driver = driver


    def setUsername(self,Username):
        self.driver.find_element(By.ID,self.text_box_UserName_id).clear()
        self.driver.find_element(By.ID,self.text_box_UserName_id).send_keys(Username)

    def setPassword(self,Password):
        self.driver.find_element(By.ID,self.text_box_Password_id).clear()
        self.driver.find_element(By.ID,self.text_box_Password_id).send_keys(Password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.link_logout_linktext).click()
