from selenium.webdriver.common.by import By


class AccountOverviewPageLocators:
    url = "https://parabank.parasoft.com/parabank/overview.htm"
    account_overview= (By.XPATH,'/html/body/div[1]/div[3]/div[1]/ul/li[2]/a')
    Account_table=(By.ID,'overviewAccountsApp')
    account_first= (By.XPATH,'//*[@id="accountTable"]/tbody/tr[1]/td[1]/a')
    available_balance = (By.XPATH,'//*[@id="accountTable"]/tbody/tr[1]/td[3]')
    account_id = (By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[1]/a')
