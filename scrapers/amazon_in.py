import logging
import time

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

def get_product_details(url):
    headers = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    }
    
    try:
        resp = requests.get(url, headers=headers)
        time.sleep(2)

        page = resp.text

        soup = BeautifulSoup(page, 'html.parser')

        title = soup.find('span', attrs={'id':'productTitle'}).text.strip()
        logger.warning(f"Product: {title}")
        

        current_price = soup.find('span', attrs={'class': 'priceToPay'})

        if current_price:
            current_price.select('.a-offscreen').text
        else :
            current_price = soup.select('#price')[0].text

        current_price = current_price.replace(',', '')
        curr_price_decimal = float(current_price[1:])
        logger.warning(f"Available @ {current_price}")

        mrp = soup.find('span', attrs={'class': 'basisPrice'})

        if mrp:
            mrp = mrp.find('span', attrs={'class':'a-offscreen'}).text
        else:
            mrp = soup.find('span', attrs={'id': 'listPrice'}).text

        mrp = mrp.replace(',', '')
        mrp_decimal = float(mrp[1:])
        logger.warning(f"MRP: {mrp}")


        asin = soup.find('table', attrs={'id': 'productDetails_detailBullets_sections1'}).find('td', attrs={'class': 'prodDetAttrValue'}).text
        asin = asin.strip()
        logger.warning(f"ASIN: {asin}")

        landingImg = soup.find('div', attrs={'id': 'main-image-container'}).find('img').get('src')
        logger.warning(f"Image has been scraped: {landingImg}")

        return {
            'asin': asin,
            'title': title,
            'url': url,
            'list_price': mrp_decimal,
            'sell_price': curr_price_decimal,
            'product_image': landingImg
            }

    except Exception as e:
        logger.warning(e)
        return {
            'error': 'Invalid URL!'
        }