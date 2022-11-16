from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('product/<str:url>', views.get_product_details),
    path('products', views.list_all_products)
]