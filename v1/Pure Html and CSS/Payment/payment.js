// Payment Gateway JavaScript

document.addEventListener('DOMContentLoaded', function () {
    initializePaymentPage();
    loadOrderData();
});

function initializePaymentPage() {
    // Event listeners for payment method selection
    const paymentMethods = document.querySelectorAll('input[name="payment-method"]');
    paymentMethods.forEach(method => {
        method.addEventListener('change', switchPaymentForm);
    });

    // Format card number input
    const cardNumberInput = document.querySelector('.card-number');
    if (cardNumberInput) {
        cardNumberInput.addEventListener('input', formatCardNumber);
        cardNumberInput.addEventListener('keypress', validateCardInput);
    }

    // Format expiry date input
    const expiryInput = document.querySelector('.expiry-date');
    if (expiryInput) {
        expiryInput.addEventListener('input', formatExpiryDate);
        expiryInput.addEventListener('keypress', validateDateInput);
    }

    // CVV validation
    const cvvInput = document.querySelector('.cvv');
    if (cvvInput) {
        cvvInput.addEventListener('input', formatCVV);
        cvvInput.addEventListener('keypress', validateNumberInput);
    }

    // Phone number formatting
    const phoneInput = document.querySelector('input[type="tel"]');
    if (phoneInput) {
        phoneInput.addEventListener('input', formatPhoneNumber);
        phoneInput.addEventListener('keypress', validateNumberInput);
    }

    // Add form validation
    setupFormValidation();
}

function switchPaymentForm() {
    const selectedMethod = document.querySelector('input[name="payment-method"]:checked').value;

    // Hide all forms
    document.getElementById('cardForm').style.display = 'none';
    document.getElementById('walletForm').style.display = 'none';
    document.getElementById('internetForm').style.display = 'none';

    // Show selected form
    switch (selectedMethod) {
        case 'card':
            document.getElementById('cardForm').style.display = 'flex';
            break;
        case 'wallet':
            document.getElementById('walletForm').style.display = 'flex';
            break;
        case 'internet':
            document.getElementById('internetForm').style.display = 'flex';
            break;
    }
}

function formatCardNumber(event) {
    let value = event.target.value.replace(/\s+/g, '').replace(/[^0-9]/gi, '');
    let formattedValue = value.match(/.{1,4}/g)?.join('-') || value;
    if (formattedValue !== value) {
        event.target.value = formattedValue;
    }
}

function formatExpiryDate(event) {
    let value = event.target.value.replace(/\D/g, '');
    if (value.length >= 2) {
        value = value.substring(0, 2) + '/' + value.substring(2, 4);
    }
    event.target.value = value;
}

function formatCVV(event) {
    let value = event.target.value.replace(/\D/g, '');
    event.target.value = value;
}

function formatPhoneNumber(event) {
    let value = event.target.value.replace(/\D/g, '');
    if (value.length <= 11) {
        if (value.length >= 4) {
            value = value.substring(0, 4) + '-' + value.substring(4);
        }
        if (value.length >= 8) {
            value = value.substring(0, 8) + '-' + value.substring(8);
        }
    }
    event.target.value = value;
}

function validateCardInput(event) {
    const char = String.fromCharCode(event.which);
    if (!/[0-9\s]/.test(char)) {
        event.preventDefault();
    }
}

function validateNumberInput(event) {
    const char = String.fromCharCode(event.which);
    if (!/[0-9]/.test(char)) {
        event.preventDefault();
    }
}

function validateDateInput(event) {
    const char = String.fromCharCode(event.which);
    if (!/[0-9/]/.test(char)) {
        event.preventDefault();
    }
}

function setupFormValidation() {
    const inputs = document.querySelectorAll('.form-input, .form-select');
    inputs.forEach(input => {
        input.addEventListener('blur', validateInput);
        input.addEventListener('input', clearInputError);
    });
}

function validateInput(event) {
    const input = event.target;
    const value = input.value.trim();

    // Remove previous error styling
    input.classList.remove('error');

    // Check if required field is empty
    if (input.hasAttribute('required') && !value) {
        showInputError(input, 'این فیلد الزامی است');
        return false;
    }

    // Specific validations
    if (input.classList.contains('card-number')) {
        return validateCardNumber(input);
    } else if (input.classList.contains('expiry-date')) {
        return validateExpiryDate(input);
    } else if (input.classList.contains('cvv')) {
        return validateCVV(input);
    } else if (input.type === 'email') {
        return validateEmail(input);
    } else if (input.type === 'tel') {
        return validatePhone(input);
    }

    return true;
}

function validateCardNumber(input) {
    const value = input.value.replace(/\D/g, '');
    if (value.length < 16) {
        showInputError(input, 'شماره کارت باید 16 رقم باشد');
        return false;
    }
    return true;
}

function validateExpiryDate(input) {
    const value = input.value;
    const [month, year] = value.split('/');

    if (!month || !year || month.length !== 2 || year.length !== 2) {
        showInputError(input, 'فرمت تاریخ نادرست است');
        return false;
    }

    const monthNum = parseInt(month);
    if (monthNum < 1 || monthNum > 12) {
        showInputError(input, 'ماه نادرست است');
        return false;
    }

    return true;
}

