import requests
import bs4
from bs4 import BeautifulSoup


def get_products():
    url = "https://tribuna.uz/"

    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, 'html.parser')

    product_titles = soup.find_all('div', class_='daily-news')

    file_name = 'products.txt'

    with open(file_name, 'w', encoding="utf-8") as file:
        for idx, title in enumerate(product_titles, 1):

            text = title.get_text(strip=True)
            file.write(f"Product {idx}:\n")
            file.write(f"  Title: {text}\n")
            file.write("\n")

    print(f"Ma'lumotlar '{file_name}' fayliga yozildi.")


print(get_products())