from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=20)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class StockLog(models.Model):
    ACTION_CHOICES = (
        ('PURCHASE', 'Purchased'),
        ('SALE', 'Sold'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    quantity = models.IntegerField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.product.name} - {self.action} - {self.quantity}"

class RawMaterial(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
from django.db import models
from .models import Product

class Purchase(models.Model):
    UNIT_CHOICES = [
        ('kg', 'Kilogram'),
        ('pcs', 'Pieces'),
        ('litre', 'Litre'),
        ('box', 'Box'),
        ('bag', 'Bag'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES, default='pcs')
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    expected_selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} {self.unit}"
