import time

from locators.home_page_locs import HomePageLocators
from locators.login_page_locs import LoginPageLocators
from pages.base_page import BasePage


class HomePage(BasePage):


    def add_to_cart(self):
        self.driver.find_element(*HomePageLocators.BUTTON_ADD_TO_CART_backpack).click()

    def remove_from_cart(self):
        self.driver.find_element(*HomePageLocators.BUTTON_REMOVE_FROM_CART_backpack).click()

    def add_to_cart2(self):
        self.driver.find_element(*HomePageLocators.BUTTON_ADD_TO_CART_bike).click()
        assert self.driver.find_element(*HomePageLocators.BUTTON_REMOVE_FROM_CART_bike).is_displayed()
    def remove_from_cart2(self):
        self.driver.find_element(*HomePageLocators.BUTTON_REMOVE_FROM_CART_bike).click()

    def go_to_cart(self):
        self.driver.find_element(*HomePageLocators.BUTTON_SHOP_CART).click()

    def logout(self):

        self.driver.find_element(*HomePageLocators.BUTTON_MENU_LIST).click()
        time.sleep(1)
        self.driver.find_element(*HomePageLocators.BUTTON_MENU_LOGOUT).click()
        time.sleep(1)
        assert self.driver.find_element(*LoginPageLocators.BUTON_LOGIN).is_displayed(), 'Nu e pg de login aici'

    def sorting_price_desc(self):
        self.driver.find_element(*HomePageLocators.BUTTON_SORT).click()
        time.sleep(1)
        self.driver.find_element(*HomePageLocators.BUTTON_SORT_PRICE_HL).click()
        time.sleep(1)
        self.preturi_desc = []
        for pret in self.driver.find_elements(*HomePageLocators.PRICES):
            self.preturi_desc.append(float(pret.text.replace('$', '').replace('.', '')))
        self.preturi_desc_check = all(
            self.preturi_desc[i] >= self.preturi_desc[i + 1] for i in range(len(self.preturi_desc) - 1))
        assert self.preturi_desc_check == True

    def sorting_price_asc(self):
        self.driver.find_element(*HomePageLocators.BUTTON_SORT).click()
        time.sleep(1)
        self.driver.find_element(*HomePageLocators.BUTTON_SORT_PRICE_LH).click()
        time.sleep(1)
        self.preturi_asc = []
        for pret in self.driver.find_elements(*HomePageLocators.PRICES):
            self.preturi_asc.append(float(pret.text.replace('$', '').replace('.', '')))
        self.preturi_asc_check = all(
            self.preturi_asc[i] <= self.preturi_asc[i + 1] for i in range(len(self.preturi_asc) - 1))

        assert self.preturi_asc_check == True

    def remove_item_button(self):
        self.driver.find_element(*HomePageLocators.BUTTON_ADD_TO_CART_backpack).click()
        time.sleep(1)
        if self.driver.find_element(*HomePageLocators.BUTTON_SHOP_CART_ITEMS_NUMBER).is_displayed():
            self.driver.find_element(*HomePageLocators.BUTTON_REMOVE_FROM_CART_backpack).click()
            time.sleep(1)
            if not self.driver.find_element(
                    *HomePageLocators.BUTTON_SHOP_CART_ITEMS_NUMBER).is_displayed() and self.driver.find_element(
                *HomePageLocators.BUTTON_ADD_TO_CART_backpack).is_displayed():
                return '"Remove button" works.'
            else:
                return '"Remove button" didnt work.'
        else:
            return False

    def this_is_home_page(self):
        assert self.driver.find_element(*HomePageLocators.BUTTON_SORT).is_displayed()

    def items_are_here(self):
        assert self.driver.find_element(*HomePageLocators.BUTTON_ADD_TO_CART_bike).is_displayed()

    def is_shop_page_open(self):
        assert self.driver.find_element(*HomePageLocators.BUTTON_ADD_TO_CART_bike).is_displayed()
