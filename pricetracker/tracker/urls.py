from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.list_all_products, name='product_list'),
    path('product/<str:asin>', views.view_product, name='view_product'),
]