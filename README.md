
# 🏗️ Inventory & Order Management System (Django + PostgreSQL + Docker)

## 🚀 Project Overview

This project is a full-stack inventory and order management system designed for Persian-speaking businesses. It allows users to place orders for inventory items and provides admins with tools to manage inventory, approve users, and review detailed reports. The system will run on Django, use PostgreSQL for data storage, and be deployed using Docker for easy management and scalability.

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)

- **Database**: PostgreSQL

- **Frontend**: HTML, CSS (offline Bootstrap with RTL support)

- **Authentication**: Phone-based with SIM800 module (for SMS)

- **Deployment**: Docker

---

## 📑 Features

### 👤 User Side
- Login with phone number & SMS password
- View confirmation and response

### User Functionality

- View current inventory, prices, and purchase options for cash and terms.

- Authenticate via SMS to confirm identity.

- Place and track orders with a limit of six capacities per order.

- Each capacity includes multiple rolls (about 23,000 kg total).

### 🛠️ Admin Panel
- Approve/reject users
- Manage inventory levels
- Update daily pricing (cash/term)
- View and export order reports
- Control business hours (open/close site)
- Track logs of all actions (💚)

### Admin Functionality

- Approve or reject users after SMS authentication.

- Manage inventory: assign rolls to cash or terms, update quantities.

- Monitor user orders and limit purchases per user.

- View comprehensive reports on inventory, user behavior, and order history.

---

## 🗂️ Folder Structure

inventory_system/\
├── inventory_app/\
│ ├── models.py\
│ ├── views.py\
│ ├── forms.py\
│ ├── urls.py\
│ └── templates/\
│ └── ...\
├── static/\
│ ├── css/\
│ │ └── bootstrap.rtl.min.css\
│ └── js/\
│ └── bootstrap.bundle.min.js\
├── .env\
├── docker-compose.yml\
├── requirements.txt\
├── manage.py\
└── README.md

---

## ⚙️ Setup Instructions

### 1. Clone the Project

```
git clone https://github.com/your-username/inventory-system.git
cd inventory-system`
```

### 2\. Create Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
```

### 3\. Install Requirements

`pip install -r requirements.txt`

### 4\. Configure Environment

Create an `.env` file:

```
DEBUG=True
SECRET_KEY=your-django-secret
DATABASE_NAME=inventory_db
DATABASE_USER=your_user
DATABASE_PASSWORD=your_password
DATABASE_HOST=db
DATABASE_PORT=5432
```

### 5\. Docker Setup

Ensure you have Docker and Docker Compose installed. Use `docker-compose.yml` for setting up containers:
```
version: '3'
services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db

  db:
    image: postgres
    environment:
      POSTGRES_DB: inventory_db
      POSTGRES_USER: your_user
      POSTGRES_PASSWORD: your_password
    volumes:
      - postgres_data:/var/lib/postgresql/data/

volumes:
  postgres_data:

```

`Run Docker Compose:`


`docker-compose up --build`

### 6\. Migrate & Create Superuser


`docker exec -it <web_container_id> python manage.py makemigrations`


---

## 🌐 Accessing the App

* User: `http://localhost:7000/form/`
* Admin: `http://localhost:7000/admin/`

---

## 🔒 Admin Login (Initial)

You must create an admin user:

```bash
python manage.py createsuperuser
```

Then log in at: `http://localhost:7000/admin/`

---

## 🌙 Offline Setup Notes

* Set `dir="rtl"` and `lang="fa"` in the `<html>` tag.

---

## 📦 Deployment Notes



---

## 📑 License

MIT License

---

## 🙋‍♂️ Author

Developed with love 💚 for the WORLD and Persian-speaking businesses.


