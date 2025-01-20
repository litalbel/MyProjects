from PythonProject.NikeProject.Pages.LowPrice import loePrice
from PythonProject.NikeProject.Pages.MenShoesPage import menShoesPage
from PythonProject.NikeProject.Pages.WomenShoesPage import womenShoesPage
from PythonProject.NikeProject.Tests.NikeBase import NikeBase

base = NikeBase()
driver = base.selenium_start()
womenShoesPage = womenShoesPage(driver)
men_shoes = menShoesPage(driver)
low_price = loePrice(driver)

driver.get("https://www.nike.com/us/")
womenShoesPage.print_hi()
men_shoes.print_hi()
low_price.print_hi()

base.selenium_end(driver)
