"""
🌐 URL patterns برای اپلیکیشن core
🏢 مسیریابی عملیات اصلی کسب‌وکار
"""

from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # 📊 داشبوردهای مخصوص هر نقش
    path('admin-dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('finance-dashboard/', views.finance_dashboard_view, name='finance_dashboard'),
    
    # 📦 مدیریت موجودی
    path('inventory/', views.inventory_list_view, name='inventory_list'),
    
    # 📋 مدیریت سفارشات
    path('orders/', views.orders_list_view, name='orders_list'),
    
    # 👥 مدیریت مشتریان
    path('customers/', views.customers_list_view, name='customers_list'),
    
    # 💰 مدیریت مالی
    path('finance/', views.finance_overview_view, name='finance_overview'),
] 