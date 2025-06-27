
📦 Project: Inventory & Order Submission System
===============================================

**Goal**: Users fill a Persian form hosted on a Raspberry Pi or WSL server. Admins manage orders, inventory, and users.\
**Stack**: Flask (Python), PostgreSQL, HTML/CSS/JS frontend, SQLite for logs (optional), and Bootstrap or Tailwind (optional for UI).

* * * * *

🔧 Phase 1: System & Environment Setup
--------------------------------------

### ✅ Tasks:

-   Configure local server on RPi or WSL.

-   Install Python, Flask, and PostgreSQL.

-   Set up static IP (RPi) or expose localhost (WSL).

-   Folder structure.

### ✅ DOs:

-   ✅ Use `venv` for Python virtual environments.

-   ✅ Use `pip freeze > requirements.txt` for reproducibility.

-   ✅ Expose port 5000 or 8000 for Flask.

-   ✅ Create a folder structure like:

```
project_root/
├── app.py
├── static/
├── templates/
├── database/
│   └── models.sql
├── instance/
│   └── config.py
├── .env
├── requirements.txt

```

### ❌ DON'Ts:

-   ❌ Don't hardcode database passwords or credentials.

-   ❌ Don't skip `.env` usage for configuration.

-   ❌ Don't use `root` PostgreSQL user in production.

* * * * *

🛠️ Phase 2: PostgreSQL Database Design
---------------------------------------

### ✅ Tables Needed:

1.  `users`: For login and role management.

2.  `orders`: All form submissions.

3.  `inventory`: Real-time item quantities.

4.  `logs` (optional): Record changes/actions.

### ✅ DOs:

-   ✅ Use SQLAlchemy (optional) for ORM.

-   ✅ Add `created_at`, `updated_at` timestamps.

-   ✅ Use ENUMs for choices like paper type or delivery type.

### ❌ DON'Ts:

-   ❌ Don't store phone numbers without validation.

-   ❌ Don't allow deletion of rows---use status or archive instead.

* * * * *

🌐 Phase 3: Frontend - User Interface (Form Page)
-------------------------------------------------

### ✅ Features:

-   User login screen (phone number + temp password).

-   Form page with:

    -   Date dropdowns (روز، ماه، سال)

    -   Inventory capacities for رول‌ها

    -   Priorities and truck selection

    -   Contact info

### ✅ DOs:

-   ✅ Use responsive HTML (Bootstrap is great).

-   ✅ Validate form before submission.

-   ✅ Support Persian text rendering (RTL support).

### ❌ DON'Ts:

-   ❌ Don't rely on JavaScript-only form logic (backend must validate too).

-   ❌ Don't store passwords in frontend code.

* * * * *

🔒 Phase 4: Authentication System
---------------------------------

### ✅ Goals:

-   Admin approves new users manually.

-   Users get temporary password until SMS API is added.

-   Admin can toggle business hours (site open/closed).

### ✅ DOs:

-   ✅ Hash passwords using bcrypt or similar.

-   ✅ Store login attempts for security.

-   ✅ Set admin flag in users table.

### ❌ DON'Ts:

-   ❌ Don't keep sessions without expiration.

-   ❌ Don't show sensitive info to unauthorized users.

* * * * *

📋 Phase 5: Backend - Form Handling & Admin Panel
-------------------------------------------------

### ✅ Server Responsibilities:

-   `/login`: Handle user auth

-   `/submit-form`: Accept user input

-   `/admin`: Admin dashboard with:

    -   User approval

    -   Inventory editing

    -   Orders overview

    -   Price updates

### ✅ DOs:

-   ✅ Store submissions in `orders` table.

-   ✅ Log all changes by admin to `logs`.

-   ✅ Check business hour status before accepting form.

### ❌ DON'Ts:

-   ❌ Don't accept duplicate form submissions.

-   ❌ Don't skip sanitizing all user inputs.

* * * * *

🧾 Phase 6: Reporting & Notifications
-------------------------------------

### ✅ Reports:

-   Admin generates daily/weekly reports.

-   Export as CSV or PDF.

### ✅ Optional:

-   Display current availability before submission.

-   Send email/SMS alerts when orders received.

* * * * *

⏰ Phase 7: Business Hours Logic
-------------------------------

### ✅ Rules:

-   Set open/close schedule in database.

-   If outside business hours:

    -   User sees "closed" message and next open time.

### ✅ DOs:

-   ✅ Compare `datetime.now()` with DB-stored hours.

-   ✅ Cache open hours daily.

### ❌ DON'Ts:

-   ❌ Don't rely on frontend only to block submissions.

* * * * *

🔧 Phase 8: Inventory & Priority Management
-------------------------------------------

### ✅ Goals:

-   Admin sets stock limits for cash/terms.

-   Items displayed with "Available", "Low", or "Not available".

### ✅ DOs:

-   ✅ Sync inventory with orders.

-   ✅ Allow admin to move stock between cash and terms.

### ❌ DON'Ts:

-   ❌ Don't update inventory blindly---log everything.

-   ❌ Don't allow overselling if capacity is reached.

* * * * *

🛡️ Phase 9: Error Handling & Security
--------------------------------------

### ✅ Error Protection:

-   Graceful handling of 404, 500.

-   Backend validation with descriptive error messages.

### ✅ Security Practices:

-   HTTPS (later via nginx + certbot).

-   Use `.env` file for credentials.

-   Limit access by IP if used internally.

* * * * *

🧪 Final Notes
--------------

### 📁 Deployment Tips:

-   Use `gunicorn` or `uWSGI` to run the Flask app.

-   Optional: Reverse proxy with `nginx`.

### 🧼 Housekeeping:

-   Add `.env`, `__pycache__/`, and sensitive files to `.gitignore`.

-   Use environment variables for DB access and admin passwords.

* * * * *

Would you like me to generate a `README.md` structure for GitHub or a full `requirements.txt` file to go with this? I can also create starter files for the form, server, and DB setup. Let me know 🙏
