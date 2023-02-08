from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name='', password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            **extra_fields
        )        

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name, last_name='', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, first_name, last_name, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=80, default='')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']


    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True

class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    
    @property
    def cart_count(self):
        return self.products.count()

    @property 
    def cart_value(self):
        return self.products.all().aggregate(Sum('price'))['price__sum']

    def __str__(self):
        return f"{self.user}'s cart containing {self.cart_count} products totalling Rs. {self.cart_value}"

class Product(models.Model):
    SITE_CHOICES = [
        ('AM', 'amazon'),
        ('FL', 'flipkart'),
        ('TQ', 'tatacliq'),
        ('MY', 'myntra'),
        ('NA', 'others')
    ]

    id = models.CharField(max_length=20, unique = True, primary_key=True, default='ASIN000')
    title = models.CharField(max_length=256)
    url = models.URLField(max_length=512, null=True)
    image_url = models.URLField(max_length=512)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    site = models.CharField(max_length=40, default='NA')

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f'{self.title} available currently @ {self.price} added on {self.added_at} last modified {self.last_modified} '
