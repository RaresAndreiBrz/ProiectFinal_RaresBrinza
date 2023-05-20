from selenium.webdriver.common.by import By


class LoginPageLocators:
    USER_INPUT = (By.ID, "user-name")
    PWD_INPUT = (By.ID, "password")
    BUTON_LOGIN = (By.ID, 'login-button')
    pwd = 'secret_sauce'
    username = 'standard_user'
    username_false = 'standard_e'
    ERROR_MSSG = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]')
    ERROR_CANCELING = (By.CLASS_NAME, 'error-button')
    LOGO = (By.XPATH, '//*[@id="root"]/div/div[1]')
