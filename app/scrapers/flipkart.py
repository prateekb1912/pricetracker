import logging
import random
import re
import time

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


def get_product_details(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
    }
    try:
        product_id = re.findall(r"itm(\w+)", url)[0]

        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.content, "html.parser")

        title = soup.find("h1").text.strip()
        logger.warning(title)

        price = soup.find("div", attrs={"class": "_16Jk6d"}).text
        logger.warning(price)

        price_decimal = int(price.replace("₹", "").replace(",", ""))
        logger.warning(price_decimal)

        product_img = soup.find("img", attrs={"class": ["_396cs4", "_2r_T1I"]}).get(
            "src"
        )

        return {
            "id": product_id,
            "title": title,
            "url": url,
            "price": price_decimal,
            "image_url": product_img,
            "site": "flipkart",
        }

    except Exception as e:
        logger.warning(e)
        return {"error": "Invalid URL!"}
