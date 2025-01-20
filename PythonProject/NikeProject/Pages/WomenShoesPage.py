import self
import time

from selenium.webdriver.common.by import By


class womenShoesPage():
    def __init__(self, driver):
        self.driver = driver

    def print_hi(self):
        print("Hi")

        womenPage = self.driver.find_element(By.LINK_TEXT, "Women").click()
        womenShoesPage = self.driver.find_element(By.LINK_TEXT, "Shoes").click()
        womenShoeResults = self.driver.find_element(By.CLASS_NAME, "results__body")
        womenFirstShoe = womenShoeResults.find_element(By.CLASS_NAME, "product-card")
        womenFirstShoePrice = womenFirstShoe.find_element(By.CLASS_NAME, "product-card__price")
        print(f"the price of first women shoe is {womenFirstShoePrice.text}")
