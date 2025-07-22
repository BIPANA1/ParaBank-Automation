
from selenium.webdriver.common.by import By

class OpenNewAccPageLocators:
    new_account = (By.CSS_SELECTOR, "#leftPanel ul li:first-child a")
    account_type = (By.ID, "type")
    account_number = (By.ID, "fromAccountId")
    open_account_button = (By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/div[1]/form/div/input')
    confirmation_message = (By.ID, "newAccountId")
    error_message = (By.ID, "openAccountError")
    url = "https://parabank.parasoft.com/parabank/openaccount.htm"

