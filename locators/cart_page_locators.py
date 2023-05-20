from selenium.webdriver.common.by import By


class CartPageLocators:
    BUTTONS_REMOVE_FROM_CART = (By.CLASS_NAME, 'btn btn_secondary btn_small cart_button')
    BUTTON_CHECKOUT = (By.ID, 'checkout')
    BUTTON_BACK_SHOPPING = (By.ID, 'continue-shopping')
    CART_QUANTITY = (By.CLASS_NAME, 'cart_quantity')
