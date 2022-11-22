from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist
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


def view_product(request, asin):
    try:
        product = Product.objects.filter(asin__contains=asin)
        return HttpResponse(product)

    except ObjectDoesNotExist:
        return HttpResponseBadRequest({'error': 'Wrong ASIN'})

def list_all_products(request):
    products_list = Product.objects.order_by('-date_added')
    
    return render(request, template_name='products_list.html', context={'list':products_list})