import pytest

from Pages.LoginPage import LoginPage
from Utils.FileHelper import read_csv

test_data = read_csv("Data/loginData.csv")

@pytest.mark.parametrize(("username", "password", "expected"), test_data)
def test_valid_login(username, password, expected, driver):
    login_page = LoginPage(driver)
    login_page.login(username, password)
    assert login_page.get_login_result() == expected

