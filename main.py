from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By #By is selector
import time

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")#search in search bar
elem.send_keys(Keys.RETURN)#keys.RETURN for enter click or returning
assert "No results found." not in driver.page_source #this should not be in result ow we will get aeertion error
time.sleep(10)
driver.close()