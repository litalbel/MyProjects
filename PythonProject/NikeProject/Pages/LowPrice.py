from PythonProject.NikeProject.Pages.MenShoesPage import menShoesPage
from PythonProject.NikeProject.Pages.WomenShoesPage import womenShoesPage
from PythonProject.NikeProject.Tests.NikeBase import NikeBase

import self
import time

from selenium.webdriver.common.by import By

#print the lowest price between women's shoes and men's shoes

class loePrice():
    def __init__(self, driver):
        self.driver = driver

    def print_hi(self):
        print("Hi")

        womenFirstShoe = self.driver
        firstWomenShoe = womenFirstShoe.find_element(By.CLASS_NAME, "product-card__price")
        price_women = firstWomenShoe.text

        menFirstShoe = self.driver
        firstMenShoe = menFirstShoe.find_element(By.CLASS_NAME, "product-card__price")
        price_men = firstMenShoe.text

        lower_number = min(price_women, price_men)

        print(f"the lowest price is {lower_number}")
