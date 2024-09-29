from rest_framework import viewsets
from .models import Doctor
from .serializers import DoctorSerializer

# Define the DoctorViewSet class
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
