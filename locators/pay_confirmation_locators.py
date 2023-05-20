from selenium.webdriver.common.by import By


class PayConfirmationLocators:
    MSSG_CONFIRM = (By.CLASS_NAME, 'complete-header')
    CHECKOUT_COMPLETE_HEADER = (By.CLASS_NAME, 'header_secondary_container')
    BUTTON_BACK_HOME = (By.ID, 'back-to-products')
    MSSG_CONFIRM_TEXT = 'Thank you for your order!'
