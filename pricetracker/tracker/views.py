from django.shortcuts import render

import requests
from bs4 import BeautifulSoup

# Create your views here.
def get_product_details(url):
    headers = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    page = resp.text

    soup = BeautifulSoup(page, 'html.parser')

    # Get the product details from the product page
    title = soup.find('h1', attrs={'id':'title'}).text.strip()
    
    current_price = soup.find('span', attrs={'class': 'priceToPay'}).find('span', attrs={'class':'a-offscreen'}).text
    curr_price_decimal = float(current_price[1:])

    mrp = soup.find('span', attrs={'class': 'a-text-price'}).find('span', attrs={'class':'a-offscreen'}).text
    mrp_decimal = float(mrp[1:])

    return 
    {
        'title': title,
        'current_price': curr_price_decimal,
        'list_price': mrp_decimal
    }


