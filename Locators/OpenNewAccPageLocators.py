from selenium.webdriver.common.by import By


class OpenNewAccPageLocators:
    url = "https://parabank.parasoft.com/parabank/openaccount.htm"
    # account_type = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div[1]/form/select[1]')
    # account_number = (By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/div[1]/form/select[2]')
    open_account_button = (By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/div[1]/form/div/input')
    # new_account = (By.XPATH,'//*[@id="leftPanel"]/ul/li[1]/a')
    new_account = (By.XPATH,'/html/body/div[1]/div[3]/div[1]/ul/li[1]/a')
    confirmation_message = (By.ID,'newAccountId')
    error_message = (By.ID, 'openAccountError')
    account_type = (By.ID, "type")
    account_number = (By.ID, "fromAccountId")


