from django.shortcuts import render, redirect
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

        if 'error' in product_data:
            return HttpResponseBadRequest('Error parsing product site')

        new_product = Product(**product_data)
        new_product.save()

        return redirect('/products')

    return render(request, 'index.html')


def view_product(request, asin):
    try:
        product = Product.objects.filter(asin__contains=asin)
        return HttpResponse(product)

    except ObjectDoesNotExist:
        return HttpResponseBadRequest({'error': 'Wrong ASIN'})


def list_all_products(request):
    products_list = Product.objects.order_by('-timestamp')

    return render(request, template_name='products_list.html', context={'list': products_list})
