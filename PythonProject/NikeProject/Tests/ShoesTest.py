
from PythonProject.NikeProject.Pages.MenShoesPage import menShoesPage
from PythonProject.NikeProject.Pages.WomenShoesPage import womenShoesPage
from PythonProject.NikeProject.Tests.NikeBase import NikeBase

base = NikeBase()
driver = base.selenium_start()
womenShoesPage = womenShoesPage(driver)
men_shoes = menShoesPage(driver)
#low_price = lowPrice(driver)

driver.get("https://www.nike.com/us/")
men_price = men_shoes.First_men_shoe()
women_price = womenShoesPage.First_women_shoe()

lower_price = min(women_price,men_price)
print(f"the lowest price is {lower_price}")

price_without_dollar = lower_price.replace("$", "")
price_without_dollar = float(price_without_dollar)
final_price = int(price_without_dollar)

assert price_without_dollar < 200, f"Test failed: The price {final_price}$ is above 200$"

print(f"Test passed: The price {final_price}$ is under 200$")


#low_price.compare_prices()



base.selenium_end(driver)
