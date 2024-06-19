from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    USER_ROLE_CHOICES = (
        ('admin', 'admin'),
        ('seller', 'seller'),
        ('client', 'client'),
    )

    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True, default='default.jpg')
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    user_role = models.CharField(max_length=10, choices=USER_ROLE_CHOICES, default='client')

    def save(self, *args, **kwargs):

        if not self.user_role:
            self.user_role = 'client'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username




class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/', null=True)

    def __str__(self):
        return self.name


class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @property
    def total_price(self):
        return self.price * self.quantity


class Cart(models.Model):
    books = models.OneToOneField(Books, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


    def __str__(self):
        return self.books.name





