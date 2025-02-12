from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, Patient, HeartRateRecord


class UserTests(APITestCase):
    def test_register_user(self):
        """
        Test user registration
        """
        url = reverse('register')
        data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'testpass123',
            'first_name': 'Test',
            'last_name': 'User'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, 'test@example.com')
    
    def test_login_user(self):
        """
        Test user login
        """
        # Create a user first
        User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        url = reverse('login')
        data = {
            'email': 'test@example.com',
            'password': 'testpass123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class PatientTests(APITestCase):
    def setUp(self):
        """
        Create a user for testing
        """
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_patient(self):
        """
        Test patient creation
        """
        url = reverse('patient-list')
        data = {
            'first_name': 'Rajeshwari',
            'last_name': 'Swapnil',
            'date_of_birth': '1971-06-23',
            'gender': 'F',
            'contact_number': '+919867560490',
            'address': '5th main , indianexpress ,Bangalore 560001'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Patient.objects.count(), 1)
        self.assertEqual(Patient.objects.get().first_name, 'Rajeshwari')

class HeartRateRecordTests(APITestCase):
    def setUp(self):
        """
        Create user and patient for testing
        """
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.patient = Patient.objects.create(
            first_name='Rajeshwari',
            last_name='Swapnil',
            date_of_birth='1971-06-23',
            gender='F',
            contact_number='+919867560490',
            address='5th main , indianexpress ,Bangalore 560001',
            assigned_to=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_create_heart_rate_record(self):
        """
        Test heart rate record creation
        """
        url = reverse('heartraterecord-list')
        data = {
            'patient': self.patient.id,
            'heart_rate': 75,
            'notes': 'Regular checkup'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(HeartRateRecord.objects.count(), 1)
        self.assertEqual(HeartRateRecord.objects.get().heart_rate, 75)

    def test_invalid_heart_rate(self):
        """
        Test heart rate validation
        """
        url = reverse('heartraterecord-list')
        data = {
            'patient': self.patient.id,
            'heart_rate': 350,  # Invalid heart rate
            'notes': 'Test'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)