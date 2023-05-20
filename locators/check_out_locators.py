from selenium.webdriver.common.by import By


class CheckoutLocators:

    FIRSTNAME_INPUT = (By.ID, 'first-name')
    LASTNAME_INPUT = (By.ID, 'last-name')
    POSTAL_INPUT = (By.ID, 'postal-code')
    BUTTON_CONTINUE = (By.ID, 'continue')
    BUTTON_CANCEL = (By.ID, 'cancel')