function validateCVV(input) {
    const value = input.value;
    if (value.length < 3 || value.length > 4) {
        showInputError(input, 'CVV باید 3 یا 4 رقم باشد');
        return false;
    }
    return true;
}

function validateEmail(input) {
    const value = input.value;
    if (value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) {
        showInputError(input, 'فرمت ایمیل نادرست است');
        return false;
    }
    return true;
}

function validatePhone(input) {
    const value = input.value.replace(/\D/g, '');
    if (value.length !== 11 || !value.startsWith('09')) {
        showInputError(input, 'شماره موبایل نادرست است');
        return false;
    }
    return true;
}

function showInputError(input, message) {
    input.classList.add('error');

    // Remove existing error message
    const existingError = input.parentNode.querySelector('.error-message');
    if (existingError) {
        existingError.remove();
    }

    // Add new error message
    const errorElement = document.createElement('div');
    errorElement.className = 'error-message';
    errorElement.textContent = message;
    input.parentNode.appendChild(errorElement);
}

function clearInputError(event) {
    const input = event.target;
    input.classList.remove('error');
    const errorMessage = input.parentNode.querySelector('.error-message');
    if (errorMessage) {
        errorMessage.remove();
    }
}

function processPayment() {
    // Show loading
    showLoading();

    // Simplified validation - just check if basic info is available
    const orderData = JSON.parse(sessionStorage.getItem('orderData') || '{}');

    if (!orderData.items || orderData.items.length === 0) {
        hideLoading();
        showMessage('اطلاعات سفارش موجود نیست. لطفاً مجدداً از صفحه خرید شروع کنید.', 'error');
        return;
    }

    // Simulate payment processing
    setTimeout(() => {
        hideLoading();

        // Always successful for testing (100% success rate)
        // Store payment success info
        const paymentData = {
            ...orderData,
            paymentDate: new Date().toISOString(),
            paymentMethod: document.querySelector('input[name="payment-method"]:checked').value,
            paymentStatus: 'completed',
            transactionId: 'TXN_' + Date.now()
        };

        sessionStorage.setItem('lastPayment', JSON.stringify(paymentData));
        sessionStorage.removeItem('orderData'); // Clear order data

        showMessage('پرداخت با موفقیت انجام شد! 🎉', 'success');
        setTimeout(() => {
            // Redirect to success page or back to index
            window.location.href = '../Index/index.html';
        }, 2000);
    }, 2000); // Reduced processing time
}

function validateAllInputs() {
    const selectedMethod = document.querySelector('input[name="payment-method"]:checked').value;
    let isValid = true;

    // Skip contact information validation for now (no security needed)
    // const contactInputs = document.querySelectorAll('.contact-form .form-input');
    // contactInputs.forEach(input => {
    //     if (!validateInput({ target: input })) {
    //         isValid = false;
    //     }
    // });

    // Validate payment method specific inputs only if filled
    switch (selectedMethod) {
        case 'card':
            const cardInputs = document.querySelectorAll('#cardForm .form-input');
            cardInputs.forEach(input => {
                // Only validate if user has entered something
                if (input.value.trim()) {
                    if (!validateInput({ target: input })) {
                        isValid = false;
                    }
                }
            });
            break;
        case 'internet':
            // Bank selection is optional for testing
            break;
    }

    return isValid;
}

function cancelPayment() {
    if (confirm('آیا مطمئن هستید که می‌خواهید پرداخت را لغو کنید؟')) {
        // Clear order data
        sessionStorage.removeItem('orderData');
        showMessage('پرداخت لغو شد', 'info');
        setTimeout(() => {
            window.location.href = '../Shopping/shopping.html';
        }, 1000);
    }
}

function goBack() {
    // Check if we have order data to go back to shopping
    const orderData = sessionStorage.getItem('orderData');
    if (orderData) {
        // Go back to shopping page
        window.location.href = '../Shopping/shopping.html';
    } else {
        // Use browser back or go to index
        if (window.history.length > 1) {
            window.history.back();
        } else {
            window.location.href = '../Index/index.html';
        }
    }
}

function showLoading() {
    document.getElementById('loadingOverlay').style.display = 'flex';
}

function hideLoading() {
    document.getElementById('loadingOverlay').style.display = 'none';
}

function showMessage(message, type = 'info') {
    // Remove existing messages
    const existingMessages = document.querySelectorAll('.message-popup');
    existingMessages.forEach(msg => msg.remove());

    // Create new message
    const messageElement = document.createElement('div');
    messageElement.className = `message-popup message-${type}`;
    messageElement.innerHTML = `
        <div class="message-content">
            <span class="message-icon">${getMessageIcon(type)}</span>
            <span class="message-text">${message}</span>
        </div>
    `;

    document.body.appendChild(messageElement);

    // Auto remove after 5 seconds
    setTimeout(() => {
        messageElement.remove();
    }, 5000);

    // Add click to close
    messageElement.addEventListener('click', () => {
        messageElement.remove();
    });
}

