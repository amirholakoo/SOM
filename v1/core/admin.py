"""
🎛️ پنل مدیریت اپلیکیشن Core - HomayOMS
📋 تنظیمات پنل مدیریت جنگو برای مدل‌های اصلی کسب‌وکار
👥 رابط کاربری فارسی برای مدیریت مشتریان، سفارشات و موجودی
"""

from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """
    🎛️ پنل مدیریت مشتریان
    📊 رابط کاربری کامل برای مدیریت اطلاعات مشتریان
    """
    
    # 📋 فیلدهای نمایش داده شده در لیست مشتریان
    list_display = [
        'customer_name',       # 👤 نام مشتری
        'phone',              # 📞 تلفن
        'status',             # 📊 وضعیت
        'national_id',        # 🆔 شناسه ملی
        'postcode',           # 📮 کد پستی
        'created_at',         # 📅 تاریخ ایجاد
        'is_active',          # ✅ فعال/غیرفعال
    ]
    
    # 🔍 فیلدهای قابل جستجو
    search_fields = [
        'customer_name',      # جستجو در نام
        'phone',              # جستجو در تلفن
        'national_id',        # جستجو در شناسه ملی
        'economic_code',      # جستجو در کد اقتصادی
    ]
    
    # 🔽 فیلترهای کناری
    list_filter = [
        'status',             # فیلتر بر اساس وضعیت
        'created_at',         # فیلتر بر اساس تاریخ ایجاد
        'updated_at',         # فیلتر بر اساس تاریخ به‌روزرسانی
    ]
    
    # 📝 ترتیب فیلدها در فرم ویرایش
    fieldsets = (
        ('👤 اطلاعات اصلی مشتری', {
            'fields': ('customer_name', 'status')
        }),
        ('📞 اطلاعات تماس', {
            'fields': ('phone', 'address', 'postcode'),
            'classes': ('collapse',)  # قابل جمع شدن
        }),
        ('🆔 کدهای قانونی', {
            'fields': ('national_id', 'economic_code'),
            'classes': ('collapse',)  # قابل جمع شدن
        }),
        ('💬 توضیحات اضافی', {
            'fields': ('comments',),
            'classes': ('collapse',)  # قابل جمع شدن
        }),
    )
    
    # 📅 فیلدهای فقط خواندنی (از BaseModel)
    readonly_fields = ['created_at', 'updated_at']
    
    # 🔢 تعداد آیتم‌ها در هر صفحه
    list_per_page = 25
    
    # ⚡ بهینه‌سازی کوئری‌ها
    list_select_related = []  # در صورت داشتن ForeignKey اضافه می‌شود
    
    # 🎯 اکشن‌های سفارشی
    actions = ['make_active', 'make_inactive']
    
    def make_active(self, request, queryset):
        """
        ✅ فعال کردن مشتریان انتخاب شده
        """
        updated = queryset.update(status='Active')
        self.message_user(
            request, 
            f'✅ {updated} مشتری فعال شدند.'
        )
    make_active.short_description = "✅ فعال کردن مشتریان انتخاب شده"
    
    def make_inactive(self, request, queryset):
        """
        ❌ غیرفعال کردن مشتریان انتخاب شده
        """
        updated = queryset.update(status='Inactive')
        self.message_user(
            request, 
            f'❌ {updated} مشتری غیرفعال شدند.'
        )
    make_inactive.short_description = "❌ غیرفعال کردن مشتریان انتخاب شده"
    
    def is_active(self, obj):
        """
        ✅ نمایش وضعیت فعال/غیرفعال با آیکون
        """
        if obj.is_active():
            return "✅ فعال"
        return "❌ غیرفعال"
    is_active.short_description = "📊 وضعیت"
    is_active.boolean = True  # نمایش به صورت آیکون بولین
