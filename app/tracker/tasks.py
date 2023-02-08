from celery import shared_task
from datetime import datetime
from scrapers import amazon_in, flipkart
from .models import Product

@shared_task(name='print_msg')
def print_msg():
    print("Celery Beat is working!")

@shared_task(name='current_time')
def print_time():
    now = datetime.now()
    print(f"Current time: {now.strftime('%H:%M:%S')}")

@shared_task(name='update_products')
def run_product_scraper():
    for product in Product.objects.all():

        if product.site == 'AM':
            updated_product_details = amazon_in.get_product_details(product.url)
        elif product.site == 'FL':
            updated_product_details = amazon_in.get_product_details(product.url)

        if updated_product_details['sell_price'] < float(product.sell_price):
            print(f"Discount {float(product.sell_price) - updated_product_details['sell_price']} for {product.title}")

            product.sell_price = updated_product_details['sell_price']
            product.save()