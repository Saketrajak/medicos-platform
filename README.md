# Medicos Platform 💊

A full-stack medicine ordering web platform built using **Django (Backend)** and **React (Frontend)**.

## 🚀 Features

### Authentication

* User Registration
* User Login using JWT Authentication

### Medicine Catalog

* View medicines
* Search medicines
* Filter medicines by category

### Cart System

* Add medicines to cart
* View cart items

### Orders

* Checkout and create orders
* View order history
* View order details

### Admin Panel

* Manage medicines
* Manage categories
* Manage orders
* Manage users

---

## 🛠 Tech Stack

### Backend

* Django
* Django REST Framework
* SQLite
* JWT Authentication

### Frontend

* React
* Vite
* Axios

---

## 📁 Project Structure

```
medicos-platform
│
├── backend
│   ├── apps
│   │   ├── users
│   │   ├── medicines
│   │   ├── cart
│   │   └── orders
│   │
│   ├── config
│   ├── manage.py
│   └── requirements.txt
│
├── frontend
│   └── React Application
│
└── README.md
```

---

## ⚙️ Installation

### Backend Setup

```
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend Setup

```
cd frontend
npm install
npm run dev
```

---

## 📡 API Endpoints

### Authentication

```
POST /api/auth/register
POST /api/auth/login
```

### Medicines

```
GET /api/medicines
GET /api/medicines/?search=paracetamol
GET /api/medicines/?category=1
```

### Cart

```
POST /api/cart/add
GET /api/cart
```

### Orders

```
POST /api/orders/create
GET /api/orders/history
GET /api/orders/<id>
```

---

## 👨‍💻 Author

**Saket Rajak**

GitHub: https://github.com/Saketrajak
