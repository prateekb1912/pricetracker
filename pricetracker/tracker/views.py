from django.shortcuts import render
from django.http import HttpResponse

import requests
import json
import time
import logging

from bs4 import BeautifulSoup

from .models import Product

logger = logging.getLogger(__name__)

# Create your views here.
def get_product_details(url):
    headers = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    }
    
    try:
        resp = requests.get(url, headers=headers)
        time.sleep(2)

        page = resp.text

        soup = BeautifulSoup(page, 'html.parser')
        # Get the product details from the product page

        title = soup.find('span', attrs={'id':'productTitle'}).text.strip()
        logger.warning(f"Product: {title}")
        
        current_price = soup.find('span', attrs={'class': 'priceToPay'}).find('span', attrs={'class':'a-offscreen'}).text
        current_price = current_price.replace(',', '')
        curr_price_decimal = float(current_price[1:])
        logger.warning(f"Available @ {current_price}")

        mrp = soup.find('span', attrs={'class': 'basisPrice'}).find('span', attrs={'class':'a-offscreen'}).text
        mrp = current_price.replace(',', '')
        mrp_decimal = float(mrp[1:])
        logger.warning(f"MRP: {mrp}")


        asin = soup.find('table', attrs={'id': 'productDetails_detailBullets_sections1'}).find('td', attrs={'class': 'prodDetAttrValue'}).text
        logger.warning(f"ASIN: {asin}")

        landingImg = soup.find('div', attrs={'id': 'main-image-container'}).find('img').get('src')
        logger.warning(f"Image has been scraped: {landingImg}")

        return {
            'asin': asin,
            'title': title,
            'currentPrice': curr_price_decimal,
            'listPrice': mrp_decimal,
            'imageURL': landingImg
            }

    except Exception:
        return {
            'error': 'Invalid URL!'
        }

def index(request):
    if request.method == 'POST':
        post_data = request.POST
        url = post_data['inputURL']

        logger.warning("HHDJHJD")

        product_data = get_product_details(url)
        logger.warning(product_data)

        # return HttpResponse(json.dumps(product_data))

        return render(request, 'product_focus.html', context = {
            'title': product_data['title'],
            'listPrice': product_data['listPrice'],
            'currentPrice': product_data['currentPrice'],
            'imageURL': product_data['imageURL']
            })


    return render(request, 'index.html')


def list_all_products(request):
    return HttpResponse(Product.objects.all())