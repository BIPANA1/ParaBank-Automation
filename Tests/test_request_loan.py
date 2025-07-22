import time
from multiprocessing.resource_tracker import register

import pytest

from Locators.LoginPageLocators import LoginPageLocators
from Locators.RequestLoanPageLocators import RequestLoanPageLocators
from Pages.LoginPage import LoginPage
from Pages.RegisterPage import RegisterPage
from Pages.RequestLoanPage import RequestLoanPage
from Utils.FileHelper import read_csv

# Load test data from CSV
test_data = read_csv("Data/requestLoan.csv")
@pytest.mark.order(7)
@pytest.mark.parametrize(
    ("loan_amount", "down_payment", "account_index", "expected"),
    test_data
)
def test_request_loan(driver, loan_amount, down_payment, account_index, expected):
    # Step 1: Log in to the application
    login_page = LoginPage(driver)
    login_page.login("Lara","1234")
    loan_page = RequestLoanPage(driver)
    loan_page.request_loan()

    # Step 3: Fill out the loan form
    loan_page.loan_pay(loan_amount)
    loan_page.down_pay(down_payment)
    loan_page.select_account(int(account_index))
    loan_page.apply_loan()
    result=loan_page.check_loan_status(RequestLoanPageLocators.loan_status)
    time.sleep(10)
    loan_page.logout()
    time.sleep(10)
    print(f"{result}")
    if expected== "Pass":
        assert result=="Approved",print(f"status: {result}")
    elif expected=="Fail":
        assert result=="Denied",print(f"status:{result}")
    else:
        print("Error Founded ")
