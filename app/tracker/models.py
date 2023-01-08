from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class Product(models.Model):
    asin = models.CharField(max_length=20, unique = True, primary_key=True, default='ASIN000')
    title = models.CharField(max_length=256)
    url = models.URLField(max_length=512, null=True)
    product_image = models.URLField(max_length=512)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    added_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} available currently @ {self.sell_price} added on {self.added_at} last modified {self.last_modified} '

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True, primary_key=True)

    USERNAME_FIELD = 'email'