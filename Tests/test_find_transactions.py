import pytest

from Pages.FindTransactionsPage import FindTransactionsPage
from Pages.LoginPage import LoginPage
from Utils.FileHelper import read_csv

test_data = read_csv("Data/findTxnData.csv")
@pytest.mark.order(6)
@pytest.mark.parametrize(("search_type", "value1", "value2", "expected"), test_data)
def test_find_transactions(search_type, value1, value2, expected, driver):
    username = "Lara"
    password = "1234"

    login_page = LoginPage(driver)
    login_page.login(username, password)

    find_txn_page = FindTransactionsPage(driver)
    find_txn_page.load()

    if search_type == "transaction_id":
        find_txn_page.search_by_transaction_id(value1)
    elif search_type == "date":
        find_txn_page.search_by_date(value1)
    elif search_type == "date_range":
        find_txn_page.search_by_date_range(value1, value2)
    elif search_type == "amount":
        find_txn_page.search_by_amount(value1)

    assert find_txn_page.get_find_txn_result() == expected