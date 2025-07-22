import pytest
from Pages.LoginPage import LoginPage
from Pages.TransferFundsPage import  TransferFundsPage
from Utils.FileHelper import read_csv

test_data = read_csv("Data/transferFunds.csv")
@pytest.mark.order(4)
@pytest.mark.parametrize((
    "amount", "expected"),test_data)
def test_transfer_fund(amount, expected, driver):
    # Step 1: Log in
    login_page = LoginPage(driver)
    login_page.login("Lara", "1234")

    # Step 2: Perform transaction
    transfer_page = TransferFundsPage(driver)
    transfer_page.load()
    transfer_page.transaction(amount)

    # Step 3: Check result
    result = transfer_page.get_transaction_result()

    # Step 4: Assert outcome
    assert result == expected, (
        f"Expected {expected} but got {result} for amount: '{amount}'"
    )