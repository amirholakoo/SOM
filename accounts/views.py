"""
👥 ویوهای مدیریت کاربران و نقش‌ها - HomayOMS
🔐 شامل لاگین، خروج، مدیریت کاربران و کنترل دسترسی
🎯 با تأکید بر امنیت و تجربه کاربری بهینه
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q
import json

from .models import User, UserSession


def login_view(request):
    """🔐 صفحه ورود اصلی با 4 گزینه مختلف"""
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')
    
    return render(request, 'accounts/login.html')


def staff_login_view(request):
    """👥 ورود کارمندان (Super Admin, Admin, Finance)"""
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')
        
        # بررسی نقش انتخاب شده
        valid_staff_roles = [
            User.UserRole.SUPER_ADMIN,
            User.UserRole.ADMIN, 
            User.UserRole.FINANCE
        ]
        
        if role not in valid_staff_roles:
            messages.error(request, '❌ نقش انتخاب شده نامعتبر است')
            return render(request, 'accounts/staff_login.html')
        
        user = authenticate(request, username=username, password=password)
        if user and user.status == User.UserStatus.ACTIVE and user.role == role:
            login(request, user)
            role_names = {
                User.UserRole.SUPER_ADMIN: 'مدیر ارشد',
                User.UserRole.ADMIN: 'ادمین',
                User.UserRole.FINANCE: 'مالی'
            }
            messages.success(request, f'🎉 خوش آمدید {role_names[role]} {user.get_full_name() or user.username}!')
            return redirect('accounts:dashboard')
        else:
            messages.error(request, '❌ نام کاربری، رمز عبور یا نقش اشتباه است')
    
    return render(request, 'accounts/staff_login.html')


def customer_login_view(request):
    """🔵 ورود مشتریان با احراز هویت SMS"""
    if request.user.is_authenticated:
        if request.user.is_customer():
            return redirect('accounts:customer_dashboard')
        else:
            return redirect('accounts:dashboard')
    
    if request.method == 'POST':
        phone = request.POST.get('phone')
        
        # بررسی شماره تلفن
        if not phone or not phone.startswith('09'):
            messages.error(request, '❌ شماره تلفن معتبر وارد کنید')
            return render(request, 'accounts/customer_login.html')
        
        # بررسی وجود کاربر با این شماره تلفن
        try:
            user = User.objects.get(phone=phone, role=User.UserRole.CUSTOMER)
            if user.status != User.UserStatus.ACTIVE:
                messages.error(request, '❌ حساب کاربری شما فعال نیست. لطفاً با پشتیبانی تماس بگیرید.')
                return render(request, 'accounts/customer_login.html')
            
            # TODO: اینجا کد SMS ارسال می‌شود
            # برای حالا، مستقیماً لاگین می‌کنیم
            login(request, user)
            messages.success(request, f'🎉 خوش آمدید مشتری گرامی {user.get_full_name() or user.username}!')
            return redirect('accounts:customer_dashboard')
            
        except User.DoesNotExist:
            messages.error(request, '❌ شماره تلفن در سیستم ثبت نشده است')
    
    return render(request, 'accounts/customer_login.html')


@login_required
def customer_dashboard_view(request):
    """🔵 داشبورد مخصوص مشتریان"""
    if not request.user.is_customer():
        messages.error(request, '❌ شما دسترسی به این بخش را ندارید')
        return redirect('accounts:dashboard')
    
    # دریافت اطلاعات مشتری مرتبط
    from core.models import Customer
    customer = Customer.objects.filter(
        customer_name=request.user.get_full_name() or request.user.username
    ).first()
    
    context = {
        'user': request.user,
        'customer': customer,
        'role_features': request.user.get_accessible_features(),
    }
    return render(request, 'accounts/customer_dashboard.html', context)


@login_required
def logout_view(request):
    """🚪 خروج کاربر از سیستم"""
    username = request.user.username
    logout(request)
    messages.success(request, f'👋 {username} با موفقیت خارج شدید')
    return redirect('accounts:login')


@login_required
def dashboard_view(request):
    """📊 داشبورد اصلی کاربران"""
    # اگر کاربر مشتری است، به داشبورد مشتری هدایت شود
    if request.user.is_customer():
        return redirect('accounts:customer_dashboard')
    
    context = {
        'user': request.user,
        'role_features': request.user.get_accessible_features(),
    }
    return render(request, 'accounts/dashboard.html', context)


@login_required
def profile_view(request):
    """👤 نمایش پروفایل کاربر"""
    return render(request, 'accounts/profile.html')


@login_required
def change_password_view(request):
    """🔐 تغییر رمز عبور"""
    return render(request, 'accounts/change_password.html')


@login_required
@permission_required('accounts.manage_all_users', raise_exception=True)
def user_list_view(request):
    """👥 لیست کاربران"""
    users = User.objects.all().order_by('-created_at')
    paginator = Paginator(users, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'user_roles': User.UserRole.choices,
        'user_statuses': User.UserStatus.choices,
    }
    return render(request, 'accounts/user_list.html', context)


@login_required
@permission_required('accounts.manage_all_users', raise_exception=True)
def user_detail_view(request, user_id):
    """👤 جزئیات کاربر"""
    user_obj = get_object_or_404(User, id=user_id)
    context = {'user_obj': user_obj}
    return render(request, 'accounts/user_detail.html', context)


@login_required
@require_http_methods(["POST"])
def update_user_status(request, user_id):
    """📊 تغییر وضعیت کاربر"""
    user_obj = get_object_or_404(User, id=user_id)
    new_status = request.POST.get('status')
    
    if new_status in [choice[0] for choice in User.UserStatus.choices]:
        user_obj.status = new_status
        user_obj.save()
        return JsonResponse({'success': True, 'message': 'وضعیت بروزرسانی شد'})
    
    return JsonResponse({'success': False, 'message': 'وضعیت نامعتبر'})


@login_required
def user_permissions_api(request):
    """API مجوزهای کاربر"""
    return JsonResponse({
        'role': request.user.role,
        'is_super_admin': request.user.is_super_admin(),
        'is_admin': request.user.is_admin(),
        'is_finance': request.user.is_finance(),
        'is_customer': request.user.is_customer(),
    })


@login_required
def check_password_strength(request):
    """🔐 بررسی قوت رمز عبور"""
    password = request.POST.get('password', '')
    score = len(password) * 10  # Simple scoring
    return JsonResponse({'score': min(score, 100), 'level': 'خوب'})
