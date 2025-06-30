#!/usr/bin/env python
"""
🧪 تست سیستم ثبت‌نام مشتریان جدید
🔍 بررسی عملکرد ثبت‌نام، تایید و ورود مشتریان
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HomayOMS.settings.dev')
django.setup()

from accounts.models import User
from core.models import Customer, ActivityLog
from django.utils import timezone

def test_customer_registration_system():
    """تست کامل سیستم ثبت‌نام مشتریان"""
    print("🧪 تست سیستم ثبت‌نام مشتریان جدید")
    print("=" * 60)
    
    # 1. تست شمارش مشتریان در انتظار
    pending_count = User.objects.filter(
        role=User.UserRole.CUSTOMER,
        status=User.UserStatus.PENDING
    ).count()
    print(f"📊 تعداد مشتریان در انتظار تایید: {pending_count}")
    
    # 2. نمایش تمام مشتریان
    print("\n📋 لیست تمام مشتریان:")
    customers = User.objects.filter(role=User.UserRole.CUSTOMER).order_by('-created_at')
    for customer in customers:
        status_emoji = {
            'pending': '⏳',
            'active': '✅',
            'inactive': '❌',
            'suspended': '⏸️'
        }.get(customer.status, '❓')
        
        print(f"   {status_emoji} {customer.get_full_name()} - {customer.phone} - {customer.get_status_display()}")
    
    # 3. نمایش لاگ‌های اخیر
    print("\n📜 لاگ‌های اخیر:")
    recent_logs = ActivityLog.objects.filter(
        action__in=['CREATE', 'APPROVE', 'REJECT']
    ).order_by('-created_at')[:5]
    
    for log in recent_logs:
        action_emoji = {
            'CREATE': '📝',
            'APPROVE': '✅',
            'REJECT': '❌'
        }.get(log.action, '📋')
        
        user_display = log.user.username if log.user else "سیستم"
        print(f"   {action_emoji} {user_display} - {log.description} - {log.created_at.strftime('%Y/%m/%d %H:%M')}")
    
    # 4. تست جستجوی کاربر با شماره تلفن
    print("\n🔍 تست جستجوی کاربر با شماره تلفن:")
    test_phone = "09123456789"
    
    # بررسی وجود کاربر
    user_exists = User.objects.filter(phone=test_phone).exists()
    print(f"   شماره {test_phone}: {'✅ موجود' if user_exists else '❌ موجود نیست'}")
    
    if user_exists:
        user = User.objects.get(phone=test_phone)
        print(f"   👤 نام: {user.get_full_name()}")
        print(f"   🎭 نقش: {user.get_role_display()}")
        print(f"   📊 وضعیت: {user.get_status_display()}")
        print(f"   ✅ فعال: {user.is_active_user()}")
    
    # 5. تست Customer objects مرتبط
    print("\n👤 Customer objects مرتبط:")
    customer_objects = Customer.objects.all().order_by('-created_at')[:5]
    for customer in customer_objects:
        print(f"   👤 {customer.customer_name} - {customer.phone} - {customer.status}")
    
    print("\n" + "=" * 60)
    print("✅ تست سیستم ثبت‌نام مشتریان تکمیل شد")
    
    # 6. راهنمای استفاده
    print("\n📖 راهنمای استفاده:")
    print("   1. مشتری جدید به /accounts/customer/sms-login/ می‌رود")
    print("   2. شماره تلفن جدید وارد می‌کند")
    print("   3. پیام 'عضو نیستید' دریافت می‌کند")
    print("   4. روی 'ثبت‌نام جدید' کلیک می‌کند")
    print("   5. فرم ثبت‌نام را پر می‌کند")
    print("   6. درخواست در انتظار تایید قرار می‌گیرد")
    print("   7. Super Admin در /accounts/users/ درخواست را تایید می‌کند")
    print("   8. مشتری پیامک تایید دریافت می‌کند")
    print("   9. مشتری می‌تواند وارد شود")

if __name__ == "__main__":
    test_customer_registration_system() 