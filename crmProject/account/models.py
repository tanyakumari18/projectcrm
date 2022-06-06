from django.db import models


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.BigIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.first_name


class Product(models.Model):
    PRODUCTS_CHOICE = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
        ('Anywhere', 'Anywhere')
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    created_date = models.DateField(auto_now=True, null=True, blank=True)
    category = models.CharField(choices=PRODUCTS_CHOICE, max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
        ('Outfordelivery', 'Outfordelivery')
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=100, null=True, blank=True)
    created_date = models.DateField(auto_now=True, null=True, blank=True)
