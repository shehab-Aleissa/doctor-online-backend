from django.shortcuts import render
from .serializers import DoctorProfileSerializer
from rest_framework.generics import (
    ListAPIView,
) 
from .models import DoctorProfile
# Create your views here.
class DoctorProfileList(ListAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer
