# 🚗 CarProject

CarProject is a Django REST API for managing car records. It allows users to create, read, update, and delete car entries, as well as filter and search cars by various attributes.

---

## ✨ Features

- List all cars with optional filtering by company or fuel type
- Retrieve details of a specific car by ID
- Filter cars by fuel type or price
- Add new cars
- Update existing car details (full or partial)
- Delete cars
- RESTful API endpoints using Django REST Framework

---

## 📁 Project Structure

```
carProject/
├── carApp/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializer.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── carProject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── requirements.txt
```

- **carApp/**: Contains the main app logic (models, serializers, views, URLs).
- **carProject/**: Django project configuration (settings, URLs, WSGI/ASGI).
- **db.sqlite3**: SQLite database file.
- **manage.py**: Django management script.
- **requirements.txt**: Python dependencies.

---

## 🚀 Setup Instructions

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository:**
    ```sh
    git clone <your-repo-url>
    cd carProject
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv .env
    # On Windows:
    .env\Scripts\activate
    # On Unix/Mac:
    source .env/bin/activate
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser (optional, for admin access):**
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

7. **Access the API:**
    - API root: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    - Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📚 API Endpoints

| Method | Endpoint                   | Description                        | Body/Params                |
|--------|----------------------------|------------------------------------|----------------------------|
| GET    | `/get_all_cars/`           | List all cars, filter by company or fuel | `company`, `fuel` (query)  |
| GET    | `/get_car/<int:id>/`       | Get details of a specific car      |                            |
| GET    | `/filter_car/`             | Filter cars by fuel or price       | `fuel`, `price` (query)    |
| POST   | `/post_car/`               | Add a new car                      | Car fields (JSON)          |
| PUT    | `/update_car/<int:id>/`    | Update a car (full/partial)        | Car fields (JSON)          |
| PATCH  | `/update_car/<int:id>/`    | Update a car (partial)             | Car fields (JSON)          |
| DELETE | `/delete_car/<int:id>/`    | Delete a car                       |                            |

---

## ⚙️ Project Configuration

- **Database:** SQLite (default, see [`carProject/settings.py`](carProject/carProject/settings.py))
- **Installed apps:** `rest_framework`, `carApp`
- **Main URLs:** [`carProject/urls.py`](carProject/carProject/urls.py), [`carApp/urls.py`](carProject/carApp/urls.py)
- **WSGI/ASGI entrypoints:** [`wsgi.py`](carProject/carProject/wsgi.py), [`asgi.py`](carProject/carProject/asgi.py)

---

## 🛠️ Customization

- **Add new fields to the car model:**  
  Edit [`models.py`](carProject/carApp/models.py) and update [`serializer.py`](carProject/carApp/serializer.py).
- **Add authentication:**  
  Configure Django REST Framework permissions in [`settings.py`](carProject/carProject/settings.py).

---

## 📜 License

This project is for educational purposes.

---

**Developed with Django and Django REST Framework.**