import unittest
from selenium import webdriver


class BaseTests(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.saucedemo.com/')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
