import logging
import random
import time

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


def get_product_details(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
    }
    # proxies_list = ["128.199.109.241:8080","113.53.230.195:3128","125.141.200.53:80","125.141.200.14:80","128.199.200.112:138","149.56.123.99:3128","128.199.200.112:80","125.141.200.39:80","134.213.29.202:4444"]
    # proxies = {'https': random.choice(proxies_list)}

    try:
        resp = requests.get(url, headers=headers)
        time.sleep(5)

        logger.warning(resp)

        page = resp.content

        soup = BeautifulSoup(page, "html.parser")

        logger.warning(soup.prettify())

        title = soup.find("span", attrs={"id": "productTitle"}).text.strip()
        logger.warning(f"Product: {title}")

        current_price = soup.find("span", attrs={"class": "priceToPay"})

        if current_price:
            current_price = current_price.find(
                "span", attrs={"class": "a-offscreen"}
            ).text
        else:
            current_price = soup.select("#price")[0].text

        current_price = current_price.replace(",", "")
        curr_price_decimal = float(current_price[1:])
        logger.warning(f"Current Price: {curr_price_decimal}")

        asin = soup.find("div", {"data-csa-c-content-id": "imageBlock"})
        logger.warning(f"ASIN: {asin}")

        if asin:
            asin = asin.find("td", attrs={"class": "prodDetAttrValue"}).text.strip()
            logger.warning(f"ASIN: {asin}")

        else:
            asin = soup.select("#rpi-attribute-book_details-isbn10")[0]
            logger.warning(f"ASIN: {asin}")
            asin = asin.select("span")[-1].text.strip()
            logger.warning(f"ASIN: {asin}")

        logger.warning(f"ASIN: {asin}")

        productImage = soup.find("img", attrs={"id": "landingImage"})

        logger.warning(productImage)

        if not productImage:
            productImage = soup.find("img", attrs={"id": "imgBlkFront"})

        logger.warning(productImage)

        productImage = productImage.get("src")

        imgURLSplit = productImage.split(".")
        del imgURLSplit[-2]

        productImageURL = ".".join(imgURLSplit)

        # logger.warning(f"Image has been scraped: {landingImg}")

        return {
            "id": asin,
            "title": title,
            "url": url,
            "price": curr_price_decimal,
            "image_url": productImageURL,
        }

    except Exception as e:
        logger.warning(e)
        return {"error": "Invalid URL!"}
