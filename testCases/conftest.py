from selenium import webdriver
import pytest
from utilities.logger import logggen
log = logggen.logger()

@pytest.fixture()
def setup(browser):
    if browser == "Chrome":
        driver = webdriver.Chrome()
        log.info("--------Launching Chrome Browser--------")

    elif browser == "Edge":
        driver = webdriver.Edge()
        log.info("--------Launching Edge Browser--------")

    else:
        log.info("---No browser Selected---")

    return driver


def pytest_addoption(parser):
    '''To read the Browser command from the Command line interface'''
    parser.addoption( "--browser", action="store", default="Chrome")

@pytest.fixture()
def browser(request):
    '''Passing the Browser value to setup method'''
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata = {
        "Project Name" : "Nop Commerce",
        "Module Name" : "Customer",
        "Tester" : "Mahesh Kumar Chinta" }


