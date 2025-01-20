import self
import time

from selenium.webdriver.common.by import By


class menShoesPage():
    def __init__(self, driver):
        self.driver = driver

    def print_hi(self):
        print("Hi")

        menPage = self.driver.find_element(By.LINK_TEXT, "Men").click()
        menShoesPage = self.driver.find_element(By.LINK_TEXT, "Shoes").click()
        menShoeResults = self.driver.find_element(By.CLASS_NAME, "results__body")
        menFirstShoe = menShoeResults.find_element(By.CLASS_NAME, "product-card")
        menFirstShoePrice = menFirstShoe.find_element(By.CLASS_NAME, "product-card__price")
        print(f"the price of first men shoe is {menFirstShoePrice.text}")
