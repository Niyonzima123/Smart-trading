from django.contrib import admin
from .models import Product, StockLog, RawMaterial

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'unit', 'purchase_price', 'selling_price', 'created_at']
    search_fields = ['name']

@admin.register(StockLog)
class StockLogAdmin(admin.ModelAdmin):
    list_display = ['product', 'action', 'quantity', 'date']
    list_filter = ['action', 'date']
    search_fields = ['product__name']

@admin.register(RawMaterial)
class RawMaterialAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'unit']
    search_fields = ['name']
