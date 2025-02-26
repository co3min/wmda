# [Scraping product prices from an e-commerce website.]

### **Exercise 1: Extracting and Cleaning Data from an API**
import requests
import pandas as pd
import re

cities = ["New York", "London", "Tokyo", "Paris", "Berlin"]


url = f"https://wttr.in/{cities[2]}?format=%C+%t"

response = requests.get(url)
data = response.text

array = data.split()

array[1] = re.sub(r'\D', '', array[1])

data = {
    "City": [cities[2]],
    "Temperature": [array[1]],
    "Weather Condition": [array[0]]
}

df = pd.DataFrame(data)

df.to_csv('out_Weather.csv', index=False)
