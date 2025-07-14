import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.LoginPage import LoginPage
from Pages.BillPayPage import BillPayPage
from Locators.BillPayPageLocators import BillPayPageLocators
from Utils.FileHelper import read_csv

test_data = read_csv("Data/BillPayPageData.csv")

@pytest.mark.parametrize((
    "payee_name", "address", "city", "state", "zip_code", "phone",
    "account_number", "verify_account_number", "amount", "from_account", "expected"
), test_data)
def test_bill_pay(payee_name, address, city, state, zip_code, phone,
                  account_number, verify_account_number, amount, from_account, expected, driver):

    login_page = LoginPage(driver)
    login_page.login("shyam2", "shyam")

    bill_pay_page = BillPayPage(driver)
    bill_pay_page.load()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(BillPayPageLocators.bill_pay_menu)
    ).click()

    bill_pay_page.enter_payee_information(payee_name, address, city, state, zip_code, phone)
    bill_pay_page.enter_account_information(account_number, verify_account_number, amount, from_account)
    bill_pay_page.send_payment()

    # Enhanced logic to detect outcome:
    if bill_pay_page.has_verify_account_mismatch_error():
        result = "failure"
    elif bill_pay_page.has_negative_amount_error():
        result = "failure"
    elif bill_pay_page.has_success_message():
        result = "success"
    else:
        result = "failure"

    assert result == expected