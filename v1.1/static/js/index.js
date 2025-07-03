// Working hours configuration
const WORKING_HOURS = {
    // Days: 0 = Sunday, 1 = Monday, ..., 6 = Saturday
    // In Iran: Saturday = 6, Sunday = 0, Monday = 1, ..., Friday = 5
    saturday: { start: 8, end: 18 },    // شنبه
    sunday: { start: 8, end: 18 },      // یکشنبه  
    monday: { start: 8, end: 18 },      // دوشنبه
    tuesday: { start: 8, end: 18 },     // سه‌شنبه
    wednesday: { start: 8, end: 18 },   // چهارشنبه
    thursday: { start: 8, end: 16 },    // پنج‌شنبه
    friday: null                         // جمعه - تعطیل
};

// Price and stock data (این داده‌ها باید از سرور دریافت شوند)
let priceData = {
    cash: {
        price: 2500000,
        stock: 150
    },
    credit: {
        price: 2800000,
        stock: 200
    }
};

// Initialize the page
document.addEventListener('DOMContentLoaded', function () {
    updatePriceDisplay();
    checkWorkingHours();

    // Update working hours display
    updateWorkingHoursDisplay();

    // Set up auto-refresh for working hours check
    setInterval(checkWorkingHours, 60000); // Check every minute

    // Set up price update interval (if connected to real-time data)
    setInterval(updatePricesFromServer, 300000); // Update every 5 minutes
});

// Check if current time is within working hours
function checkWorkingHours() {
    const now = new Date();
    const currentDay = now.getDay(); // 0 = Sunday, 1 = Monday, etc.
    const currentHour = now.getHours();

    // Convert day number to our working hours key
    const dayNames = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'];
    const todaySchedule = WORKING_HOURS[dayNames[currentDay]];

    const mainContent = document.getElementById('mainContent');
    const closedContent = document.getElementById('closedContent');

    if (!todaySchedule) {
        // Today is closed (Friday)
        showClosedContent();
        return false;
    }

    if (currentHour >= todaySchedule.start && currentHour < todaySchedule.end) {
        // We're open
        showMainContent();
        return true;
    } else {
        // We're closed
        showClosedContent();
        return false;
    }
}

function showMainContent() {
    document.getElementById('mainContent').style.display = 'flex';
    document.getElementById('closedContent').style.display = 'none';
}

function showClosedContent() {
    document.getElementById('mainContent').style.display = 'none';
    document.getElementById('closedContent').style.display = 'flex';
}

// Update working hours display in the closed content
function updateWorkingHoursDisplay() {
    const workingHoursElement = document.getElementById('workingHoursDisplay');
    if (workingHoursElement) {
        // You can customize this based on your needs
        workingHoursElement.textContent = 'شنبه تا چهارشنبه: 08:00 - 18:00، پنج‌شنبه: 08:00 - 16:00';
    }
}

// Update price display on the page
function updatePriceDisplay() {
    // Update cash price and stock
    const cashPriceElement = document.getElementById('cashPrice');
    const cashStockElement = document.getElementById('cashStock');

    if (cashPriceElement) {
        cashPriceElement.textContent = formatPrice(priceData.cash.price) + ' تومان';
    }

    if (cashStockElement) {
        cashStockElement.textContent = priceData.cash.stock + ' کیلو';
    }

    // Update credit price and stock
    const creditPriceElement = document.getElementById('creditPrice');
    const creditStockElement = document.getElementById('creditStock');

    if (creditPriceElement) {
        creditPriceElement.textContent = formatPrice(priceData.credit.price) + ' تومان';
    }

    if (creditStockElement) {
        creditStockElement.textContent = priceData.credit.stock + ' کیلو';
    }
}

// Format price with Persian number separators
function formatPrice(price) {
    return price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, '٬');
}

