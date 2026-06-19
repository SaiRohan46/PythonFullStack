#Hello day-29
'''
import pandas as pd
import bs4
data={
    'Dish':['VeBiriyani','CFPBiriyani','CMBiriyani','CKBiriyani','CLBiriyani',
            'SchezwanVeg','SChezwanChick','VegKalmi'],
    'Price':['299','309','319','329','339','349','359','369']
    }
df=pd.DataFrame(data)
df['Price']=pd.to_numeric(df['Price'])
top_5=df.nlargest(5,'Price')
sort_=df.sort_values(by='Dish')
print(sort_)
print(top_5)
print(df)
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re
URL = "http://books.toscrape.com/"
try:
    response = requests.get(URL)
    response.encoding = "utf-8"
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error :", e)
    exit()
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")
book_names = []
book_prices = []
for book in books:
    name = book.h3.a["title"]
    price_text = book.find("p", class_="price_color").text
    price = float(re.findall(r"\d+\.\d+", price_text)[0])
    book_names.append(name)
    book_prices.append(price)
df = pd.DataFrame({
"Book_Name": book_names,
"Price": book_prices
})
print(df)
print(df.shape)
print(df.head())
df.to_csv("books_data.csv", index=False)
print("CSV File Saved Successfully!")
plt.figure(figsize=(10,5))
plt.bar(
df["Book_Name"][:10],
df["Price"][:10]
)
plt.xticks(rotation=90)
plt.xlabel("Book Names")
plt.ylabel("Price (£)")
plt.title("Top 10 Book Prices")
plt.tight_layout()
plt.show()





















