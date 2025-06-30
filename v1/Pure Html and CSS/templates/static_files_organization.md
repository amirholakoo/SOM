# Static Files Organization for Django Templates

## Directory Structure

```
static/
├── css/
│   ├── styles.css           # Main styles (from Index/styles.css and Stlyles/styles.css)
│   ├── admin.css            # Admin panel styles (from Admin/admin.css)
│   ├── login.css            # Login page styles (from Auth/login.css)
│   ├── verification.css     # Verification page styles (from Recieve Code/verification.css)
│   └── shopping.css         # Shopping page styles (from Shopping/shopping.css)
├── js/
│   ├── script.js            # Main JavaScript (from Index/script.js and Scripts/script.js)
│   ├── admin.js             # Admin panel JavaScript (from Admin/admin.js)
│   ├── login.js             # Login page JavaScript (from Auth/login.js)
│   ├── verification.js      # Verification page JavaScript (from Recieve Code/verification.js)
│   └── shopping.js          # Shopping page JavaScript (from Shopping/shopping.js)
└── images/
    └── (any future image assets)
```

## File Mappings

### CSS Files:
- `Index/styles.css` → `static/css/styles.css`
- `Stlyles/styles.css` → merge with above (if different)
- `Admin/admin.css` → `static/css/admin.css`
- `Auth/login.css` → `static/css/login.css`
- `Recieve Code/verification.css` → `static/css/verification.css`
- `Shopping/shopping.css` → `static/css/shopping.css`

### JavaScript Files:
- `Index/script.js` → `static/js/script.js`
- `Scripts/script.js` → merge with above (if different)
- `Admin/admin.js` → `static/js/admin.js`
- `Auth/login.js` → `static/js/login.js`
- `Recieve Code/verification.js` → `static/js/verification.js`
- `Shopping/shopping.js` → `static/js/shopping.js`

## Django Settings

Make sure to configure static files in your Django settings:

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"
```

## Template Usage

In templates, load static files using:

```django
{% load static %}
<link rel="stylesheet" href="{% static 'css/styles.css' %}">
<script src="{% static 'js/script.js' %}"></script>
``` 