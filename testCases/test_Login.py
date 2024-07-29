#Creating a test cases to validate Login page
import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from utilities.readProperities import Readconfig
from utilities.Screenshots import Screen
from utilities.logger import logggen

class Test_001_Login:
    Base_URl = Readconfig.getApplicationUrl()
    Username = Readconfig.getUsername()
    Password = Readconfig.getPassword()
    screen = Screen()
    log = logggen.logger()

    def test_homepage_title(self,setup):
        self.log.info("------------Test Case1------------ ")
        self.driver = setup
        self.driver.get(self.Base_URl)
        ac_title=self.driver.title
        if ac_title == "Your store. Login":
            assert True
            self.screen.Screenshots("Screenshots/Homepage_title_true.png",self.driver)
            self.driver.close()
            self.log.info("------------Succesfully logged in------------ ")
        else:
            self.screen.Screenshots("Screenshots/Homepage_title_false.png",self.driver)
            self.driver.close()
            self.log.error("------------Failed to logged in------------ ")
            assert False

    def test_loginpage(self,setup):
        self.log.info("------------Test Case2------------ ")
        self.driver = setup
        self.driver.get(self.Base_URl)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.Username)
        self.lp.setPassword(self.Password)
        self.lp.clickLogin()
        ac_title = self.driver.title

        if ac_title == "Dashboard / nopCommerce administration":
            assert True
            self.screen.Screenshots("Screenshots/loginpagetrue.png",self.driver)
            self.driver.close()
            self.log.info("------------Succesfully logged in------------ ")
        else:
            self.screen.Screenshots("Screenshots/loginpage.png",self.driver)
            self.driver.close()
            self.log.info("------------Failed  ------------ ")
            assert False











