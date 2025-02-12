from rest_framework import serializers
from .models import User,Patient,HeartRateRecord

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ('id','email','username','password','first_name','last_name')
        extra_kwargs = {'password':{'write-only':True}}

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Patient
        fields = '__all__'

class HeartRateRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeartRateRecord
        fields = '__all__'