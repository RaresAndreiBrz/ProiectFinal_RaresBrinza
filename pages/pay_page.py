from locators.home_page_locs import HomePageLocators
from locators.pay_page_locators import PayPageLocators
from pages.base_page import BasePage


class PayPage(BasePage):

    def go_to_to_pay(self):
        self.driver.find_element(*PayPageLocators.BUTTON_FINISH).click()

    def check_total_price(self):
        self.preturi = []
        for pret in self.driver.find_elements(*HomePageLocators.PRICES):
            self.preturi.append(pret.text.replace('$', '').replace('.', ''))
        suma_preturi = sum(int(numar) for numar in self.preturi)
        self.suma_preturilor = []
        self.suma_preturilor.append(suma_preturi)
        self.total_price_no_tax = self.driver.find_element(*PayPageLocators.SUBTOTAL_AMOUNT_TEXT).text.replace(
            'Item total: $', '').replace(
            '.', '')
        self.tax = self.driver.find_element(*PayPageLocators.TOTAL_TAX).text.replace('Tax: $', '').replace(
            '.', '')
        self.total_price = int(self.tax) + int(self.total_price_no_tax)
        self.final_price = self.driver.find_element(*PayPageLocators.TOTAL_AMOUNT_TEXT).text.replace('Total: $',
                                                                                                     '').replace(
            '.', '')
        assert int(self.final_price) == int(self.total_price), "Suma nu e egala"
