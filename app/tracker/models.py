from django.db import models
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
    def num_products(self):
        return self.product_set.count()

    def __str__(self):
        return f"{self.user}'s cart containing {self.num_products} products"

class Product(models.Model):
    asin = models.CharField(max_length=20, unique = True, primary_key=True, default='ASIN000')
    title = models.CharField(max_length=256)
    url = models.URLField(max_length=512, null=True)
    product_image = models.URLField(max_length=512)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    added_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title} available currently @ {self.sell_price} added on {self.added_at} last modified {self.last_modified} '
