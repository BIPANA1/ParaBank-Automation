import pytest
import csv

from Pages.BillPayPage import BillPayPage
from Pages.LoginPage import LoginPage

def read_csv(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)

@pytest.mark.parametrize("data", read_csv("Data/BillPayPageData.csv"))
def test_bill_pay(driver, data):
    username = "shyam2"
    password = "shyam"

    login_page = LoginPage(driver)
    login_page.login(username, password)

    bill_pay_page = BillPayPage(driver)
    bill_pay_page.load()

    bill_pay_page.enter_payee_information(
        data["payee_name"],
        data["address"],
        data["city"],
        data["state"],
        data["zip_code"],
        data["phone"]
    )

    bill_pay_page.enter_account_information(
        data["account_number"],
        data["verify_account_number"],
        data["amount"],
        data["from_account"]
    )

    bill_pay_page.send_payment()

    assert bill_pay_page.has_success_message() == data["expected"]