function getMessageIcon(type) {
    switch (type) {
        case 'success': return '✅';
        case 'error': return '❌';
        case 'warning': return '⚠️';
        default: return 'ℹ️';
    }
}

// Add CSS for error states and messages
const style = document.createElement('style');
style.textContent = `
    .form-input.error,
    .form-select.error {
        border-color: #e74c3c !important;
        background: rgba(231, 76, 60, 0.1) !important;
    }
    
    .error-message {
        color: #e74c3c;
        font-size: 0.9rem;
        margin-top: 5px;
        font-weight: 600;
    }
    
    .message-popup {
        position: fixed;
        top: 20px;
        right: 20px;
        background: white;
        border-radius: 12px;
        padding: 15px 20px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
        z-index: 10000;
        cursor: pointer;
        animation: slideIn 0.3s ease;
        max-width: 400px;
    }
    
    .message-content {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .message-icon {
        font-size: 1.2rem;
    }
    
    .message-text {
        font-family: 'Vazirmatn', Tahoma, Arial, sans-serif;
        font-weight: 600;
        color: #2c3e50;
    }
    
    .message-success {
        border-left: 4px solid #27ae60;
    }
    
    .message-error {
        border-left: 4px solid #e74c3c;
    }
    
    .message-warning {
        border-left: 4px solid #f39c12;
    }
    
    .message-info {
        border-left: 4px solid #3498db;
    }
    
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @media (max-width: 768px) {
        .message-popup {
            right: 10px;
            left: 10px;
            max-width: none;
        }
    }
`;
document.head.appendChild(style);

function loadOrderData() {
    // Get order data from session storage
    const orderDataStr = sessionStorage.getItem('currentOrder');
    if (!orderDataStr) {
        // If no order data, redirect back to shopping
        showMessage('داده‌های سفارش یافت نشد. در حال بازگشت به صفحه خرید...', 'error');
        setTimeout(() => {
            window.location.href = '../Shopping/shopping.html';
        }, 2000);
        return;
    }

    const orderData = JSON.parse(orderDataStr);
    displayOrderSummary(orderData);
    updateFinalPriceInButton(orderData.summary.finalAmount);
}

function displayOrderSummary(orderData) {
    // Update order items
    const orderItemsContainer = document.querySelector('.order-items');
    if (orderItemsContainer && orderData.products && orderData.products.length > 0) {
        orderItemsContainer.innerHTML = orderData.products.map(product => `
            <div class="order-item">
                <div class="item-info">
                    <span class="item-name">${product.name}</span>
                    <span class="item-specs">
                        ${product.tableType === 'cash' ? 'نقدی' : 'نسیه'}
                        <br>تعداد: ${formatNumber(product.quantity)} کیلو
                    </span>
                </div>
                <div class="item-price">${formatPrice(product.totalPrice)} تومان</div>
            </div>
        `).join('');
    }

    // Update totals
    updateOrderTotals(orderData.summary);
}

function updateOrderTotals(orderData) {
    const totalsContainer = document.querySelector('.order-totals');
    if (totalsContainer) {
        totalsContainer.innerHTML = `
            <div class="total-row final-total">
                <span class="total-label">مبلغ کل:</span>
                <span class="total-value">${formatPrice(orderData.finalAmount)} تومان</span>
            </div>
        `;
    }
}

function updateFinalPriceInButton(finalTotal) {
    const payBtn = document.querySelector('.pay-btn .btn-text');
    if (payBtn) {
        payBtn.textContent = `پرداخت ${formatPrice(finalTotal)} تومان`;
    }
}

function formatPrice(price) {
    return new Intl.NumberFormat('fa-IR').format(Math.round(price));
}

function formatNumber(number) {
    return new Intl.NumberFormat('fa-IR').format(number);
}

/**
 * Update order summary display
 */
function updateOrderSummary() {
    const summaryContainer = document.getElementById('orderSummary');
    if (!summaryContainer || !currentOrder) return;

    const { products, summary } = currentOrder;

    // Products HTML
    const productsHTML = products.map(product => `
        <div class="order-item">
            <div class="item-details">
                <div class="item-name">${product.name}</div>
                <div class="item-meta">
                    <span class="item-type ${product.tableType}-badge">
                        ${product.tableType === 'cash' ? 'نقدی' : 'نسیه'}
                    </span>
                    <span class="item-quantity">${convertToPersianNumbers(product.quantity)} کیلو</span>
                </div>
            </div>
            <div class="item-price">${formatPrice(product.totalPrice)}</div>
        </div>
    `).join('');

    // Summary HTML (without discount)
    summaryContainer.innerHTML = `
        <div class="order-products">
            ${productsHTML}
        </div>
        <div class="order-totals">
            <div class="total-row final-total">
                <span class="total-label">مبلغ کل:</span>
                <span class="total-value">${formatPrice(summary.finalAmount)}</span>
            </div>
            <div class="order-meta">
                <span class="meta-item">${convertToPersianNumbers(summary.itemCount)} قلم کالا</span>
                <span class="meta-separator">•</span>
                <span class="meta-item">${convertToPersianNumbers(summary.totalQuantity)} کیلو</span>
            </div>
        </div>
    `;
} 