from django.shortcuts import render
from django.http import HttpResponse

import logging

from .models import Product
from scrapers.amazon_in import get_product_details

logger = logging.getLogger(__name__)

def index(request):
    if request.method == 'POST':
        post_data = request.POST
        url = post_data['inputURL']
        
        product_data = get_product_details(url)
        
        new_product = Product(**product_data)
        new_product.save();

    return render(request, 'index.html')


def list_all_products(request):
    return HttpResponse(Product.objects.all())