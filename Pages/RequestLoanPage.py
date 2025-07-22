import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Locators.RequestLoanPageLocators import RequestLoanPageLocators
from Utils.ElementHelper import ElementHelper


class RequestLoanPage(ElementHelper):
    def request_loan(self):
        """Navigate to the loan request page."""
        self.driver.get(RequestLoanPageLocators.url)

    def loan_pay(self, loan_amount):
        """Enter the loan amount."""
        self.element_click_call(RequestLoanPageLocators.transfer_click)
        self.element_send_keys(RequestLoanPageLocators.loan_amount, loan_amount)

    def down_pay(self, down_payment):
        """Enter the down payment."""
        self.element_send_keys(RequestLoanPageLocators.down_payment, down_payment)

    def select_account(self, account_index=0):
        # Wait until dropdown is populated with options
        WebDriverWait(self.driver, 10).until(
            lambda d: len(Select(d.find_element(*RequestLoanPageLocators.from_account)).options) > 0
        )
        time.sleep(2)
        account_dropdown = Select(self.driver.find_element(*RequestLoanPageLocators.from_account))
        time.sleep(2)
        if account_dropdown.options:
            account_dropdown.select_by_index(account_index)
        else:
            print("⚠️ From Account dropdown is empty — skipping selection")

        """Select an account from the dropdown."""
        # dropdown = self.driver.find_element(*RequestLoanPageLocators.from_account)
        # self.select_by_index(dropdown, account_index)

    def apply_loan(self):
        """Click the apply button to submit the loan form."""
        self.element_click_call(RequestLoanPageLocators.apply_button)
        time.sleep(2)
    def logout (self):
        self.element_click_call(RequestLoanPageLocators.logout)
        time.sleep(2)

    def check_loan_result(self):
        """Check if the loan application failed or succeeded."""
        try:
            error_message = self.driver.get_text(RequestLoanPageLocators.internal_error_message)
            return f"Loan request failed: {error_message}"
        except Exception:
            return "Loan request submitted successfully!"
    def check_loan_status(self,locator):

        try:
            status=self.get_element_text(locator)
            return status
        except Exception:
            return"Error Found"

#status=self.driver.get_text(RequestLoanPageLocators.loan_status)




