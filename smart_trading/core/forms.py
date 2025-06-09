from django import forms
from .models import Product, StockLog

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'unit', 'purchase_price', 'selling_price']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = StockLog
        fields = ['product', 'quantity']
    
    def save(self, commit=True):
        log = super().save(commit=False)
        log.action = 'PURCHASE'
        if commit:
            log.save()
            log.product.quantity += log.quantity
            log.product.save()
        return log

class SaleForm(forms.ModelForm):
    class Meta:
        model = StockLog
        fields = ['product', 'quantity']

    def save(self, commit=True):
        log = super().save(commit=False)
        log.action = 'SALE'
        if commit:
            log.save()
            log.product.quantity -= log.quantity
            log.product.save()
        return log
    
from django import forms
from .models import Purchase

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = [
            'product',
            'quantity',
            'unit',
            'purchase_price',
            'expected_selling_price',
            'return_date',
        ]
        widgets = {
            'return_date': forms.DateInput(attrs={'type': 'date'}),
        }

