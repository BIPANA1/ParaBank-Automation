import pytest
from Pages.LoginPage import LoginPage
from Pages.AccountOverviewPage import AccountOverviewPage

def test_account_overview_fetch(driver):
    # Step 1: Log in
    login_page = LoginPage(driver)
    login_page.login("Lara", "1234")

    # Step 2: Fetch account info
    overview_page = AccountOverviewPage(driver)
    account_number, available_balance = overview_page.get_account_info()

    # Step 3: Log results
    print(f"\n--- Account Overview ---")
    print(f"Account Number: {account_number if account_number else 'Not found'}")
    print(f"Available Balance: ₹{available_balance if available_balance is not None else 'Unavailable'}")

    # Optional sanity check
    assert account_number is not None, "Account number not found."
    assert available_balance is not None, "Available balance could not be fetched."