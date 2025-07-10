import pytest

from Pages.RegisterPage import RegisterPage
from Utils.FileHelper import read_csv

test_data = read_csv("Data/registerData.csv")

@pytest.mark.parametrize(("firstname", "lastname","address","city","state","zipcode","phone","ssn","username","password","confirm_password"), test_data)
def test_register(firstname,lastname,address,city,state,zipcode,phone,ssn,username,password,confirm_password, driver):
    register_page = RegisterPage(driver)
    register_page.enter_register_button()
    register_page.enter_firstname(firstname)
    register_page.enter_lastname(lastname)
    register_page.enter_address(address)
    register_page.enter_city(city)
    register_page.enter_state(state)
    register_page.enter_zipcode(zipcode)
    register_page.enter_phone(phone)
    register_page.enter_ssn(ssn)
    register_page.enter_username(username)
    register_page.enter_password(password)
    register_page.enter_confirm(confirm_password)
    register_page.click_register()


    assert "register.htm" in driver.current_url.lower(), "Did not redirected to the Welcome Page."