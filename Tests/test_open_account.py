import pytest
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locators.OpenNewAccPageLocators import OpenNewAccPageLocators
from Pages.LoginPage import LoginPage
from Pages.OpenNewAccountPage import OpenAccountPage
from Utils.FileHelper import read_csv

test_data = read_csv("Data/newAccountData.csv")
@pytest.mark.order(3)

@pytest.mark.parametrize(("account_type", "expected_result"), test_data)
def test_open_new_account(account_type, expected_result, driver):
    login_page = LoginPage(driver)
    login_page.login("Lara", "1234")

    open_account_page = OpenAccountPage(driver)

    # First navigate properly
    open_account_page.element_click_call(OpenNewAccPageLocators.new_account)
    # open_account_page.load()

    # Wait for dropdown readiness
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(OpenNewAccPageLocators.account_type))
    WebDriverWait(driver, 10).until(
        lambda d: len(Select(d.find_element(*OpenNewAccPageLocators.account_number)).options) > 0
    )

    # Perform account opening
    result = open_account_page.open_account(account_type)

    # If result is returned from open_account(), use it
    if result:
        actual_result = result
    else:
        actual_result = open_account_page.get_transaction_result()

    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
