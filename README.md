# 🏢 HomayOMS - Inventory & Order Management System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2+-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-In%20Development-orange.svg)]()

> **Enterprise-grade Inventory & Order Management System** with multi-role authentication, SMS verification, and modern UI/UX design.

## 📋 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [🚀 Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📦 Installation](#-installation)
- [🔧 Django Management Commands](#-django-management-commands)
- [🔐 Authentication System](#-authentication-system)
- [📊 Project Structure](#-project-structure)
- [✅ Completed Features](#-completed-features)
- [📝 TODO List](#-todo-list)
- [🤝 Contributing](#-contributing)
- [👥 Contributors](#-contributors)
- [📄 License](#-license)

## 🎯 Project Overview

HomayOMS is a comprehensive **Inventory & Order Management System** designed for modern businesses. Built with Django and featuring a sophisticated multi-role authentication system, it provides secure access for different user types with role-based permissions and SMS verification for customers.

### 🎨 Key Highlights

- **🔐 Multi-Role Authentication**: 4 distinct user roles with separate login flows
- **📱 SMS Verification**: Secure customer authentication via SMS
- **🎨 Modern UI/UX**: Beautiful, responsive design with Tailwind CSS
- **🌐 Persian RTL Support**: Full support for Persian language and RTL layout
- **🔒 Role-Based Access Control**: Granular permissions for each user type
- **📊 Real-time Dashboard**: Role-specific dashboards with relevant metrics

## 🚀 Features

### 🔐 Authentication & Security
- **4-Role Login System**: Super Admin, Admin, Finance, Customer
- **SMS Verification**: Customer authentication via mobile verification
- **Session Management**: Secure user sessions with activity tracking
- **Password Security**: Encrypted password storage with expiration
- **Role Validation**: Strict role-based access control

### 👥 User Management
- **Custom User Model**: Extended Django User with role-based fields
- **Profile Management**: User profile editing and management
- **Status Tracking**: Active, Inactive, Suspended, Pending statuses
- **Activity Monitoring**: Last login and activity tracking

### 🏢 Business Features
- **Customer Management**: Complete customer profile system
- **Inventory Tracking**: Product and stock management (planned)
- **Order Processing**: Order creation and management (planned)
- **Financial Management**: Pricing and invoice system (planned)
- **Reporting System**: Business analytics and reports (planned)

### 🎨 User Interface
- **Responsive Design**: Works perfectly on all devices
- **Modern UI**: Clean, professional interface with animations
- **Persian Support**: Full RTL layout and Persian text support
- **Accessibility**: WCAG compliant design patterns
- **Dark/Light Mode**: Theme switching capability (planned)

## 🛠️ Tech Stack

### Backend
- **Python 3.8+**: Core programming language
- **Django 5.2+**: Web framework with admin interface
- **SQLite/PostgreSQL**: Database management
- **Django REST Framework**: API development (planned)

### Frontend
- **Tailwind CSS**: Utility-first CSS framework
- **HTML5/CSS3**: Modern web standards
- **JavaScript**: Interactive functionality
- **Vazirmatn Font**: Persian typography

### DevOps & Tools
- **Git**: Version control
- **Docker**: Containerization (planned)
- **GitHub Actions**: CI/CD pipeline (planned)
- **Nginx**: Web server (production)

### Security
- **Django Security**: Built-in security features
- **HTTPS**: SSL/TLS encryption
- **CSRF Protection**: Cross-site request forgery protection
- **XSS Prevention**: Cross-site scripting protection

## 📦 Installation

### Prerequisites
```bash
Python 3.8+
pip
git
```

### Quick Start
```bash
# Clone the repository
git clone https://github.com/amirholakoo/IOMS.git
cd IOMS/v1

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Create test customer
python manage.py create_test_customer

# Run development server
python manage.py runserver
```

### Environment Configuration
```bash
# Copy environment file
cp .env.example .env

# Edit environment variables
nano .env
```

## 🔧 Django Management Commands

> **📝 For Next Developer**: This section contains all custom Django management commands created for testing, development, and system setup. These commands are essential for development workflow and testing.

### 📊 Command Overview

| Command | App | Purpose | Usage |
|---------|-----|---------|-------|
| `create_full_test_data` | accounts | Create test users for all roles | `python manage.py create_full_test_data` |
| `setup_roles` | accounts | Setup roles and permissions | `python manage.py setup_roles` |
| `create_test_products` | core | Create test products | `python manage.py create_test_products` |
| `create_daily_test_customer` | accounts | Create daily test customers | `python manage.py create_daily_test_customer` |
| `create_test_users` | accounts | Create test users | `python manage.py create_test_users` |
| `create_fake_test_data` | accounts | Create fake test data | `python manage.py create_fake_test_data` |
| `create_test_customer` | accounts | Create single test customer | `python manage.py create_test_customer` |
| `create_specific_user_activities` | accounts | Create user activities | `python manage.py create_specific_user_activities` |

### 🚀 Essential Commands for Development

#### 1. **Complete System Setup**
```bash
# Setup roles and create super admin
python manage.py setup_roles --create-superuser --username admin --password admin123

# Create full test data for all roles
python manage.py create_full_test_data

# Create test products
python manage.py create_test_products --count 20
```

#### 2. **Test User Creation**
```bash
# Create test users for all roles (recommended)
python manage.py create_full_test_data

# Output will show:
# ============================================================
# 📋 اطلاعات ورود تستی برای همه نقش‌ها:
# ------------------------------------------------------------
# نقش            نام کاربری     موبایل         رمز عبور    
# ------------------------------------------------------------
# 🔴 Super Admin  superadmin1    09120000001    123456      
# 🟡 Admin        admin1         09120000002    123456      
# 🟢 Finance      finance1       09120000003    123456      
# 🔵 Customer     customer1      09120000004    123456      
# 🔵 Customer     customer2      09120000005    123456      
# ============================================================
```

#### 3. **SMS Testing**
```bash
# Create daily test customers for SMS testing
python manage.py create_daily_test_customer --count 5 --prefix 0915

# Use these phone numbers for SMS verification testing
# Codes will appear in terminal/logs
```

### 📁 Command Locations

```
v1/
├── accounts/management/commands/
│   ├── create_full_test_data.py          # ⭐ Main test data command
│   ├── setup_roles.py                    # Role and permission setup
│   ├── create_test_users.py              # Test user creation
│   ├── create_fake_test_data.py          # Fake data generation
│   ├── create_daily_test_customer.py     # Daily customer creation
│   ├── create_test_customer.py           # Single customer creation
│   └── create_specific_user_activities.py # User activity creation
└── core/management/commands/
    └── create_test_products.py           # Product test data
```

### 🎯 Command Details

#### **`create_full_test_data`** ⭐ **Most Important**
- **Purpose**: Creates test users for all 4 roles (Super Admin, Admin, Finance, Customer)
- **Features**: 
  - All users are set to `ACTIVE` status
  - Unique usernames, phones, and emails
  - Password: `123456` for all users
  - Prints beautiful table with login credentials
- **Usage**: `python manage.py create_full_test_data`
- **Output**: Complete login table in terminal

#### **`setup_roles`**
- **Purpose**: Initializes user groups, permissions, and optionally creates Super Admin
- **Features**:
  - Creates user groups for all roles
  - Assigns permissions to groups
  - Can create Super Admin with custom credentials
- **Usage**: 
  ```bash
  python manage.py setup_roles
  python manage.py setup_roles --create-superuser --username admin --password admin123
  ```

#### **`create_test_products`**
- **Purpose**: Creates test products for inventory testing
- **Features**:
  - Generates realistic product data
  - Creates activity logs for each product
  - Calculates prices based on dimensions and quality
  - Supports bulk creation with `--count` parameter
- **Usage**: 
  ```bash
  python manage.py create_test_products
  python manage.py create_test_products --count 50
  python manage.py create_test_products --clear  # Clear existing products first
  ```

#### **`create_daily_test_customer`**
- **Purpose**: Creates test customers for SMS verification testing
- **Features**:
  - Generates unique phone numbers
  - Creates customers with `ACTIVE` status
  - Perfect for SMS testing workflow
- **Usage**:
  ```bash
  python manage.py create_daily_test_customer
  python manage.py create_daily_test_customer --count 10 --prefix 0915
  ```

### 🔧 Development Workflow

#### **For New Developer Setup**
```bash
# 1. Clone and setup project
git clone https://github.com/amirholakoo/IOMS.git
cd IOMS/v1
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 2. Setup database
python manage.py migrate

# 3. Create test data
python manage.py create_full_test_data
python manage.py create_test_products --count 10

# 4. Start development
python manage.py runserver
```

#### **For Testing Different Roles**
```bash
# Use the credentials from create_full_test_data output
# Login URLs:
# - Staff: http://127.0.0.1:8000/accounts/staff/login/?role=super_admin
# - Customer: http://127.0.0.1:8000/accounts/customer/sms-login/
```

#### **For SMS Testing**
```bash
# 1. Create test customers
python manage.py create_daily_test_customer --count 3

# 2. Use phone numbers in customer SMS login
# 3. Check terminal for SMS codes (fake SMS implementation)
```

### 🛠️ Customizing Commands

#### **Adding New Test Data**
```python
# Example: Adding new user to create_full_test_data.py
{
    'username': 'newuser',
    'password': '123456',
    'first_name': 'نام',
    'last_name': 'نام خانوادگی',
    'role': User.UserRole.ADMIN,
    'phone': '09120000006',
    'email': 'newuser@homayoms.com',
    'is_staff': True,
    'is_superuser': False,
}
```

#### **Creating New Commands**
```bash
# Create new command
python manage.py startapp myapp
mkdir myapp/management
mkdir myapp/management/commands
touch myapp/management/__init__.py
touch myapp/management/commands/__init__.py
```

### 📝 Best Practices

1. **Always use `create_full_test_data`** for initial setup
2. **Test SMS with `create_daily_test_customer`** 
3. **Use `--clear` flag** when you want fresh data
4. **Check command output** for login credentials
5. **Use `--count` parameter** for bulk data creation
6. **Run commands in virtual environment**

### 🚨 Troubleshooting

#### **Command Not Found**
```bash
# Ensure you're in the correct directory
cd v1/

# Check if command exists
python manage.py help | grep create
```

#### **Permission Errors**
```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Check Django installation
python manage.py check
```

#### **Database Errors**
```bash
# Run migrations first
python manage.py migrate

# Check database connection
python manage.py dbshell
```

### 📚 Additional Resources

- **Django Management Commands**: [Django Documentation](https://docs.djangoproject.com/en/stable/howto/custom-management-commands/)
- **Command Structure**: All commands follow Django's BaseCommand pattern
- **Output Formatting**: Commands use Django's styling for beautiful terminal output
- **Error Handling**: All commands include proper error handling and user feedback

---

## 🔐 Authentication System

### User Roles & Permissions

| Role | Access Level | Features |
|------|-------------|----------|
| **🔴 Super Admin** | Full System Access | User management, System settings, All modules |
| **🟡 Admin** | Operational Access | Customer management, Orders, Inventory, Reports |
| **🟢 Finance** | Financial Access | Pricing, Invoices, Financial reports, Payments |
| **🔵 Customer** | Limited Access | Own orders, Profile management, SMS verification |

### Login Flows

1. **Staff Login** (`/accounts/staff/login/`)
   - Username + Password authentication
   - Role validation
   - Session management

2. **Customer Login** (`/accounts/customer/login/`)
   - Phone number verification
   - SMS code authentication
   - No password required

## 📊 Project Structure

```
HomayOMS/
├── accounts/                 # User authentication & management
│   ├── models.py            # Custom User model with roles
│   ├── views.py             # Authentication views
│   ├── urls.py              # URL routing
│   └── management/          # Django management commands
├── core/                    # Core business logic
│   ├── models.py            # Customer, Order models
│   ├── views.py             # Business views
│   └── urls.py              # Core URL routing
├── HomayOMS/                # Project settings
│   ├── settings/            # Environment-based settings
│   ├── urls.py              # Main URL configuration
│   └── baseModel.py         # Base model with timestamps
├── templates/               # HTML templates
│   ├── accounts/            # Authentication templates
│   └── core/                # Business templates
├── static/                  # Static files (CSS, JS, images)
├── requirements.txt         # Python dependencies
└── manage.py               # Django management script
```

## ✅ Completed Features

### 🔐 Authentication & User Management
- ✅ **Custom User Model**: Extended Django User with role-based fields
- ✅ **Multi-Role Login System**: 4 distinct login flows
- ✅ **SMS Verification**: Customer authentication via phone
- ✅ **Role-Based Access Control**: Granular permissions
- ✅ **Session Management**: User activity tracking
- ✅ **Profile Management**: User profile editing

### 🎨 User Interface
- ✅ **Professional Login Pages**: Beautiful 4-role login interface
- ✅ **Responsive Design**: Mobile-first approach
- ✅ **Persian RTL Support**: Full Persian language support
- ✅ **Modern UI Components**: Tailwind CSS styling
- ✅ **Customer Dashboard**: Role-specific dashboard
- ✅ **Staff Dashboard**: Admin and management interfaces

### 🏢 Business Logic
- ✅ **Customer Model**: Complete customer profile system
- ✅ **Base Model**: Timestamp fields for all models
- ✅ **Admin Interface**: Django admin customization
- ✅ **Management Commands**: Test user creation utilities

### 🔧 Development & DevOps
- ✅ **Environment Configuration**: Local, Dev, Production settings
- ✅ **Git Version Control**: Complete project history
- ✅ **Documentation**: Comprehensive code documentation
- ✅ **Code Quality**: Persian comments and emojis
- ✅ **Security Best Practices**: CSRF, XSS protection

## 📝 TODO List

### 🔐 Authentication Enhancements
- [ ] **SMS API Integration**: Connect to SMS service provider
- [ ] **Two-Factor Authentication**: Additional security layer
- [ ] **Password Reset**: Email-based password recovery
- [ ] **Account Lockout**: Brute force protection
- [ ] **Login History**: Detailed login tracking

### 🏢 Business Features
- [ ] **Product Management**: Product catalog and categories
- [ ] **Inventory Tracking**: Stock levels and movements
- [ ] **Order Management**: Order creation and processing
- [ ] **Invoice System**: Automated invoice generation
- [ ] **Payment Integration**: Payment gateway integration
- [ ] **Shipping Management**: Delivery tracking
- [ ] **Supplier Management**: Vendor and supplier profiles

### 📊 Analytics & Reporting
- [ ] **Sales Reports**: Revenue and sales analytics
- [ ] **Inventory Reports**: Stock level reports
- [ ] **Customer Analytics**: Customer behavior insights
- [ ] **Financial Reports**: Profit/loss statements
- [ ] **Dashboard Widgets**: Real-time metrics

### 🎨 User Experience
- [ ] **Dark Mode**: Theme switching capability
- [ ] **Notifications**: Real-time notifications
- [ ] **Search Functionality**: Global search across modules
- [ ] **Data Export**: CSV/Excel export capabilities
- [ ] **Bulk Operations**: Mass data operations

### 🔧 Technical Improvements
- [ ] **API Development**: RESTful API endpoints
- [ ] **Database Optimization**: Query optimization
- [ ] **Caching System**: Redis integration
- [ ] **Background Tasks**: Celery integration
- [ ] **Testing Suite**: Unit and integration tests
- [ ] **Docker Deployment**: Containerization
- [ ] **CI/CD Pipeline**: Automated deployment

### 📱 Mobile & Integration
- [ ] **Mobile App**: React Native mobile application
- [ ] **Webhook Integration**: Third-party integrations
- [ ] **Email Notifications**: Automated email system
- [ ] **SMS Notifications**: Bulk SMS capabilities
- [ ] **Barcode Scanning**: QR code integration

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Development Guidelines
- Follow PEP 8 Python style guide
- Add Persian comments with emojis
- Write comprehensive tests
- Update documentation
- Use meaningful commit messages

## 👥 Contributors

### Lead Developers

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/idarbandi">
        <img src="https://avatars.githubusercontent.com/idarbandi" width="100px;" alt=""/>
        <br />
        <sub><b>Amir DarBandi</b></sub>
      </a>
      <br />
      <sub>Full Stack Developer</sub>
      <br />
      <a href="https://github.com/idarbandi" title="GitHub">🔗 GitHub</a>
    </td>
    <td align="center">
      <a href="https://github.com/Parsa-Parvizi">
        <img src="https://avatars.githubusercontent.com/Parsa-Parvizi" width="100px;" alt=""/>
        <br />
        <sub><b>Parsa Parvizi</b></sub>
      </a>
      <br />
      <sub>Backend Developer</sub>
      <br />
      <a href="https://github.com/Parsa-Parvizi" title="GitHub">🔗 GitHub</a>
    </td>
  </tr>
</table>

### Development Team

- **🎯 Amir DarBandi** - Project Lead & Full Stack Development
  - Expertise: Python, Django, JavaScript, React, Laravel
  - Focus: System architecture, UI/UX, DevOps
  
- **🎯 Parsa Parvizi** - Backend Development & Security
  - Expertise: Python, Django, Cybersecurity, Database Design
  - Focus: Authentication system, Security implementation

### Special Thanks
- **Homayoun Paper & Cardboard Industries Co.** - Project sponsor
- **Django Community** - Framework and documentation
- **Tailwind CSS Team** - UI framework

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**🏢 HomayOMS** - *Enterprise Inventory & Order Management System*

[![GitHub stars](https://img.shields.io/github/stars/amirholakoo/IOMS?style=social)](https://github.com/amirholakoo/IOMS)
[![GitHub forks](https://img.shields.io/github/forks/amirholakoo/IOMS?style=social)](https://github.com/amirholakoo/IOMS)

*Built with ❤️ by the HomayOMS Team*

</div> 
