from django.db import models

# Create your models here.
class Product(models.Model):
    asin = models.CharField(max_length=20, unique = True, primary_key=True, default='ASIN000')
    title = models.CharField(max_length=256)
    url = models.URLField(max_length=512, null=True)
    product_image = models.URLField(max_length=512)
    list_price = models.DecimalField(max_digits=10, decimal_places=2)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} @ {self.sell_price}'