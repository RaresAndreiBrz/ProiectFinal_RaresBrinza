import time

from locators.home_page_locs import HomePageLocators
from locators.login_page_locs import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def get_logo(self):
        return self.driver.find_element(*LoginPageLocators.LOGO).is_displayed()

    def login_true(self):
        self.driver.find_element(*LoginPageLocators.USER_INPUT).send_keys(*LoginPageLocators.username)
        self.driver.find_element(*LoginPageLocators.PWD_INPUT).send_keys(*LoginPageLocators.pwd)
        self.driver.find_element(*LoginPageLocators.BUTON_LOGIN).click()
        time.sleep(1)

    def login_false(self):
        self.driver.find_element(*LoginPageLocators.USER_INPUT).send_keys(*LoginPageLocators.username_false)
        self.driver.find_element(*LoginPageLocators.PWD_INPUT).send_keys(*LoginPageLocators.pwd)
        self.driver.find_element(*LoginPageLocators.BUTON_LOGIN).click()

    def is_login_error_displayed(self):
        return self.driver.find_element(*LoginPageLocators.ERROR_MSSG).is_displayed()

    def is_shop_page_open(self):
        assert self.driver.find_element(*HomePageLocators.BUTTON_ADD_TO_CART_bike).is_displayed()

    def go_to_shop_page(self):
        self.login_true()
