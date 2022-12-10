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
        time.sleep(5)

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

        asin = soup.find('table', attrs={'id': 'productDetails_detailBullets_sections1'})
        if asin:
            asin = asin.find('td', attrs={'class': 'prodDetAttrValue'}).text.strip()
        else:
            asin = soup.select('#rpi-attribute-book_details-isbn10')[0]
            asin = asin.select('span')[-1].text.strip()
            logger.warning(asin)

        logger.warning(f"ASIN: {asin}")

        landingImg = soup.find('div', attrs={'id': 'main-image-container'}).find('img').get('src')
        logger.warning(f"Image has been scraped: {landingImg}")

        return {
            'asin': asin,
            'title': title,
            'url': url,
            'sell_price': curr_price_decimal,
            'product_image': landingImg
            }

    except Exception as e:
        logger.warning(e)
        return {
            'error': 'Invalid URL!'
        }