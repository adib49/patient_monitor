### Note
### Janitri Backend Assignment
1. Read SETUP.md for the full setup and running tests.
2. Read api_documentation.md for api documentation.

### Database Design
1. User-Patient Relationship:
   - One-to-many relationship between users (healthcare providers) and patients
   - Assumes many patients can be assigned to one healthcare provider
   - Allows for easy tracking of patient assignments

2. Heart Rate Monitoring:
   - Separate model for heart rate records
   - Timestamps for tracking measurement history
   - Validation for realistic heart rate values (0-300 BPM)

### Authentication
- Simple email/password authentication implemented
- Assumes single-tenant system (all users within same organization)

### API Design
- RESTful architecture following Django REST Framework conventions
- Nested routing for related resources
- Comprehensive validation at both model and serializer levels


## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

