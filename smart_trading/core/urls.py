from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-product/', views.add_product, name='add_product'),
    path('purchase/', views.purchase_product, name='purchase_product'),
    path('sell/', views.sell_product, name='sell_product'),
    path('view-purchases/', views.view_purchases, name='view_purchases'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

]


    

