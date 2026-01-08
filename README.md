# Django API Boilerplate

A simple Django REST API boilerplate with a health check endpoint.

## Features

- Django 4.2+ with Django REST Framework
- Health check endpoint at `/api/health/`
- SQLite database (default)
- Basic project structure ready for expansion

## Setup

1. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

The server will start at `http://127.0.0.1:8000/`

## API Endpoints

### Health Check
- **URL:** `/api/health/`
- **Method:** `GET`
- **Response:**
  ```json
  {
    "status": "healthy",
    "timestamp": "2026-01-07T12:00:00.000000Z",
    "service": "Django API"
  }
  ```

### Admin Panel
- **URL:** `/admin/`
- Access the Django admin interface (requires superuser account)

## Project Structure

```
.
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── myproject/            # Main project configuration
│   ├── __init__.py
│   ├── settings.py       # Project settings
│   ├── urls.py          # Main URL configuration
│   ├── wsgi.py          # WSGI configuration
│   └── asgi.py          # ASGI configuration
└── api/                  # API application
    ├── __init__.py
    ├── apps.py          # App configuration
    ├── views.py         # API views (health check)
    └── urls.py          # API URL routing
```

## Next Steps

- Add more API endpoints in `api/views.py`
- Create models in `api/models.py`
- Add serializers in `api/serializers.py`
- Configure environment variables for production
- Add authentication and permissions
- Set up a proper database (PostgreSQL, MySQL, etc.)

## Security Notes

- The `SECRET_KEY` in `settings.py` is for development only
- Set `DEBUG = False` in production
- Configure `ALLOWED_HOSTS` for production
- Use environment variables for sensitive configuration

