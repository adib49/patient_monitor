from django.contrib import admin
from .models import User, Patient, HeartRateRecord

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'date_joined', 'is_staff')
    search_fields = ('email', 'username')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'assigned_to')
    search_fields = ('first_name', 'last_name')
    list_filter = ('gender', 'assigned_to')

@admin.register(HeartRateRecord)
class HeartRateRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'heart_rate', 'recorded_at')
    list_filter = ('patient', 'recorded_at')