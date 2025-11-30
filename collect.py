
from bs4 import BeautifulSoup
import os
import pandas as pd
d={'title':[],'price':[],'link':[]}


for file in os.listdir("data"):
    try:
        with open(f"data/{file}", encoding="utf-8") as f:
            html_doc=f.read()
        soup = BeautifulSoup(html_doc,'html.parser')
        t=soup.find('h2')
        title=t.get_text()
        

        for a in soup.find_all("a"):
            if a and a.find("h2"):     # Check a exists + contains h2
                link = "https://www.amazon.in/"+a.get("href")   #domain name gives active link
                if link:
                    pass

        p=soup.find('span',attrs={'class':'a-price-whole'})
        price=p.get_text()

        d['title'].append(title)
        d['price'].append(price)
        d['link'].append(link)
        # print(title,link,price)
    
        # break #if not used break it will give title of every product/just for checking one product
    except Exception as e:
        print(e)
# print(soup.prettify()) #it will give hltm list in cmdpmt

df=pd.DataFrame(data=d)
df.to_excel('data.xlsx')