from selenium.webdriver.common.by import By


class RequestLoanPageLocators:
    url = "https://parabank.parasoft.com/parabank/requestloan.htm"
    transfer_click = (By.XPATH,'//*[@id="leftPanel"]/ul/li[7]/a')
    loan_amount = (By.ID,'amount')
    down_payment = (By.ID,'downPayment')
    from_account = (By.ID,'fromAccountId')
    apply_button = (By.XPATH,'//*[@id="requestLoanForm"]/form/table/tbody/tr[4]/td[2]/input')

    loan_error_message = "https://parabank.parasoft.com/parabank/requestloan.htm"
    internal_error_message = (By.XPATH,'//*[@id="requestLoanError"]/p')
    loan_status=(By.XPATH,'//*[@id="loanStatus"]')
    logout=(By.XPATH,'//*[@id="leftPanel"]/ul/li[8]/a')
