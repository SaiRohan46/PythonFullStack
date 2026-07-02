'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import re
from bs4 import BeautifulSoup
url="https://books.toscrape.com/"
try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text,"html.parser")
    books = []
    for article in soup.find_all("article",class_="product_pod"):
        title = article.h3.a["title"]
        price = article.find("p",class_="price_color").text
        books.append({"Title": title, "Price": price})
    df = pd.DataFrame(books)
    print(df.head())
    df["Price"] = (
        df["Price"]
        .str.replace("Â","", regex=False)  
        .str.replace("£","", regex=False)   
        .astype(float)                       
    )
    plt.figure(figsize=(12,6)) 
    plt.bar(df["Title"],df["Price"],color="skyblue", edgecolor="black")
    plt.xlabel("Price (£)")
    plt.ylabel("Number of Books")
    plt.title("Book Price Distribution")
    plt.xticks(rotation=90, ha="center")
    plt.show()
except Exception as e:
    print("Error occurred:", e)

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
plt.bar(df["Book_Name"][:10],df["Price"][:10])
plt.xticks(rotation=90)
plt.xlabel("Book Names")
plt.ylabel("Price (£)")
plt.title("Top 10 Book Prices")
plt.show()