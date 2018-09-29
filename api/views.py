from django.shortcuts import render
from .serializers import DoctorProfileSerializer, ScheduelSerializer, FavouriteDoctorSerializer
from rest_framework.generics import (
    ListAPIView, CreateAPIView
) 
from rest_framework.views import APIView
from .models import DoctorProfile, Scheduel, FavouriteDoctor
# Create your views here.
class DoctorProfileList(ListAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer

class ScheduelList(ListAPIView):
    queryset = Scheduel.objects.all()
    serializer_class = ScheduelSerializer

class MakeFavourite(CreateAPIView):
    queryset = FavouriteDoctor.objects.all()
    serializer_class = FavouriteDoctorSerializer

class FavouriteList(ListAPIView):
    serializer_class = FavouriteDoctorSerializer
    
# THIS WILL GET ONLY THE LIST OF THE DOCTORS THAT HAVE BEEN FAVOURITE BY THE LOGGED IN USER
    def def get_queryset(self):
        queryset = FavouriteDoctor.objects.filter(user=self.request.user)
        return queryset

    