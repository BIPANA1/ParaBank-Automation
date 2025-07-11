from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locators.BillPayPageLocators import BillPayPageLocators
from Utils.ElementHelper import ElementHelper

class BillPayPage(ElementHelper):
    def load(self):
        self.driver.get(BillPayPageLocators.url)

    def enter_payee_information(self, name, address, city, state, zip_code, phone):
        self.element_send_keys(BillPayPageLocators.payee_name_input, name)
        self.element_send_keys(BillPayPageLocators.payee_address_input, address)
        self.element_send_keys(BillPayPageLocators.payee_city_input, city)
        self.element_send_keys(BillPayPageLocators.payee_state_input, state)
        self.element_send_keys(BillPayPageLocators.payee_zip_code_input, zip_code)
        self.element_send_keys(BillPayPageLocators.payee_phone_input, phone)

    def enter_account_information(self, account_number, verify_account_number, amount, from_account):
        self.element_send_keys(BillPayPageLocators.account_number_input, account_number)
        self.element_send_keys(BillPayPageLocators.verify_account_number_input, verify_account_number)
        self.element_send_keys(BillPayPageLocators.amount_input, amount)
        self.element_send_keys(BillPayPageLocators.from_account_input, from_account)

    def send_payment(self):
        self.element_click_call(BillPayPageLocators.send_payment_button)

    def has_success_message(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(BillPayPageLocators.success_message)
            )
            return True
        except TimeoutException:
            return False
