# from selenium.webdriver.support import expected_conditions as EC
#
# import pytest
# from selenium.webdriver.support.wait import WebDriverWait
#
# from Locators.OpenNewAccPageLocators import OpenNewAccPageLocators
# from Pages.LoginPage import LoginPage
# from Pages.OpenNewAccountPage import OpenAccountPage
# from Utils.FileHelper import read_csv
#
# test_data = read_csv("Data/newAccountData.csv")
#
# @pytest.mark.parametrize(("account_type", "from_account", "expected_result"), test_data)
# def test_open_account(account_type, from_account, expected_result, driver):
#     username = "bipana"
#     password = "1234"
#
#     login_page = LoginPage(driver)
#     login_page.login(username, password)
#
#     open_account_page = OpenAccountPage(driver)
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located(OpenNewAccPageLocators.account_type))
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located(OpenNewAccPageLocators.account_number))
#     # open_account_page.select_dropdown_by_index(account_type, from_account)
#     assert open_account_page.get_open_account_result() == expected_result

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locators.OpenNewAccPageLocators import OpenNewAccPageLocators
from Pages.LoginPage import LoginPage
from Pages.OpenNewAccountPage import OpenAccountPage
from Utils.FileHelper import read_csv

test_data = read_csv("Data/newAccountData.csv")

@pytest.mark.parametrize(("account_type", "account_number", "expected_result"), test_data)
def test_open_account(account_type, account_number, expected_result, driver):
    username = "bipana"
    password = "1234"

    login_page = LoginPage(driver)
    login_page.login(username, password)

    open_account_page = OpenAccountPage(driver)
    open_account_page.element_click_call(OpenNewAccPageLocators.new_account)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(OpenNewAccPageLocators.account_type))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(OpenNewAccPageLocators.account_number))

    # open_account_page.open_account(account_type, account_number)

    assert open_account_page.get_open_account_result() == expected_result
