from django.shortcuts import render
from .serializers import DoctorProfileSerializer, ScheduelSerializer
from rest_framework.generics import (
    ListAPIView,
) 
from .models import DoctorProfile, Scheduel
# Create your views here.
class DoctorProfileList(ListAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer

class ScheduelList(ListAPIView):
    queryset = Scheduel.objects.all()
    serializer_class = ScheduelSerializer