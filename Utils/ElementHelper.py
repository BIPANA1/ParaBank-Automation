from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ElementHelper:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def element_send_keys(self, locator, text):
        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def element_click_call(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    # checks if element(s) exists and is visible (returns True/False)
    def is_element_present(self, locator):
        try:
            self.wait.until(EC.visibility_of_any_elements_located(locator))
            return True
        except TimeoutException:
            return False

    # returns the text of the element or None if not present
    def get_element_text(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text
        except TimeoutException:
            return None