"""
🏢 مدل‌های اصلی اپلیکیشن Core - HomayOMS
📋 این فایل شامل مدل‌های اصلی کسب‌وکار مانند مشتری، سفارش و موجودی است
👥 تمام مدل‌ها از BaseModel ارث‌بری می‌کنند تا دارای فیلدهای زمانی باشند
"""

from django.db import models
from HomayOMS.baseModel import BaseModel


class Customer(BaseModel):
    """
    👤 مدل مشتری - اطلاعات کامل مشتریان سیستم
    
    🎯 این مدل برای ذخیره اطلاعات مشتریان کسب‌وکار استفاده می‌شود
    📋 شامل اطلاعات تماس، آدرس، و کدهای قانونی مشتری
    ⏰ دارای فیلدهای created_at و updated_at از BaseModel
    
    🔧 استفاده:
        customer = Customer.objects.create(
            customer_name="نام مشتری",
            phone="09123456789",
            address="آدرس کامل"
        )
    """
    
    # 📊 وضعیت مشتری
    status = models.CharField(
        max_length=255, 
        blank=True, 
        default='Active',
        verbose_name="📊 وضعیت مشتری",
        help_text="وضعیت فعلی مشتری در سیستم (Active, Inactive, Suspended)"
    )
    
    # 👤 نام مشتری (اجباری)
    customer_name = models.CharField(
        max_length=255, 
        null=False,
        verbose_name="👤 نام مشتری",
        help_text="نام کامل یا نام شرکت مشتری (اجباری)"
    )
    
    # 🏠 آدرس کامل
    address = models.TextField(
        blank=True,
        verbose_name="🏠 آدرس",
        help_text="آدرس کامل محل سکونت یا کسب‌وکار مشتری"
    )
    
    # 📞 شماره تلفن
    phone = models.CharField(
        max_length=20, 
        blank=True,
        verbose_name="📞 شماره تلفن",
        help_text="شماره تلفن تماس مشتری (همراه یا ثابت)"
    )
    
    # 💬 توضیحات اضافی
    comments = models.TextField(
        blank=True,
        verbose_name="💬 توضیحات",
        help_text="یادداشت‌ها و توضیحات اضافی درباره مشتری"
    )
    
    # 💼 کد اقتصادی خریدار (فیلد جدید)
    economic_code = models.CharField(
        "💼 کد اقتصادی خریدار", 
        max_length=15, 
        blank=True, 
        null=True,
        help_text="کد اقتصادی شرکت یا کسب‌وکار مشتری برای صدور فاکتور رسمی"
    )
    
    # 📮 کد پستی خریدار (فیلد جدید)
    postcode = models.CharField(
        "📮 کد پستی خریدار", 
        max_length=10, 
        blank=True, 
        null=True,
        help_text="کد پستی ده رقمی آدرس مشتری"
    )
    
    # 🆔 شناسه ملی خریدار (فیلد جدید)
    national_id = models.CharField(
        "🆔 شناسه ملی خریدار", 
        max_length=50, 
        blank=True, 
        null=True,
        help_text="شناسه ملی (اشخاص حقیقی) یا شناسه اقتصادی (اشخاص حقوقی)"
    )
    
    class Meta:
        verbose_name = "👤 مشتری"
        verbose_name_plural = "👥 مشتریان"
        ordering = ['-created_at']  # 📅 مرتب‌سازی بر اساس تاریخ ایجاد (جدیدترین ابتدا)
        
        # 📇 ایندکس‌های پایگاه داده برای بهبود عملکرد
        indexes = [
            models.Index(fields=['customer_name']),   # 🔍 جستجوی سریع بر اساس نام
            models.Index(fields=['phone']),           # 📞 جستجوی سریع بر اساس تلفن
            models.Index(fields=['national_id']),     # 🆔 جستجوی سریع بر اساس شناسه ملی
            models.Index(fields=['status']),          # 📊 فیلتر بر اساس وضعیت
        ]
    
    def clean(self):
        """
        🧹 اعتبارسنجی داده‌های مدل قبل از ذخیره
        ✅ بررسی صحت کد پستی، شناسه ملی و سایر فیلدها
        """
        from django.core.exceptions import ValidationError
        
        # 📮 بررسی طول کد پستی
        if self.postcode and len(self.postcode) != 10:
            raise ValidationError({
                'postcode': '📮 کد پستی باید دقیقاً 10 رقم باشد'
            })
        
        # 🆔 بررسی طول شناسه ملی (برای اشخاص حقیقی)
        if self.national_id and len(self.national_id) == 10:
            # اعتبارسنجی کد ملی ایرانی می‌تواند در آینده اضافه شود
            pass
    
    def __str__(self):
        """
        📄 نمایش رشته‌ای مشتری
        """
        return f"👤 {self.customer_name}"
    
    def get_full_address(self):
        """
        🏠 دریافت آدرس کامل شامل کد پستی
        📍 ترکیب آدرس و کد پستی برای نمایش کامل
        """
        if self.address and self.postcode:
            return f"{self.address} - کد پستی: {self.postcode}"
        elif self.address:
            return self.address
        else:
            return "❌ آدرس ثبت نشده"
    
    def is_active(self):
        """
        ✅ بررسی فعال بودن مشتری
        🔍 بررسی وضعیت مشتری برای عملیات‌های کسب‌وکار
        """
        return self.status.lower() == 'active'
    
    def get_contact_info(self):
        """
        📞 دریافت اطلاعات تماس کامل
        📋 ترکیب تلفن و آدرس برای نمایش سریع
        """
        contact_parts = []
        if self.phone:
            contact_parts.append(f"📞 {self.phone}")
        if self.address:
            contact_parts.append(f"🏠 {self.address}")
        
        return " | ".join(contact_parts) if contact_parts else "❌ اطلاعات تماس ناقص"
