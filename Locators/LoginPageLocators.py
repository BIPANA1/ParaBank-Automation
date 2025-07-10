from selenium.webdriver.common.by import By


class LoginPageLocators:
    url = 'https://parabank.parasoft.com/parabank/index.htm'
    username_xpath = (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/form/div[1]/input')
    password_xpath = (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/form/div[2]/input')
    loginButton_xpath = (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/form/div[3]/input')
    error_message = (By.XPATH, '//div[contains(@class, "error")]')
