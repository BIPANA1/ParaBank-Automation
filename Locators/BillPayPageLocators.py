from selenium.webdriver.common.by import By

class BillPayPageLocators:
    url = "https://parabank.parasoft.com/parabank/billpay.htm"

    # Payee Information
    payee_name_input = (By.ID, 'payeeName')
    payee_address_input = (By.ID, 'payeeAddress')
    payee_city_input = (By.ID, 'payeeCity')
    payee_state_input = (By.ID, 'payeeState')
    payee_zip_code_input = (By.ID, 'payeeZipCode')
    payee_phone_input = (By.ID, 'payeePhoneNumber')

    # Account Information
    account_number_input = (By.ID, 'payeeAccountNumber')
    verify_account_number_input = (By.ID, 'verifyAccount')
    amount_input = (By.ID, 'amount')
    from_account_input = (By.ID, 'fromAccountId')

    # Buttons
    send_payment_button = (By.ID, 'sendPayment')
    success_message = (By.CLASS_NAME, 'success')
