from selenium.webdriver.common.by import By


class PayPageLocators:
    BUTTON_FINISH = (By.ID, 'finish')
    BUTTON_CANCEL = (By.ID, 'cancel')
    TOTAL_AMOUNT_TEXT = (By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]')
    SUBTOTAL_AMOUNT_TEXT = (By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
    TOTAL_TAX = (By.CLASS_NAME, 'summary_tax_label')
