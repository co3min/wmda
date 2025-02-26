### **Exercise 2: Web Scraping a Product Listings Page**
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"


response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("div", class_="thumbnail")

data = {
"name": [], "price":[]
}

for product in products[:10]: 
    name = product.find('a', class_='title')['title'].strip()
    price = product.find("h4", class_="price").text.strip()
    data["name"].append(name)
    data["price"].append(price)

df = pd.DataFrame(data=data)

df.to_csv("products.csv", index=False)