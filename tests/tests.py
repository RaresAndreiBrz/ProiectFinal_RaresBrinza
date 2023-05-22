import time


from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.pay_confirmation_page import PayConfirmationPage
from pages.pay_page import PayPage
from base_test import BaseTests


class Tests(BaseTests):

    def test_Login_false(self):
        logare1 = LoginPage(self.driver)
        logare1.login_false()
        logare1.is_login_error_displayed()

    def test_Login_true(self):
        logare2 = LoginPage(self.driver)
        logare2.login_true()
        logare3 = HomePage(self.driver)
        logare3.is_shop_page_open()

    def test_Login_Out(self):
        logare3 = LoginPage(self.driver)
        logare3.login_true()
        logout_33 = HomePage(self.driver)
        logout_33.logout()

    def test_sorting_ascending_price(self):
        logare4 = LoginPage(self.driver)
        logare4.login_true()
        sort1 = HomePage(self.driver)
        sort1.sorting_price_asc()

    def test_sorting_descending_price(self):
        logare5 = LoginPage(self.driver)
        logare5.login_true()
        sort2 = HomePage(self.driver)
        sort2.sorting_price_desc()

    def test_adding_item(self):
        logare6 = LoginPage(self.driver)
        logare6.login_true()
        time.sleep(1)
        add1 = HomePage(self.driver)
        time.sleep(1)
        add1.add_to_cart()

    def test_remove_cart_item(self):
        log1 = LoginPage(self.driver)
        log1.login_true()
        add2 = HomePage(self.driver)
        time.sleep(1)
        add2.add_to_cart()
        add2.add_to_cart2()
        time.sleep(1)
        add2.go_to_cart()
        time.sleep(1)
        btnremove = HomePage(self.driver)
        btnremove.remove_from_cart()
        time.sleep(1)
        btnremovecehck = CartPage(self.driver)
        btnremovecehck.check_items_correctly()

    def test_add_and_check_cart_items(self):
        log2 = LoginPage(self.driver)
        log2.login_true()
        time.sleep(1)
        add3 = HomePage(self.driver)
        add3.add_to_cart()
        add3.add_to_cart2()
        time.sleep(1)
        add3.go_to_cart()
        time.sleep(1)
        check1 = CartPage(self.driver)
        check1.check_items_correctly()

    def test_final_price(self):
        log3 = LoginPage(self.driver)
        log3.login_true()
        check1 = HomePage(self.driver)
        check1.add_to_cart()
        check1.add_to_cart2()
        check1.go_to_cart()
        check2 = CartPage(self.driver)
        check2.go_to_info_order()
        time.sleep(1)
        complete_info = CheckoutPage(self.driver)
        complete_info.insert_info()
        complete_info.continue_to_final_step()
        price_final = PayPage(self.driver)
        time.sleep(1)
        price_final.check_total_price()

    def test_back_to_shop_from_cart(self):
        log3 = LoginPage(self.driver)
        log3.login_true()
        time.sleep(1)
        check1 = HomePage(self.driver)
        check1.add_to_cart()
        time.sleep(1)
        check1.go_to_cart()
        check2 = CartPage(self.driver)
        time.sleep(1)
        this_url = self.driver.current_url
        check2.go_to_inventory_page()
        time.sleep(1)
        next_url = self.driver.current_url
        assert next_url != this_url, "URL acelasi"

    def test_place_order(self):
        log_1 = LoginPage(self.driver)
        log_1.login_true()
        order1 = HomePage(self.driver)
        order1.add_to_cart()
        order1.go_to_cart()
        next_step = CartPage(self.driver)
        time.sleep(1)
        next_step.go_to_info_order()
        other_step = CheckoutPage(self.driver)
        other_step.insert_info()
        time.sleep(1)
        other_step.continue_to_final_step()
        time.sleep(1)
        move_forward = PayPage(self.driver)
        move_forward.go_to_to_pay()
        time.sleep(1)
        last_step = PayConfirmationPage(self.driver)
        time.sleep(1)
        last_step.order_succesfully()
