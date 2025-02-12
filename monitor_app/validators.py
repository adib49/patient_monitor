from rest_framework import serializers
from datetime import date

def validate_date_of_birth(value):

    if value > date.today():
        raise serializers.ValidationError("Date of birth cannot be in the future")
    return value

def validate_heart_rate(value):

    if value < 0 or value > 300 :
        raise serializers.ValidationError("Heart rate must be between  and 300 BPM")
    return value