// Handle cash purchase - redirect to login
function handleCashPurchase() {
    if (!checkWorkingHours()) {
        alert('متأسفانه در حال حاضر خارج از ساعت کاری هستیم.');
        return;
    }

    if (priceData.cash.stock <= 0) {
        alert('متأسفانه موجودی نقدی تمام شده است.');
        return;
    }

    // // هدایت به صفحه لاگین برای خرید نقدی
    const confirmed = confirm(`آیا مایل به خرید نقدی به قیمت ${formatPrice(priceData.cash.price)} تومان هستید؟`);

    if (confirmed) {
        // ذخیره نوع خرید در localStorage برای استفاده بعد از لاگین
        localStorage.setItem('purchaseType', 'cash');
        localStorage.setItem('purchasePrice', priceData.cash.price);

        // هدایت به صفحه لاگین
        window.location.href = '/accounts/customer/sms-login/';
    }
}

// Handle credit purchase - redirect to login
function handleCreditPurchase() {
    if (!checkWorkingHours()) {
        alert('متأسفانه در حال حاضر خارج از ساعت کاری هستیم.');
        return;
    }

    if (priceData.credit.stock <= 0) {
        alert('متأسفانه موجودی نسیه تمام شده است.');
        return;
    }

    // هدایت به صفحه لاگین برای خرید نسیه
    const confirmed = confirm(`آیا مایل به خرید نسیه به قیمت ${formatPrice(priceData.credit.price)} تومان هستید؟`);

    if (confirmed) {
        // ذخیره نوع خرید در localStorage برای استفاده بعد از لاگین
        localStorage.setItem('purchaseType', 'credit');
        localStorage.setItem('purchasePrice', priceData.credit.price);

        // هدایت به صفحه لاگین
        window.location.href = '/accounts/customer/sms-login/';
    }
}

// Update prices from server (placeholder function)
async function updatePricesFromServer() {
    try {
        // This would typically be an API call to your Django backend
        // const response = await fetch('/api/prices/');
        // const data = await response.json();
        // priceData = data;
        // updatePriceDisplay();

        console.log('Price update check (placeholder)');
    } catch (error) {
        console.error('Error updating prices:', error);
    }
}

// Add loading animation for buttons
function addLoadingToButton(button) {
    const originalText = button.innerHTML;
    button.innerHTML = '<span class="loading">در حال پردازش...</span>';
    button.disabled = true;

    // Simulate loading time
    setTimeout(() => {
        button.innerHTML = originalText;
        button.disabled = false;
    }, 2000);
}

// Add click event listeners with loading animation
document.addEventListener('DOMContentLoaded', function () {
    const cashBtn = document.querySelector('.cash-btn');
    const creditBtn = document.querySelector('.credit-btn');

    if (cashBtn) {
        cashBtn.addEventListener('click', function () {
            addLoadingToButton(this);
            setTimeout(handleCashPurchase, 100);
        });
    }

    if (creditBtn) {
        creditBtn.addEventListener('click', function () {
            addLoadingToButton(this);
            setTimeout(handleCreditPurchase, 100);
        });
    }
});

// Accessibility improvements
document.addEventListener('keydown', function (e) {
    // Handle Enter key for purchase buttons
    if (e.key === 'Enter' && e.target.classList.contains('purchase-btn')) {
        e.target.click();
    }
});

// Add focus indicators for keyboard navigation
document.addEventListener('DOMContentLoaded', function () {
    const focusableElements = document.querySelectorAll('.purchase-btn, .refresh-btn, .social-link');

    focusableElements.forEach(element => {
        element.addEventListener('focus', function () {
            this.style.outline = '3px solid #3498db';
            this.style.outlineOffset = '2px';
        });

        element.addEventListener('blur', function () {
            this.style.outline = 'none';
        });
    });
});

// Error handling for network issues
window.addEventListener('online', function () {
    console.log('اتصال اینترنت برقرار شد');
    updatePricesFromServer();
});

window.addEventListener('offline', function () {
    console.log('اتصال اینترنت قطع شد');
    // You could show a notification to the user here
});

// Performance monitoring
const perfObserver = new PerformanceObserver((list) => {
    const entries = list.getEntries();
    entries.forEach((entry) => {
        console.log(`${entry.name}: ${entry.duration}ms`);
    });
});

if ('PerformanceObserver' in window) {
    perfObserver.observe({ entryTypes: ['navigation', 'resource'] });
} 

function toggleMenu() {
    const menu = document.getElementById("navbarMenu");
    menu.classList.toggle("show");
}

