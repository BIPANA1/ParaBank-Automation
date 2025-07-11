import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    baseUrl = "https://parabank.parasoft.com/"
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(baseUrl)
    yield driver
    driver.quit()