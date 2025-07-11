from webbrowser import register

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.RegisterPageLocators import RegisterPageLocators
from Utils.ElementHelper import ElementHelper


class RegisterPage(ElementHelper):
    def load(self, path=""):
        self.driver.get(self.driver.current_url + path)

    def register(self, firstname, lastname,address, city,state, zipcode,phone,ssn,username,password,confirm_password):
        self.element_click_call(RegisterPageLocators.register)
        self.element_send_keys(RegisterPageLocators.first_name, firstname)
        self.element_send_keys(RegisterPageLocators.last_name, lastname)
        self.element_send_keys(RegisterPageLocators.address, address)
        self.element_send_keys(RegisterPageLocators.city, city)
        self.element_send_keys(RegisterPageLocators.state,state)
        self.element_send_keys(RegisterPageLocators.zipcode, zipcode)
        self.element_send_keys(RegisterPageLocators.phone,phone)
        self.element_send_keys(RegisterPageLocators.ssn,ssn)
        self.element_send_keys(RegisterPageLocators.username,username)
        self.element_send_keys(RegisterPageLocators.password,password)
        self.element_send_keys(RegisterPageLocators.confirm_password,confirm_password)

    def get_register_result(self):
        if self.is_element_present(RegisterPageLocators.success_message):
            return "success"

        if self.is_element_present(RegisterPageLocators.error_message):
            return "success"

        if self.is_element_present(RegisterPageLocators.pw_error):
            return "success"

        return "validation_error"
