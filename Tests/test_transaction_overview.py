import pytest
from Pages.LoginPage import LoginPage
from Pages.TransactionOverviewPage import TransactionOverviewPage
from Pages.AccountOverviewPage import AccountOverviewPage
from Utils.FileHelper import read_csv

test_data = read_csv("Data/transferOverview.csv")

@pytest.mark.parametrize(("amount", "expected"), test_data)
def test_transfer_and_validate_balance(amount, expected, driver):
    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.login("Lara", "1234")

    # Step 2: Get initial balance from AccountOverviewPage
    account_page = AccountOverviewPage(driver)
    _, initial_balance = account_page.get_account_info()
    assert initial_balance is not None, "Initial balance could not be retrieved."
    print(f"Initial Available Balance: ₹{initial_balance}")

    # Step 3: Perform transaction from account index 1 to 0
    transfer_page = TransactionOverviewPage(driver)
    transfer_page.load()
    transfer_page.transaction(str(amount))

    # Step 4: Validate transaction success
    result = transfer_page.get_transaction_result()
    assert result == expected, f"Expected '{expected}', but got '{result}'"

    # Step 5: Navigate back and get updated balance
    updated_account_page = AccountOverviewPage(driver)
    _, updated_balance = updated_account_page.get_account_info()
    assert updated_balance is not None, "Updated balance could not be retrieved."
    print(f"Updated Available Balance: ₹{updated_balance}")

    # Step 6: Compare balances if transaction was successful
    if expected == "success":
        expected_increase = float(amount)
        actual_increase = updated_balance - initial_balance
        print(f"Amount Received by Receiver: ₹{actual_increase}")
        # Validate that actual increase matches expected transfer amo
        assert abs(actual_increase - expected_increase) < 0.01, (
            f"Expected increase: ₹{expected_increase}, but got ₹{actual_increase}"

        )