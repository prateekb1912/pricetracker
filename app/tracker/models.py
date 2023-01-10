from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name="", password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name
        )        

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name, last_name="", password=None):
        user = self.model(
            email,
            password = password,
            first_name = first_name,
            last_name = last_name
        )        

        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=64, null=False, blank=True)
    last_name = models.CharField(max_length=80, null=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']


    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin


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
