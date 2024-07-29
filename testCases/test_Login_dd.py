#Creating a test cases to validate Login page
import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from utilities.readProperities import Readconfig
from utilities.Screenshots import Screen
from utilities.logger import logggen
from utilities import Excelutilities

class Test_002_dd_Login:
    Base_URl = Readconfig.getApplicationUrl()
    path = "TestData/Testdata1.xlsx"
    screen = Screen()
    log = logggen.logger()

    def test_loginpage(self,setup):
        self.log.info("-----------Test_002_dd_login---------")
        self.log.info("------------Test Case2------------ ")
        self.driver = setup
        self.driver.get(self.Base_URl)
        self.lp = LoginPage(self.driver)


        self.rows = Excelutilities.getRowCount(self.path,'Sheet1')
        self.log.info(f"the no.of rows in sheet {self.rows}")

        self.columns = Excelutilities.getColumnCount(self.path,'Sheet1')
        self.log.info(f"the no.of rows in sheet {self.columns}")

        results = []

        for i in range(2,self.rows+1):
            for j in range(1,self.columns):
                self.user = Excelutilities.readData(self.path,'Sheet1',i,j)
                self.password = Excelutilities.readData(self.path,'Sheet1',i,j)
                self.exp = Excelutilities.readData(self.path, 'Sheet1', i, j)
                self.lp.setUsername(self.user)
                self.lp.setPassword(self.password)
                self.lp.clickLogin()
                ac_title = self.driver.title
                exp_value = "Dashboard / nopCommerce administration"

                if ac_title == exp_value:
                    if self.exp == "Pass":
                        self.screen.Screenshots("Screenshots/loginpagetrue.png",self.driver)
                        self.lp.clickLogout()
                        results.append("pass")
                        self.log.info("------------Succesfully logged in------------ ")
                    elif self.exp == "Fail":
                        self.screen.Screenshots("Screenshots/loginpageFalse.png", self.driver)
                        self.lp.clickLogout()
                        results.append("Fail")
                        self.log.info("------------Failed------------ ")

                elif ac_title != exp_value:
                    if self.exp == "Pass":
                        self.screen.Screenshots("Screenshots/loginpageFailed.png",self.driver)
                        results.append("Fail")
                        self.log.info("------------Failed------------ ")
                    elif self.exp == "Fail":
                        self.screen.Screenshots("Screenshots/loginpagepassed.png", self.driver)
                        results.append("Pass")
                        self.log.info("------------Passed------------ ")

        if "Fail" not in results:
            self.log.info("****** Login DDT Test Passed ******")
            self.driver.close()
            assert True
        else:
            self.log.info("****** Login DDT Test Failed ******")
            self.driver.close()
            assert False














