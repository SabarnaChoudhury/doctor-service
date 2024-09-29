from django.urls import path, include
from rest_framework import routers
from doctor.views import DoctorViewSet  # Ensure this path points to the correct views module

router = routers.DefaultRouter()
router.register(r'doctors', DoctorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
