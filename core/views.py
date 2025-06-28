"""
🏢 ویوهای اصلی کسب‌وکار - HomayOMS
📊 داشبوردها و عملیات اصلی سیستم
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from accounts.permissions import check_user_permission


@login_required
@check_user_permission('is_admin')
def admin_dashboard_view(request):
    """📊 داشبورد مدیریت"""
    context = {
        'title': '📊 داشبورد مدیریت',
        'user': request.user,
    }
    return render(request, 'core/admin_dashboard.html', context)


@login_required  
@check_user_permission('is_finance')
def finance_dashboard_view(request):
    """💰 داشبورد مالی"""
    context = {
        'title': '💰 داشبورد مالی',
        'user': request.user,
    }
    return render(request, 'core/finance_dashboard.html', context)


@login_required
@permission_required('accounts.manage_inventory', raise_exception=True)
def inventory_list_view(request):
    """📦 لیست موجودی"""
    context = {'title': '📦 مدیریت موجودی'}
    return render(request, 'core/inventory_list.html', context)


@login_required
@permission_required('accounts.manage_orders', raise_exception=True)
def orders_list_view(request):
    """📋 لیست سفارشات"""
    context = {'title': '📋 مدیریت سفارشات'}
    return render(request, 'core/orders_list.html', context)


@login_required
@permission_required('accounts.manage_customers', raise_exception=True)
def customers_list_view(request):
    """👥 لیست مشتریان"""
    context = {'title': '👥 مدیریت مشتریان'}
    return render(request, 'core/customers_list.html', context)


@login_required
@check_user_permission('is_finance')
def finance_overview_view(request):
    """💰 نمای کلی مالی"""
    context = {'title': '💰 نمای کلی مالی'}
    return render(request, 'core/finance_overview.html', context)
