from operator import index

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from Locators.TransferFundPageLocators import TransferFundPageLocators
from Utils.ElementHelper import ElementHelper

class TransactionOverviewPage(ElementHelper):

    def load(self):
        # Transfer fund page ko URL ma navigate garne
        self.driver.get(TransferFundPageLocators.url)

    def get_balance_by_account_index(self, account_index):
        try:
            # Account Overview tab ma click garne
            self.element_click_call(TransferFundPageLocators.account_overview)

            self.get_element_text(TransferFundPageLocators.account_table)

            # Specific index ko account balance nikalne (1-based indexing)
            balance_locator = (
                By.XPATH,
                f"//*[@id='accountTable']/tbody/tr[{account_index + 1}]/td[2]"
            )
            balance_element = self.driver.find_element(*balance_locator)

            # Balance text lai clean garera float ma convert garne
            balance_text = balance_element.text.replace("$", "").replace(",", "").strip()
            return float(balance_text)

        except (TimeoutException, NoSuchElementException, ValueError) as e:
            print(f"[Balance Fetch Error]: {e}")
            return None

    def transaction(self, amount):
        try:
            # Transfer tab ma click garne
            self.element_click_call(TransferFundPageLocators.transfer_click)

            # Amount enter garne
            self.element_send_keys(TransferFundPageLocators.amount, amount)

            self.wait_for_dropdown_and_select_by_index(TransferFundPageLocators.from_account, index=1, min_options = 2)
            self.wait_for_dropdown_and_select_by_index(TransferFundPageLocators.to_account, index=0)

            # Transfer button click garne
            self.element_click_call(TransferFundPageLocators.transfer_button)

        except Exception as e:
            print(f"[Transaction Error]: {e}")

    def get_transaction_result(self):
        try:
            # Internal error check garne — failure case
            if self.is_element_present(TransferFundPageLocators.internal_error_message):
                return "failure"

            # Success message ko presence check garne
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(TransferFundPageLocators.success_message)
            )
            return "success"

        except Exception as e:
            print(f"[Result Check Error]: {e}")
            return "unknown"

    def compare_receiver_balance_after_transaction(self, amount, receiver_index=0):
        # Step 1: Transaction agadi receiver ko balance capture garne
        initial_balance = self.get_balance_by_account_index(receiver_index)
        if initial_balance is None:
            return "initial_balance_not_found"

        # Step 2: Transfer fund page load garne & transaction suru garne
        self.load()
        self.transaction(str(amount))

        # Step 3: Transaction result check garne
        transaction_status = self.get_transaction_result()
        if transaction_status != "success":
            return f"transaction_failed:{transaction_status}"

        # Step 4: Pheri overview page ma gayera updated balance nikalne
        updated_balance = self.get_balance_by_account_index(receiver_index)
        if updated_balance is None:
            return "updated_balance_not_found"

        # Step 5: Expected increase ra actual increase compare garne
        expected_increase = float(amount)
        actual_increase = updated_balance - initial_balance

        if abs(actual_increase - expected_increase) < 0.01:
            return "balance_upgraded"
        else:
            return f"expected_increase:{expected_increase}, actual_increase:{actual_increase}"