from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import User, Patient,HeartRateRecord
from .serializers import UserSerializer,PatientSerializer,HeartRateRecordSerializer

@api_view(['POST'])
def register_user(request):
    """
    Register a new user

    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    """
    Login user 
    """
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response(
            {'error':'Invalid credentials'},
            status=status.HTTP_401_UNAUTHORIZED

        )
    
    user = authenticate(username=user.username, password=password)
    if user:
        serializer = UserSerializer(user)
        return Response(serializer.data)
    return Response(
        {'error': 'Invalid credentials'}, 
        status=status.HTTP_401_UNAUTHORIZED
    )

class PatientViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing patient information
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def perform_create(self, serializer):
        serializer.save(assigned_to = self.request.user)

class HeartRateRecordViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing heart rate records
    """
    queryset = HeartRateRecord.objects.all()
    serializer_class = HeartRateRecordSerializer

    def get_queryset(self):
        """
        Optionally filter heart rate records by patient_id
        """
        queryset = HeartRateRecord.objects.all()
        patient_id = self.request.query_params.get('patient_id', None)
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset

