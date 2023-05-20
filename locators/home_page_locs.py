from selenium.webdriver.common.by import By


class HomePageLocators:
    BUTTON_SORT = (By.CLASS_NAME, 'product_sort_container')
    BUTTON_SORT_PRICE_LH = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[3]')
    BUTTON_SORT_PRICE_HL = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[4]')
    PRICES = (By.CLASS_NAME, "inventory_item_price")
    NAMES = (By.CLASS_NAME, "inventory_item_name")
    BUTTON_SHOP_CART = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    BUTTON_ADD_TO_CART_backpack = (By.ID, 'add-to-cart-sauce-labs-backpack')
    BUTTON_REMOVE_FROM_CART_backpack = (By.ID, 'remove-sauce-labs-backpack')
    BUTTON_ADD_TO_CART_tshirt = (By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')
    BUTTON_REMOVE_FROM_CART_tshirt = (By.ID, 'remove-test.allthethings()-t-shirt-(red)')
    BUTTON_ADD_TO_CART_bike = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    BUTTON_REMOVE_FROM_CART_bike = (By.ID, 'remove-sauce-labs-bike-light')
    BUTTON_MENU_LIST = (By.ID, 'react-burger-menu-btn')
    BUTTON_MENU_ALL_ITEMS = (By.ID, 'inventory_sidebar_link')
    BUTTON_MENU_ABOUT = (By.ID, 'about_sidebar_link')
    BUTTON_MENU_LOGOUT = (By.ID, 'logout_sidebar_link')
    BUTTON_MENU_RESET_STATE = (By.ID, 'reset_sidebar_link')
    BUTTON_SHOP_CART_ITEMS_NUMBER = (By.CLASS_NAME, 'shopping_cart_badge')
