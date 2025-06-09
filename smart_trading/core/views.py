from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Product, Purchase
from .forms import ProductForm, PurchaseForm, SaleForm
from .decorators import group_required

# Dashboard view - for Admin & Staff
@login_required
@group_required('Admin', 'Staff')
def dashboard(request):
    products = Product.objects.all()
    return render(request, 'core/dashboard.html', {'products': products})

# Add a product - Admin only
@login_required
@group_required('Admin')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully.")
            return redirect('dashboard')
    else:
        form = ProductForm()
    return render(request, 'core/add_product.html', {'form': form})

# Purchase a product - Admin or Staff
@login_required
@group_required('Admin', 'Staff')
def purchase_product(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product purchased successfully.")
            return redirect('dashboard')
    else:
        form = PurchaseForm()
    return render(request, 'core/purchase.html', {'form': form})

# Sell a product - Admin or Staff
@login_required
@group_required('Admin', 'Staff')
def sell_product(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product sold successfully.")
            return redirect('dashboard')
    else:
        form = SaleForm()
    return render(request, 'core/sell.html', {'form': form})

# View purchases - Admin or Staff
@login_required
@group_required('Admin', 'Staff')
def view_purchases(request):
    purchases = Purchase.objects.select_related('product').order_by('-purchase_date')
    return render(request, 'core/view_purchases.html', {'purchases': purchases})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')
