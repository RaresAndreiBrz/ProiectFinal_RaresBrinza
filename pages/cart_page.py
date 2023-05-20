import time

from locators.cart_page_locators import CartPageLocators
from locators.home_page_locs import HomePageLocators
from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(self.URL)


    def go_to_info_order(self):
        self.driver.find_element(*CartPageLocators.BUTTON_CHECKOUT).click()

    def check_items_correctly(self):
        items_in_cart = self.driver.find_elements(*CartPageLocators.CART_QUANTITY)
        time.sleep(1)
        items_on_icon = self.driver.find_element(*HomePageLocators.BUTTON_SHOP_CART_ITEMS_NUMBER).text
        time.sleep(1)
        assert int(len(items_in_cart)) == int(items_on_icon), 'Nu sunt cifrele obiecte / cos identice'

    def go_to_inventory_page(self):
        self.driver.find_element(*CartPageLocators.BUTTON_BACK_SHOPPING).click()
