class BasePage:
    URL = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        self.driver = driver

    def back(self):
        self.driver.back()
