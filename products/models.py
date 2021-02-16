from django.db import models
from accounts.models import UserAccounts

class Category(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    added_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ['name']
    def __str__(self):
        return self.name

class AddCart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(UserAccounts, on_delete=models.CASCADE)
    def __str__(self):
        return self.name