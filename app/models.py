from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Warehouse(models.Model):
    name = models.CharField(max_length=50)
    shop = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)            # FK
    def __str__(self) -> str:
        return f"{self.name}, {self.shop}({self.address})"


class Product(models.Model):
    title = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    amount  = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    units = models.CharField(max_length=50)
    income_date = models.DateField(auto_now_add=True, null=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True)            # FK
    def __str__(self) -> str:
        return f"{self.title}, {self.brand}"

class Client(models.Model):
    name = models.CharField(max_length=30)
    shop_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    debt = models.PositiveSmallIntegerField(default=0)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True)            # FK
    def __str__(self) -> str:
        return f"{self.name}, {self.shop_name}({self.address})"


class Statistics(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True)
    amount = models.PositiveSmallIntegerField(default=1)
    total = models.PositiveSmallIntegerField()
    payed = models.PositiveSmallIntegerField()
    debt = models.PositiveSmallIntegerField(default=0)
    def __str__(self) -> str:
        return f"{self.product} --- {self.warehouse}11"
    