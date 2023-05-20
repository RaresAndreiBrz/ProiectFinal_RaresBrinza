from locators.check_out_locators import CheckoutLocators
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(self.URL)

    def insert_info(self):
        self.driver.find_element(*CheckoutLocators.FIRSTNAME_INPUT).send_keys('Marius')
        self.driver.find_element(*CheckoutLocators.LASTNAME_INPUT).send_keys('Mirela')
        self.driver.find_element(*CheckoutLocators.POSTAL_INPUT).send_keys('2023')

    def continue_to_final_step(self):
        self.driver.find_element(*CheckoutLocators.BUTTON_CONTINUE).click()

    def cancel_checkout(self):
        self.driver.find_element(*CheckoutLocators.BUTTON_CANCEL).click()
