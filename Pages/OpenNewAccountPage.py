from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.OpenNewAccPageLocators import OpenNewAccPageLocators
from Locators.TransferFundPageLocators import TransferFundPageLocators
from Utils.ElementHelper import ElementHelper

class OpenAccountPage(ElementHelper):
    def open_account(self, account_type_text):
        self.element_click_call(OpenNewAccPageLocators.new_account)
        self.is_element_present(OpenNewAccPageLocators.account_type)
        self.wait_for_dropdown_and_select_by_index(OpenNewAccPageLocators.account_number, index=0)

        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(OpenNewAccPageLocators.account_type))
        # WebDriverWait(self.driver, 10).until(
        #     lambda d: len(Select(d.find_element(*OpenNewAccPageLocators.account_number)).options) > 0
        # )

        # Handle blank or invalid account_type
        if not account_type_text.strip():
            print(" Blank account type — skipping selection")
            return "validation_error"

        try:
            Select(self.driver.find_element(*OpenNewAccPageLocators.account_type)).select_by_visible_text(account_type_text)
        except Exception as e:
            print(f" Invalid account type '{account_type_text}' — {e}")
            return "validation_error"

        number_dropdown = Select(self.driver.find_element(*OpenNewAccPageLocators.account_number))
        first_value = number_dropdown.options[0].get_attribute("value")
        number_dropdown.select_by_value(first_value)

        open_button = self.driver.find_element(*OpenNewAccPageLocators.open_account_button)
        self.driver.execute_script("arguments[0].click();", open_button)
        return None

    def get_transaction_result(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(TransferFundPageLocators.success_message)
            )
            return "success"
        except:
            if self.is_element_present(TransferFundPageLocators.amount_error_message):
                return "failure"
            return "unknown"


