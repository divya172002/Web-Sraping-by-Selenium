# its a good practice to download all the page's html file so that we won't miss any information and then scrape data from that files.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By #By is selector
import time

driver = webdriver.Chrome()
query='laptop'
file=0
for i in range(1,2):

    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=3H1FBBXIL5DZ8&sprefix=laptop%2Caps%2C249&ref=nb_sb_noss_2")
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    # print(elems.text) #gives textual information in cmd itself

    # print(elems.get_attribute('outerHTML'))#it will give you html of that product part

    print(f'{len(elems)} items found')

    for elem in elems:
        # print(elem.text)
        d=elem.get_attribute('outerHTML')
        with open(f"data/{query}_{file}.html","w",encoding="utf-8") as f:
            f.write(d)
            file+=1
            
    time.sleep(1)
driver.close()
