
import pytest

from Pages.RegisterPage import RegisterPage
from Utils.FileHelper import read_csv

test_data = read_csv("Data/registerData.csv")

@pytest.mark.parametrize(("firstname", "lastname","address","city","state","zipcode","phone","ssn","username","password","confirm_password","expected"), test_data)
def test_register(firstname,lastname,address,city,state,zipcode,phone,ssn,username,password,confirm_password,expected, driver):
    register_page = RegisterPage(driver)
    register_page.register(firstname, lastname, address, city, state, zipcode, phone, ssn, username, password, confirm_password)

    assert register_page.get_register_result() == expected
