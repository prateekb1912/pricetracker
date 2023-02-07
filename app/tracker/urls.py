from django.urls import path
import django.contrib.auth.views as authviews

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.list_all_products, name='product_list'),
    path('product/<str:id>', views.view_product, name='view_product'),
    path('delete/<str:id>', views.delete_product, name='delete_product'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
]