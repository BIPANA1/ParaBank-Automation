from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.AccountOverviewPageLocators import AccountOverviewPageLocators
from Utils.ElementHelper import ElementHelper
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class AccountOverviewPage(ElementHelper):
    def get_account_info(self):
        try:
            # Navigate to Account Overview
            self.element_click_call(AccountOverviewPageLocators.account_overview)

            # Wait for table to appear
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(AccountOverviewPageLocators.Account_table)
            )

            # Fetch elements
            account_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(AccountOverviewPageLocators.account_first)
            )
            balance_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(AccountOverviewPageLocators.available_balance)
            )

            # balance_id = WebDriverWait(self.driver,5).until(
            #     EC.presence_of_element_located(AccountOverviewPageLocators.account_id)
            # )
            #



            # Extract and clean values
            account_number = account_element.text.strip()
            available_balance_text = balance_element.text.replace("$", "").replace(",", "").strip()

            print(f"Raw balance text: '{available_balance_text}'")

            try:
                available_balance_float = float(available_balance_text)
            except ValueError:
                print("Warning: Could not convert balance to float.")
                available_balance_float = None

            print(f"Available Balance: ₹{available_balance_float if available_balance_float is not None else 'Unavailable'}")
            return account_number, available_balance_float

        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error fetching account info: {e}")
            return None