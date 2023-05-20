from locators.pay_confirmation_locators import PayConfirmationLocators
from pages.base_page import BasePage


class PayConfirmationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def order_succesfully(self):
        assert self.driver.find_element(*PayConfirmationLocators.MSSG_CONFIRM).is_displayed(), "Eroare msj confirmare"

    def messages_displayed(self):
        assert self.driver.find_element(
            *PayConfirmationLocators.MSSG_CONFIRM).text == PayConfirmationLocators.MSSG_CONFIRM_TEXT, "Text gresit"
        assert self.driver.find_element(
            *PayConfirmationLocators.CHECKOUT_COMPLETE_HEADER).is_displayed(), "Nu e header-ul"
