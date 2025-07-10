from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.RegisterPageLocators import RegisterPageLocators

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_register_button(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, RegisterPageLocators.register))).click()

    def enter_firstname(self, firstname):
        self.wait.until(EC.presence_of_element_located((By.ID, RegisterPageLocators.first_name))).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.wait.until(EC.presence_of_element_located((By.ID, RegisterPageLocators.last_name))).send_keys(lastname)

    def enter_address(self, address):
        self.wait.until(EC.presence_of_element_located((By.ID, RegisterPageLocators.address))).send_keys(address)

    def enter_city(self, city):
        self.wait.until(EC.presence_of_element_located((By.ID, RegisterPageLocators.city))).send_keys(city)

    def enter_state(self, state):
        self.wait.until(EC.presence_of_element_located((By.ID, RegisterPageLocators.state))).send_keys(state)

    def enter_zipcode(self, zipcode):
        self.wait.until(EC.presence_of_element_located((By.ID, RegisterPageLocators.zipcode))).send_keys(zipcode)

    def enter_phone(self, phone):
        self.wait.until(EC.presence_of_element_located((By.ID, RegisterPageLocators.phone))).send_keys(phone)

    def enter_ssn(self, ssn):
        self.wait.until(EC.presence_of_element_located((By.ID, RegisterPageLocators.ssn))).send_keys(ssn)

    def enter_username(self, username):
        self.wait.until(EC.presence_of_element_located((By.ID, RegisterPageLocators.username))).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.presence_of_element_located((By.ID, RegisterPageLocators.password))).send_keys(password)

    def enter_confirm(self, confirm_password):
        self.wait.until(EC.presence_of_element_located((By.ID, RegisterPageLocators.confirm_password))).send_keys(confirm_password)

    def click_register(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, RegisterPageLocators.register_button))).click()

    def click_register_link(self):
        pass
