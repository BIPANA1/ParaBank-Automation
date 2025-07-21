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

@pytest.mark.parametrize(
    ("loan_amount", "down_payment", "account_index", "expected"),
    test_data
)
def test_request_loan(driver, loan_amount, down_payment, account_index, expected):
    # Step 1: Log in to the application
    login_page = LoginPage(driver)
    login_page.login("bij","1234")
    #login_page.login(LoginPageLocators.valid_username, LoginPageLocators.valid_password)  # Replace with valid credentials if needed
    #register_page=RegisterPage(driver)
    #register_page.register("Lara","Del","Kathmandu","Nepal",223,"5E6542W",9876513245,871,"Laradel1","Laradel123","Laradel123")
    # Step 2: Go to the Request Loan page
    loan_page = RequestLoanPage(driver)
    loan_page.request_loan()

    # Step 3: Fill out the loan form
    loan_page.loan_pay(loan_amount)
    loan_page.down_pay(down_payment)
    loan_page.select_account(int(account_index))
    loan_page.apply_loan()

    # Step 4: Capture and validate result
    #result = loan_page.check_loan_result()
    result=loan_page.check_loan_status(RequestLoanPageLocators.loan_status)
    #result2 = loan_page.check_loan_status(RequestLoanPageLocators.loan_approved)
    #result3 = loan_page.check_loan_status(RequestLoanPageLocators.loan_rejected)
    print(f"{result}")
    if expected== "Pass":
        assert result=="Approved",print(f"status: {result}")
    elif expected=="Fail":
        assert result=="Denied",print(f"status:{result}")
    else:
        print("Error Founded ")
    # assert result == expected, (
    #     f"\n❌ Loan Request Test Failed\n"
    #     f"→ Loan Amount: {loan_amount}\n"
    #     f"→ Down Payment: {down_payment}\n"
    #     f"→ Account Index: {account_index}\n"
    #     f"→ Expected: {expected}\n"
    #     f"→ Got: {result}\n"
    # )
    #assert result==expected,print(f"{result}{expected}")
