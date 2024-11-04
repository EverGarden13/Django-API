from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_items = models.ManyToManyField(MenuItem)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')])
    delivery_crew = models.ForeignKey(User, related_name='delivery_crew', on_delete=models.SET_NULL, null=True, blank=True)

class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()