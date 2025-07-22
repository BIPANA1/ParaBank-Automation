from selenium.webdriver.common.by import By

class RegisterPageLocators:
    error_message = (By.ID, 'customer.username.errors')
    pw_error = (By.ID, 'repeatedPassword.errors')
    success_message_class = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/h1')
    error = (By.CLASS_NAME,'error')
    url = "https://parabank.parasoft.com/parabank/register.htm"
    register=(By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/p[2]/a')
    first_name =(By.ID,'customer.firstName')
    last_name =(By.ID,'customer.lastName')
    address=(By.ID,'customer.address.street')
    city=(By.ID,'customer.address.city')
    state=(By.ID,'customer.address.state')
    zipcode=(By.ID,'customer.address.zipCode')
    phone =(By.ID,'customer.phoneNumber')
    ssn=(By.ID,'customer.ssn')
    username=(By.ID,'customer.username')
    password= (By.ID,'customer.password')
    confirm_password=(By.ID,'repeatedPassword')
    register_button = (By.XPATH, "/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[13]/td[2]/input")


