from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('products', views.list_all_products)
]