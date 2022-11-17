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
        return render(request, 'product_focus.html', context=product_data)

    return render(request, 'index.html')


def list_all_products(request):
    return HttpResponse(Product.objects.all())