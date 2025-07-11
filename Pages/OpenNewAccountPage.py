from Locators.OpenNewAccPageLocators import OpenNewAccPageLocators
from Utils.ElementHelper import ElementHelper

from selenium.webdriver.support.ui import Select

class OpenAccountPage(ElementHelper):
    def open_account(self, account_type, account_number):
        # self.driver.get(OpenNewAccPageLocators.url)
        self.element_click_call(OpenNewAccPageLocators.new_account)
        self.select_dropdown_by_index(OpenNewAccPageLocators.account_type, account_type)
        self.select_dropdown_by_index(OpenNewAccPageLocators.account_number, account_number)
        self.element_click_call(OpenNewAccPageLocators.open_account_button)

    def get_open_account_result(self):
        if self.is_element_present(OpenNewAccPageLocators.confirmation_message):
            return "success"
        elif self.is_element_present(OpenNewAccPageLocators.error_message):
            return "validation_error"
        else:
            return "unknown"

    def select_dropdown_by_index(self, locator, index):
        select = Select(self.driver.find_element(*locator))
        select.select_by_index(int(index))



