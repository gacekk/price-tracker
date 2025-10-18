import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.de/dp/B01LXY99X4'
THRESHOLD = 100.00  # example price threshold in EUR
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def get_price(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    price_text = soup.find('span', {'id': 'priceblock_ourprice'})
    if price_text:
        price = float(price_text.text.replace('€', '').replace(',', '.').strip())
        return price
    return None

def notify(price):
    if price <= THRESHOLD:
        print(f"Alert: Price dropped to {price} EUR!")

if __name__ == "__main__":
    price = get_price(URL)
    if price is not None:
        notify(price)
    else:
        print("Failed to retrieve price.")
