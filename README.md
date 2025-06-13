# 🚗 CarProject

CarProject is a Django REST API for managing cars, their engines, manufacturers, and features. It demonstrates the use of one-to-one, one-to-many, and many-to-many relationships in Django models, and exposes endpoints for CRUD operations and listing related data.

---

## ✨ Features

- List, create, update, and delete cars
- List all manufacturers, features, and engines
- Filter cars by company or fuel type
- Demonstrates:
  - **One-to-One**: Each car has one engine
  - **One-to-Many**: Each car is made by one manufacturer, but a manufacturer can make many cars
  - **Many-to-Many**: Each car can have multiple features, and each feature can belong to multiple cars

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

---

## 🗃️ Models & Relationships

### `Engine`
- `engine_cc`: Integer (engine capacity)
- `engine_type`: String (type of engine)

### `Manufacturer`
- `country`: String (manufacturer's country)

### `Feature`
- `name`: String (feature name)

### `Cars`
- `company`: String (car company)
- `model`: String (car model)
- `fuel`: String (fuel type)
- `price`: String (price)
- `engine`: **OneToOneField** to `Engine` (each car has one engine)
- `manufacturer`: **ForeignKey** to `Manufacturer` (each car has one manufacturer, a manufacturer can have many cars)
- `features`: **ManyToManyField** to `Feature` (each car can have multiple features, each feature can belong to multiple cars)

---

## 🚀 Setup Instructions

1. **Clone the repository:**
    ```sh
    git clone <your-repo-url>
    cd carProject
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv .env
    .env\Scripts\activate
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser (optional):**
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

---

## 📚 API Endpoints

| Method | Endpoint                   | Description                        |
|--------|----------------------------|------------------------------------|
| GET    | `/get_all_cars/`           | List all cars, filter by company or fuel |
| GET    | `/get_car/<id>/`           | Get details of a specific car      |
| POST   | `/post_car/`               | Add a new car                      |
| PUT/PATCH | `/update_car/<id>/`     | Update a car (full/partial)        |
| DELETE | `/delete_car/<id>/`        | Delete a car                       |
| GET    | `/get_manufacturer/`       | List all manufacturers             |
| GET    | `/get_feature/`            | List all features                  |
| GET    | `/get_engine/`             | List all engines                   |

---

## 🛠️ Views Overview

- **Car Views**: CRUD operations for cars, including filtering by company or fuel.
- **Manufacturer/Feature/Engine Views**: List all manufacturers, features, or engines.
- **Serializers**: Handle nested and related data for all models.

---

## 🧪 Testing

To run tests (if implemented):

```sh
python manage.py test
```

---

## 📜 License

This project is for educational purposes.

---

**Developed with Django and Django