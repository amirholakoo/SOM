"""
🏭 تنظیمات محیط تولید - HomayOMS
🔒 این فایل برای سرور تولید با حداکثر امنیت طراحی شده است
🗄️ از پایگاه داده PostgreSQL و تنظیمات امنیتی پیشرفته استفاده می‌کند
"""

from .base import *
import sys
import os

# 📁 اضافه کردن مسیر اصلی پروژه به Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))

# 📥 واردات تنظیمات پایگاه داده از config.py
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

# 🔐 تنظیمات امنیتی تولید
DEBUG = False                    # ❌ غیرفعال کردن حالت دیباگ
ALLOWED_HOSTS = ALLOWED_HOSTS    # 🌐 هاست‌های مجاز از متغیر محیطی

# 🗄️ پایگاه داده PostgreSQL برای تولید
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # 🐘 موتور PostgreSQL
        'NAME': DB_NAME,          # 📊 نام پایگاه داده
        'USER': DB_USER,          # 👤 نام کاربری
        'PASSWORD': DB_PASSWORD,  # 🔐 رمز عبور
        'HOST': DB_HOST,          # 🏠 آدرس سرور
        'PORT': DB_PORT,          # 🚪 پورت اتصال
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# 🛡️ تنظیمات امنیتی پیشرفته برای تولید
SECURE_BROWSER_XSS_FILTER = True          # 🚫 فیلتر XSS مرورگر
SECURE_CONTENT_TYPE_NOSNIFF = True        # 🚫 جلوگیری از Content-Type sniffing
SECURE_HSTS_SECONDS = 31536000            # ⏰ HSTS برای یک سال
SECURE_HSTS_INCLUDE_SUBDOMAINS = True     # 🌐 HSTS برای زیردامنه‌ها
SECURE_HSTS_PRELOAD = True                # 📋 HSTS preload
SECURE_SSL_REDIRECT = True                # 🔀 هدایت به HTTPS
SESSION_COOKIE_SECURE = True             # 🍪 کوکی نشست امن
CSRF_COOKIE_SECURE = True                # 🍪 کوکی CSRF امن
X_FRAME_OPTIONS = 'DENY'                 # 🚫 جلوگیری از iframe

# 📊 سیستم لاگ‌گیری تولید
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / 'logs' / 'django_production.log',
            'maxBytes': 1024*1024*5,  # 📏 حداکثر 5 مگابایت
            'backupCount': 10,        # 🗂️ نگه‌داری 10 فایل قبلی
            'formatter': 'verbose',   # 📝 فرمت کامل
        },
        'error_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / 'logs' / 'django_errors.log',
            'maxBytes': 1024*1024*5,  # 📏 حداکثر 5 مگابایت
            'backupCount': 10,        # 🗂️ نگه‌داری 10 فایل قبلی
            'formatter': 'verbose',   # 📝 فرمت کامل
            'level': 'ERROR',         # ⚠️ فقط خطاها
        },
    },
    'root': {
        'handlers': ['file'],
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'error_file'],
            'level': 'INFO',          # 📋 سطح اطلاعات
            'propagate': False,
        },
    },
}

# 📧 تنظیمات ایمیل برای تولید (SMTP)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'your-smtp-host.com'        # 🏠 سرور SMTP
# EMAIL_PORT = 587                         # 🚪 پورت SMTP
# EMAIL_USE_TLS = True                     # 🔐 استفاده از TLS
# EMAIL_HOST_USER = 'your-email@domain.com'    # 👤 ایمیل کاربری
# EMAIL_HOST_PASSWORD = 'your-email-password'  # 🔒 رمز عبور ایمیل

# 🔗 تنظیمات CORS برای تولید (محدود)
CORS_ALLOW_ALL_ORIGINS = False            # ❌ جلوگیری از دسترسی کلی
CORS_ALLOWED_ORIGINS = CORS_ALLOWED_ORIGINS  # ✅ فقط دامنه‌های مجاز

# 🗄️ تنظیمات کش برای تولید (Redis توصیه می‌شود)
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.redis.RedisCache',
#         'LOCATION': 'redis://127.0.0.1:6379/1',
#     }
# }

# 📝 تنظیمات نشست برای تولید
SESSION_COOKIE_AGE = 3600                 # ⏰ مدت اعتبار 1 ساعت
SESSION_EXPIRE_AT_BROWSER_CLOSE = True    # 🚪 انقضا هنگام بستن مرورگر 