# Patient Heart Rate Monitoring System

## 🚀 Quick Start 

```bash
# 1. Clone and enter project
git clone https://github.com/adib49/patient_monitor
cd patient_monitor

# 2. Create and activate virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Unix/MacOS:
# source venv/bin/activate

# 3. Install and run
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

That's it! The API is now running at http://localhost:8000/api/

### Quick Test Endpoints:
1. Register: POST http://localhost:8000/api/register/
2. Login: POST http://localhost:8000/api/login/
3. View Patients: GET http://localhost:8000/api/patients/

Sample registration payload:
```json
{
    "email": "test@example.com",
    "username": "testuser",
    "password": "testpass123",
    "first_name": "Test",
    "last_name": "User"
}
```

For full documentation and details, continue reading below and for api endpoints check api_documentation.md


## Tech Stack

- Python 3.9+
- Django 5.0.2
- Django REST Framework 3.14.0
- SQLite (built-in database)

## Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation and Setup

1. Clone the repository
```bash
git clone https://github.com/yourusername/patient-monitor.git
cd patient-monitor
```

2. Create and activate virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Unix/MacOS
python -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser (optional)
```bash
python manage.py createsuperuser
```

6. Run the development server
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`

## Running Tests

```bash
# Run all tests
python manage.py test

```








