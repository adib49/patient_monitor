from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'patients', views.PatientViewSet)
router.register(r'heart-rates', views.HeartRateRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
]

