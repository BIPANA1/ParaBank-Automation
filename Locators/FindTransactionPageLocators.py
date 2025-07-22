from selenium.webdriver.common.by import By


class FindTransactionPageLocators:
    url = "https://parabank.parasoft.com/parabank/findtrans.htm"

    # by txn id
    transaction_id_input = (By.ID, 'transactionId')
    button_txn_id = (By.ID, 'findById')

    # by date
    date_input = (By.ID, 'transactionDate')
    button_txn_date = (By.ID, 'findByDate')

    # by date range
    from_date_input = (By.ID, 'fromDate')
    to_date_input = (By.ID, 'toDate')
    button_txn_date_range = (By.ID, 'findByDateRange')

    # by amount
    amount_input = (By.ID, 'amount')
    button_txn_amount = (By.ID, 'findByAmount')

    # misc
    error_message = (By.CLASS_NAME, "error")
    transaction_rows = (By.CSS_SELECTOR, "#transactionBody tr")

