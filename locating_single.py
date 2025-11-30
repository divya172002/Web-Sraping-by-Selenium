from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By #By is selector
import time

driver = webdriver.Chrome()
query='laptop'
driver.get(f"https://www.amazon.in/s?k={query}&crid=3H1FBBXIL5DZ8&sprefix=laptop%2Caps%2C249&ref=nb_sb_noss_2")
elem = driver.find_element(By.CLASS_NAME, "puis-card-container")
# print(elem.text) #gives textual information in cmd itself

print(elem.get_attribute('outerHTML'))#it will give you html of that product part

time.sleep(10)
driver.close()

