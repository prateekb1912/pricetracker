from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

import requests
import json
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
    current_price = current_price.replace(',', '')
    curr_price_decimal = float(current_price[1:])

    mrp = soup.find('span', attrs={'class': 'a-text-price'}).find('span', attrs={'class':'a-offscreen'}).text
    mrp = current_price.replace(',', '')
    mrp_decimal = float(mrp[1:])

    asin = soup.find('table', attrs={'id': 'productDetails_detailBullets_sections1'}).find('td', attrs={'class': 'prodDetAttrValue'}).text

    return {
        'asin': asin,
        'title': title,
        'current_price': curr_price_decimal,
        'list_price': mrp_decimal
        }

def get_url(request):
    url = 'https://www.amazon.in/dp/B09NVPSCQT'

    data = get_product_details(url)

    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

@require_http_methods(["GET", "POST"])
def index(request):
    print(request.method == 'POST')
    if request.method == 'POST':
        print(request.GET)

    return render(request, 'index.html')