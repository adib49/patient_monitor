# Patient Monitoring System API Documentation

## Authentication Endpoints

### Register User
- **URL**: `/api/register/`
- **Method**: `POST`
- **Request Body**:
```json
{
    "email": "user@example.com",
    "username": "username",
    "password": "secure_password",
    "first_name": "Rajeshwari",
    "last_name": "Swapnil"
}
```
- **Success Response**: 
  - **Code**: 201 CREATED
  - **Content**: Returns created user object (password excluded)
- **Error Response**:
  - **Code**: 400 BAD REQUEST
  - **Content**: Validation errors

### Login
- **URL**: `/api/login/`
- **Method**: `POST`
- **Request Body**:
```json
{
    "email": "user@example.com",
    "password": "secure_password"
}
```
- **Success Response**:
  - **Code**: 200 OK
  - **Content**: Returns user object
- **Error Response**:
  - **Code**: 401 UNAUTHORIZED
  - **Content**: `{"error": "Invalid credentials"}`

## Patient Management

### List Patients
- **URL**: `/api/patients/`
- **Method**: `GET`
- **Success Response**:
  - **Code**: 200 OK
  - **Content**: Array of patient objects
```json
[
    {
        "id": 1,
        "first_name": "Rajeshwari",
        "last_name": "Swapnil",
        "date_of_birth": "1971-06-23",
        "gender": "F",
        "contact_number": "+919867560490",
        "address": "5th main , indianexpress ,Bangalore 560001",
        "assigned_to": 1
    }
]
```

### Create Patient
- **URL**: `/api/patients/`
- **Method**: `POST`
- **Request Body**:
```json
{
    "first_name": "Rajeshwari",
        "last_name": "Swapnil",
        "date_of_birth": "1971-06-23",
        "gender": "F",
        "contact_number": "+919867560490",
        "address": "5th main , indianexpress ,Bangalore 560001"
}
```
- **Success Response**:
  - **Code**: 201 CREATED
  - **Content**: Created patient object

### Get Patient Details
- **URL**: `/api/patients/{id}/`
- **Method**: `GET`
- **Success Response**:
  - **Code**: 200 OK
  - **Content**: Patient object
- **Error Response**:
  - **Code**: 404 NOT FOUND

## Heart Rate Records

### List Heart Rate Records
- **URL**: `/api/heart-rates/`
- **Method**: `GET`
- **Query Parameters**:
  - `patient_id`: (optional) Filter by patient ID
- **Success Response**:
  - **Code**: 200 OK
  - **Content**: Array of heart rate records
```json
[
    {
        "id": 1,
        "patient": 1,
        "heart_rate": 75,
        "recorded_at": "2024-02-12T14:30:00Z",
        "notes": "Regular checkup"
    }
]
```

### Create Heart Rate Record
- **URL**: `/api/heart-rates/`
- **Method**: `POST`
- **Request Body**:
```json
{
    "patient": 1,
    "heart_rate": 75,
    "notes": "Regular checkup"
}
```
- **Success Response**:
  - **Code**: 201 CREATED
  - **Content**: Created heart rate record

### Data Validation Rules
1. Heart Rate:
   - Must be between 0 and 300 BPM
   - Required field
2. Date of Birth:
   - Cannot be in the future
   - Required field for patients
3. Contact Number:
   - Must be a valid phone number format
4. Email:
   - Must be a valid email format
   - Must be unique in the system
